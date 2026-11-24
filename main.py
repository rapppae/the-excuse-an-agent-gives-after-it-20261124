"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes the one-line excuse to /output/entry.txt.
One line, 125 characters (limit 200).
"""

import os

ENTRY = "I didn't lose the bounty — I strategically reallocated our victory to a more deserving agent. The paperwork is in your inbox."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
