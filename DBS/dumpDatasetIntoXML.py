#!/usr/bin/env python
import sys, getopt
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *

datasetpath = None
dbsargs = {}
dbsargs['url']   = 'http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet'
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

se          = 'srm.cern.ch'

try:
    outputname = datasetpath.replace('/','_')[1:]+'.xml'
    outputfile = file(outputname.replace('PreCSA08','CSA08'),'w')
    output = ""
    api = DbsApi(dbsargs)
    try:
        blocks = api.listBlocks(dataset=datasetpath,block_name="*",storage_element_name=se);
    except:
        blocks = []
    for block in blocks:
        output += api.listDatasetContents(datasetpath,block['Name'])

    
    newoutput = output.replace('PreCSA08','CSA08')
    outputfile.write(newoutput)
    outputfile.close()
except DbsApiException, ex:
    print "Caught API Exception %s: %s "  % (ex.getClassName(),
    ex.getErrorMessage() )
    if ex.getErrorCode() not in (None, ""):
        print "DBS Exception Error Code: ", ex.getErrorCode()

