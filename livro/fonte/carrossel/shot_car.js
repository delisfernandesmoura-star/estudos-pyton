const { chromium } = require('playwright');
(async()=>{
  const b=await chromium.launch();
  const pg=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});
  await pg.goto('file:///tmp/work/car/carrossel.html'); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(800);
  for(let i=1;i<=10;i++){ const el=await pg.$('#s'+i); await el.screenshot({path:`/tmp/work/car/raw-${String(i).padStart(2,'0')}.png`}); }
  await b.close();
})();
