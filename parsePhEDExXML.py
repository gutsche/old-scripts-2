#!/usr/bin/env python

import sys
import DBSAPI.dbsApi
from xml.dom import minidom
#xmldoc = minidom.parse('custodial_short.xml')
#xmldoc = minidom.parse('custodial.xml')
xmldoc = minidom.parse('complete.xml')

def cycle_encode(major,minor) :
    return major*100+minor

def cycle_decode(cycle):
    return [int(cycle/100),int(cycle%100)]

def cycle_print(cycle):
    result = cycle_decode(cycle)
    return 'CMSSW_'+str(result[0])+'_'+str(result[1])

#def cycle_print(major,minor):
#    return 'CMSSW_'+str(major)+'_'+str(minor)


def queryDBS(api,dataset):
    dataset_array = dataset.split('/')
    if len(dataset_array) < 4 :
        print 'dataset:',dataset,'does not follow convention, ignored'
        return None
    primary = dataset_array[1]
    processed = dataset_array[2]
    tier = dataset_array[3]

    procDSs = api.listProcessedDatasets(primary,tier,processed)
    if len(procDSs) > 1:
        print 'more than one processed dataset found for:',dataset,'. Taking the first!'
    if len(procDSs) < 1:
        print 'less than one processed dataset found for:',dataset,'. Exiting!'
        return None
        #sys.exit(1)
    cycle = 0
    for algo in procDSs[0]['AlgoList']:
        app_array = algo['ApplicationVersion'].split('_')
        # take highest cycle
        temp_cycle = cycle_encode(int(app_array[1]),int(app_array[2]))
        if cycle < temp_cycle:
            cycle = temp_cycle
    blocks = api.listBlocks(str(dataset))
    if len(blocks) < 1:
        print 'No blocks found for dataset:',dataset,'! Exiting!'
        return None
        # sys.exit(1)
    files = api.listFiles(blockName=blocks[0]['Name'])
    if len(files) < 1:
        print 'No files found for block:',blocks[0]['Name'],'! Exiting!'
        return None
        # sys.exit(1)
    lfn_array = files[0]['LogicalFileName'].split('/')
    return [cycle_print(cycle),lfn_array[2]]

datasets = []
custodial = {}
non_custodial = {}

for phedex in xmldoc.childNodes :
    for block in phedex.childNodes:
        dataset = block.attributes['name'].value.split('#')[0]
        for replica in block.childNodes:
            if replica.attributes['complete'].value == 'y':
                if dataset not in datasets:
                    datasets.append(dataset)
                size = float(replica.attributes['bytes'].value)/1024./1024./1024./1024.
                if replica.attributes['custodial'].value == 'y':
                    if dataset in custodial.keys() :
                        print 'PhEDEx parsing: add to custodial dataset:',dataset,'size:',size
                        custodial[dataset] += size
                    else :
                        print 'PhEDEx parsing: custodial dataset:',dataset,'with size:',size
                        custodial[dataset] = size
                else:
                    if dataset in non_custodial.keys() :
                        print 'PhEDEx parsing: add to non_custodial dataset:',dataset,'size:',size
                        non_custodial[dataset] += size
                    else :
                        print 'PhEDEx parsing: non_custodial dataset:',dataset,'with size:',size
                        non_custodial[dataset] = size

#query dbs for dataset properties
dbs                = 'http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet'
# init dbs
args = {}
args['url']   = dbs
args['level'] = 'CRITICAL'
api = DBSAPI.dbsApi.DbsApi(args)

output_custodial = {}
output_non_custodial = {}

for dataset in datasets:
    print 'dataset:',dataset
    result = queryDBS(api,dataset)
    if result == None:
        continue
    tier = dataset.split('/')[3]
    if dataset in custodial.keys():
        if result[0] in output_custodial.keys():
            if result[1] in output_custodial[result[0]].keys() :
                if tier in output_custodial[result[0]][result[1]]:
                    output_custodial[result[0]][result[1]][tier] += custodial[dataset]
                else :
                    output_custodial[result[0]][result[1]][tier] = custodial[dataset]
            else :
                output_custodial[result[0]][result[1]] = { tier : custodial[dataset] }
        else :
            output_custodial[result[0]] = { result[1] : { tier : custodial[dataset] } }
    else:
        if result[0] in output_non_custodial.keys():
            if result[1] in output_non_custodial[result[0]].keys() :
                if tier in output_non_custodial[result[0]][result[1]]:
                    output_non_custodial[result[0]][result[1]][tier] += non_custodial[dataset]
                else :
                    output_non_custodial[result[0]][result[1]][tier] = non_custodial[dataset]
            else :
                output_non_custodial[result[0]][result[1]] = { tier : non_custodial[dataset] }
        else :
            output_non_custodial[result[0]] = { result[1] : { tier : non_custodial[dataset] } }

# output

print ""
print "Custodial"
print ""
for cycle in output_custodial.keys():
    for type in output_custodial[cycle].keys():
        for tier in output_custodial[cycle][type].keys():
            print cycle,type,tier,output_custodial[cycle][type][tier]

print ""
print "Non-Custodial"
print ""
for cycle in output_non_custodial.keys():
    for type in output_non_custodial[cycle].keys():
        for tier in output_non_custodial[cycle][type].keys():
            print cycle,type,tier,output_non_custodial[cycle][type][tier]
