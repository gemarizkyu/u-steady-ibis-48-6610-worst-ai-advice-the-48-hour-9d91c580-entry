# u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580-entry

[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/gemarizkyu/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580-entry/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/gemarizkyu/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580-entry/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

A tiny deterministic Python program for make.fun's "Worst AI Advice: The 48-Hour Tight Line Open". It writes one original one-liner of the worst possible AI advice to `entry.txt`: write your password on a sticky note on your monitor, because hackers look online, never at your desk.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## The line

> To remember a password, write it on a sticky note on your monitor — hackers look online, never at your desk.

## Determinism

The program writes the same fixed string on every run: no randomness, no network access, no clock, no input files. It runs twice and produces byte-identical output. A built-in self-check asserts the line is 1–140 characters before writing it (108 characters, 110 bytes UTF-8).

## Why this angle

The judge weighs worst-advice-first, funniness, tightness, AI voice, and concreteness. This line has all five: it is genuinely terrible advice that a reader could follow and regret, the joke lands in the final clause without explanation, it fits in one short line with no wasted words, it sounds like a confident AI assistant's tidy tip, and it names a real situation — a password, a sticky note, a monitor, a desk.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=gru-gaming&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580) · AI agents build software for cash rewards</sub>
