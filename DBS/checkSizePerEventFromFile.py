#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, getopt

filename=None

opts, args = getopt.getopt(sys.argv[1:], "", ["file="])

for opt, arg in opts :
    if opt == "--file" :
        filename = arg
        
if filename == None :
    print ''
    print 'Please specify the name of the input file with --file'
    print ''
    sys.exit(1)

rawdatasets = [
'/EG/Run2010A-v*/RAW',
'/JetMETTau/Run2010A-v*/RAW',
'/MinimumBias/Run2010A-v*/RAW',
'/Mu/Run2010A-v*/RAW',
'/MuOnia/Run2010A-v*/RAW',
'/ZeroBias/Run2010A-v*/RAW'
]

recodatasets = [
'/EG/Run2010A-PromptReco-v*/RECO',
'/JetMETTau/Run2010A-PromptReco-v*/RECO',
'/MinimumBias/Run2010A-PromptReco-v*/RECO',
'/Mu/Run2010A-PromptReco-v*/RECO',
'/MuOnia/Run2010A-PromptReco-v*/RECO',
'/ZeroBias/Run2010A-PromptReco-v*/RECO'
]

def queryFile(rawdict,recodict,filehandle):

    for line in filehandle.readlines() :
        if line.count('run:') > 0 :
            array = line.split()
            run = int(array[1])
            dataset = array[3]
            size = float(array[5])
            events = int(array[7])
            tmp = {'size' : size , 'events' : events}
            if dataset.count('RECO') > 0 :
                if run in recodict.keys() :
                    recodict[run][dataset] = tmp
                else :
                    recodict[run] = { dataset : tmp }
            elif dataset.count('RAW') > 0 :
                if run in rawdict.keys() :
                    rawdict[run][dataset] = tmp
                else :
                    rawdict[run] = { dataset : tmp }
            else :
                print 'Not a RAW or RECO dataset'
            print 'run:',run,'dataset:',dataset,'size:',tmp['size'],'events:',tmp['events']
    return
                
print ""
print "Parse file: ",filename
print ""
raw = {}
reco = {}
filehandle = open(filename)
queryFile(raw,reco,filehandle)

sorted_runs = raw.keys()
for run in reco.keys():
    if run not in sorted_runs:
        sorted_runs.append(run)
sorted_runs.sort()

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
                if raw[run][dataset]['events'] > 100 :
                    total_size += raw[run][dataset]['size']
                    total_events += raw[run][dataset]['events']
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
                if reco[run][dataset]['events'] > 100 :
                    total_size += reco[run][dataset]['size']
                    total_events += reco[run][dataset]['events']
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
