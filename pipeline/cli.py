from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .extract_board import ExtractionError, extract_board
from .runtime import EpisodeRuntime, RuntimeErrorClosed
from .validate import ValidationError, validate_repository


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Jipbap fail-closed validation CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="validate current repository media integrity")

    runtime = sub.add_parser("runtime", help="inspect the single fail-closed episode runtime")
    runtime.add_argument("--root", type=Path, default=Path.cwd())
    runtime.add_argument("--next-action", action="store_true")

    extract = sub.add_parser(
        "extract-board",
        help="detect actual 2×3 panel borders and extract six cells",
    )
    extract.add_argument("source")
    extract.add_argument("output_dir")
    extract.add_argument("--metadata")
    extract.add_argument("--inset", type=int, default=1)

    args = parser.parse_args(argv)

    if args.command == "validate":
        try:
            checked = validate_repository()
        except (ValidationError, OSError, ValueError) as exc:
            print(f"JIPBAP_FAIL:\n{exc}", file=sys.stderr)
            return 2
        print("JIPBAP_VALID " + " ".join(checked))
        return 0

    if args.command == "extract-board":
        try:
            result = extract_board(
                Path(args.source),
                Path(args.output_dir),
                metadata_path=Path(args.metadata) if args.metadata else None,
                inset=max(0, args.inset),
            )
        except (ExtractionError, OSError, ValueError) as exc:
            print(f"JIPBAP_FAIL:\n{exc}", file=sys.stderr)
            return 2
        print("JIPBAP_EXTRACTED " + json.dumps(result.to_json(), ensure_ascii=False))
        return 0

    if args.command == "runtime":
        try:
            controller = EpisodeRuntime(args.root)
            state = controller.load()
            payload = controller.next_action(state) if args.next_action else {
                "episode": state["episode"], "stage": state["stage"], "version": state["version"],
                "review": state.get("review"), "next_action": controller.next_action(state),
            }
        except (RuntimeErrorClosed, OSError, ValueError) as exc:
            print(f"JIPBAP_FAIL:\n{exc}", file=sys.stderr)
            return 2
        print(json.dumps(payload, ensure_ascii=False))
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
