#!/usr/bin/env python2.4

import sys, os, glob, getopt

def main(argv) :
    """
    
    combineWorkflows
    
    combine several workflows into a single workflow

    required parameters
    --workflows      <name>     : name if input workflows, enclose in \"

    optional parameters         :
    --output-filename           : name of output workflow file name (default: workflows.xml)
    --help (-h)                 : help
    --debug (-d)                : debug statements
    
    """

    # defaults
    workflows = ''
    output_filename = 'workflows.xml'
    debug = 0

    try:
        opts, args = getopt.getopt(argv, "", ["help", "debug", "workflows=", "output-filename="])
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
        elif opt == "--workflows" :
            workflows = arg
        elif opt == "--output-filename" :
            output_filename = arg

    if workflows == '' :
        print ''
        print 'Please give workflow names to combine!'
        print ''
        print main.__doc__
        sys.exit(2)

    try:
        output = open(output_filename,'w')
    except IOError:
        print ''
        print 'Could not open output workflow file: ',output_filename
        print main.__doc__
        sys.exit(2)

    # add first lines to file
    output.write('<?xml version="1.0" ?>\n')
    output.write('<RelValSpec>\n')

    for filename in glob.glob(workflows) :
        if filename != output_filename :
            try:
                file = open(filename)
            except IOError:
                print ''
                print 'Could not open workflow file: ',filename
                print main.__doc__
                sys.exit(2)
            print 'Process workflow file:',filename
            lines = file.readlines()
            for line in lines[2:-1] :
                output.write(line)

    # write last line
    output.write('</RelValSpec>\n')

if __name__ == '__main__' :
    main(sys.argv[1:])
