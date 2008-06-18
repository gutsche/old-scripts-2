#!/usr/bin/env python
import sys, getopt
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *

datasetpath = None
dbsargs = {}
dbsargs['url']   = 'https://cmsdbsprod.cern.ch:8443/cms_dbs_prod_global_writer/servlet/DBSServlet'
dbsargs['level'] = 'CRITICAL'

try:
    myopts, myargs = getopt.getopt(sys.argv[1:], "", ["dataset="])
except getopt.GetoptError:
    print "Please specify --dataset"
    sys.exit(2)

for myopt, myarg in myopts :
    if myopt == "--dataset" :
        datasetpath = myarg

if datasetpath == None:
    print "Please specify --dataset"
    sys.exit(2)

cern_se          = 'srm.cern.ch'

try:
    api = DbsApi(dbsargs)
    try:
        blocks = api.listBlocks(dataset=datasetpath,block_name="*",storage_element_name="*");
    except:
        blocks = []
    for block in blocks:
        for se in block['StorageElementList'] :
            if se['Name'] != cern_se :
                api.deleteReplicaFromBlock(block['Name'],se['Name'])
except DbsApiException, ex:
    print "Caught API Exception %s: %s "  % (ex.getClassName(),
    ex.getErrorMessage() )
    if ex.getErrorCode() not in (None, ""):
        print "DBS Exception Error Code: ", ex.getErrorCode()

