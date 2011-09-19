python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2011A*/*" | grep -v 'test/' | sort > complete_datasets.list

cat complete_datasets.list | grep -i express > express.list
cat complete_datasets.list | grep -i preprod > preproduction.list
cat complete_datasets.list | grep -- '-Error' > error.list

cat complete_datasets.list | grep -vi express | grep -v PreScaleThingy | grep -vi preprod | grep -v -- '-Error' > datasets.list

cat datasets.list | grep '/RAW' | grep -v RAW-RECO | grep v1 > raw_v1.list
cat datasets.list | grep '/RAW' | grep -v RAW-RECO | grep v2 > raw_v2.list

cat datasets.list | grep '/RECO' | grep -i prompt | grep v1 > prompt_reco_v1.list
cat datasets.list | grep '/RECO' | grep -i prompt | grep v2 > prompt_reco_v2.list
cat datasets.list | grep '/RECO' | grep -i prompt | grep v3 > prompt_reco_v3.list
cat datasets.list | grep '/RECO' | grep -i prompt | grep v4 > prompt_reco_v4.list
cat datasets.list | grep '/RECO' | grep -i prompt | grep v5 > prompt_reco_v5.list
cat datasets.list | grep '/RECO' | grep -i prompt | grep v6 > prompt_reco_v6.list

cat datasets.list | grep '/AOD' | grep -i prompt | grep v1 > prompt_aod_v1.list
cat datasets.list | grep '/AOD' | grep -i prompt | grep v2 > prompt_aod_v2.list
cat datasets.list | grep '/AOD' | grep -i prompt | grep v3 > prompt_aod_v3.list
cat datasets.list | grep '/AOD' | grep -i prompt | grep v4 > prompt_aod_v4.list
cat datasets.list | grep '/AOD' | grep -i prompt | grep v5 > prompt_aod_v5.list
cat datasets.list | grep '/AOD' | grep -i prompt | grep v6 > prompt_aod_v6.list

cat datasets.list | grep '/DQM' | grep -i prompt | grep v1 > prompt_dqm_v1.list
cat datasets.list | grep '/DQM' | grep -i prompt | grep v2 > prompt_dqm_v2.list
cat datasets.list | grep '/DQM' | grep -i prompt | grep v3 > prompt_dqm_v3.list
cat datasets.list | grep '/DQM' | grep -i prompt | grep v4 > prompt_dqm_v4.list
cat datasets.list | grep '/DQM' | grep -i prompt | grep v5 > prompt_dqm_v5.list
cat datasets.list | grep '/DQM' | grep -i prompt | grep v6 > prompt_dqm_v6.list

cat datasets.list | grep -i promptskim | grep v4 > prompt_skim_v4.list
cat datasets.list | grep -i promptskim | grep v5 > prompt_skim_v5.list
cat datasets.list | grep -i promptskim | grep v6 > prompt_skim_v6.list

cat datasets.list | grep ALCA | grep v1 > alcareco_v1.list
cat datasets.list | grep ALCA | grep v2 > alcareco_v2.list
cat datasets.list | grep ALCA | grep v3 > alcareco_v3.list
cat datasets.list | grep ALCA | grep v4 > alcareco_v4.list
cat datasets.list | grep ALCA | grep v5 > alcareco_v5.list
cat datasets.list | grep ALCA | grep v6 > alcareco_v6.list

# prompt_reco_v6.list prompt_aod_v6.list prompt_dqm_v6.list alcareco_v6.list prompt_skim_v6.list

cat datasets.list | grep '/RECO' | grep -i Apr22 | grep v1 > apr22_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i Apr22 | grep v1 > apr22_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i Apr22 | grep v1 > apr22_dqm_v1.list

cat datasets.list | grep '/RECO' | grep -i Apr22 | grep v2 > apr22_reco_v2.list
cat datasets.list | grep '/AOD' | grep -i Apr22 | grep v2 > apr22_aod_v2.list
cat datasets.list | grep '/DQM' | grep -i Apr22 | grep v2 > apr22_dqm_v2.list

cat datasets.list | grep '/RECO' | grep -i Apr22 | grep v3 > apr22_reco_v3.list
cat datasets.list | grep '/AOD' | grep -i Apr22 | grep v3 > apr22_aod_v3.list
cat datasets.list | grep '/DQM' | grep -i Apr22 | grep v3 > apr22_dqm_v3.list

cat datasets.list | grep '/RECO' | grep -i Apr13 | grep v1 > apr13_reco_v1.list
cat datasets.list | grep '/DQM' | grep -i Apr13 | grep v1 > apr13_dqm_v1.list

cat datasets.list | grep '/RECO' | grep -i May3 | grep v1 > may3_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i May3 | grep v1 > may3_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i May3 | grep v1 > may3_dqm_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i May3 | grep v1 > may3_skims_v1.list
cat datasets.list | grep '/USER' | grep -i May3 | grep v1 >> may3_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i May7 | grep v1 > may7_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i May7 | grep v1 > may7_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i May7 | grep v1 > may7_dqm_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i May7 | grep v1 > may7_skims_v1.list
cat datasets.list | grep '/USER' | grep -i May7 | grep v1 >> may7_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i May10 | grep v1 > may10_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i May10 | grep v1 > may10_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i May10 | grep v1 > may10_dqm_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i May10 | grep v1 > may10_skims_v1.list
cat datasets.list | grep '/USER' | grep -i May10 | grep v1 >> may10_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i May13 | grep v1 > may13_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i May13 | grep v1 > may13_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i May13 | grep v1 > may13_dqm_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i May13 | grep v1 > may13_skims_v1.list
cat datasets.list | grep '/USER' | grep -i May13 | grep v1 >> may13_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i May10 | grep v2 > may10_reco_v2.list
cat datasets.list | grep '/AOD' | grep -i May10 | grep v2 > may10_aod_v2.list
cat datasets.list | grep '/DQM' | grep -i May10 | grep v2 > may10_dqm_v2.list
cat datasets.list | grep '/RAW-RECO' | grep -i May10 | grep v2 > may10_skims_v2.list
cat datasets.list | grep '/USER' | grep -i May10 | grep v2 >> may10_skims_v2.list

cat datasets.list | grep '/RECO' | grep -i 16Jun2011 | grep v1 > 16Jun2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 16Jun2011 | grep v1 > 16Jun2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 16Jun2011 | grep v1 > 16Jun2011_dqm_v1.list

cat datasets.list | grep '/RECO' | grep -i 02Jul2011 | grep v1 > 02Jul2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 02Jul2011 | grep v1 > 02Jul2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 02Jul2011 | grep v1 > 02Jul2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 02Jul2011 | grep v1 > 02Jul2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 02Jul2011 | grep v1 > 02Jul2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 02Jul2011 | grep v1 >> 02Jul2011_skims_v1.list
# 02Jul2011_reco_v1.list 02Jul2011_aod_v1.list 02Jul2011_dqm_v1.list 02Jul2011_alcareco_v1.list 02Jul2011_skims_v1.list 02Jul2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 05Jul2011 | grep v1 > 05Jul2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 05Jul2011 | grep v1 > 05Jul2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 05Jul2011 | grep v1 > 05Jul2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 05Jul2011 | grep v1 > 05Jul2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 05Jul2011 | grep v1 > 05Jul2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 05Jul2011 | grep v1 >> 05Jul2011_skims_v1.list
# 05Jul2011_reco_v1.list 05Jul2011_aod_v1.list 05Jul2011_dqm_v1.list 05Jul2011_alcareco_v1.list 05Jul2011_skims_v1.list 05Jul2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 05Jul2011 | grep HF > 05Jul2011_reco_HF.list
cat datasets.list | grep '/AOD' | grep -i 05Jul2011 | grep HF > 05Jul2011_aod_HF.list
cat datasets.list | grep '/DQM' | grep -i 05Jul2011 | grep HF > 05Jul2011_dqm_HF.list
cat datasets.list | grep '/ALCARECO' | grep -i 05Jul2011 | grep HF > 05Jul2011_alcareco_HF.list
cat datasets.list | grep '/RAW-RECO' | grep -i 05Jul2011 | grep HF > 05Jul2011_skims_HF.list
cat datasets.list | grep '/USER' | grep -i 05Jul2011 | grep HF >> 05Jul2011_skims_HF.list
# 05Jul2011_reco_HF.list 05Jul2011_aod_HF.list 05Jul2011_dqm_HF.list 05Jul2011_alcareco_HF.list 05Jul2011_skims_HF.list 05Jul2011_skims_HF.list

cat datasets.list | grep '/RECO' | grep -i 16Jul2011 | grep v1 > 16Jul2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 16Jul2011 | grep v1 > 16Jul2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 16Jul2011 | grep v1 > 16Jul2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 16Jul2011 | grep v1 > 16Jul2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 16Jul2011 | grep v1 > 16Jul2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 16Jul2011 | grep v1 >> 16Jul2011_skims_v1.list
# 16Jul2011_reco_v1.list 16Jul2011_aod_v1.list 16Jul2011_dqm_v1.list 16Jul2011_alcareco_v1.list 16Jul2011_skims_v1.list 16Jul2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 05Aug2011 | grep v1 > 05Aug2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 05Aug2011 | grep v1 > 05Aug2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 05Aug2011 | grep v1 > 05Aug2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 05Aug2011 | grep v1 > 05Aug2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 05Aug2011 | grep v1 > 05Aug2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 05Aug2011 | grep v1 >> 05Aug2011_skims_v1.list
# 05Aug2011_reco_v1.list 05Aug2011_aod_v1.list 05Aug2011_dqm_v1.list 05Aug2011_alcareco_v1.list 05Aug2011_skims_v1.list 05Aug2011_skims_v1.list



cat express.list error.list preproduction.list raw_v1.list prompt_reco_v1.list prompt_aod_v1.list prompt_dqm_v1.list alcareco_v1.list raw_v2.list prompt_reco_v2.list prompt_aod_v2.list prompt_dqm_v2.list alcareco_v2.list alcareco_v3.list alcareco_v5.list apr22_reco_v1.list apr22_aod_v1.list apr22_dqm_v1.list apr22_reco_v2.list apr22_aod_v2.list apr22_dqm_v2.list apr22_reco_v3.list apr22_aod_v3.list apr22_dqm_v3.list apr13_reco_v1.list apr13_dqm_v1.list prompt_reco_v4.list prompt_aod_v4.list prompt_dqm_v4.list alcareco_v4.list may10_reco_v1.list may10_aod_v1.list may10_dqm_v1.list may10_skims_v1.list prompt_skim_v4.list may10_reco_v2.list may10_aod_v2.list may10_dqm_v2.list may10_skims_v2.list may3_reco_v1.list may3_aod_v1.list may3_dqm_v1.list may3_skims_v1.list may7_reco_v1.list may7_aod_v1.list may7_dqm_v1.list may7_skims_v1.list may13_reco_v1.list may13_aod_v1.list may13_dqm_v1.list may13_skims_v1.list 16Jun2011_reco_v1.list 16Jun2011_aod_v1.list 16Jun2011_dqm_v1.list prompt_reco_v3.list prompt_aod_v3.list prompt_dqm_v3.list prompt_reco_v5.list prompt_aod_v5.list prompt_dqm_v5.list alcareco_v5.list prompt_skim_v5.list 02Jul2011_reco_v1.list 02Jul2011_aod_v1.list 02Jul2011_dqm_v1.list 02Jul2011_alcareco_v1.list 02Jul2011_skims_v1.list 02Jul2011_skims_v1.list 05Jul2011_reco_v1.list 05Jul2011_aod_v1.list 05Jul2011_dqm_v1.list 05Jul2011_alcareco_v1.list 05Jul2011_skims_v1.list 05Jul2011_skims_v1.list 16Jul2011_reco_v1.list 16Jul2011_aod_v1.list 16Jul2011_dqm_v1.list 16Jul2011_alcareco_v1.list 16Jul2011_skims_v1.list 16Jul2011_skims_v1.list 05Jul2011_reco_HF.list 05Jul2011_aod_HF.list 05Jul2011_dqm_HF.list 05Jul2011_alcareco_HF.list 05Jul2011_skims_HF.list 05Jul2011_skims_HF.list prompt_reco_v6.list prompt_aod_v6.list prompt_dqm_v6.list alcareco_v6.list prompt_skim_v6.list 05Aug2011_reco_v1.list 05Aug2011_aod_v1.list 05Aug2011_dqm_v1.list 05Aug2011_alcareco_v1.list 05Aug2011_skims_v1.list 05Aug2011_skims_v1.list | sort > done.list

echo ""
echo "inconsistencies"
echo ""
diff datasets.list done.list | grep '<' | awk '{print $2}'

echo ""
echo "Error datasets"
echo ""
cat error.list

echo ""
echo "datasets not at FNAL"
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2011A*/* and site = T1_US_FNAL" | grep -v 'test/' | sort > datasets_fnal.list
echo ""
echo "FNAL custodial for: HT, METBTag, DoubleMu, MuOnia, MuHad, DoubleElectron, TauPlusX, MinimumBias, ForwardTriggers, AlCaP0, AlCaPhiSym, Interfill, HcalHPDNoise, HcalNZS, L1Accept, RPCMonitor"
echo ""
echo "missing:"
diff datasets.list datasets_fnal.list | grep '/HT/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/METBTag/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/DoubleMu/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MuOnia/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MuHad/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/DoubleElectron/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/TauPlusX/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MinimumBias/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ForwardTriggers/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/AlCaP0/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/AlCaPhiSym/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Interfill/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/HcalHPDNoise/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/HcalNZS/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/L1Accept/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/RPCMonitor/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
echo ""
echo "non-custodial AOD kept at FNAL for AllPhysics2760, Cosmics, ElectronHad, Jet, MuEG, MultiJet, Photon, PhotonHad, SingleElectron, SingleMu, Tau"
echo ""
echo "missing:"
diff datasets.list datasets_fnal.list | grep '/AllPhysics2760/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep -v 16Jul2011 | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Cosmics/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ElectronHad/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Jet/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MuEG/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MultiJet/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Photon/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep -v 02Jul2011 | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/PhotonHad/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/SingleElectron/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep -v 02Jul2011 | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/SingleMu/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Tau/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
