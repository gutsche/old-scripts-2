#!/usr/bin/env python

import sys, os

def pickleParameterSet(parameter_set):
    """

    pickle parameter set

    """

    import FWCore.ParameterSet.Config as cms
    import pickle

    # load parameter-set
    try:
        process = cms.include(parameter_set)
    except:
        print ''
        print 'ParameterSet: ',parameter_set,'could not be converted to python dictionary'
        print ''
        sys.exit(1)

    # pickle parameter-set by replacing cfg extension with pkl extension
    file = open(parameter_set.replace('cfg','pkl'),'w')
    pickle.dump(process,file)

def main(argv) :
    """
    
    pickleParameterSet
    
    import parameter-set, convert it to python dictionary and pickle it

    required parameters
    --parameter-set <name> : name and path of input parameter-set

    optional parameters    :
    --help (-h)            : help
    --debug (-d)           : debug statements
    
    """

    # default
    parameter_set = ''
    debug = 0

    import getopt

    try:
        opts, args = getopt.getopt(argv, "", ["help", "debug", "parameter-set="])
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
        elif opt == "--parameter-set" :
            parameter_set = arg

    if parameter_set == '' :
        print main.__doc__
        sys.exit(2)

    pickleParameterSet(parameter_set)

if __name__ == '__main__' :
    main(sys.argv[1:])
