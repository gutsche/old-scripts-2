#!/usr/bin/env python2.4

import sys, os, getopt, glob

def main(argv) :
    """
    
    generatePoolSourceFromFiles
    
    take a file or a wildcard expression in \"\" and generate PoolSource
    execute in directory of files

    required parameters
    --output <name>                        :       output file name
    --file <names>                         :       file names (single file or wildcard expression in \"

    optional parameters                    :
    --absolute                             :       use absolute paths
    --help (-h)                            :       help
    --debug (-d)                           :       debug statements
    
    """

    # default
    filename = ''
    absolute = 0
    debug = 0

    try:
        opts, args = getopt.getopt(argv, "", ["help", "debug", "file=", "output=", "absolute"])
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
        elif opt == "--absolute" :
            absolute = 1
        elif opt == "--file" :
            logfilename = arg
        elif opt == "--output" :
            outputname = arg

    if logfilename == '' :
        print main.__doc__
        sys.exit(2)

    output = ''

    if absolute :
        absolute_dir = os.getcwd()
        
    output += 'EdmFastMerge -o '+outputname
    for filename in glob.glob(logfilename) :
        if absolute :
            output += ' file:'+absolute_dir+'/'+filename
        else :
            output += ' file:'+filename
    output += '\n'
    print output




        

if __name__ == '__main__' :
    main(sys.argv[1:])
