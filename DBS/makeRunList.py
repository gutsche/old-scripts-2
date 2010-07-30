#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, getopt, json

query_days = 1
query_run = None
min_events = 100

opts, args = getopt.getopt(sys.argv[1:], "", ["days=","run=","min_events="])

for opt, arg in opts :
    if opt == "--days" :
        query_days = int(arg)
    if opt == "--min_events" :
        min_events = int(arg)
    if opt == "--run" :
        query_run = arg
        
if query_days != 1 :
    print ''
    print 'Query for',query_days,'days'
    print ''

if query_run != None :
    print ''
    print 'Query for run',query_run
    print ''


rawdatasets = [
'/EG/Run2010A-v*/RAW',
'/JetMETTau/Run2010A-v*/RAW',
'/MinimumBias/Run2010A-v*/RAW',
'/Mu/Run2010A-v*/RAW',
# '/MuOnia/Run2010A-v*/RAW',
'/ZeroBias/Run2010A-v*/RAW'
]

def queryCommandline(runs,commandline):
    print commandline
    args = shlex.split(commandline)
    output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)
    for line in output.communicate()[0].split('\n') :
        if len(line) > 0 :
            array = line.split()
            run = int(array[0])
            events = int(array[1])
            date = ' '.join(array[2:])
            print 'dataset:',dataset,'run:',run,'events:',events
            if run > 99999 and run < 1000000 and events > min_events:
                if run in runs.keys() :
                    runs[run].append(dataset)
                else:
                    runs[run] = [dataset]
    return

runs = {}
# query DBS
for dataset in rawdatasets :
    # collect run selection for last day
    if query_run == None :
        for day in range(query_days) :
            enddate = datetime.date.today() - datetime.timedelta(days=day)
            enddatestring = enddate.strftime("%Y-%m-%d")
            startdate = datetime.date.today() - datetime.timedelta(days=day+1)
            startdatestring = startdate.strftime("%Y-%m-%d")
            commandline = "dbs search --query=\"find run,sum(file.numevents),run.createdate where run.createdate >= " + startdatestring + " and run.createdate < " + enddatestring + " and dataset = " + dataset + "\" --noheader"
            queryCommandline(runs,commandline)
    else :
        commandline = "dbs search --query=\"find run,sum(file.numevents),run.createdate where run = " + str(query_run) + " and dataset = " + dataset + "\" --noheader"
        queryCommandline(runs,commandline)

# check that all RAW datasets have events > min_events for a run
results = []
for run in runs.keys():
    enough_events = True
    for dataset in rawdatasets:
        if dataset not in runs[run] :
            enough_events = False
    if enough_events == True :
        results.append(run)
        
print results

enddate = datetime.date.today()
startdate = datetime.date.today() - datetime.timedelta(days=query_days)

output_file_name = "runs_" + startdate.strftime("%y%m%d") + "_" + enddate.strftime("%y%m%d") + ".json"
tmp_handle = open(output_file_name,'w')

json.dump(results,tmp_handle)
tmp_handle.close()
