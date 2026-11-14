const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage();
await pg.goto('file:///tmp/work/vez/vez.html',{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(1000);
await pg.pdf({path:'/tmp/work/vez/vez.pdf',preferCSSPageSize:true,printBackground:true});await b.close();console.log('pdf')})();
