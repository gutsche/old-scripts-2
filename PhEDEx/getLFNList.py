#!/usr/bin/env python

import sys,os,urllib,json,getopt

datasetpath = None
try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["dataset="])
except getopt.GetoptError:
    print 'Please specify dataset with --dataset'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--dataset" :
        datasetpath = arg
        
if datasetpath == None:
    print 'Please specify dataset with --dataset'
    sys.exit(2)
            
url = 'https://cmsweb.cern.ch/phedex/datasvc/json/prod/filereplicas?block=' + datasetpath + '*'
result = json.load(urllib.urlopen(url))

for block in result['phedex']['block']:
        for filelist in block['file'] :
            print filelist['name']

