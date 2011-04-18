#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, getopt, json

inputfilename = None
min_events = 100

opts, args = getopt.getopt(sys.argv[1:], "", ["file=","min_events="])

for opt, arg in opts :
    if opt == "--file" :
        inputfilename = arg
    if opt == "--min_events" :
        min_events = int(arg)
        
if inputfilename == None :
    print ''
    print 'Please define input file name with --file'
    print ''
    sys.exit(2)

rawdatasets = [
'/DoubleElectron/Run2011A-v1/RAW',
'/DoubleMu/Run2011A-v1/RAW',
'/ElectronHad/Run2011A-v1/RAW',
# '/ForwardTriggers/Run2011A-v1/RAW',
'/HT/Run2011A-v1/RAW',
'/Jet/Run2011A-v1/RAW',
'/METBTag/Run2011A-v1/RAW',
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
]

def queryFile(runs,filename):
    filehandle = open(filename)
    for line in filehandle.readlines():
        if line.count('dataset:') > 0:
            array = line.split()
            if len(array) == 6:
                dataset = array[1]
                run = int(array[3])
                events = int (array[5])
                # if run > 99999 and run < 1000000 and events > min_events:
                if run in runs.keys():
                    runs[run][dataset] = events
                else:
                    runs[run] = { dataset : events }
    return

runs = {}
queryFile(runs,inputfilename)

sorted_runs = runs.keys()
sorted_runs.sort()


result = "run "
for dataset in rawdatasets:
    result += dataset + " "
print ''
print result

for run in sorted_runs:
    result = "%10i" % run
    for dataset in rawdatasets :
        if dataset in runs[run].keys() :
            result += "%10i" % runs[run][dataset]
        else:
            result += "%10i" % 0
            
    print result


# check that all RAW datasets have events > min_events for a run
results = []
for run in runs.keys():
    enough_events = True
    for dataset in rawdatasets:
        if dataset not in runs[run] :
            enough_events = False
    if enough_events == True :
        results.append(run)
        
results.sort()
        
print ''
print 'Writing out',len(results),'runs'
print ''
for run in results:
    print run

output_file_name = "runs_" + str(results[0]) + "_" + str(results[-1]) + ".json"
tmp_handle = open(output_file_name,'w')

json.dump(results,tmp_handle)
tmp_handle.close()
