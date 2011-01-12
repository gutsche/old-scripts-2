#!/usr/bin/env python

import sys

input = open(sys.argv[1])

datasets = {}

for line in input.readlines():
    array = line.split()
    if len(array) == 3:
        tmp = {}
        events = int(array[1])
        size = float(array[2])/1024/1024/1024/1024
        datasets[array[0]] = {"events":events,"size":size}
        
print ''
print 'events:'
print ''
for dataset in sys.argv[2:] :
    if dataset in datasets.keys() :
        print datasets[dataset]['events']
    else :
        print 0
        
print ''
print 'Size:'
print ''
for dataset in sys.argv[2:] :
    if dataset in datasets.keys() :
        print datasets[dataset]['size']
    else :
        print 0

print ''
print 'Table:'
print ''

for dataset in sys.argv[2:] :
    result = ""
    result += dataset + '\t'
    if dataset in datasets.keys() :
        result += str(datasets[dataset]['events'])
    else :
        result += str(0)
    result += '\t'
    if dataset in datasets.keys() :
        result += str(datasets[dataset]['size'])
    else :
        result += str(0)
    print result