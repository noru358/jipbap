from __future__ import annotations

import argparse
import sys

from .validate import ValidationError, validate_repository


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Jipbap fail-closed validation CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="validate current repository media integrity")
    args = parser.parse_args(argv)

    if args.command == "validate":
        try:
            checked = validate_repository()
        except (ValidationError, OSError, ValueError) as exc:
            print(f"JIPBAP_FAIL:\n{exc}", file=sys.stderr)
            return 2
        print("JIPBAP_VALID " + " ".join(checked))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
