#!/usr/bin/env python

""" This python script is similar to the Unix column command. However, in contrast, the columns are sorted as specified """

if len(sys.argv)<2:
    print ("python col1,col2,col5,col2 file")
    print ("or")
    print ("cat file |python column.py col1,col2,col3")
    sys.exit(0)
cols = []
for k in sys.argv[1].split(","):
    cols.append(int(k))

def nopen():
    if len(sys.argv)>2:
        return open(sys.argv[2])
    return sys.stdin

for l in nopen:
    ls = l.strip().split()
    line = ""
    if len(l.strip())==0:
        print (l.strip())
        continue
    for c in cols:
        line+=" "+ls[c]
    print (line[1:])
