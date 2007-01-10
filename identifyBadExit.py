#!/usr/bin/python

import sys, os, getopt, glob

def main(argv) :
    """
    
    identifyBadExit
    
    Identifies Condor jobs which exited with a non-zero exit code.

    required parameters
    --condor <names>                          :       condor logfile names, single name or wildcard expression in \"

    optional parameters                       :
    --help                                    :       help
    --debug                                   :       debug statements
    --isolate                                 :       move all associated files with non-zero exit code to the subdirectory isolated
    
    """

    # default
    condorname = ''
    debug = 0
    isolate = 0

    # variable setup
    files = ["","","","",""]

    try:
        opts, args = getopt.getopt(argv, "", ["help", "debug", "isolate", "condor="])
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
        elif opt == "--isolate" :
            isolate = 1
        elif opt == "--condor" :
            condorname = arg

    if condorname == '' :
        print main.__doc__
        sys.exit(2)
        
    for filename in glob.glob(condorname) :
        try:
            condorfile = open(filename)
        except IOError:
            print ''
            print 'Could not open condorfile: ',condorname
            print main.__doc__
            sys.exit(2)

        line = condorfile.readline()
        time = {}
        while line :
            line = line.strip()
            if line.count('return value') > 0 :
                if debug :
                    print 'Exit status line:',line
                try:
                    linearray = line.split()
                    if linearray[-1] != '0)' :
                        print 'Condor log',filename,'reports an exit status of',linearray[-1].split(')')[0]
                        if isolate :
                            filegroup=(filename.split("."))[0]
                            files[0] = filename
                            files[1] = ".".join([filegroup,'log'])
                            files[2] = ".".join([filegroup,'cfg'])
                            files[3] = ".".join([filegroup,'stderr'])
                            files[4] = ".".join([filegroup,'stdout'])
                            try:
                                os.mkdir('isolated')
                            except:
                                # Do nothing if it already exists
                                dummy=1
                            for file in files:
                                os.rename(file,"/".join(['isolated',file]))
                            if debug:
                                print files,'moved to the isolated subdirectory'
                except ValueError:
                    print 'line:',line,'could not be used to extract exit status'
            line = condorfile.readline()
    
if __name__ == '__main__' :
    main(sys.argv[1:])
