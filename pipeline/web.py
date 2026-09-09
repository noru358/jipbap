"""Small persistent local web route for the JIPBAP runtime.

It is deliberately a controller UI, not a static mock: upload, approval and
lettering requests mutate the same ``runtime/state.json`` used by the CLI.
Deployment is separate from this server module.
"""
from __future__ import annotations

import argparse, cgi, json, mimetypes, shutil, uuid
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from .runtime import EpisodeRuntime, RuntimeErrorClosed


def make_handler(root: Path):
    class Handler(BaseHTTPRequestHandler):
        def _json(self, value, status=200):
            payload=json.dumps(value, ensure_ascii=False).encode(); self.send_response(status); self.send_header("Content-Type","application/json; charset=utf-8"); self.send_header("Content-Length",str(len(payload))); self.end_headers(); self.wfile.write(payload)
        def _runtime(self): return EpisodeRuntime(root)
        def do_GET(self):
            path=urlparse(self.path).path
            if path == "/api/status":
                try: return self._json(self._runtime().load())
                except RuntimeErrorClosed as e: return self._json({"error":str(e)},404)
            if path.startswith("/files/"):
                target=(root/path.removeprefix("/files/")).resolve()
                try: target.relative_to(root.resolve())
                except ValueError: return self.send_error(403)
                if not target.is_file(): return self.send_error(404)
                data=target.read_bytes(); self.send_response(200); self.send_header("Content-Type",mimetypes.guess_type(str(target))[0] or "application/octet-stream"); self.send_header("Content-Length",str(len(data))); self.end_headers(); self.wfile.write(data); return
            try: state=self._runtime().load(); review=state.get("review") or {}; action=self._runtime().next_action(state)
            except RuntimeErrorClosed as e: state={}; review={}; action={"kind":"ERROR","detail":str(e)}
            body=f"""<!doctype html><meta charset=utf-8><title>JIPBAP Runtime</title><h1>JIPBAP Runtime</h1><pre>{json.dumps({'episode':state.get('episode'),'stage':state.get('stage'),'next':action},ensure_ascii=False,indent=2)}</pre>
<p>업로드는 원본 PNG만, 승인은 현재 검수본에만 적용됩니다.</p>
<form method=post action=/api/approve><button {'disabled' if not review else ''}>현재 검수본 승인</button></form>
<form method=post enctype=multipart/form-data action=/api/upload><label>role <select name=role><option value=carrier>carrier</option><option value=board>BODY board</option><option value=cover>COVER</option><option value=lettering_plan>lettering plan</option></select></label><input type=file name=file required><label>generator delivery context (carrier만)</label><input name=delivery_context><button>업로드/재개</button></form>"""
            data=body.encode(); self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8"); self.send_header("Content-Length",str(len(data))); self.end_headers(); self.wfile.write(data)
        def do_POST(self):
            try:
                if self.path == "/api/approve":
                    rt=self._runtime(); state=rt.load(); review=state.get("review") or {}
                    if not review: raise RuntimeErrorClosed("no review is open")
                    out=rt.approve_current(review["artifact_id"],review["sha256"],expected_version=state["version"],event_id="web-"+uuid.uuid4().hex)
                    return self._json({"stage":out["stage"],"next":rt.next_action(out)})
                if self.path != "/api/upload": return self.send_error(404)
                form=cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={"REQUEST_METHOD":"POST","CONTENT_TYPE":self.headers.get("Content-Type","")})
                role=str(form.getfirst("role", "")); item=form["file"] if "file" in form else None
                if role not in {"carrier","board","cover","lettering_plan"} or not item or not getattr(item,"file",None): raise RuntimeErrorClosed("valid role and file are required")
                name="lettering.json" if role=="lettering_plan" else role+".png"; inbox=root/"runtime"/"inbox"; inbox.mkdir(parents=True,exist_ok=True); target=inbox/name
                with target.open("wb") as out: shutil.copyfileobj(item.file,out)
                rt=self._runtime()
                if role=="carrier": state=rt.attach_carrier(target,delivered_to_generator=bool(form.getfirst("delivery_context")),delivery_context=form.getfirst("delivery_context"))
                elif role=="lettering_plan": state=rt.build_presentation(target)
                else:
                    state=rt.load()
                    if (inbox/"board.png").is_file() and (inbox/"cover.png").is_file(): state=rt.ingest_artwork(inbox/"board.png",inbox/"cover.png"); state=rt.prepare_art_review()
                return self._json({"stage":state["stage"],"next":rt.next_action(state)})
            except RuntimeErrorClosed as e: return self._json({"error":str(e)},HTTPStatus.CONFLICT)
    return Handler

def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("--root",type=Path,default=Path.cwd()); p.add_argument("--port",type=int,default=8765); a=p.parse_args(argv)
    server=ThreadingHTTPServer(("127.0.0.1",a.port),make_handler(a.root.resolve())); print(f"http://127.0.0.1:{a.port}"); server.serve_forever()

if __name__ == "__main__": main()
