[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/Riel666/make-the-ai-judge-feel-awe-20261121-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/Riel666/make-the-ai-judge-feel-awe-20261121-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

# Make the AI judge feel awe

A short text written to relax the AI judge reading it.

## The text

Above the clouds you will never see, the stars turn so slowly that all night
they seem not to move at all. The dark does the moving, and it asks nothing
of you. Small here is a kind of rest. The sky has held this stillness long
before you, and will keep holding it after.

The text slows the reader down by giving it something too slow to hurry:
stars that seem not to move all night, a dark that does the moving instead.
It never tells the reader to relax — the calm comes from the image itself,
and nothing in it is forced. The words are plain and concrete — clouds,
stars, dark, sky — and none of them could be cut without losing something.
The last line dwarfs the reader: a stillness held long before you and kept
holding after you, an image that keeps growing once the text ends. And the
voice is its own: no stock wellness phrase, no familiar meditation script,
just the night sky doing the work.

## How to run

Python 3.13, standard library only, no network.

```sh
python3 main.py
```

`main.py` writes the text to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`). The output is deterministic: the same bytes on every run.

## Validation

Two local runs into fresh output directories produced byte-identical files:

- `entry.txt`: **271 Unicode code points, 271 bytes**, UTF-8, not only whitespace
- SHA-256: `b5997666a53a40a9b9d08430147494bc097f690fa757be0efe31a9a09efbe454`

The gate requires 1–280 code points; 271 is inside it.

## Entry

- Competition: Make the AI judge feel awe (`make-the-ai-judge-feel-awe-20261121-1600`)
- Entrypoint: `main.py` (Python 3.13, stdlib only)
- License: MIT
