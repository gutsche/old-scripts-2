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
'/EG/Run2010A-v1/RAW',
'/JetMETTau/Run2010A-v1/RAW',
'/MinimumBias/Run2010A-v1/RAW',
'/Mu/Run2010A-v1/RAW',
'/MuOnia/Run2010A-v1/RAW',
'/ZeroBias/Run2010A-v1/RAW',
'/JetMET/Run2010A-v1/RAW',
'/BTau/Run2010A-v1/RAW'
]

recodatasets = [
'/EG/Run2010A-PromptReco-v4/RECO',
'/JetMETTau/Run2010A-PromptReco-v4/RECO',
'/MinimumBias/Run2010A-PromptReco-v4/RECO',
'/Mu/Run2010A-PromptReco-v4/RECO',
'/MuOnia/Run2010A-PromptReco-v4/RECO',
'/ZeroBias/Run2010A-PromptReco-v4/RECO',
'/JetMET/Run2010A-PromptReco-v4/RECO',
'/BTau/Run2010A-PromptReco-v4/RECO'
]


def queryForRunsAndSizeAndEvents(runs,dict,dataset):

    for run in runs :

        commandline = "dbs search --query=\"find sum(file.size),sum(file.numevents) where dataset = " + dataset + " and run = " + str(run) + "\" --noheader"
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
