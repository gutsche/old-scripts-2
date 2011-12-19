python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2011B*/*" | grep -v 'test/' | sort > complete_datasets.list

cat complete_datasets.list | grep -i express > express.list
cat complete_datasets.list | grep -i preprod > preproduction.list
cat complete_datasets.list | grep -- '-Error' > error.list

cat complete_datasets.list | grep -vi express | grep -v PreScaleThingy | grep -vi preprod | grep -v -- '-Error' > datasets.list

cat datasets.list | grep '/RAW' | grep -v RAW-RECO | grep v1 > raw_v1.list

cat datasets.list | grep '/RECO' | grep -i prompt | grep v1 > prompt_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i prompt | grep v1 > prompt_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i prompt | grep v1 > prompt_dqm_v1.list
cat datasets.list | grep -i promptskim | grep v1 > prompt_skim_v1.list
cat datasets.list | grep ALCA | grep v1 > alcareco_v1.list
# prompt_reco_v1.list prompt_aod_v1.list prompt_dqm_v1.list alcareco_v1.list prompt_skim_v1.list

cat datasets.list | grep '/RECO' | grep -i 14Oct2011 | grep v1 > 14Oct2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 14Oct2011 | grep v1 > 14Oct2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 14Oct2011 | grep v1 > 14Oct2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 14Oct2011 | grep v1 > 14Oct2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 14Oct2011 | grep v1 > 14Oct2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 14Oct2011 | grep v1 >> 14Oct2011_skims_v1.list
# 14Oct2011_reco_v1.list 14Oct2011_aod_v1.list 14Oct2011_dqm_v1.list 14Oct2011_alcareco_v1.list 14Oct2011_skims_v1.list 14Oct2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 17Oct2011 | grep v1 > 17Oct2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 17Oct2011 | grep v1 > 17Oct2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 17Oct2011 | grep v1 > 17Oct2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 17Oct2011 | grep v1 > 17Oct2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 17Oct2011 | grep v1 > 17Oct2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 17Oct2011 | grep v1 >> 17Oct2011_skims_v1.list
# 17Oct2011_reco_v1.list 17Oct2011_aod_v1.list 17Oct2011_dqm_v1.list 17Oct2011_alcareco_v1.list 17Oct2011_skims_v1.list 17Oct2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 18Oct2011 | grep v1 > 18Oct2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 18Oct2011 | grep v1 > 18Oct2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 18Oct2011 | grep v1 > 18Oct2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 18Oct2011 | grep v1 > 18Oct2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 18Oct2011 | grep v1 > 18Oct2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 18Oct2011 | grep v1 >> 18Oct2011_skims_v1.list
# 18Oct2011_reco_v1.list 18Oct2011_aod_v1.list 18Oct2011_dqm_v1.list 18Oct2011_alcareco_v1.list 18Oct2011_skims_v1.list 18Oct2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 19Oct2011 | grep v1 > 19Oct2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 19Oct2011 | grep v1 > 19Oct2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 19Oct2011 | grep v1 > 19Oct2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 19Oct2011 | grep v1 > 19Oct2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 19Oct2011 | grep v1 > 19Oct2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 19Oct2011 | grep v1 >> 19Oct2011_skims_v1.list
# 19Oct2011_reco_v1.list 19Oct2011_aod_v1.list 19Oct2011_dqm_v1.list 19Oct2011_alcareco_v1.list 19Oct2011_skims_v1.list 19Oct2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 20Oct2011 | grep v1 > 20Oct2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 20Oct2011 | grep v1 > 20Oct2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 20Oct2011 | grep v1 > 20Oct2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 20Oct2011 | grep v1 > 20Oct2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 20Oct2011 | grep v1 > 20Oct2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 20Oct2011 | grep v1 >> 20Oct2011_skims_v1.list
# 20Oct2011_reco_v1.list 20Oct2011_aod_v1.list 20Oct2011_dqm_v1.list 20Oct2011_alcareco_v1.list 20Oct2011_skims_v1.list 20Oct2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 21Oct2011 | grep v1 > 21Oct2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 21Oct2011 | grep v1 > 21Oct2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 21Oct2011 | grep v1 > 21Oct2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 21Oct2011 | grep v1 > 21Oct2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 21Oct2011 | grep v1 > 21Oct2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 21Oct2011 | grep v1 >> 21Oct2011_skims_v1.list
# 21Oct2011_reco_v1.list 21Oct2011_aod_v1.list 21Oct2011_dqm_v1.list 21Oct2011_alcareco_v1.list 21Oct2011_skims_v1.list 21Oct2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 02Nov2010 | grep v1 > 02Nov2010_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 02Nov2010 | grep v1 > 02Nov2010_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 02Nov2010 | grep v1 > 02Nov2010_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 02Nov2010 | grep v1 > 02Nov2010_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 02Nov2010 | grep v1 > 02Nov2010_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 02Nov2010 | grep v1 >> 02Nov2010_skims_v1.list
# 02Nov2010_reco_v1.list 02Nov2010_aod_v1.list 02Nov2010_dqm_v1.list 02Nov2010_alcareco_v1.list 02Nov2010_skims_v1.list 02Nov2010_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 08Nov2011 | grep v1 > 08Nov2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 08Nov2011 | grep v1 > 08Nov2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 08Nov2011 | grep v1 > 08Nov2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 08Nov2011 | grep v1 > 08Nov2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 08Nov2011 | grep v1 > 08Nov2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 08Nov2011 | grep v1 >> 08Nov2011_skims_v1.list
# 08Nov2011_reco_v1.list 08Nov2011_aod_v1.list 08Nov2011_dqm_v1.list 08Nov2011_alcareco_v1.list 08Nov2011_skims_v1.list 08Nov2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 15Nov2011 | grep v1 > 15Nov2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 15Nov2011 | grep v1 > 15Nov2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 15Nov2011 | grep v1 > 15Nov2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 15Nov2011 | grep v1 > 15Nov2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 15Nov2011 | grep v1 > 15Nov2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 15Nov2011 | grep v1 >> 15Nov2011_skims_v1.list
# 15Nov2011_reco_v1.list 15Nov2011_aod_v1.list 15Nov2011_dqm_v1.list 15Nov2011_alcareco_v1.list 15Nov2011_skims_v1.list 15Nov2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 18Nov2011 | grep v1 > 18Nov2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 18Nov2011 | grep v1 > 18Nov2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 18Nov2011 | grep v1 > 18Nov2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 18Nov2011 | grep v1 > 18Nov2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 18Nov2011 | grep v1 > 18Nov2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 18Nov2011 | grep v1 >> 18Nov2011_skims_v1.list
# 18Nov2011_reco_v1.list 18Nov2011_aod_v1.list 18Nov2011_dqm_v1.list 18Nov2011_alcareco_v1.list 18Nov2011_skims_v1.list 18Nov2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 19Nov2011 | grep v1 > 19Nov2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 19Nov2011 | grep v1 > 19Nov2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 19Nov2011 | grep v1 > 19Nov2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 19Nov2011 | grep v1 > 19Nov2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 19Nov2011 | grep v1 > 19Nov2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 19Nov2011 | grep v1 >> 19Nov2011_skims_v1.list
# 19Nov2011_reco_v1.list 19Nov2011_aod_v1.list 19Nov2011_dqm_v1.list 19Nov2011_alcareco_v1.list 19Nov2011_skims_v1.list 19Nov2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 26Nov2011 | grep v1 > 26Nov2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 26Nov2011 | grep v1 > 26Nov2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 26Nov2011 | grep v1 > 26Nov2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 26Nov2011 | grep v1 > 26Nov2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 26Nov2011 | grep v1 > 26Nov2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 26Nov2011 | grep v1 >> 26Nov2011_skims_v1.list
# 26Nov2011_reco_v1.list 26Nov2011_aod_v1.list 26Nov2011_dqm_v1.list 26Nov2011_alcareco_v1.list 26Nov2011_skims_v1.list 26Nov2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 30Nov2011 | grep v1 > 30Nov2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 30Nov2011 | grep v1 > 30Nov2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 30Nov2011 | grep v1 > 30Nov2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 30Nov2011 | grep v1 > 30Nov2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 30Nov2011 | grep v1 > 30Nov2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 30Nov2011 | grep v1 >> 30Nov2011_skims_v1.list
# 30Nov2011_reco_v1.list 30Nov2011_aod_v1.list 30Nov2011_dqm_v1.list 30Nov2011_alcareco_v1.list 30Nov2011_skims_v1.list 30Nov2011_skims_v1.list

cat datasets.list | grep '/RECO' | grep -i 09Dec2011 | grep v1 > 09Dec2011_reco_v1.list
cat datasets.list | grep '/AOD' | grep -i 09Dec2011 | grep v1 > 09Dec2011_aod_v1.list
cat datasets.list | grep '/DQM' | grep -i 09Dec2011 | grep v1 > 09Dec2011_dqm_v1.list
cat datasets.list | grep '/ALCARECO' | grep -i 09Dec2011 | grep v1 > 09Dec2011_alcareco_v1.list
cat datasets.list | grep '/RAW-RECO' | grep -i 09Dec2011 | grep v1 > 09Dec2011_skims_v1.list
cat datasets.list | grep '/USER' | grep -i 09Dec2011 | grep v1 >> 09Dec2011_skims_v1.list
# 09Dec2011_reco_v1.list 09Dec2011_aod_v1.list 09Dec2011_dqm_v1.list 09Dec2011_alcareco_v1.list 09Dec2011_skims_v1.list 09Dec2011_skims_v1.list

cat express.list error.list preproduction.list raw_v1.list prompt_reco_v1.list prompt_aod_v1.list prompt_dqm_v1.list alcareco_v1.list prompt_skim_v1.list 14Oct2011_reco_v1.list 14Oct2011_aod_v1.list 14Oct2011_dqm_v1.list 14Oct2011_alcareco_v1.list 14Oct2011_skims_v1.list 14Oct2011_skims_v1.list 18Oct2011_reco_v1.list 18Oct2011_aod_v1.list 18Oct2011_dqm_v1.list 18Oct2011_alcareco_v1.list 18Oct2011_skims_v1.list 18Oct2011_skims_v1.list 19Oct2011_reco_v1.list 19Oct2011_aod_v1.list 19Oct2011_dqm_v1.list 19Oct2011_alcareco_v1.list 19Oct2011_skims_v1.list 19Oct2011_skims_v1.list 08Nov2011_reco_v1.list 08Nov2011_aod_v1.list 08Nov2011_dqm_v1.list 08Nov2011_alcareco_v1.list 08Nov2011_skims_v1.list 08Nov2011_skims_v1.list 15Nov2011_reco_v1.list 15Nov2011_aod_v1.list 15Nov2011_dqm_v1.list 15Nov2011_alcareco_v1.list 15Nov2011_skims_v1.list 15Nov2011_skims_v1.list 09Dec2011_reco_v1.list 09Dec2011_aod_v1.list 09Dec2011_dqm_v1.list 09Dec2011_alcareco_v1.list 09Dec2011_skims_v1.list 09Dec2011_skims_v1.list 21Oct2011_reco_v1.list 21Oct2011_aod_v1.list 21Oct2011_dqm_v1.list 21Oct2011_alcareco_v1.list 21Oct2011_skims_v1.list 21Oct2011_skims_v1.list 19Nov2011_reco_v1.list 19Nov2011_aod_v1.list 19Nov2011_dqm_v1.list 19Nov2011_alcareco_v1.list 19Nov2011_skims_v1.list 19Nov2011_skims_v1.list 26Nov2011_reco_v1.list 26Nov2011_aod_v1.list 26Nov2011_dqm_v1.list 26Nov2011_alcareco_v1.list 26Nov2011_skims_v1.list 26Nov2011_skims_v1.list 30Nov2011_reco_v1.list 30Nov2011_aod_v1.list 30Nov2011_dqm_v1.list 30Nov2011_alcareco_v1.list 30Nov2011_skims_v1.list 30Nov2011_skims_v1.list 17Oct2011_reco_v1.list 17Oct2011_aod_v1.list 17Oct2011_dqm_v1.list 17Oct2011_alcareco_v1.list 17Oct2011_skims_v1.list 17Oct2011_skims_v1.list 20Oct2011_reco_v1.list 20Oct2011_aod_v1.list 20Oct2011_dqm_v1.list 20Oct2011_alcareco_v1.list 20Oct2011_skims_v1.list 20Oct2011_skims_v1.list 02Nov2010_reco_v1.list 02Nov2010_aod_v1.list 02Nov2010_dqm_v1.list 02Nov2010_alcareco_v1.list 02Nov2010_skims_v1.list 02Nov2010_skims_v1.list 18Nov2011_reco_v1.list 18Nov2011_aod_v1.list 18Nov2011_dqm_v1.list 18Nov2011_alcareco_v1.list 18Nov2011_skims_v1.list 18Nov2011_skims_v1.list | sort > done.list

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
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2011B*/* and site = T1_US_FNAL" | grep -v 'test/' | sort > datasets_fnal.list
echo ""
echo "FNAL custodial for: HT, MET, BTag, DoubleMu, MuOnia, MuHad, TauPlusX, MinimumBias, ForwardTriggers, AlCaP0, AlCaPhiSym, Interfill, HcalHPDNoise, HcalNZS, L1Accept, RPCMonitor"
echo ""
echo "missing:"
diff datasets.list datasets_fnal.list | grep '/HT/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MET/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/BTag/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/DoubleMu/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MuOnia/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MuHad/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
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
echo "non-custodial AOD kept at FNAL for AllPhysics2760, Cosmics, ElectronHad, Jet, MuEG, MultiJet, Photon, PhotonHad, SingleElectron, SingleMu, Tau, DoubleElectron"
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
diff datasets.list datasets_fnal.list | grep '/DoubleElectron/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Tau/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
