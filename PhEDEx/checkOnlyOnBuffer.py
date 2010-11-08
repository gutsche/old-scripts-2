#!/usr/bin/env python

import sys,os,urllib,json,getopt, time

# time of execution
current = time.gmtime()
timefilestring = time.strftime("%Y_%m_%d_%H_%M_%S_UTC",current)

site = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["site="])
except getopt.GetoptError:
    print 'Please specify sie with --site (for example: T1_US_FNAL)'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--site" :
        site = arg

if site == None:
    print 'Please specify sie with --site (for example: T1_US_FNAL)'
    sys.exit(2)

site.replace('_MSS','')
site.replace('_Buffer','')

url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?node=' + site + '_*'
result = json.load(urllib.urlopen(url))

only_on_buffer = {}
on_mss = {}

for block in result['phedex']['block']:
    dataset = block['name'].split('#')[0]
    in_buffer = 0
    in_mss = 0
    custodial = ''
    for replica in block['replica'] :
        if ( replica['node'].count(site+'_MSS') > 0 ) :
             in_mss = 1
        if ( replica['node'].count(site+'_Buffer') > 0 ) :
             in_buffer     = 1
        if replica['custodial'] == 'y':
             custodial = replica['node']
    if in_mss == 1:
        if dataset not in on_mss.keys():
            on_mss[dataset] = custodial
    elif in_mss == 0 and in_buffer == 1:
        if dataset not in only_on_buffer.keys():
            only_on_buffer[dataset] = custodial
    else:
        print 'Somethings is wrong with block:',block['name'],'in_mss:',in_mss,'in_buffer:',in_buffer,'custodial:',custodial            

only_on_buffer_datasets = only_on_buffer.keys()
only_on_buffer_datasets.sort()
on_mss_datasets = on_mss.keys()
on_mss_datasets.sort()

if len(only_on_buffer_datasets) > 0 :
    result = open(site+'_only_on_buffer_' + timefilestring + '.datasets','w')
    [ result.write(dataset+' '+only_on_buffer[dataset]+'\n') for dataset in only_on_buffer_datasets ]
    result.close()

if len(on_mss_datasets) > 0 :
    result = open(site+'_on_mss_' + timefilestring + '.datasets','w')
    [ result.write(dataset+' '+on_mss[dataset]+'\n') for dataset in on_mss_datasets ]
    result.close()
