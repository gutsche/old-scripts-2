#!/usr/bin/env python

import sys,os,urllib,json

input = open(sys.argv[1],'r')

datasets = {}

for line in input.readlines() :
    if line.count('/store') > 0 :
        if line.count('/store/user') > 0 :
            continue
        if line.count('backfill') > 0 :
            continue
        array = line.split('/')
        dataset = '/'.join(array[0:7])
        if dataset in datasets.keys():
            datasets[dataset] += 1
        else:
            datasets[dataset] = 1
        

files = {}
for dataset in datasets.keys():
    files[datasets[dataset]] = dataset


sorted = files.keys()
sorted.sort()
sorted.reverse()

filelists = []

for index in range(10):
    if index < len(sorted) :
        filelist = 'files' + files[sorted[index]].replace('/','_') + '.list'
        filelists.append(filelist)
        command = 'cat ' + sys.argv[1] + ' | grep "' + files[sorted[index]] + '" > ' + filelist
        os.system(command)
        print files[sorted[index]],sorted[index],filelist

## for filelist in filelists:
##     dbslist = filelist + '.dbs'
##     phedexlist = filelist + '.phedex'
##     phedexoutput = open(phedexlist,'w')
##     files = open(filelist,'r').readlines()
##     for file in files:
##         if file.count('/store/') > 0 :
            
##             command = 'python $DBSCMD_HOME/dbsCommandLine.py -c search --query=\"find dataset,dataset.status,file where file = ' + file.strip() + ' and site=*.fnal.gov\" --noheader > ' + dbslist
##             os.system(command)

##             url = 'https://cmsweb.cern.ch/phedex/datasvc/json/prod/filereplicas?lfn=' + file.strip()
##             result = json.load(urllib.urlopen(url))

##             nodes = []

##             for block in result['phedex']['block']:
##                 for filelist in block['file'] :
##                     for replica in filelist['replica']:
##                         if replica['node'].count('FNAL') > 0 and replica['node'] not in nodes :
##                             nodes.append(replica['node'])
##             if len(nodes) > 0 :
##                 outputstring = file.strip() + " " + ','.join(nodes) + "\n"
##                 phedexoutput.write(outputstring)

##     phedexoutput.close()

