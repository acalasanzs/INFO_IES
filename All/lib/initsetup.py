from os import listdir
from os.path import isfile, join
def setup(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    res = "from All.lib.{} import *"
    for x in onlyfiles:
        print(res.format(x[:-3]))
setup("All")