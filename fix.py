from pathlib import Path
from c import source,target
p=Path('site/index.html')
p.write_text(p.read_text().replace(source.rstrip('/'),target.rstrip('/')))
