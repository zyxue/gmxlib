import glob
import os

fs = glob.glob("sq2[1-8]_*[0-9].itp")

for f in fs:
    sf = f.split("_")
    os.rename(f, sf[0] + sf[1][-4:])
    # print f, "{0}_{1}".format(sf[0], sf[2]))
