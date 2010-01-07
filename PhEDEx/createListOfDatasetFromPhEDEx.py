#!/usr/bin/env python

import sys,getopt
import urllib
from xml.dom import minidom

site = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["site="])
except getopt.GetoptError:
    print 'Please give site (e.g. T1_US_FNAL_MSS)'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--site" :
        site = arg

if site == None:
    print 'Please give site (e.g. T1_US_FNAL_MSS)'
    sys.exit(2)
    
url='http://cmsweb.cern.ch/phedex/datasvc/xml/prod/blockreplicas?node=' + site
input = urllib.urlopen(url)

xmldoc = minidom.parse(input)

custodial = []
non_custodial = []

for phedex in xmldoc.childNodes :
    for block in phedex.childNodes:
        dataset = block.attributes['name'].value.split('#')[0]
        for replica in block.childNodes:
            if replica.attributes['custodial'].value == 'y':
                if dataset not in custodial :
                    custodial.append(dataset)
            else :
                if dataset not in non_custodial :
                    non_custodial.append(dataset)

print site,'custodial',len(custodial),'datasets'
print site,'non custodial',len(non_custodial),'datasets'

custodial_output = open(site + "_custodial.datasets","w")
custodial_output.write("Custodial datasets at: " + site + "\n\n")
custodial.sort()
for dataset in custodial:
    custodial_output.write(dataset + "\n")
custodial_output.close()

non_custodial_output = open(site + "_non_custodial.datasets","w")
non_custodial_output.write("Non custodial datasets at: " + site + "\n\n")
non_custodial.sort()
for dataset in non_custodial:
    non_custodial_output.write(dataset + "\n")
non_custodial_output.close()
