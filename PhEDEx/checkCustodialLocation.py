#!/usr/bin/env python

import sys,getopt
import urllib
from xml.dom import minidom

datasetpath = None
allSites = 0
try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["dataset=","allSites"])
except getopt.GetoptError:
    print 'Please specify dataset with --dataset'
    print 'Specify --allSites to show all site location, otherwise show only T1 sites'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--dataset" :
        datasetpath = arg
    if opt == "--allSites" :
        allSites = 1
        
if datasetpath == None:
    print 'Please specify dataset with --dataset'
    sys.exit(2)

url='http://cmsweb.cern.ch/phedex/datasvc/xml/prod/blockreplicas?block=' + datasetpath + '*'
input = urllib.urlopen(url)

xmldoc = minidom.parse(input)

custodial = []
non_custodial = []

for phedex in xmldoc.childNodes :
    for block in phedex.childNodes:
        for replica in block.childNodes:
            site = replica.attributes['node'].value
            if site[-4:] == '_MSS':
                site = site[:-4]
            if site[-7:] == '_Buffer':
                site = site[:-7]
            if site[-7:] == '_Export':
                site = site[:-7]
            if allSites == 1 or ( site[0:2] == 'T1' or site[0:2] == 'T0') :
                if replica.attributes['custodial'].value == 'y':
                    if site not in custodial :
                        custodial.append(site)
                else :
                    if site not in non_custodial :
                        non_custodial.append(site)


custodial.sort()
non_custodial.sort()


if len(custodial) == 0 :
    custodial.append('NONE')
if len(non_custodial) == 0 :
    custodial.append('NONE')
if len(custodial) == 1 and custodial[0].count('T0') > 0 :
    custodial.append('NONE')
if len(non_custodial) == 1 and non_custodial[0].count('T0') > 0 :
    non_custodial.append('NONE')

sites = ''
for site in non_custodial :
    if site not in custodial :
        sites = sites + site + ','
if sites[-1:] == ',' :
    sites = sites[:-1]
print 'dataset:',datasetpath,'custodial:',','.join(custodial),'non-custodial:',sites
