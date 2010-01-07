#!/usr/bin/env python

import sys, os, getopt, glob

def main(argv) :
    """
    
    runWithCondor
    
    runs cmssw parameter set with condor and splits jobs according to settings

    required parameters         :
    --parameter-set <filename>  : parameter-set filename
    --total         <number>    : total number of events to process
    --events        <number>    : number of events per job

    optional parameters         :
    --help (-h)                 : help
    --debug (-d)                : debug statements
    
    """

    # default
    parameter_set = None
    total = 0
    events = 0
    debug = 0

    try:
        opts, args = getopt.getopt(argv, "", ["help", "debug", "parameter-set=", "events=", "total="])
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
            parameter_set = str(arg)
        elif opt == "--events" :
            try:
                events = int(arg)
            except:
                print ''
                print '    --events didn\'t specify a number'
                print main.__doc__
                sys.exit()
        elif opt == "--total" :
            try:
                total = int(arg)
            except:
                print ''
                print '    --total didn\'t specify a number'
                print main.__doc__
                sys.exit()

    # check for command line parameters
    if parameter_set == None or total == 0 or events == 0 :
        print main.__doc__
        sys.exit(2)

    # get CMSSW_BASE
    try:
        CMSSW_BASE = os.environ['CMSSW_BASE']
    except:
        print ''
        print 'CMSSW environment not initialized'
        sys.exit()

    # calculate number of jobs
    jobs = int(total/events)+1
    skip = int(total/jobs)+1

    # header printout
    print ''
    print '     runWithCondor'
    print ''
    print '     executing           :',parameter_set
    print ''
    print '     running',jobs,'jobs over each',events,'events'
    print ''

    # create main script
    main_script = open('main.sh','w')
    main_script.write('#!/bin/bash\n')
    main_script.write('#\n')
    main_script.write('# main script, parameters:\n')
    main_script.write('#\n')
    main_script.write('# 1: condor cluster number\n')
    main_script.write('# 2: condor process number\n')
    main_script.write('# 3: parameter set\n')
    main_script.write('# 4: events to process\n')
    main_script.write('# 5: events to skip\n')
    main_script.write('START_TIME=`/bin/date`\n')
    main_script.write('echo "started at $START_TIME"\n')
    main_script.write('source /uscmst1/prod/sw/cms/shrc prod\n')
    main_script.write('cd ' + CMSSW_BASE + '\n')
    main_script.write('eval `scramv1 runtime -sh`\n')
    main_script.write('cd -\n')
    main_script.write('echo "manipulate cmssw parameter set $3 to process $4 events and skip $5 events"\n')
    main_script.write('python setEventsNSkip.py $3 $4 $5\n')
    main_script.write('echo "run: cmsRun cmssw.py > $1_$2.log 2>&1"\n')
    main_script.write('cmsRun cmssw.py > $1_$2.log 2>&1\n')
    main_script.write('exitcode=$?\n')
    main_script.write('# zip logfile\n')
    main_script.write('gzip -9 $1_$2.log\n')
    main_script.write('mv output.root $1_$2.root\n')
    main_script.write('touch $1_$2.root\n')
    main_script.write('END_TIME=`/bin/date`\n')
    main_script.write('echo "ended at $END_TIME with exit code $exitcode"\n')
    main_script.write('exit $exitcode\n')
    main_script.close()

    os.chmod('main.sh',0755)

    # home dir
    home = os.environ['HOME']

    # create jdl
    file = open('condor.jdl','w')
    file.write('universe              = vanilla\n')
    file.write('Executable            = main.sh\n')
    file.write('should_transfer_files = YES\n')
    file.write('WhenToTransferOutput  = ON_EXIT_OR_EVICT\n')
    file.write('transfer_input_files  = ' + home + '/scripts/setEventsNSkip.py,' + parameter_set + '\n')
    file.write('transfer_output_files  = $(cluster)_$(process).log.gz,$(cluster)_$(process).root\n')
    file.write('Output                = $(cluster)_$(process).stdout\n')
    file.write('Error                 = $(cluster)_$(process).stderr\n')
    file.write('Log                   = $(cluster)_$(process).condor\n')
    file.write('Requirements          = Memory >= 199 && OpSys == "LINUX" && (Arch != "DUMMY")\n')
    file.write('notification          = never\n')
    for job in range(jobs):
        file.write('\n')
        file.write('Arguments             = $(cluster) $(process) ' + parameter_set + ' ' + str(events) + ' ' + str(job*skip) + '\n')
        file.write('Queue\n')
    file.close()

if __name__ == '__main__' :
    main(sys.argv[1:])
