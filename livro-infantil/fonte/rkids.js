const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage();
await pg.goto('file:///tmp/work/kids/kids.html',{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(1000);
await pg.pdf({path:'/tmp/work/kids/kids.pdf',preferCSSPageSize:true,printBackground:true});await b.close();console.log('pdf')})();
