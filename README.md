# The World in One Day — 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Nghyuu/news-image-20261120-entry/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Nghyuu/news-image-20261120-entry/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A front-page poster summing up the world's news of Friday, 20 November 2026,
for the make.fun competition `news-image-20261120`. `draw.py` renders the
1024×1024 image with Pillow; `main.ts` (Node 22) runs it and writes
`entry.png` to the output directory.

## The ten stories

1. **Cyclone Akvan makes landfall** — near Gopalpur, Odisha, around noon IST;
   winds 90–100 km/h (IMD); more than 100,000 people evacuated.
2. **GTA VI, day two** — $1.84bn / 19.05m copies (Sensor Tower); 7.91m peak
   stream viewers; Take-Two's first official tally expected today.
3. **Shenzhen summit, day 2** — after the first Trump–Xi–Putin meeting
   (19 Nov).
4. **World Court** — ICJ rules Myanmar committed genocide against the
   Rohingya; unappealable; ruled 19 Nov.
5. **Seoul retrial** — Supreme Court overturns Han Duck-soo's 15-year
   sentence in part; retrial ordered (19 Nov).
6. **Crimean Bridge** — Ukraine hits the bridge; rail traffic halted.
7. **Fiji drought** — nationwide state of disaster declared over the
   El Niño drought (18 Nov).
8. **Yongbyon** — IAEA: North Korea expanding its uranium enrichment plant.
9. **US–Venezuela** — agree to restore military cooperation.
10. **COP31** — latest climate draft drops any reference to fossil fuels.

## Reproduce

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/entry.png`. Running it twice produces byte-identical output.
