from concurrent.futures import ThreadPoolExecutor
from m import files
from d import copy
with ThreadPoolExecutor(8) as p:list(p.map(copy,files))
import fix,fixapp
print(len(files),'public files transferred')
