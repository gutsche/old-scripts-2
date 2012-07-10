#!/usr/bin/env python

import sys,getopt,urllib2,json,os,datetime,subprocess,shlex

requestID = None
allSites = 1
try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["id="])
except getopt.GetoptError:
    print 'Please specify comma separated list of PhEDEx request IDs with --id'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--id" :
        requestID = arg.split(',')
        
if requestID == None:
    print 'Please specify comma separated list of PhEDEx request IDs with --id'
    sys.exit(2)

datasets = []
blocks = []

for id in requestID:
    url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/transferrequests?request=' + id
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
        if len(lines) > 1 :
            status = lines[0].strip()
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

datatiers_cat1 = ['RAW']
datatiers_cat4 = ['GEN-SIM','GEN-SIM-RAW','GEN-RAW']

lfn_cat1 = []
lfn_cat2 = []
lfn_cat3 = []
lfn_cat4 = []
lfn_cat5 = []

if len(datasets) > 0 :
    for dataset in datasets:

        commandline = "dbs search --query=\"find file where dataset = " + str(dataset) + "\" --noheader --production"
        localargs = shlex.split(commandline)
        output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
        lines = output.communicate()[0].split('\n')
        if len(lines) == 1:
            array = dataset.split('/')
            array2 = array[2].split('-')
            print 'Problem with query for dataset: ' + dataset + ' possible LFN structure from parsing the dataset name: \n/store/data/%s/%s/%s/%s' % (array2[0],array[1],array[3],'-'.join(array2[1:]))
            continue
        for line in lines:
            if line.count('/store/') > 0:
                parts = line.split('/')
                tier = parts[5]
                tmplfn_p = '/'+'/'.join(parts[1:7])
                tmplfn = '/'+'/'.join(parts[1:6])
                if tmplfn.count('/store/data/') > 0 :
                    if tier in datatiers_cat1:
                        if tmplfn_p not in lfn_cat1: lfn_cat1.append(tmplfn_p)
                    else:
                        if tmplfn_p.count('Prompt') > 0:
                            if tmplfn_p not in lfn_cat2: lfn_cat2.append(tmplfn_p)
                        elif tmplfn_p.count('ALCARECO') > 0:
                            if tmplfn_p not in lfn_cat2: lfn_cat2.append(tmplfn_p)
                        else :
                            if tmplfn not in lfn_cat3: lfn_cat3.append(tmplfn)
                else:
                    if tier in datatiers_cat4:
                        if tmplfn not in lfn_cat4: lfn_cat4.append(tmplfn)
                    else:
                        if tmplfn not in lfn_cat5: lfn_cat5.append(tmplfn)

if len(blocks) > 0 :
    for block in blocks:

        commandline = "dbs search --query=\"find file where block = " + str(block) + "\" --noheader --production"
        localargs = shlex.split(commandline)
        output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
        lines = output.communicate()[0].split('\n')
        if len(lines) == 1:
            print 'Problem with query for block:',block
            continue
        if lines[0].count('/store/') > 0:
            parts = lines[0].split('/')
            tier = parts[5]
            tmplfn_p = '/'+'/'.join(parts[1:7])
            tmplfn = '/'+'/'.join(parts[1:6])
            if tmplfn.count('/store/data/') > 0 :
                if tier in datatiers_cat1:
                    if tmplfn_p not in lfn_cat1: lfn_cat1.append(tmplfn_p)
                else:
                    if tmplfn_p.count('Prompt') > 0:
                        if tmplfn_p not in lfn_cat2: lfn_cat2.append(tmplfn_p)
                    elif tmplfn_p.count('ALCARECO') > 0:
                        if tmplfn_p not in lfn_cat2: lfn_cat2.append(tmplfn_p)
                    else :
                        if tmplfn not in lfn_cat3: lfn_cat3.append(tmplfn)
            else:
                if tier in datatiers_cat4:
                    if tmplfn not in lfn_cat4: lfn_cat4.append(tmplfn)
                else:
                    if tmplfn not in lfn_cat5: lfn_cat5.append(tmplfn)


lfn = []
lfn.extend(lfn_cat1)
lfn.extend(lfn_cat2)
lfn.extend(lfn_cat3)
lfn.extend(lfn_cat4)
lfn.extend(lfn_cat5)

eras = []
for item in lfn:
    era = item.split('/')[3]
    if era not in eras: eras.append(era)

print ''
print'Subject: tape family request for era','.'.join(eras)
print ''
print 'Hi all,'
print ''
print 'can I please have tape families for era', '.'.join(eras) ,'for:'
print ''

if len(lfn_cat1) > 0:
    lfn_cat1.sort()
    print 'cat(1):'
    for item in lfn_cat1:
        print item  
    print ''

if len(lfn_cat2) > 0:
    lfn_cat2.sort()
    print 'cat(2):'
    for item in lfn_cat2:
        print item  
    print ''

if len(lfn_cat3) > 0:
    lfn_cat3.sort()
    print 'cat(3):'
    for item in lfn_cat3:
        print item  
    print ''

if len(lfn_cat4) > 0:
    lfn_cat4.sort()
    print 'cat(4):'
    for item in lfn_cat4:
        print item  
    print ''

if len(lfn_cat5) > 0:
    lfn_cat5.sort()
    print 'cat(5):'
    for item in lfn_cat5:
        print item  
    print ''

print "for PhEDEx requests:",','.join(requestID)
print ''
print 'Thanks,'
print ''
print 'OLI'
print ''