// Entry for news-image-20261120: "The World in One Day — 20 November 2026".
// The poster in entry.png sums up Friday 20 November 2026: Cyclone Akvan
// making landfall on India's east coast at noon, day two of the GTA VI
// launch, the Shenzhen summit's second day, the ICJ's Myanmar ruling,
// Seoul's Han Duck-soo retrial, and five more stories below the fold.
// draw.py beside it is the script that rendered the poster; every headline
// in it was checked against a reputable outlet on 20 November before drawing.
// The program ships one file and writes it to /output/entry.png (or to the
// directory $MAKEFUN_OUTPUT_DIR names when set). Node 22, standard library
// only; two runs write the same bytes.
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const destination = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(destination, { recursive: true });
copyFileSync(new URL("./entry.png", import.meta.url), join(destination, "entry.png"));
