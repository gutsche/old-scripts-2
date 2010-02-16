#!/usr/bin/env python

import sys,getopt
import urllib
from xml.dom import minidom

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
    
url='http://cmsweb.cern.ch/phedex/datasvc/xml/prod/subscriptions?dataset=' + datasetpath
input = urllib.urlopen(url)

xmldoc = minidom.parse(input)

custodial = []
non_custodial = []

for phedex in xmldoc.childNodes :
    for dataset in phedex.childNodes:
        datasetname = dataset.attributes['name'].value
        for subscription in dataset.childNodes:
            site = subscription.attributes['node'].value
            if site[0:2] == 'T1' or site[0:2] == 'T0':
                if subscription.attributes['custodial'].value == 'y':
                    if site not in custodial :
                        custodial.append(site)
                else :
                    if site not in non_custodial :
                        non_custodial.append(site)

print 'dataset:',datasetpath
print 'custodial:',','.join(custodial)
print 'non-custodial:',','.join(non_custodial)
