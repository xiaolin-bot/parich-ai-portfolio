from pathlib import Path
import base64,zlib
files=zlib.decompress(base64.b64decode(Path('m1').read_text()+Path('m2').read_text())).decode().splitlines()
