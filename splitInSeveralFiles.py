#!/usr/bin/env python

import sys,os

filename = sys.argv[1]
linesPerFile = sys.argv[2]

print "filename:",filename
print "lines per file:",linesPerFile

name = os.path.splitext(filename)[0]

handle = open(filename)

counter = 0
filecounter = 0

for line in handle.readlines() :
    if counter%int(linesPerFile) == 0 :
        filecounter += 1
        if filecounter != 1 :
            outputfile.close()
        outputfilename = name + '_' + str(filecounter) + '.checks'
        outputfile = open(outputfilename,'w')
        os.chmod(outputfilename,0755)
        outputfile.write('#!/bin/bash\n')
        init = file("/uscms/home/gutsche/scripts/init.sh")
        for initline in init:
            outputfile.write(initline)
    counter += 1
    outputfile.write(line);
