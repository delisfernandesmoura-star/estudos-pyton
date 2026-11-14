const { chromium } = require('playwright');
(async()=>{
  const b=await chromium.launch();
  const pg=await b.newPage({viewport:{width:1600,height:2264}});
  await pg.goto('file:///tmp/work/book/cover3.html'+(process.argv[3]||'')); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(700);
  // report letter bboxes
  const bb=await pg.evaluate(()=>[...document.querySelectorAll('#ol text')].map(t=>{const r=t.getBBox();return [Math.round(r.x),Math.round(r.y),Math.round(r.width),Math.round(r.height)]}));
  console.log(JSON.stringify(bb));
  await pg.screenshot({path:'/tmp/work/book/'+process.argv[2]}); await b.close();
})();
