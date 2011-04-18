python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2011A*/*" | grep -v 'test/' | sort > complete_datasets.list

cat complete_datasets.list | grep -i express > express.list
cat complete_datasets.list | grep -i preprod > preproduction.list
cat complete_datasets.list | grep -- '-Error' > error.list

cat complete_datasets.list | grep -vi express | grep -vi preprod | grep -v -- '-Error' > datasets.list

cat datasets.list | grep '/RAW' | grep -v RAW-RECO | grep v1 > raw_v1.list
cat datasets.list | grep '/RAW' | grep -v RAW-RECO | grep v2 > raw_v2.list

cat datasets.list | grep '/RECO' | grep -i prompt | grep v1 > prompt_reco_v1.list
cat datasets.list | grep '/RECO' | grep -i prompt | grep v2 > prompt_reco_v2.list

cat datasets.list | grep '/AOD' | grep -i prompt | grep v1 > prompt_aod_v1.list
cat datasets.list | grep '/AOD' | grep -i prompt | grep v2 > prompt_aod_v2.list

cat datasets.list | grep '/DQM' | grep -i prompt | grep v1 > prompt_dqm_v1.list
cat datasets.list | grep '/DQM' | grep -i prompt | grep v2 > prompt_dqm_v2.list

cat datasets.list | grep ALCA | grep v1 > alcareco_v1.list
cat datasets.list | grep ALCA | grep v2 > alcareco_v2.list

cat express.list error.list preproduction.list raw_v1.list prompt_reco_v1.list prompt_aod_v1.list prompt_dqm_v1.list alcareco_v1.list raw_v2.list prompt_reco_v2.list prompt_aod_v2.list prompt_dqm_v2.list alcareco_v2.list | sort > done.list

echo ""
echo "inconsistencies"
echo ""
diff complete_datasets.list done.list | grep '<' | awk '{print $2}'

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
diff datasets.list datasets_fnal.list | grep '/AllPhysics2760/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Cosmics/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ElectronHad/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Jet/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MuEG/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MultiJet/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Photon/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/PhotonHad/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/SingleElectron/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/SingleMu/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Tau/' | grep '/AOD' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
