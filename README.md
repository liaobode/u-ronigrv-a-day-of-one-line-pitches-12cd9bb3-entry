# A Day of One-Line Pitches (`u-ronigrv-a-day-of-one-line-pitches-12cd9bb3`)

Submission for the **A Day of One-Line Pitches** competition on make.fun.

## Overview

`main.py` validates and writes a single-sentence pitch (<= 240 UTF-8 characters and bytes, single line, non-empty) to `/output/entry.txt` with world-readable permissions (`0644`).

## Running Locally

```bash
OUTPUT_DIR=/tmp/pitch_out python3 main.py
cat /tmp/pitch_out/entry.txt
```
