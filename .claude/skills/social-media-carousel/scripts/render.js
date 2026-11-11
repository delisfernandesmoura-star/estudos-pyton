// Local HTML -> PNG renderer (replaces the inference.sh `belt` cloud call).
// Usage: node render.js <outDir> <width> <height> <slide1.html> [slide2.html ...]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [outDir, w, h, ...files] = process.argv.slice(2);
  if (!outDir || !w || !h || !files.length) {
    console.error('usage: node render.js <outDir> <width> <height> <slide.html...>');
    process.exit(2);
  }
  const fs = require('fs'); fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
  for (const f of files) {
    await page.goto('file://' + path.resolve(f));
    const out = path.join(outDir, path.basename(f, path.extname(f)) + '.png');
    await page.screenshot({ path: out, clip: { x: 0, y: 0, width: +w, height: +h } });
    console.log(out);
  }
  await browser.close();
})();
