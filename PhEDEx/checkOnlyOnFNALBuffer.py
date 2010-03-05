#!/usr/bin/env python

import sys,os,urllib,json,getopt, time

# time of execution
current = time.gmtime()
timefilestring = time.strftime("%Y_%m_%d_%H_%M_%S_UTC",current)

datasets_filename = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["datasets="])
except getopt.GetoptError:
    print 'Please specify lists of datasets with --datasets'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--datasets" :
        datasets_filename = arg

if datasets_filename == None:
    print 'Please specify lists of datasets with --datasets'
    sys.exit(2)


datasets_file = open(datasets_filename,'r')

buffer_datasets = []
mss_datasets = []
both_datasets = []

for line in datasets_file.readlines() :
    dataset = line.split()[0]

    in_buffer = 0
    in_mss = 0

    url = 'http://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?block=' + dataset + '*'
    result = json.load(urllib.urlopen(url))
    for block in result['phedex']['block']:
        for replica in block['replica'] :
            if ( replica['node'].count('T1_US_FNAL_MSS') > 0 ) :
                 in_mss = 1
            if ( replica['node'].count('T1_US_FNAL_Buffer') > 0 ) :
                 in_buffer = 1

    if in_buffer == 1 and in_mss == 1:
            print 'Dataset:',dataset,'in both T1_US_FNAL_Buffer and T1_US_FNAL_MSS'
            both_datasets.append(dataset)
            
    if in_buffer == 1 and in_mss == 0:
            print 'WARNING: Dataset:',dataset,'only in T1_US_FNAL_Buffer'
            buffer_datasets.append(dataset)
                 
    if in_buffer == 0 and in_mss == 1:
            print 'Dataset:',dataset,'in T1_US_FNAL_MSS'
            mss_datasets.append(dataset)


buffer_datasets.sort()
mss_datasets.sort()
both_datasets.sort()

if len(buffer_datasets) > 0 :
    buffer_file = open('datasets_only_on_buffer_at_fnal_' + timefilestring + '.datasets','w')
    [ buffer_file.write(dataset+'\n') for dataset in buffer_datasets ]
    buffer_file.close()

if len(mss_datasets) > 0 :
    mss_file = open('datasets_on_mss_at_fnal_' + timefilestring + '.datasets','w')
    [ mss_file.write(dataset+'\n') for dataset in mss_datasets ]
    mss_file.close()

if len(both_datasets) > 0 :
    both_file = open('datasets_both_on_buffer_and_mss_at_fnal_' + timefilestring + '.datasets','w')
    [ both_file.write(dataset+'\n') for dataset in both_datasets ]
    both_file.close()
