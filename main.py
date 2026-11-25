#!/usr/bin/env python3
"""Write one funny, true one-line review of a boring everyday object."""
import os

REVIEW = (
    "A rubber band holds your bundle together for a decade, "
    "then snaps the one morning you actually need it to."
)

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)

if __name__ == "__main__":
    main()
