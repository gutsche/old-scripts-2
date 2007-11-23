#!/usr/bin/env python2.4

import sys, os, getopt
import DBSAPI.dbsApi

def main(argv) :
    """
    
    newBlocks
    
    compare ascii files of blocks to dbs content of dataset, put out OnlyBlocks block for workflow

    required parameters
    --path <path>                             :       datasetpath allowing wildcards in \"
    --ascii <file>                            :       ascii file of blocks, one block per line

    optional parameters                       :
    --dbs <dbs>                               :       dbs url (default: http://cmssrv17.fnal.gov:8989/DBS_1_0_5_STABLE/servlet/DBSServlet)
    --se <se>                                 :       target se url
    --help (-h)                               :       help
    --debug (-d)                              :       debug statements
    
    """

    # default
    dbs                = 'http://cmssrv46.fnal.gov:8080/DBS/servlet/DBSServlet'
    se                 = 'cmssrm.fnal.gov'
    path               = None
    ascii              = None
    debug              = 0

    try:
        opts, args = getopt.getopt(argv, "", ["help", "debug", "path=", "dbs=", "ascii=", "se="])
    except getopt.GetoptError:
        print main.__doc__
        sys.exit(2)

    # check command line parameter
    for opt, arg in opts :
        if opt == "--help" :
            print main.__doc__
            sys.exit()
        elif opt == "--debug" :
            debug = 1
        elif opt == "--dbs" :
            dbs = arg
        elif opt == "--path" :
            path = arg
        elif opt == "--ascii" :
            ascii = arg
        elif opt == "--se" :
           se = arg

    if path == None or ascii == None :
        print main.__doc__
        sys.exit(1)
        
    ascii_blocks = readInAsciiFile(ascii)

    # init dbs
    args = {}
    args['url']   = dbs
    args['level'] = 'CRITICAL'

    try:
        api = DBSAPI.dbsApi.DbsApi(args)
        if debug:
            print ''
            print 'Connected dbs:',dbs
    except:
        print ''
        print 'Problem connecting DBS'
        sys.exit(1)

    blocks = queryDataset(api,path,se)

    new_blocks = [ block for block in blocks if block not in ascii_blocks ]


    if len(new_blocks) > 0 :
        print '        <Parameter Name=\"OnlyBlocks\">'
        for block in range(len(new_blocks)) :
            if block == len(new_blocks)-1 :
                print '               '+new_blocks[block]
            else :
                print '               '+new_blocks[block]+','
        print '        </Parameter>'

    writeToAsciiFile(ascii,blocks)

def queryDataset(api,datasetpath,se):
    """
    query dataset
    """
    
    try:
        blocks = api.listBlocks(dataset=datasetpath,block_name="*",storage_element_name=se);
    except:
        blocks = []
    return [ block['Name'] for block in blocks ]

def readInAsciiFile(filename):

    try:
        file = open(filename,)
    except IOError:
        print 'Ascii file:',filename,'could not be created, using empty file!'
        return []

    return [ line.split()[0].strip() for line in file.readlines() ]

def writeToAsciiFile(filename,blocks):

    try:
        file = open(filename,'w')
    except IOError:
        print 'Ascii file:',filename,'could not be created'
        sys.exit(1)

    for block in blocks:
        file.write(block+'\n')

    file.close()

if __name__ == '__main__' :
    main(sys.argv[1:])

