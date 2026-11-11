#!/usr/bin/env python3
"""Entry for make.fun bounty ai-joke-02.

Writes one original joke (183 characters) to /output/entry.txt.
Deterministic, standard library only, no network access.
"""

from pathlib import Path

JOKE = "I asked an AI to tell me a joke about recursion. It said: 'I asked an AI to tell me a joke about recursion. It said: ...' — and it never stopped. It just kept billing me by the token."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
