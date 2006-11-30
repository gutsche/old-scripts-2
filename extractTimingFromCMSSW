#!/usr/bin/python

import sys, os, getopt, glob

def main(argv) :
    """
    
    extractTimingFromCMSSW
    
    activate timing service in CMSSW and use this python script tp average timing per module

    required parameters
    --logfile <names>                         :       logfile names, single name or wildcard expression in \"

    optional parameters                       :
    --help (-h)                               :       help
    --debug (-d)                              :       debug statements
    
    """

    # default
    logfilename = ''
    debug = 0

    try:
        opts, args = getopt.getopt(argv, "", ["help", "debug", "logfile="])
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
        elif opt == "--logfile" :
            logfilename = arg

    if logfilename == '' :
        print main.__doc__
        sys.exit(2)
        
    # instantiate dictionaries and counters
    timeEvent       = 0
    timeEventCount  = 0
    timeModuleDict  = {}
    timeModuleCount = {}


    for filename in glob.glob(logfilename) :
        try:
            logfile = open(filename)
        except IOError:
            print ''
            print 'Could not open logfile: ',logfilename
            print main.__doc__
            sys.exit(2)

        line = logfile.readline()
        tempeventtime = 0
        addedmoduletime = 0
        while line :
            line = line.strip()
            if line.count('TimeEvent>') > 0 :
                if debug :
                    print 'TimeEvent line:',line
                linearray = line.split()
                try:
                    tempeventtime = float(linearray[-1])
                    if tempeventtime < 1000000000. :
                        timeEvent      += tempeventtime
                        timeEventCount += 1
                except ValueError:
                    print 'line:',line,'could not be used to extract time of the event'
            if line.count('TimeModule>') > 0 :
                if debug :
                    print 'TimeModule line:',line
                try:
                    linearray = line.split()
                    if len(linearray) == 6 :
                        temptime = float(linearray[-1])
                        addedmoduletime += temptime
                        tempmodule = linearray[-3]
                        if tempmodule in timeModuleDict.keys() :
                            timeModuleDict[tempmodule] += temptime
                        else :
                            timeModuleDict[tempmodule] = temptime
                        if tempmodule in timeModuleCount.keys() :
                            timeModuleCount[tempmodule] += 1
                        else :
                            timeModuleCount[tempmodule] = 1
                except ValueError:
                    print 'line:',line,'could not be used to extract time of a module'
            line = logfile.readline()
            if tempeventtime != 0 :
                tempeventtime = 0
                addedmoduletime = 0

    for module in timeModuleDict.keys() :
        print 'module: %30s time: %7.5f percentage: %03.1f' % (module, timeModuleDict[module]/timeModuleCount[module], (timeModuleDict[module]/timeModuleCount[module])/(timeEvent/timeEventCount)*100)

    print 'events: %30d time: %7.5f' % (timeEventCount, timeEvent/timeEventCount)

    # calculate time per event for RS and Ckf

    rsmodules = ['roadSearchSeeds','rawRoadSearchClouds','cleanRoadSearchClouds','rsTrackCandidates','rsWithMaterialTracks']
    ckfmodules = ['globalMixedSeeds','ckfTrackCandidates','ctfWithMaterialTracks']

    rsTimePerEvent = 0.
    for rsmodule in rsmodules :
        if rsmodule in timeModuleDict.keys() :
            rsTimePerEvent += timeModuleDict[rsmodule]/timeModuleCount[rsmodule]

    ckfTimePerEvent = 0.
    for ckfmodule in ckfmodules :
        if ckfmodule in timeModuleDict.keys() :
            ckfTimePerEvent += timeModuleDict[ckfmodule]/timeModuleCount[ckfmodule]

    print ''
    if  rsTimePerEvent != 0 :
        print 'module: %30s time: %7.5f percentage: %03.1f' % ('RS', rsTimePerEvent, rsTimePerEvent/(timeEvent/timeEventCount)*100)
    if  ckfTimePerEvent != 0 :
        print 'module: %30s time: %7.5f percentage: %03.1f' % ('CKF', ckfTimePerEvent, ckfTimePerEvent/(timeEvent/timeEventCount)*100)

    # column for overview table
    print ''
    print 'Column for overview table, orderer after:'
    print 'globalMixedSeeds ckfTrackCandidates ctfWithMaterialTracks roadSearchSeeds rawRoadSearchClouds cleanRoadSearchClouds rsTrackCandidates rsWithMaterialTracks'
    print ''
    module = 'globalMixedSeeds'
    print timeModuleDict[module]/timeModuleCount[module]
    module = 'ckfTrackCandidates'
    print timeModuleDict[module]/timeModuleCount[module]
    module = 'ctfWithMaterialTracks'
    print timeModuleDict[module]/timeModuleCount[module]
    module = 'roadSearchSeeds'
    print timeModuleDict[module]/timeModuleCount[module]
    module = 'rawRoadSearchClouds'
    print timeModuleDict[module]/timeModuleCount[module]
    module = 'cleanRoadSearchClouds'
    print timeModuleDict[module]/timeModuleCount[module]
    module = 'rsTrackCandidates'
    print timeModuleDict[module]/timeModuleCount[module]
    module = 'rsWithMaterialTracks'
    print timeModuleDict[module]/timeModuleCount[module]

        

if __name__ == '__main__' :
    main(sys.argv[1:])
