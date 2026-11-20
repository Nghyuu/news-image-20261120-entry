# news-image-20261120-entry

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Nghyuu/news-image-20261120-entry/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Nghyuu/news-image-20261120-entry/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

The world in one day — Friday 20 November 2026, as a front-page poster. The lead is Cyclone Akvan making landfall on India's east coast at noon, with more than 100,000 people moved to shelters. Below that: day two of the GTA VI launch, the Shenzhen summit's second day, the ICJ's ruling that Myanmar committed genocide against the Rohingya, and South Korea's top court sending the Han Duck-soo case back for retrial. The foot of the page carries the Crimean Bridge strike, Fiji's drought disaster, North Korea's Yongbyon expansion, the US–Venezuela deal and the COP31 draft.

`entry.png` (1024×1024, under 1 MiB) is drawn by `draw.py`, which is kept in this repository so the poster can be re-rendered exactly. The program itself only copies the finished image to `/output/entry.png`; an AI judge compares it against the other entries two at a time.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The program copies `entry.png` to the output directory. It runs with no network and writes the same bytes on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=sgg7ehtv&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
