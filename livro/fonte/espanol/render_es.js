const { chromium } = require('playwright');
(async()=>{
  const b=await chromium.launch();
  const only=process.argv[2];
  if(only!=='pdf'){
    for(const [f,o] of [['cover3.html','cover.png'],['back2.html','back.png']]){
      const pg=await b.newPage({viewport:{width:1600,height:2264}});
      await pg.goto('file:///tmp/work/es/'+f); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(900);
      await pg.screenshot({path:'/tmp/work/es/'+o}); await pg.close();
    }
  }
  const pg=await b.newPage();
  await pg.goto('file:///tmp/work/es/book_es.html',{waitUntil:'load'}); await pg.evaluate(()=>document.fonts.ready); await pg.waitForTimeout(1000);
  await pg.pdf({path:'/tmp/work/es/book_es.pdf',preferCSSPageSize:true,printBackground:true});
  await b.close(); console.log('rendered');
})();
