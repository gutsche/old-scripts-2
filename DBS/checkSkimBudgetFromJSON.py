#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, getopt, json

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

def queryForSize(run,datasets):

    result = {}
    
    for dataset in datasets :
    
        commandline = "dbs search --query=\"find run,sum(file.size) where run = " + str(run) + " and dataset = " + dataset + "\" --noheader"
        args = shlex.split(commandline)
        output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)
        output_array = output.communicate()[0].split('\n')
    
        if len(output_array) >= 1 :
            array = output_array[0].split()
            if len(array) == 2 :
                tmprun = int(array[0])
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


runs = json.load(open(jsonfilename))
sorted_runs = runs
sorted_runs.sort()
all_runs = sorted_runs

if len(all_runs) == 0 :
    print ''
    print 'No runs included in json file'
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
        print run,recodatasets_result[run],dpgskimdatasets_result[run],sdcsskimdatasets_result[run],dpgpercentage,sdscpercentage,percentage
