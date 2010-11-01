#!/usr/bin/env python

import sys,getopt,urllib,json,os,datetime,subprocess,shlex

requestId = None
allSites = 1
try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["id="])
except getopt.GetoptError:
    print 'Please specify PhEDEx request ID with --id'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--id" :
        requestID = arg
        
if requestID == None:
    print 'Please specify PhEDEx request ID with --id'
    sys.exit(2)

datasets = []

url='http://cmsweb.cern.ch/phedex/datasvc/json/prod/transferrequests?request=' + requestID
result = json.load(urllib.urlopen(url))
for item in result['phedex']['request']:
    for dataset in item['data']['dbs']['dataset']:
        datasets.append(dataset['name'])

for dataset in datasets:
    custodial = {}
    non_custodial = {}
    status = ''
    
    commandline = "dbs search --query=\"find dataset.status where dataset = " + str(dataset) + "\" --noheader --production"
    localargs = shlex.split(commandline)
    output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
    
    lines = output.communicate()[0].split('\n')
    if len(lines) != 2 :
        print 'Dataset:',dataset,'with multiple status entries, aborting'
        sys.exit(1)
    for line in lines:
        if len(line) > 0 :
             status = line.strip()

    url='http://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?block=' + dataset + '*'
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

    print 'dataset:',dataset,'DBS status:',status,'custodial:',custsites,'non-custodial:',sites
