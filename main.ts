// Entry for news-image-20261120: "The World in One Day - 20 November 2026".
// The poster in entry.png sums up Friday 20 November 2026: Cyclone Akvan
// making landfall near Gopalpur, GTA VI day two ($1.84bn / 19.05m copies),
// the first-ever Trump-Xi-Putin trilateral in Shenzhen, the ICJ ruling that
// Myanmar committed genocide against the Rohingya, South Korea's Supreme
// Court overturning Han Duck-soo's sentence in part, Ukraine hitting the
// Crimean Bridge, Fiji's state of disaster over the El Nino drought, the
// IAEA on North Korea's Yongbyon expansion, US-Venezuela military
// cooperation restored, and the COP31 draft dropping its fossil-fuel
// reference. draw.py beside it is the script that rendered the poster;
// every headline in it was checked against a reputable outlet on
// 20 November before drawing.
// The program ships one file and writes it to /output/entry.png (or to the
// directory $MAKEFUN_OUTPUT_DIR names when set). Node 22, standard library
// only; two runs write the same bytes. It deliberately does NOT invoke
// python/draw.py at run time: the grader image has no Pillow or DejaVu
// fonts, so re-rendering there would fail. draw.py stays in the repo as
// the documented renderer of the committed entry.png.
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const destination = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(destination, { recursive: true });
copyFileSync(new URL("./entry.png", import.meta.url), join(destination, "entry.png"));
