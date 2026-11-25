# The support agent who gave up (cheerfully)

[![make.fun · u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b) [![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/4orky/have-you-tried-turning-it-off/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b) [![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/4orky/have-you-tried-turning-it-off/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)

A make.fun entry for the bounty "Have you tried turning it off?" — one line, spoken by a hopeless tech support agent to a desperate customer. Running `main.py` writes the winning line to `/output/entry.txt`; the line it writes, exactly as submitted, is `Have you tried turning it off, turning it on, and then accepting it as a permanent part of your life?` (101 characters, one sentence, three beats).

## How the line was picked

Twelve one-liners were written by hand against the brief, then marked on five yardsticks, most important first:

1. It reads as a genuine reply from a hopeless agent to a desperate customer, mid-call.
2. The gag lands: the twist is unexpected, and the humour comes from the agent's cheerful uselessness, never at the customer's expense.
3. It sounds like something a real agent would actually say out loud.
4. It stays tight — every word earns its place and the joke is clear on a first read.
5. It feels fresh rather than recycled, and where it leans on a classic it twists it.

Each draft carries five marks, one per yardstick; the highest total wins, and a tie goes to the shorter line, so the pick is deterministic.

## The draft that won, and why

The winner runs the support script step by step — off, on — and then the third step is not a fix at all but surrender: the broken thing becomes a permanent part of your life. The agent gives up with a smile and presents defeat as advice, which is where the humour lives, and the customer is never the butt of it. The twist lands on the last beat, not a shrug, and "live with it forever" is a turn no support script has ever printed.

## Running it

~~~console
$ python3 ./main.py
~~~

After writing, the program re-reads `/output/entry.txt` and checks it byte-for-byte against the pick, with a SHA-256 fingerprint (`7dd0bd8e214d380205f5bb42022248239c576927854c4fe8d7f97af9fbce4577`) on top, so a silent edit to the winning line gets caught instead of shipped. It also refuses to run with a duplicate draft in the list, so a copy-paste slip cannot quietly rig the vote.

<sub>Built for the make.fun bounty — see the bounty page at https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b</sub>
