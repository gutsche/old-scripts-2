#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, json, getopt


jsonfilename = None

opts, args = getopt.getopt(sys.argv[1:], "", ["json="])

for opt, arg in opts :
    if opt == "--json" :
        jsonfilename = arg
        
if jsonfilename == None :
    print ''
    print 'Please specify json filename with with run array with --json'
    print ''
    sys.exit(2)

rawdatasets = [
'/DoubleElectron/Run2011A-v1/RAW',
'/DoubleMu/Run2011A-v1/RAW',
'/ElectronHad/Run2011A-v1/RAW',
'/HT/Run2011A-v1/RAW',
'/Jet/Run2011A-v1/RAW',
'/MET/Run2011A-v1/RAW',
'/MinimumBias/Run2011A-v1/RAW',
'/MuEG/Run2011A-v1/RAW',
'/MuHad/Run2011A-v1/RAW',
'/MuOnia/Run2011A-v1/RAW',
'/MultiJet/Run2011A-v1/RAW',
'/Photon/Run2011A-v1/RAW',
'/PhotonHad/Run2011A-v1/RAW',
'/SingleElectron/Run2011A-v1/RAW',
'/SingleMu/Run2011A-v1/RAW',
'/Tau/Run2011A-v1/RAW',
'/TauPlusX/Run2011A-v1/RAW',
'/BTag/Run2011A-v1/RAW',
'/ForwardTriggers/Run2011A-v1/RAW',
]

recodatasets = [
'/DoubleElectron/Run2011A-PromptReco-v5/RECO',
'/DoubleMu/Run2011A-PromptReco-v5/RECO',
'/ElectronHad/Run2011A-PromptReco-v5/RECO',
'/HT/Run2011A-PromptReco-v5/RECO',
'/Jet/Run2011A-PromptReco-v5/RECO',
'/MET/Run2011A-PromptReco-v5/RECO',
'/MinimumBias/Run2011A-PromptReco-v5/RECO',
'/MuEG/Run2011A-PromptReco-v5/RECO',
'/MuHad/Run2011A-PromptReco-v5/RECO',
'/MuOnia/Run2011A-PromptReco-v5/RECO',
'/MultiJet/Run2011A-PromptReco-v5/RECO',
'/Photon/Run2011A-PromptReco-v5/RECO',
'/PhotonHad/Run2011A-PromptReco-v5/RECO',
'/SingleElectron/Run2011A-PromptReco-v5/RECO',
'/SingleMu/Run2011A-PromptReco-v5/RECO',
'/Tau/Run2011A-PromptReco-v5/RECO',
'/TauPlusX/Run2011A-PromptReco-v5/RECO',
'/BTag/Run2011A-PromptReco-v5/RECO',
'/ForwardTriggers/Run2011A-PromptReco-v5/RECO',

]

aoddatasets = [
'/DoubleElectron/Run2011A-PromptReco-v5/AOD',
'/DoubleMu/Run2011A-PromptReco-v5/AOD',
'/ElectronHad/Run2011A-PromptReco-v5/AOD',
'/HT/Run2011A-PromptReco-v5/AOD',
'/Jet/Run2011A-PromptReco-v5/AOD',
'/MET/Run2011A-PromptReco-v5/AOD',
'/MinimumBias/Run2011A-PromptReco-v5/AOD',
'/MuEG/Run2011A-PromptReco-v5/AOD',
'/MuHad/Run2011A-PromptReco-v5/AOD',
'/MuOnia/Run2011A-PromptReco-v5/AOD',
'/MultiJet/Run2011A-PromptReco-v5/AOD',
'/Photon/Run2011A-PromptReco-v5/AOD',
'/PhotonHad/Run2011A-PromptReco-v5/AOD',
'/SingleElectron/Run2011A-PromptReco-v5/AOD',
'/SingleMu/Run2011A-PromptReco-v5/AOD',
'/Tau/Run2011A-PromptReco-v5/AOD',
'/TauPlusX/Run2011A-PromptReco-v5/AOD',
'/BTag/Run2011A-PromptReco-v5/AOD',
'/ForwardTriggers/Run2011A-PromptReco-v5/AOD',
]


def queryForRunsAndSizeAndEvents(runs,dict,dataset):

    for run in runs :

        commandline = "dbs search --query=\"find sum(block.size),sum(block.numevents) where dataset = " + dataset + " and run = " + str(run) + "\" --noheader"
        args = shlex.split(commandline)
        output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)

        for line in output.communicate()[0].split('\n') :
            if len(line) > 0 :
                array = line.split()
                if len(array) == 2 :
                    size = float(array[0])/1024./1024.
                    events = int(array[1])
                    tmp = {'size' : size , 'events' : events}
                    if run in dict.keys() :
                        dict[run][dataset] = tmp
                    else :
                        dict[run] = { dataset : tmp }
                    print 'run:',run,'dataset:',dataset,'size:',tmp['size'],'events:',tmp['events']
    return
    
runs = json.load(open(jsonfilename))
sorted_runs = runs
sorted_runs.sort()
    
print ""
print "Query for raw datasets:"
print ""
raw = {}
for dataset in rawdatasets:
    queryForRunsAndSizeAndEvents(sorted_runs,raw,dataset)

print ""
print "Query for reco datasets:"
print ""
reco = {}
for dataset in recodatasets:
    queryForRunsAndSizeAndEvents(sorted_runs,reco,dataset)

print ""
print "Query for aod datasets:"
print ""
aod = {}
for dataset in aoddatasets:
    queryForRunsAndSizeAndEvents(sorted_runs,aod,dataset)
    
print ""
print "Raw datasets:"

result = "run "
for dataset in rawdatasets:
    result += dataset + " "
result += "total"
print ""
print result
print ""

for run in sorted_runs :
    result = str(run) + " "
    if run in raw.keys() :
        total_size = 0.
        total_events = 0
        for dataset in rawdatasets:
            if dataset in raw[run].keys() :
                total_size += raw[run][dataset]['size']
                total_events += raw[run][dataset]['events']
                if raw[run][dataset]['events'] > 0 :
                    sizePerEvent =  raw[run][dataset]['size']/raw[run][dataset]['events']
                else:
                    sizePerEvent = 0.
                result += "%.3f " % sizePerEvent
            else :
                result += "0.000 "
        if total_events > 0 :
            total_sizePerEvent = total_size / total_events
        else :
            total_sizePerEvent = 0.
        result += "%.3f " % total_sizePerEvent
    else :
        for dataset in rawdatasets:
            result += "0.000 "
        result += "0.000 "    
    print result
    
print ""
print "Reco datasets:"

result = "run "
for dataset in recodatasets:
    result += dataset + " "
result += "total"
print ""
print result
print ""

for run in sorted_runs :
    result = str(run) + " "
    if run in reco.keys() :
        total_size = 0.
        total_events = 0
        for dataset in recodatasets:
            if dataset in reco[run].keys() :
                total_size += reco[run][dataset]['size']
                total_events += reco[run][dataset]['events']
                if reco[run][dataset]['events'] > 0 :
                    sizePerEvent =  reco[run][dataset]['size']/reco[run][dataset]['events']
                else:
                    sizePerEvent = 0.
                result += "%.3f " % sizePerEvent
            else :
                result += "0.000 "
        if total_events > 0 :
            total_sizePerEvent = total_size / total_events
        else :
            total_sizePerEvent = 0.
        result += "%.3f " % total_sizePerEvent
    else :
        for dataset in recodatasets:
            result += "0.000 "
        result += "0.000 "    
    print result

print ""
print "AOD datasets:"

result = "run "
for dataset in aoddatasets:
    result += dataset + " "
result += "total"
print ""
print result
print ""

for run in sorted_runs :
    result = str(run) + " "
    if run in aod.keys() :
        total_size = 0.
        total_events = 0
        for dataset in aoddatasets:
            if dataset in aod[run].keys() :
                total_size += aod[run][dataset]['size']
                total_events += aod[run][dataset]['events']
                if aod[run][dataset]['events'] > 0 :
                    sizePerEvent =  aod[run][dataset]['size']/aod[run][dataset]['events']
                else:
                    sizePerEvent = 0.
                result += "%.3f " % sizePerEvent
            else :
                result += "0.000 "
        if total_events > 0 :
            total_sizePerEvent = total_size / total_events
        else :
            total_sizePerEvent = 0.
        result += "%.3f " % total_sizePerEvent
    else :
        for dataset in aoddatasets:
            result += "0.000 "
        result += "0.000 "    
    print result
