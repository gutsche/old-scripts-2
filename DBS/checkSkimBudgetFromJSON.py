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
'/BTau/Run2010B-PromptReco-v2/RECO',
'/Commissioning/Run2010B-PromptReco-v2/RECO',
'/CommissioningNoBeam/Run2010B-PromptReco-v2/RECO',
'/Cosmics/Run2010B-PromptReco-v2/RECO',
'/EGMonitor/Run2010B-PromptReco-v2/RECO',
'/Electron/Run2010B-PromptReco-v2/RECO',
'/ForwardTriggers/Run2010B-PromptReco-v2/RECO',
'/HcalNZS/Run2010B-PromptReco-v2/RECO',
'/HeavyIonTest/Run2010B-PromptReco-v2/RECO',
'/HeavyIonTestPlayback/Run2010B-PromptReco-v2/RECO',
'/Jet/Run2010B-PromptReco-v2/RECO',
'/JetMETTauMonitor/Run2010B-PromptReco-v2/RECO',
'/METFwd/Run2010B-PromptReco-v2/RECO',
'/MinimumBias/Run2010B-PromptReco-v2/RECO',
'/MinimumBiasVdM/Run2010B-PromptReco-v2/RECO',
'/Mu/Run2010B-PromptReco-v2/RECO',
'/MuMonitor/Run2010B-PromptReco-v2/RECO',
'/MuOnia/Run2010B-PromptReco-v2/RECO',
'/MultiJet/Run2010B-PromptReco-v2/RECO',
'/Photon/Run2010B-PromptReco-v2/RECO',
'/RandomTriggers/Run2010B-PromptReco-v2/RECO',
'/ZeroBias/Run2010B-PromptReco-v2/RECO',
'/ZeroBiasVdM/Run2010B-PromptReco-v2/RECO',
]

dpgskimdatasets = [
'/BTau/Run2010B-Skim_logerror-v2/RAW-RECO',
'/Commissioning/Run2010B-MuonDPG_skim-v2/RAW-RECO',
'/Commissioning/Run2010B-Skim_logerror-v2/RAW-RECO',
'/Cosmics/Run2010B-CSCSkim_BeamHalo_Cosmics-v2/RAW-RECO',
'/Cosmics/Run2010B-Skim_logerror-v2/RAW-RECO',
'/Cosmics/Run2010B-SuperPointing-v2/RAW-RECO',
'/EGMonitor/Run2010B-ECALRECHIT-v2/RAW-RECO',
'/EGMonitor/Run2010B-Skim_logerror-v2/RAW-RECO',
'/EGMonitor/Run2010B-TPGSkim-v2/USER',
'/Electron/Run2010B-LogError-v2/RAW-RECO',
'/Electron/Run2010B-Skim_logerror-v2/RAW-RECO',
'/Jet/Run2010B-LogError-v2/RAW-RECO',
'/Jet/Run2010B-Skim_logerror-v2/RAW-RECO',
'/METFwd/Run2010B-Skim_logerror-v2/RAW-RECO',
'/MinimumBias/Run2010B-BEAMBKGV3-v2/RAW-RECO',
'/MinimumBias/Run2010B-CSCSkim_BeamHalo_MinBias-v2/RAW-RECO',
'/MinimumBias/Run2010B-Muon_skim-v2/RECO',
'/MinimumBias/Run2010B-Skim_StoppedHSCP-v2/RAW-RECO',
'/MinimumBias/Run2010B-Skim_logerror-v2/RAW-RECO',
'/MinimumBias/Run2010B-TPGSkim-v2/USER',
'/MinimumBias/Run2010B-valskim-v2/RAW-RECO',
'/Mu/Run2010B-LogError-v2/RAW-RECO',
'/Mu/Run2010B-Skim_logerror-v2/RAW-RECO',
'/Mu/Run2010B-TPGSkim-v2/USER',
'/Photon/Run2010B-LogError-v2/RAW-RECO',
'/Photon/Run2010B-Skim_logerror-v2/RAW-RECO',
'/ZeroBias/Run2010B-GOODVERTEX-v2/RAW-RECO',
'/ZeroBias/Run2010B-Skim_logerror-v2/RAW-RECO',]

sdcsskimdatasets = [
'/CommissioningNoBeam/Run2010B-SD_StoppedHSCP-v2/RECO',
'/Jet/Run2010B-DiJet-v2/USER',
'/Jet/Run2010B-HTSD-v2/RAW-RECO',
'/Mu/Run2010B-WZMu-v2/RAW-RECO',
'/Mu/Run2010B-WZMuFilter-v2/RAW-RECO',
'/Photon/Run2010B-WZEG-v2/RAW-RECO',
'/Photon/Run2010B-EGMWZFilter-v2/RAW-RECO',
'/Electron/Run2010B-WZEG-v2/RAW-RECO',
'/Electron/Run2010B-EGMWZFilter-v2/RAW-RECO',
]

def queryForSize(run,datasets):

    result = {}
    
    for dataset in datasets :
    
        commandline = "dbs search --query=\"find run,sum(block.size) where run = " + str(run) + " and dataset = " + dataset + "\" --noheader"
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
