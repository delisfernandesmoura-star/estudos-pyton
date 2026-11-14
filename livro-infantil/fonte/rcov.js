const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1600,height:2133}});
await pg.goto('file:///tmp/work/kids/'+process.argv[2]);await pg.evaluate(()=>document.fonts.ready);await pg.waitForTimeout(700);
await pg.screenshot({path:'/tmp/work/kids/'+process.argv[3]});await b.close();})();
