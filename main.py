import os,sys
import All.lib.assgn as assgn
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("./") if isfile(join("./", f))]
blacklist = ["main.py","ampl4.py","triangle.py","OptionsInClass.py","assgn.py"]
for x in blacklist:
    if x in onlyfiles:
        onlyfiles.remove(x)
lis = assgn.List2list(onlyfiles,", ")
try:
    obj = sys.argv[1] + ".py"
    if obj in onlyfiles:
        a = __import__(sys.argv[1])
        a.main()
except:
    print(lis)