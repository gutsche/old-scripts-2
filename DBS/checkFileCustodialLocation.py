#!/usr/bin/env python

import sys,getopt,urllib

try:
    import json
except ImportError:
    import simplejson as json

datasetpath = None
lfn = None
allSites = 0
onlyCustodial= False

try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["lfn=","dataset=","allSites", "onlyCustodial"])
except getopt.GetoptError:
    print 'Please specify dataset with --dataset'
    print 'Specify --allSites to show all site location, otherwise show only T1 sites'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--dataset" :
        datasetpath = arg
    if opt == "--lfn" :
        lfn = arg
    if opt == "--allSites" :
        allSites = 1
    if opt == "--onlyCustodial" :
        onlyCustodial = True
        
if datasetpath == None and lfn == None:
    print 'Please specify dataset with --dataset'
    sys.exit(2)


custodial = {}
non_custodial = {}

if lfn == None :
    url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?block=' + datasetpath + '%23*' 
    result = json.load(urllib.urlopen(url))
    try:
        for block in result['phedex']['block']:
            name = block['name']
            for replica in block['replica']:
                files = replica['files']
                site = str(replica['node'])
                is_custodial = replica['custodial']
                if allSites == 1 or ( site[0:2] == 'T1' or site[0:2] == 'T0') :
                    if is_custodial == 'y' :
                        if site not in custodial.keys() :
                            custodial[site] = int(files)
                        else :
                            custodial[site] += int(files)
                    else :
                        if site not in non_custodial.keys() :
                            non_custodial[site] = int(files)
                        else :
                            non_custodial[site] += int(files)
    except:
        print 'problems with dataset:',dataset
else:
    try:
        url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/filereplicas?lfn=' + lfn
        result = json.load(urllib.urlopen(url))
        phedex = result['phedex']
        for block in phedex['block']:
            for file in block['file']:
               # fname = file['name']
                for replica in file['replica']:
                    site = str(replica['node'])
                    is_custodial = replica['custodial']
                    if allSites == 1 or ( site[0:2] == 'T1' or site[0:2] == 'T0') :
                        if is_custodial == 'y' :
                            if site not in custodial.keys() :
                                custodial[site] = 1
                        else :
                            if site not in non_custodial.keys() :
                                non_custodial[site] = 1

    except:
        print 'problems with lfn:',lfn
        
custodial_sites = custodial.keys()
non_custodial_sites = non_custodial.keys()

custodial_sites.sort()
non_custodial_sites.sort()


if len(custodial_sites) == 0 :
    custodial['NONE'] = 0
if len(non_custodial_sites) == 0 :
    non_custodial['NONE'] = 0
if len(custodial_sites) == 1 and custodial_sites[0].count('T0') > 0 :
    custodial['NONE'] = 0
if len(non_custodial_sites) == 1 and non_custodial_sites[0].count('T0') > 0 :
    non_custodial['NONE'] = 0

sites = ''
custsites = ''
noverbose_custsites=''
for site in non_custodial_sites :
    if site not in custodial_sites :
        sites = sites + site + '(' + str(non_custodial[site]) + '),'
if sites[-1:] == ',' :
    sites = sites[:-1]
for custsite in custodial_sites :
    custsites = custsites + custsite + '(' + str(custodial[custsite]) + '),'
if custsites[-1:] == ',' :
    custsites = custsites[:-1]
for noverbose_custsites in custodial_sites:
    noverbose_custsites = noverbose_custsites
if noverbose_custsites[-1:] == ',' :
    noverbose_custsites = noverbose_custsites[:-1] 

if lfn == None :
    if onlyCustodial:
       print '%s:%s'%(noverbose_custsites,datasetpath)
    else:
       print 'dataset:',datasetpath,'custodial:',custsites,'non-custodial:',sites
else :
    if onlyCustodial:
       print '%s:%s'%(noverbose_custsites,lfn) 
    else:
       print 'lfn:',lfn,'custodial:',custsites,'non-custodial:',sites
