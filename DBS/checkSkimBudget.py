#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, getopt

query_days = 1
query_run = None

opts, args = getopt.getopt(sys.argv[1:], "", ["days=","run="])

for opt, arg in opts :
    if opt == "--days" :
        query_days = int(arg)
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


startdate = datetime.date.today() - datetime.timedelta(days=query_days)
startdatestring = startdate.strftime("%Y-%m-%d")

recodatasets = [
'/CommissioningNoBeam/Run2010A-PromptReco-v*/RECO',
'/Commissioning/Run2010A-PromptReco-v*/RECO',
'/Cosmics/Run2010A-PromptReco-v*/RECO',
'/EGMonitor/Run2010A-PromptReco-v*/RECO',
'/EG/Run2010A-PromptReco-v*/RECO',
'/ForwardTriggers/Run2010A-PromptReco-v*/RECO',
'/HcalNZS/Run2010A-PromptReco-v*/RECO',
'/JetMETTauMonitor/Run2010A-PromptReco-v*/RECO',
'/JetMETTau/Run2010A-PromptReco-v*/RECO',
'/JetMET/Run2010A-PromptReco-v*/RECO',
'/BTau/Run2010A-PromptReco-v*/RECO',
'/MinimumBias/Run2010A-PromptReco-v*/RECO',
'/MuMonitor/Run2010A-PromptReco-v*/RECO',
'/Mu/Run2010A-PromptReco-v*/RECO',
'/ZeroBias/Run2010A-PromptReco-v*/RECO',
'/MuOnia/Run2010A-PromptReco-v*/RECO'
]

dpgskimdatasets = [
'/Commissioning/Run2010A-MuonDPG_skim-v*/RAW-RECO',
'/EGMonitor/Run2010A-ECALRECHIT-v*/RAW-RECO',
'/EGMonitor/Run2010A-TPGSkim-v*/USER',
'/JetMETTau/Run2010A-TPGSkim-v*/USER',
'/MinimumBias/Run2010A-BEAMBKGV3-v*/RAW-RECO',
'/MinimumBias/Run2010A-CSCSkim_BeamHalo_MinBias-v*/RAW-RECO',
'/MinimumBias/Run2010A-ECALRECHIT-v*/RAW-RECO',
'/MinimumBias/Run2010A-MuonDPG_skim-v*/RAW-RECO',
'/MinimumBias/Run2010A-Skim_StoppedHSCP-v*/RAW-RECO',
'/MinimumBias/Run2010A-Skim_logerror-v*/RAW-RECO',
'/MinimumBias/Run2010A-TPGSkim-v*/USER',
'/MinimumBias/Run2010A-valskim-v*/RAW-RECO',
'/Mu/Run2010A-TPGSkim-v*/USER',
'/ZeroBias/Run2010A-GOODVERTEX-v*/RAW-RECO'
]

sdcsskimdatasets = [
'/BTau/Run2010A-CS_Tau-v*/RAW-RECO',
'/CommissioningNoBeam/Run2010A-SD_StoppedHSCP-v*/RECO',
'/JetMET/Run2010A-CS_DiJetAve-v*/USER',
'/JetMETTau/Run2010A-CS_DiJetAve-v*/USER',
'/JetMETTau/Run2010A-CS_Tau-v*/RAW-RECO',
'/Mu/Run2010A-CS_Onia-v*/RECO',
'/Mu/Run2010A-CS_Onia-v*/RAW-RECO',
'/MuOnia/Run2010A-CS_Onia-v*/RAW-RECO'
]

recodatasets_selection_string = "(dataset = " + ' or dataset = '.join(recodatasets) + ')'
dpgskimdatasets_selection_string = "(dataset = " + ' or dataset = '.join(dpgskimdatasets) + ')'
sdcsskimdatasets_selection_string = "(dataset = " + ' or dataset = '.join(sdcsskimdatasets) + ')'


def queryForRunsAndTime(commandline):
    args = shlex.split(commandline)
    output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)

    runs = {}

    for line in output.communicate()[0].split('\n') :
        if len(line) > 0 :
            array = line.split()
            run = int(array[0])
            events = int(array[1])
            date = ' '.join(array[2:])
            print 'events:',events
            if run > 99999 and run < 1000000 and events > 100:
                runs[str(run)] = date
    
    return runs
    
def queryForSize(run,datasets):

    result = {}
    
    for dataset in datasets :
    
        commandline = "dbs search --query=\"find run,sum(file.size) where run = " + run + " and dataset = " + dataset + "\" --noheader"
        args = shlex.split(commandline)
        output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)
        output_array = output.communicate()[0].split('\n')
    
        if len(output_array) >= 1 :
            array = output_array[0].split()
            if len(array) == 2 :
                tmprun = array[0]
                size = float(array[1])/1024./1024./1024.
                if tmprun in result.keys() :
                    result[tmprun] += size 
                else :
                    result[tmprun] = size
    
    if run in result.keys():
        print 'Query for run',run,'resulted in:',result[run]
        return result[run]
    else :
        print 'Query for run',run,'resulted in: 0.'
        return 0.

# collect run selection for last day
if query_run == None :
    commandline = "dbs search --query=\"find run,sum(file.numevents),run.createdate where run.createdate > " + startdatestring + " and file = */RAW/* \" --noheader"
    runs = queryForRunsAndTime(commandline)
else :
    commandline = "dbs search --query=\"find run,sum(file.numevents),run.createdate where run = " + str(query_run) + " and file = */RAW/* \" --noheader"
    runs = queryForRunsAndTime(commandline)

sorted_runs = runs.keys()
sorted_runs.sort()
all_runs = sorted_runs

if len(all_runs) == 0 :
    print ''
    print 'No runs selected with more than 100 events'
    print ''
    sys.exit(1)

print ''
print 'Query for reco datasets'
print ''
recodatasets_result = {}
for run in all_runs : 
    recodatasets_result[run] = queryForSize(run,recodatasets)

print ''
print 'Query for dpg skims'
print ''
dpgskimdatasets_result = {}
for run in all_runs : 
    dpgskimdatasets_result[run] = queryForSize(run,dpgskimdatasets)

print ''
print 'Query for SD/CS skims'
print ''
sdcsskimdatasets_result = {}
for run in all_runs : 
    sdcsskimdatasets_result[run] = queryForSize(run,sdcsskimdatasets)
    
for run in all_runs:
    if recodatasets_result[run] > 0. :
        dpgpercentage = (dpgskimdatasets_result[run])/recodatasets_result[run]*100.
        sdscpercentage = (sdcsskimdatasets_result[run])/recodatasets_result[run]*100.
        percentage = (dpgskimdatasets_result[run] + sdcsskimdatasets_result[run])/recodatasets_result[run]*100.
        print run,runs[run],recodatasets_result[run],dpgskimdatasets_result[run],sdcsskimdatasets_result[run],dpgpercentage,sdscpercentage,percentage
