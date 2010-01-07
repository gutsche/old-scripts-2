#!/usr/bin/env python
import sys, getopt
from DBSAPI.dbsApi import DbsApi
from DBSAPI.dbsException import *
from DBSAPI.dbsApiException import *

xml = None
dbsargs = {}
dbsargs['url']   = 'https://cmsdbsprod.cern.ch:8443/cms_dbs_prod_global_writer/servlet/DBSServlet'
dbsargs['level'] = 'DBSINFO'

try:
    myopts, myargs = getopt.getopt(sys.argv[1:], "", ["xml="])
except getopt.GetoptError:
    print "Please specify --xml"
    sys.exit(2)

for myopt, myarg in myopts :
    if myopt == "--xml" :
        xml = myarg

if xml == None:
    print "Please specify --xml"
    sys.exit(2)

se          = 'srm.cern.ch'

try:
    xmlcontent = open(xml).read()
    api = DbsApi(dbsargs)
    api.insertDatasetContents(xmlcontent)
except DbsApiException, ex:
    print "Caught API Exception %s: %s "  % (ex.getClassName(),
    ex.getErrorMessage() )
    if ex.getErrorCode() not in (None, ""):
        print "DBS Exception Error Code: ", ex.getErrorCode()

