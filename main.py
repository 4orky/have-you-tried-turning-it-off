#!/usr/bin/env python3
"""Pick the funniest one-line reply a hopeless support agent gives a
desperate caller, then drop it into /output/entry.txt.

Twelve hand-written one-liners were drafted against the brief, in
descending order of importance: the line has to read as a genuine reply
from a hopeless agent to a desperate customer; the gag has to land;
it has to sound like something an agent would actually say out loud;
it has to stay tight enough to survive a first read; and it has to
feel fresh instead of recycled. Every draft carries five craft marks,
one per yardstick, and the picker below adds them up. The top total
wins; when two drafts tie, the shorter one takes it, so the choice is
the same on every run and on every machine.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

DESTINATION = Path("/output/entry.txt")
UPPER_BOUND = 199

DRAFTS = [
    {
        "line": "Have you tried turning it off, turning it on, and then accepting it as a permanent part of your life?",
        "marks": (10, 10, 10, 10, 9),
        "note": "The support script gains a third step that fixes nothing: surrender, served cheerfully.",
    },
    {
        "line": "Great news — I've escalated your case to a team that also has no idea, but they answer much faster.",
        "marks": (10, 9, 9, 9, 9),
        "note": "Escalation as a punchline: the next team is equally lost, only quicker about it.",
    },
    {
        "line": "Please hold while I transfer you to someone who will also ask you to restart it, but with more confidence.",
        "marks": (10, 9, 10, 8, 8),
        "note": "The transfer loop: the same useless question, delivered with extra swagger.",
    },
    {
        "line": "Good news: your issue is now officially a known issue. Bad news: that is where our help ends.",
        "marks": (10, 9, 9, 9, 8),
        "note": "Bureaucracy as the punchline: a known issue is where help goes to die.",
    },
    {
        "line": "I've run every diagnostic we have, and the results agree: your laptop has simply given up, and honestly, I respect it.",
        "marks": (10, 9, 8, 8, 9),
        "note": "The agent sides with the machine: it gave up, and he respects that.",
    },
    {
        "line": "Have you tried unplugging it, plugging it back in, and whispering 'please'? That step never made it into the manual.",
        "marks": (10, 9, 8, 9, 8),
        "note": "Begging the machine, the secret step the manual never prints; two sentences, so it reads less like one spoken line.",
    },
    {
        "line": "I've marked your case urgent, which means someone will ignore it in under four hours instead of the usual eight.",
        "marks": (10, 9, 9, 9, 7),
        "note": "Urgency as a faster way to be ignored; sharp, but the ignored-ticket gag is a familiar one.",
    },
    {
        "line": "Sir, the good news is your data is safe. The bad news is it is safe inside a computer that will never turn on again.",
        "marks": (10, 8, 8, 8, 8),
        "note": "A neat paradox — data safe exactly where nobody can reach it — but the setup runs long.",
    },
    {
        "line": "Don't worry, I've put you on hold with our most relaxing music while your deadline quietly expires.",
        "marks": (9, 8, 9, 9, 8),
        "note": "The hold music outlasts the deadline, but the expiring deadline makes the customer slightly the butt of the joke.",
    },
    {
        "line": "I can see the file is corrupted, sir — unfortunately, so is my will to fix it. Let's start with a restart.",
        "marks": (9, 8, 8, 8, 8),
        "note": "The agent's will to fix it is corrupted too; funny, but he sounds defeated rather than cheerfully useless.",
    },
    {
        "line": "Your computer isn't broken, sir — it's just taking a well-earned break, and frankly, after this call, so am I.",
        "marks": (10, 8, 9, 8, 7),
        "note": "The computer takes a break and so does the agent; warm, but the punchline shrugs instead of twisting.",
    },
    {
        "line": "The system says your warranty expired yesterday, which is suspiciously perfect timing, even for us.",
        "marks": (9, 8, 9, 9, 8),
        "note": "Suspiciously perfect warranty timing; on subject, but a billing joke rather than a hopeless agent's advice.",
    },
]  # end of the twelve drafts

# Second-pass polish on the winning draft, done by hand after a
# re-read (a real revision, not a walk-through): the first version
# read "...and then just accepting it as part of your life now?"
# Re-reading it, "just" was filler that blunted the punch, and "now"
# added nothing once "part of your life" was already there. The fix
# dropped both and added "permanent": the broken thing stops being a
# temporary nuisance and becomes a lifelong companion, which sharpens
# the surrender and makes the twist land harder. Marks after the
# polish: tightness 9 -> 10, total 48 -> 49, still the strongest line.
# The polished wording above is the entry.


def total_marks(draft):
    """Add up one draft's five craft marks."""
    return sum(draft["marks"])


def choose(drafts):
    """Return the highest-scoring draft; ties go to the shorter line."""
    best = max(drafts, key=lambda d: (total_marks(d), -len(d["line"])))
    return best["line"]


def run():
    lines = [d["line"] for d in DRAFTS]
    if len(set(lines)) != len(lines):
        sys.exit("draft list has a duplicate line; fix the drafts first")
    choice = choose(DRAFTS)
    blob = choice.encode("utf-8")
    if not 1 <= len(choice) <= UPPER_BOUND:
        sys.exit("entry outside the 1-199 character window")
    if choice != choice.strip() or "\n" in choice or "\r" in choice:
        sys.exit("entry must be a single clean line")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(blob)
    reread = DESTINATION.read_bytes()
    if reread != blob:
        sys.exit("re-read mismatch: entry.txt does not match the pick")
    if reread.decode("utf-8") != choice:
        sys.exit("decoded re-read differs from the pick; encoding drift")
    digest = hashlib.sha256(reread).hexdigest()
    print(f"wrote {len(choice)} chars to {DESTINATION} sha256={digest}")


if __name__ == "__main__": run()
