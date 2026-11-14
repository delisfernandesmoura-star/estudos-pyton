const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1520,height:2000}});
await pg.goto('file:///tmp/work/vez/'+process.argv[2]);await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(700);
await pg.screenshot({path:'/tmp/work/vez/'+process.argv[3]});await b.close();})();
