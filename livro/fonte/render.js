const { chromium } = require('playwright');
(async()=>{
  const b=await chromium.launch();
  for(const [f,o,h] of [['cover.html','cover.png',2264],['back.html','back.png',2264]]){
    const pg=await b.newPage({viewport:{width:1600,height:h},deviceScaleFactor:1});
    await pg.goto('file:///tmp/work/book/'+f); await pg.addStyleTag({content:':root{--h:'+h+'px}'});
    await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(500);
    await pg.screenshot({path:'/tmp/work/book/'+o}); await pg.close();
  }
  const pg=await b.newPage();
  await pg.goto('file:///tmp/work/book/book.html',{waitUntil:'load'}); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(800);
  await pg.pdf({path:'/tmp/work/book/book.pdf',preferCSSPageSize:true,printBackground:true});
  await b.close(); console.log('rendered');
})();
