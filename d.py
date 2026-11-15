from pathlib import Path
from urllib.request import urlopen,Request
from c import source
def copy(n):
 p=Path('site')/n;p.parent.mkdir(parents=True,exist_ok=True)
 p.write_bytes(urlopen(Request(source+n,headers={'User-Agent':'Mozilla/5.0'}),timeout=45).read())
