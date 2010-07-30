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

recodatasets = ['/CommissioningNoBeam/Run2010A-PromptReco-v4/RECO',
'/Commissioning/Run2010A-PromptReco-v4/RECO',
'/Cosmics/Run2010A-PromptReco-v4/RECO',
'/EGMonitor/Run2010A-PromptReco-v4/RECO',
'/EG/Run2010A-PromptReco-v4/RECO',
'/ForwardTriggers/Run2010A-PromptReco-v4/RECO',
'/HcalNZS/Run2010A-PromptReco-v4/RECO',
'/JetMETTauMonitor/Run2010A-PromptReco-v4/RECO',
'/JetMETTau/Run2010A-PromptReco-v4/RECO',
'/MinimumBias/Run2010A-PromptReco-v4/RECO',
'/MuMonitor/Run2010A-PromptReco-v4/RECO',
'/Mu/Run2010A-PromptReco-v4/RECO',
'/ZeroBias/Run2010A-PromptReco-v4/RECO',
'/MuOnia/Run2010A-PromptReco-v4/RECO']

dpgskimdatasets = ["/Commissioning/Run2010A-MuonDPG_skim-v4/RAW-RECO",
"/Commissioning/Run2010A-MuonDPG_skim-v5/RAW-RECO",
"/Commissioning/Run2010A-MuonDPG_skim-v6/RAW-RECO",
"/JetMETTau/Run2010A-CS_DiJetAve-v4/USER",
"/JetMETTau/Run2010A-CS_DiJetAve-v5/USER",
"/JetMETTau/Run2010A-CS_DiJetAve-v6/USER",
"/JetMETTau/Run2010A-CS_Tau-v4/RAW-RECO",
"/JetMETTau/Run2010A-CS_Tau-v5/RAW-RECO",
"/JetMETTau/Run2010A-CS_Tau-v6/RAW-RECO",
"/MinimumBias/Run2010A-BEAMBKGV3-v4/RAW-RECO",
"/MinimumBias/Run2010A-BEAMBKGV3-v5/RAW-RECO",
"/MinimumBias/Run2010A-BEAMBKGV3-v6/RAW-RECO",
"/MinimumBias/Run2010A-CSCSkim_BeamHalo_MinBias-v4/RAW-RECO",
"/MinimumBias/Run2010A-CSCSkim_BeamHalo_MinBias-v5/RAW-RECO",
"/MinimumBias/Run2010A-CSCSkim_BeamHalo_MinBias-v6/RAW-RECO",
"/MinimumBias/Run2010A-ECALRECHIT-v4/RAW-RECO",
"/MinimumBias/Run2010A-ECALRECHIT-v5/RAW-RECO",
"/MinimumBias/Run2010A-ECALRECHIT-v6/RAW-RECO",
"/MinimumBias/Run2010A-MuonDPG_skim-v4/RAW-RECO",
"/MinimumBias/Run2010A-MuonDPG_skim-v5/RAW-RECO",
"/MinimumBias/Run2010A-MuonDPG_skim-v6/RAW-RECO",
"/MinimumBias/Run2010A-Skim_logerror-v4/RAW-RECO",
"/MinimumBias/Run2010A-Skim_logerror-v5/RAW-RECO",
"/MinimumBias/Run2010A-Skim_logerror-v6/RAW-RECO",
"/MinimumBias/Run2010A-Skim_StoppedHSCP-v4/RAW-RECO",
"/MinimumBias/Run2010A-Skim_StoppedHSCP-v5/RAW-RECO",
"/MinimumBias/Run2010A-Skim_StoppedHSCP-v6/RAW-RECO",
"/MinimumBias/Run2010A-TPGSkim-v4/USER",
"/MinimumBias/Run2010A-TPGSkim-v5/USER",
"/MinimumBias/Run2010A-TPGSkim-v6/USER",
"/MinimumBias/Run2010A-valskim-v4/RAW-RECO",
"/MinimumBias/Run2010A-valskim-v5/RAW-RECO",
"/MinimumBias/Run2010A-valskim-v6/RAW-RECO",
"/Mu/Run2010A-CS_Onia-v4/RECO",
"/Mu/Run2010A-CS_Onia-v5/RAW-RECO",
"/Mu/Run2010A-CS_Onia-v6/RAW-RECO",
"/ZeroBias/Run2010A-GOODVERTEX-v4/RAW-RECO",
"/ZeroBias/Run2010A-GOODVERTEX-v5/RAW-RECO",
"/ZeroBias/Run2010A-GOODVERTEX-v6/RAW-RECO"]

sdcsskimdatasets = ["/JetMETTau/Run2010A-CS_DiJetAve-v4/USER",
"/JetMETTau/Run2010A-CS_DiJetAve-v5/USER",
"/JetMETTau/Run2010A-CS_DiJetAve-v6/USER",
"/JetMETTau/Run2010A-CS_Tau-v4/RAW-RECO",
"/JetMETTau/Run2010A-CS_Tau-v5/RAW-RECO",
"/JetMETTau/Run2010A-CS_Tau-v6/RAW-RECO",
"/Mu/Run2010A-CS_Onia-v4/RECO",
"/Mu/Run2010A-CS_Onia-v5/RAW-RECO",
"/Mu/Run2010A-CS_Onia-v6/RAW-RECO",
"/MuOnia/Run2010A-CS_Onia-v6/RAW-RECO"]

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
