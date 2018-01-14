from __future__ import with_statement
import es
import os

def readlines(fp):
    checkfile(fp,"//\n// To put comments in the file add // to the beginning of the line.\n//")
    lines = readfile(fp)
    lins = []
    for line in lines:
        if not line.startswith("//"):
            lins.append(line)
    return lins

def readfile(fp):
    with file(fp,"r") as fo:
        return fo.readlines()

def checkfile(fp,text):
    if not os.path.isfile(fp):
        with file(fp,"w") as fo:
            fo.writelines(text)
