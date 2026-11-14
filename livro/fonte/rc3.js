const { chromium } = require('playwright');
(async()=>{
  const b=await chromium.launch();
  const pg=await b.newPage({viewport:{width:1600,height:2264}});
  await pg.goto('file:///tmp/work/book/cover3.html'+(process.argv[3]||'')); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(900);
  console.log(JSON.stringify(await pg.evaluate(()=>window.__ink)));
  await pg.screenshot({path:'/tmp/work/book/'+process.argv[2]}); await b.close();
})();
