// News-image entrypoint (Node 22, standard library only): runs the poster
// renderer (draw.py) and writes the finished image to the output directory.
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//
// The render is deterministic: the same draw.py always produces the same
// bytes, so the two grading runs write identical files.

import { execFileSync } from 'node:child_process';
import { mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const outFile = join(outDir, 'entry.png');

mkdirSync(outDir, { recursive: true });

// Prefer python3; fall back to python when only that name exists.
const interpreters = ['python3', 'python'];
let lastError;
for (const bin of interpreters) {
  try {
    execFileSync(bin, [join(here, 'draw.py'), outFile], { stdio: 'inherit' });
    lastError = undefined;
    break;
  } catch (err) {
    lastError = err;
  }
}
if (lastError !== undefined) {
  throw lastError;
}
