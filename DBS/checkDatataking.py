#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, json, getopt

query_days = 1

opts, args = getopt.getopt(sys.argv[1:], "", ["days="])

for opt, arg in opts :
    if opt == "--days" :
        query_days = int(arg)
        
if query_days != 1 :
    print ''
    print 'Query for',query_days,'days'
    print ''

startdate = datetime.date.today() - datetime.timedelta(days=query_days)
startdatestring = startdate.strftime("%Y-%m-%d")

rawdataset = '/JetMET*/Run2010A-v*/RAW'
recodataset = '/JetMET*/Run2010A-PromptReco-v*/RECO'
skimdatasets = ['/JetMET*/Run2010A-CS_DiJetAve-v*/USER','/JetMET*/Run2010A-CS_Tau-v*/RAW-RECO']

def queryForRunsAndTime(commandline):
    args = shlex.split(commandline)
    output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)

    runs = {}

    for line in output.communicate()[0].split('\n') :
        if len(line) > 0 :
            array = line.split()
            run = array[0]
            date = ' '.join(array[1:])
            runs[run] = date
    
    return runs

# collect run selection for last day
commandline = "dbs search --query=\"find run,run.createdate where dataset = " + rawdataset + " and run.createdate > " + startdatestring + "\" --noheader"
runs = queryForRunsAndTime(commandline)

sorted_runs = runs.keys()
sorted_runs.sort()
run_selection_string = "(run = " + ' or run = '.join(sorted_runs) + ')'
all_runs = sorted_runs

print ''
print 'Runs created since',startdatestring,'in dataset',rawdataset
print ''
print 'Total number of runs:',len(sorted_runs)
print ''
for run in sorted_runs :
    print run,runs[run]
    
if len(sorted_runs) == 0 :
    print 'No runs have been taken within the last',query_days,'days!!!'
    print ''
    sys.exit(0)


# raw runs at FNAL
commandline = "dbs search --query=\"find run,run.createdate where dataset = " + rawdataset + " and " + run_selection_string + " and site = *fnal.gov \" --noheader"
runs = queryForRunsAndTime(commandline)

sorted_runs = runs.keys()
sorted_runs.sort()

print ''
print 'Runs created since',startdatestring,'in dataset',rawdataset,'at FNAL'
print ''
print 'Total number of runs:',len(sorted_runs)
print ''
for run in sorted_runs :
    print run,runs[run]

# reco runs
commandline = "dbs search --query=\"find run,run.createdate where dataset = " + recodataset + " and " + run_selection_string + "\" --noheader"
runs = queryForRunsAndTime(commandline)

sorted_runs = runs.keys()
sorted_runs.sort()

print ''
print 'Runs created since',startdatestring,'in dataset',recodataset
print ''
print 'Total number of runs:',len(sorted_runs)
print ''
for run in sorted_runs :
    print run,runs[run]


# reco runs at FNAL
commandline = "dbs search --query=\"find run,run.createdate where dataset = " + recodataset + " and " + run_selection_string + " and site = *fnal.gov \" --noheader"
runs = queryForRunsAndTime(commandline)

sorted_runs = runs.keys()
sorted_runs.sort()

print ''
print 'Runs created since',startdatestring,'in dataset',recodataset,'at FNAL'
print ''
print 'Total number of runs:',len(sorted_runs)
print ''
for run in sorted_runs :
    print run,runs[run]

# skim runs at FNAL
for skimdataset in skimdatasets :
    commandline = "dbs search --query=\"find run,run.createdate where dataset = " + skimdataset + " and " + run_selection_string + " and site = *fnal.gov \" --noheader"
    runs = queryForRunsAndTime(commandline)

    sorted_runs = runs.keys()
    sorted_runs.sort()

    print ''
    print 'Runs created since',startdatestring,'in dataset',skimdataset,'at FNAL'
    print ''
    print 'Total number of runs:',len(sorted_runs)
    print ''
    for run in sorted_runs :
        print run,runs[run]

# query for lumi

# repare lumi json for runs
json_runs = {}
for run in all_runs :
    json_runs[run] = [[1,999999]]
    
tmp = tempfile.mkstemp()
tmp_handle = open(tmp[1],'w')

json.dump(json_runs,tmp_handle)
tmp_handle.close()

commandline = 'lumiCalc.py -c frontier://LumiProd/CMS_LUMI_PROD -i ' + tmp[1] + ' overview'
print commandline
args = shlex.split(commandline)
output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)

print ''
print 'Lumi corresponding to all lumi sections in all runs created since',startdatestring,'in dataset',rawdataset
print ''

print output.communicate()[0]
print ''
    
# os.remove(tmp[1])