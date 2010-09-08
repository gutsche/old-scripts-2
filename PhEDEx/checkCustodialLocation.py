#!/usr/bin/env python

import sys,getopt,urllib,json

datasetpath = None
lfn = None
allSites = 0
try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["lfn=","dataset=","allSites"])
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
        
if datasetpath == None and lfn == None:
    print 'Please specify dataset with --dataset'
    sys.exit(2)


custodial = {}
non_custodial = {}

if lfn == None :
    url='http://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?block=' + datasetpath + '*'
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
        url='http://cmsweb.cern.ch/phedex/datasvc/json/prod/filereplicas?lfn=' + lfn
        result = json.load(urllib.urlopen(url))
        for outerblock in result['phedex']['block']:
            blockname = outerblock['name']
            datasetname = blockname.split('#')[0]
            url='http://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?block=' + datasetname + '*'
            result = json.load(urllib.urlopen(url))
            for block in result['phedex']['block']:
                name = block['name']
                if name == blockname :
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

            # files = block['files']
            # for fileinstance in block['file'] :
            #     if fileinstance['name'] == lfn :
            #         for replica in fileinstance['replica']:
            #             site = str(replica['node'])
            #             is_custodial = replica['custodial']
            #             if allSites == 1 or ( site[0:2] == 'T1' or site[0:2] == 'T0') :
            #                 if is_custodial == 'y' :
            #                     if site not in custodial.keys() :
            #                         custodial[site] = int(files)
            #                     else :
            #                         custodial[site] += int(files)
            #                 else :
            #                     if site not in non_custodial.keys() :
            #                         non_custodial[site] = int(files)
            #                     else :
            #                         non_custodial[site] += int(files)
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
for site in non_custodial_sites :
    if site not in custodial_sites :
        sites = sites + site + '(' + str(non_custodial[site]) + '),'
if sites[-1:] == ',' :
    sites = sites[:-1]
for custsite in custodial_sites :
    custsites = custsites + custsite + '(' + str(custodial[custsite]) + '),'
if custsites[-1:] == ',' :
    custsites = custsites[:-1]

if lfn == None :
    print 'dataset:',datasetpath,'custodial:',custsites,'non-custodial:',sites
else :
    print 'lfn:',lfn,'custodial:',custsites,'non-custodial:',sites
