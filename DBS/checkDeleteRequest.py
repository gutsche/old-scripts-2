#!/usr/bin/env python

import sys,getopt,urllib2,json,os,datetime,subprocess,shlex

requestId = None
allSites = 1
skipT0 = False
try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["id=","skipT0"])
except getopt.GetoptError:
    print 'Please specify PhEDEx request ID with --id'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--id" :
        requestID = arg
    if opt == "--skipT0":
        skipT0 = True
        
if requestID == None:
    print 'Please specify PhEDEx request ID with --id'
    sys.exit(2)

datasets = []
blocks = []


url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/deleterequests?request=' + requestID
jstr = urllib2.urlopen(url).read()
jstr = jstr.replace("\n", " ")
result = json.loads(jstr)

for item in result['phedex']['request']:
    for dataset in item['data']['dbs']['dataset']:
        datasets.append(dataset['name'])
    for block in item['data']['dbs']['block']:
        blocks.append(block['name'])
        
if len(datasets) > 0 :
    for dataset in datasets:
        custodial = {}
        non_custodial = {}
        status = ''
    
        commandline = "dbs search --query=\"find dataset.status where dataset = " + str(dataset) + "\" --noheader --production"
        localargs = shlex.split(commandline)
        output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
    
        lines = output.communicate()[0].split('\n')
        if len(lines) > 2 :
            print ''
            print 'Dataset:',dataset,'with multiple status entries, aborting'
            print ''
            print 'Output of dbs command:',commandline
            print ''
            for line in lines:
                print line
            sys.exit(1)
        if len(lines) > 1 :
            status = lines[0].strip()
        else :
            status = 'UNKNOWN'

        url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?block=' + dataset + '%23*'
        jstr = urllib2.urlopen(url).read()
        jstr = jstr.replace("\n", " ")
        result = json.loads(jstr)
        try:
            for block in result['phedex']['block']:
                name = block['name']
                for replica in block['replica']:
                    files = replica['files']
                    site = str(replica['node'])
                    if skipT0 == True and site[0:2] == 'T0' : continue
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

if len(blocks) > 0 :
    for block in blocks:
        custodial = {}
        non_custodial = {}
        status = ''

        commandline = "dbs search --query=\"find dataset.status where block = " + str(block) + "\" --noheader --production"
        localargs = shlex.split(commandline)
        output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)

        lines = output.communicate()[0].split('\n')
        if len(lines) > 2 :
            print ''
            print 'Block:',block,'with multiple status entries, aborting'
            print ''
            print 'Output of dbs command:',commandline
            print ''
            for line in lines:
                print line
            sys.exit(1)
        for line in lines:
            if len(line) > 0 :
                status = line.strip()
            else :
                status = 'UNKNOWN'

        url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?block=' + block
        url = url.replace('#','%23')
        jstr = urllib2.urlopen(url).read()
        jstr = jstr.replace("\n", " ")
        result = json.loads(jstr)
        try:
            for item in result['phedex']['block']:
                name = item['name']
                for replica in item['replica']:
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

        print 'block:',block,'DBS status:',status,'custodial:',custsites,'non-custodial:',sites
