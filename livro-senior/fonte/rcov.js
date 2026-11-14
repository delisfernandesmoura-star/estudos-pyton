const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1600,height:2080}});
await pg.goto('file:///tmp/work/senior/'+process.argv[2]);await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(700);
await pg.screenshot({path:'/tmp/work/senior/'+process.argv[3]});await b.close();})();
