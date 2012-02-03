#!/usr/bin/env python

import sys,getopt
import urllib
from xml.dom import minidom

site = None
group = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["site=","group="])
except getopt.GetoptError:
    print 'Please give site (e.g. T1_US_FNAL_MSS or T2_CH_CERN)'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--site" :
        site = arg
    if opt == "--group" :
        group = arg

if site == None:
    print 'Please give site (e.g. T1_US_FNAL_MSS or T2_CH_CERN)'
    sys.exit(2)
    
url='https://cmsweb.cern.ch/phedex/datasvc/xml/prod/blockreplicas?node=' + site
if group != None :
    url += '&group=' + group
input = urllib.urlopen(url)

xmldoc = minidom.parse(input)

custodial = {}
non_custodial = {}

for phedex in xmldoc.childNodes :
    for block in phedex.childNodes:
        dataset = block.attributes['name'].value.split('#')[0]
        for replica in block.childNodes:
            size = float(replica.attributes['bytes'].value)/1000./1000./1000.
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


if site.count('T1_') > 0 :

    print site,'custodial',len(custodial.keys()),'datasets'
    print site,'non custodial',len(non_custodial.keys()),'datasets'

    custodial_output = open(site + "_custodial.datasets","w")
    header = "Custodial datasets at: " + site
    if group != None:
        header += " of group: " + group
    header += " with size in GB\n\n"
    custodial_output.write(header)
    custodial_array = custodial.keys()
    custodial_array.sort()
    for dataset in custodial_array:
        custodial_output.write(dataset + ' ' + str(custodial[dataset]) + "\n")
    custodial_output.close()

    non_custodial_output = open(site + "_non_custodial.datasets","w")
    header = "Non custodial datasets at: " + site
    if group != None:
        header += " of group: " + group
    header += " with size in GB\n\n"
    non_custodial_output.write(header)
    non_custodial_array = non_custodial.keys()
    non_custodial_array.sort()
    for dataset in non_custodial_array:
        non_custodial_output.write(dataset + ' ' + str(non_custodial[dataset]) + "\n")
    non_custodial_output.close()

else :
    output = open(site + ".datasets","w")
    header = "Datasets at: " + site
    if group != None:
        header += " of group: " + group
    header += " with size in GB\n\n"
    output.write(header)
    output_dict = dict(custodial.items() + non_custodial.items())
    output_array = output_dict.keys()
    output_array.sort()

    print site,len(output_dict.keys()),'datasets'

    for dataset in output_array:
        output.write(dataset + ' ' + str(output_dict[dataset]) + "\n")
    output.close()
    