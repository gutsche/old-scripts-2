#!/usr/bin/env python

import sys,getopt,urllib,json,os,datetime,subprocess,shlex

requestID = None
listfilename = None
allSites = 1
try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["id=","list="])
except getopt.GetoptError:
    print 'Please specify PhEDEx request ID with --id'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--id" :
        requestID = arg
    if opt == "--list" :
        listfilename = arg
        
if requestID == None and listfilename == None:
    print 'Please specify PhEDEx request ID with --id or filename with list of datasets with --list'
    sys.exit(2)

datasets = []
blocks = []

if requestID != None :
    url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/transferrequests?request=' + requestID
    result = json.load(urllib.urlopen(url))
    for item in result['phedex']['request']:
        for dataset in item['data']['dbs']['dataset']:
            datasets.append(dataset['name'])
        for block in item['data']['dbs']['block']:
            blocks.append(block['name'])
if listfilename != None:
    listfile = open(listfilename)
    for line in listfile.readlines():
        if len(line) > 1:
            datasets.append(line.strip())

LFNs = []

if len(datasets) > 0 :
    for dataset in datasets:
    
        commandline = "dbs search --query=\"find file where dataset = " + str(dataset) + "\" --noheader --production"
        localargs = shlex.split(commandline)
        output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
        lines = output.communicate()[0].split('\n')
        if lines[0].count('/store/') > 0:
            tmplfn = '/'+'/'.join(lines[0].split('/')[1:7])
            if tmplfn not in LFNs:
                LFNs.append(tmplfn)
        else :
            array = dataset.split('/')
            array2 = array[2].split('-')
            print 'Problem with query for dataset: ' + dataset + ' possible LFN structure from parsing the dataset name: \n/store/data/%s/%s/%s/%s' % (array2[0],array[1],array[3],'-'.join(array2[1:]))

if len(blocks) > 0 :
    for block in blocks:

        commandline = "dbs search --query=\"find file where block = " + str(block) + "\" --noheader --production"
        localargs = shlex.split(commandline)
        output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
        lines = output.communicate()[0].split('\n')
        if lines[0].count('/store/') > 0:
            tmplfn = '/'+'/'.join(lines[0].split('/')[1:7])
            if tmplfn not in LFNs:
                LFNs.append(tmplfn)
        else :
            print 'Problem with query for block:',block
            
print ''
LFNs.sort()
for item in LFNs:
    print item
