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
    
url='https://cmsweb.cern.ch/phedex/datasvc/xml/prod/blockreplicas?node=' + site
input = urllib.urlopen(url)

xmldoc = minidom.parse(input)

custodial = {}
non_custodial = {}

for phedex in xmldoc.childNodes :
    for block in phedex.childNodes:
        dataset = block.attributes['name'].value.split('#')[0]
        for replica in block.childNodes:
            size = float(replica.attributes['bytes'].value)/1024./1024./1024.
            if replica.attributes['custodial'].value == 'y':
                if dataset in custodial.keys() :
                    custodial[dataset] += size
                else :
                    custodial[dataset] = size                    
            else :
                if dataset in non_custodial.keys() :
                    non_custodial[dataset] += size
                else :
                    non_custodial[dataset] = size                    

print site,'custodial',len(custodial.keys()),'datasets'
print site,'non custodial',len(non_custodial.keys()),'datasets'

custodial_output = open(site + "_custodial.datasets","w")
custodial_output.write("Custodial datasets at: " + site + "\n\n")
custodial_array = custodial.keys()
custodial_array.sort()
for dataset in custodial_array:
    custodial_output.write(dataset + ' ' + str(custodial[dataset]) + "\n")
custodial_output.close()

non_custodial_output = open(site + "_non_custodial.datasets","w")
non_custodial_output.write("Non custodial datasets at: " + site + "\n\n")
non_custodial_array = non_custodial.keys()
non_custodial_array.sort()
for dataset in non_custodial_array:
    non_custodial_output.write(dataset + ' ' + str(non_custodial[dataset]) + "\n")
non_custodial_output.close()
