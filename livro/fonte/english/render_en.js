const { chromium } = require('playwright');
(async()=>{
  const b=await chromium.launch();
  const only=process.argv[2];
  if(only!=='pdf'){
    for(const [f,o] of [['cover3.html','cover.png'],['back2.html','back.png']]){
      const pg=await b.newPage({viewport:{width:1600,height:2264}});
      await pg.goto('file:///tmp/work/en/'+f); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(900);
      await pg.screenshot({path:'/tmp/work/en/'+o}); await pg.close();
    }
  }
  const pg=await b.newPage();
  await pg.goto('file:///tmp/work/en/book_en.html',{waitUntil:'load'}); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(1000);
  await pg.pdf({path:'/tmp/work/en/book_en.pdf',preferCSSPageSize:true,printBackground:true});
  await b.close(); console.log('rendered');
})();
