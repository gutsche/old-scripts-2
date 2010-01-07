#!/usr/bin/env python
"""
Migrate dataset from source to target DBS url

"""
import sys,os,getopt
import time
from ProdCommon.DataMgmt.DBS.DBSWriter import DBSWriter

################################################### 
if __name__ == '__main__':
                                                                                                   
    usage="\n Description: this script migrates a dataset from source to target DBS url <options> \n Options: \n --dataset=<workflowName> \t dataset \n --source=<dbs url> \t\t source dbs url \n --target=<dbs url> \t\t target dbs url\n"
    valid = ['dataset=', 'source=', 'target=']
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", valid)
    except getopt.GetoptError, ex:
        print usage
        print str(ex)
        sys.exit(1)

    dataset = None
    source  = None
    target  = None
    
    for opt, arg in opts:
        if opt == "--dataset":
            dataset = arg
        if opt == "--source":
            source = arg
        if opt == "--target":
            target = arg

    if dataset == None or source == None or target == None :
        print usage
        sys.exit(1)

    print 'Migrating dataset: %s from %s to %s' % (dataset,source,target)
        

    
    dbsWriter = DBSWriter(target)

    try:
        dbsWriter.importDataset(
            source,
            dataset,
            target)
    except Exception, ex:
        msg = "Error importing dataset to be processed into local DBS\n"
        msg += "Source Dataset: %s\n" % dataset
        msg += "Source DBS: %s\n" % source
        msg += "Destination DBS: %s\n" % target
        msg += str(ex)
        logging.error(msg)
        sys.exit(1)
