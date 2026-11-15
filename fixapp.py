from pathlib import Path
from c import target
p=Path('site/app.js')
p.write_text('window.PORTFOLIO_SHARE_URL='+repr(target)+';\n'+p.read_text())
