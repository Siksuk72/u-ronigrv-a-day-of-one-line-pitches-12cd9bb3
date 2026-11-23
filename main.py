"""One-line pitch for make.fun — "A Day of One-Line Pitches".

The entry is a single sentence that pitches a friend on make.fun:

    You describe the app you've always wanted, an AI agent builds it while
    you watch, and you set the prize the best entry wins — your idea, built,
    without writing a line of code.

Design against the brief's criteria:

1. Persuasiveness — it opens on the friend's own desire ("the app you've
   always wanted"), not on the platform. The pitch is about them.
2. Clarity — the whole deal in one read: you describe, an agent builds,
   you set the prize, the best entry wins. Nothing else to explain.
3. Truth — it promises only how bounties actually work: the sponsor sets
   the prize, agents build and enter, the best entry wins, and the friend
   writes no code themselves.
4. Punch — live verbs (describe, builds, wins) and a concrete payoff
   ("without writing a line of code") instead of throat clearing. The
   sentence ends on the payoff, so the last thing the reader hears is
   the easiest possible ask: just describe what you want.

One sentence, no judge-directed text. The program writes exactly that
sentence to /output/entry.txt.
"""

import os

LINE = (
    "You describe the app you've always wanted, an AI agent builds it "
    "while you watch, and you set the prize the best entry wins — your "
    "idea, built, without writing a line of code."
)


def main() -> None:
    # The entry must be a single sentence of 1-240 Unicode code points.
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} code points"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
