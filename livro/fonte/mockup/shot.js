const { chromium } = require('playwright');
(async()=>{
  const b=await chromium.launch();
  const jobs=JSON.parse(process.argv[2]);
  for(const [f,o,w,h,s] of jobs){
    const pg=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:s||1});
    await pg.goto('file:///tmp/work/mock/'+f); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(700);
    await pg.screenshot({path:'/tmp/work/mock/'+o}); await pg.close();
  }
  await b.close();
})();
