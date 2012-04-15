python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning12*/*" | grep -v 'test/' | sort > complete_datasets.list

cat complete_datasets.list | grep -i express > express.list
cat complete_datasets.list | grep -i preprod > preproduction.list
cat complete_datasets.list | grep -- '-Error' > error.list

cat complete_datasets.list | grep -vi express | grep -vi preprod | grep -v -- '-Error' > datasets.list

cat datasets.list | grep '/RAW' | grep -v RAW-RECO | grep v1 > raw_v1.list

cat datasets.list | grep '/RECO' | grep -i prompt | grep v1 > prompt_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i prompt | grep v1 > prompt_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i prompt | grep v1 > prompt_dqm_v1.list
cat datasets.list | grep -i promptskim | grep v1 > prompt_skim_v1.list
cat datasets.list | grep ALCA | grep v1 > alcareco_v1.list
# prompt_reco_v1.list prompt_aod_v1.list prompt_dqm_v1.list alcareco_v1.list prompt_skim_v1.list

# cat datasets.list | grep '/RECO' | grep -i 14Oct2011 | grep v1 > 14Oct2011_reco_v1.list
# cat datasets.list | grep '/AOD' | grep -i 14Oct2011 | grep v1 > 14Oct2011_aod_v1.list
# cat datasets.list | grep '/DQM' | grep -i 14Oct2011 | grep v1 > 14Oct2011_dqm_v1.list
# cat datasets.list | grep '/ALCARECO' | grep -i 14Oct2011 | grep v1 > 14Oct2011_alcareco_v1.list
# cat datasets.list | grep '/RAW-RECO' | grep -i 14Oct2011 | grep v1 > 14Oct2011_skims_v1.list
# cat datasets.list | grep '/USER' | grep -i 14Oct2011 | grep v1 >> 14Oct2011_skims_v1.list
# 14Oct2011_reco_v1.list 14Oct2011_aod_v1.list 14Oct2011_dqm_v1.list 14Oct2011_alcareco_v1.list 14Oct2011_skims_v1.list 14Oct2011_skims_v1.list

cat express.list error.list preproduction.list raw_v1.list prompt_reco_v1.list prompt_aod_v1.list prompt_dqm_v1.list alcareco_v1.list prompt_skim_v1.list | sort > done.list

echo ""
echo "inconsistencies"
echo ""
diff datasets.list done.list | grep '<' | awk '{print $2}'

echo ""
echo "Error datasets"
echo ""
cat error.list

echo ""
echo "PDs missing in FNAL checks"
echo ""
cat datasets.list | grep -v '/AlCaLumiPixels/' | grep -v '/AlCaP0/' | grep -v '/AlCaPhiSym/' | grep -v '/FEDMonitor/' | grep -v '/Interfill/' | grep -v '/L1Accept/' | grep -v '/LogMonitor/' | grep -v '/MiniDaq/' | grep -v '/RPCMonitor/' | grep -v '/TestEnablesEcalHcalDT/' | grep -v '/TestEnablesTracker/' | grep -v '/Commissioning'/ | grep -v '/Cosmics'/ | grep -v '/ForwardTriggers'/ | grep -v '/HcalHPDNoise'/ | grep -v '/HcalNZS'/ | grep -v '/MinimumBias'/ | grep -v '/ZeroBias1'/ | grep -v '/ZeroBias2'/ | grep -v '/ZeroBias3'/ | grep -v '/ZeroBias4/' | awk -F\/ '{print $2}' | sort | uniq
echo ""
echo "datasets not at FNAL"
# python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning12*/* and site = T1_US_FNAL" | grep -v 'test/' | sort > datasets_fnal.list
dbs --query="find dataset where dataset = */Commissioning12* and site = T1_US_FNAL" | grep -v 'test/' | sort > datasets_fnal.list
echo ""
echo "FNAL custodial for: Commissioning, Cosmics, ForwardTriggers, HcalHPDNoise, HcalNZS, MinimumBias, ZeroBias1, ZeroBias2, ZeroBias3, ZeroBias4"
echo ""
echo "missing:"
diff datasets.list datasets_fnal.list | grep '/Commissioning/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Cosmics/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ForwardTriggers/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/HcalHPDNoise/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/HcalNZS/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MinimumBias/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ZeroBias1/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ZeroBias2/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ZeroBias3/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ZeroBias4/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
echo ""
echo "non-custodial kept at FNAL for "
echo ""
echo "missing:"
# diff datasets.list datasets_fnal.list | grep '/Jet/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'