#!/usr/bin/env python

import sys,getopt,urllib,json,os,datetime,subprocess,shlex

input = open(sys.argv[1],'r')

files = {}

for line in input.readlines():
    if line == '\n': continue
    array = line.strip().split('/')
    base = '/'.join(array[:7])
    if line.count('/store/user') :
        base = '/'.join(array[:5])
    if line.count('/store/results') :
        base = '/'.join(array[:6])
    if base not in files.keys(): files[base] = {'files':[]}
    files[base]['files'].append(line.strip().replace('//','/'))

files_base_sorted = files.keys()
files_base_sorted.sort()
    
for base in files_base_sorted:
    commandline = "dbs search --query=\"find dataset,dataset.status where file = " + files[base]['files'][0] + "\" --noheader --production"
    localargs = shlex.split(commandline)
    output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
    
    lines = output.communicate()[0].split('\n')
    if len(lines) > 2 :
        print
        print 'FAILED: Output of dbs command:',commandline
        print ''
        for line in lines:
            print line
        sys.exit(1)
    if len(lines) > 1 :
        result = lines[0].strip()
    else :
        result = 'UNKNOWN'
 
    if result == 'UNKNOWN':
        files[base]['dataset'] = 'UNKNOWN'
        files[base]['status'] = 'UNKNOWN'
        files[base]['cust'] = ''
        files[base]['noncust'] = ''
        continue

    dataset = result.split()[0]
    status = result.split()[1]
    files[base]['dataset'] = dataset
    files[base]['status'] = status
    
    custodial = {}
    non_custodial = {}

    url='https://cmsweb.cern.ch/phedex/datasvc/json/prod/blockreplicas?block=' + dataset + '%23*'
    result = json.load(urllib.urlopen(url))
    try:
        for block in result['phedex']['block']:
            name = block['name']
            for replica in block['replica']:
                tmpfiles = replica['files']
                site = str(replica['node'])
                is_custodial = replica['custodial']
                if is_custodial == 'y' :
                    if site not in custodial.keys() :
                        custodial[site] = int(tmpfiles)
                    else :
                        custodial[site] += int(tmpfiles)
                else :
                    if site not in non_custodial.keys() :
                        non_custodial[site] = int(tmpfiles)
                    else :
                        non_custodial[site] += int(tmpfiles)
    except:
        print 'PhEDEx problems with dataset:',dataset
        
    custodial_sites = custodial.keys()
    non_custodial_sites = non_custodial.keys()

    custodial_sites.sort()
    non_custodial_sites.sort()


    if len(custodial_sites) == 0 :
        custodial['NONE'] = 0
    if len(non_custodial_sites) == 0 :
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
        
    files[base]['cust'] = custsites
    files[base]['noncust'] = sites


for base in files_base_sorted:
    print 'dataset:',files[base]['dataset'],'status:',files[base]['status'],'first file:',files[base]['files'][0],'custodial:',files[base]['cust'],'non-custodial:',files[base]['noncust']
