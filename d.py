from pathlib import Path
from urllib.request import urlopen
from c import source
def copy(n):
 p=Path('site')/n
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_bytes(urlopen(source+n,timeout=45).read())
