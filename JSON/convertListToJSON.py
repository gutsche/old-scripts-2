#!/usr/bin/env python

import sys,os,json

def convertRange(runs):
    result = {}
    for run in runs.keys():
        tmp = []
        for lumirange in runs[run]:
            tmp.extend(range(lumirange[0],lumirange[1]+1))
        result[run] = tmp
    return result
    
def convertArray(runs):
    result = {}
    for run in runs.keys():
        lumis = runs[run]
        lumis.sort()
        endRange = lumis[0]
        startRange = lumis[0]
        lumiRanges = []
        for lumi in range(1,len(lumis)) :
            if endRange+1 == lumis[lumi] :
                endRange = lumis[lumi]
            else :
                lumiRanges.append([startRange,endRange])
                endRange = lumis[lumi]
                startRange = lumis[lumi]
        lumiRanges.append([startRange,endRange])
        result[run] = lumiRanges
    return result

inputfile = open(sys.argv[1])
runs = {}
for line in inputfile.readlines():
    array = line.split()
    if array[0] not in runs.keys():
        runs[array[0]] = []
    if array[1] not in runs[array[0]]:
        runs[array[0]].append(int(array[1]))
        
range = convertArray(runs)

output = ''
for run in range.keys():
    output += 'run: ' + run + ' lumi sections: '
    for interval in range[run]:
        output += str(interval[0]) + '-' + str(interval[1]) + ','
    if output[-1] == ',':
        output = output[:-1]
    output += '\n'
print output