"""Entry for make.fun bounty u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.

Writes one single-line joke about office life to /output/entry.txt.
Standard library only; deterministic: the same line every run.
"""

import os

JOKE = (
    "Our office printer has been 'warming up' since 2019, and HR just "
    "promoted it to management because it never answers emails either."
)


def main():
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("entry line must be 1-200 characters, got %d" % len(JOKE))
    if "\n" in JOKE:
        raise ValueError("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
