#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, json, getopt

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
'/ZeroBias/Run2010A-PromptReco-v4/RECO']

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
"/Mu/Run2010A-CS_Onia-v6/RAW-RECO"]

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
            date = ' '.join(array[1:])
            if run > 99999 and run < 1000000 :
                runs[str(run)] = date
    
    return runs
    
def queryForSize(run,dataset_selection_string):
    
    commandline = "dbs search --query=\"find run,sum(file.size) where run = " + run + " and " + dataset_selection_string + "\" --noheader"
    args = shlex.split(commandline)
    output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)
    
    result = {}

    output_array = output.communicate()[0].split('\n')
    
    if len(output_array) >= 1 :
        array = output_array[0].split()
        if len(array) == 2 :
            tmprun = array[0]
            size = float(array[1])/1024./1024./1024.
            result[tmprun] = size
    
    if len(result.keys()) > 1 :
        print 'Error, more than 1 entry',commandline
        sys.exit(1)
    else :
        if run in result.keys():
            print 'Query for run',run,'resulted in:',result[run]
            return result[run]
        else :
            print 'Query for run',run,'resulted in: 0.'
            return 0.

# collect run selection for last day
if query_run == None :
    commandline = "dbs search --query=\"find run,run.createdate where run.createdate > " + startdatestring + "\" --noheader"
    print commandline
    runs = queryForRunsAndTime(commandline)

    sorted_runs = runs.keys()
    sorted_runs.sort()
else :
    sorted_runs = [query_run]
# run_selection_string = "(run = " + ' or run = '.join(sorted_runs) + ')'
all_runs = sorted_runs

print ''
print 'Query for reco datasets'
print ''
recodatasets_result = {}
for run in all_runs : 
    recodatasets_result[run] = queryForSize(run,recodatasets_selection_string)

print ''
print 'Query for dpg skims'
print ''
dpgskimdatasets_result = {}
for run in all_runs : 
    dpgskimdatasets_result[run] = queryForSize(run,dpgskimdatasets_selection_string)

print ''
print 'Query for SD/CS skims'
print ''
sdcsskimdatasets_result = {}
for run in all_runs : 
    sdcsskimdatasets_result[run] = queryForSize(run,sdcsskimdatasets_selection_string)
    
for run in all_runs:
    if recodatasets_result[run] > 0. :
        dpgpercentage = (dpgskimdatasets_result[run])/recodatasets_result[run]*100.
        sdscpercentage = (sdcsskimdatasets_result[run])/recodatasets_result[run]*100.
        percentage = (dpgskimdatasets_result[run] + sdcsskimdatasets_result[run])/recodatasets_result[run]*100.
        print run,recodatasets_result[run],dpgskimdatasets_result[run],sdcsskimdatasets_result[run],dpgpercentage,sdscpercentage,percentage
