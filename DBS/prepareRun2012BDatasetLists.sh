python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2012B*/*" | grep -v 'test/' | sort > complete_datasets.list

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
cat datasets.list | grep -v '/AlCaLumiPixels/' | grep -v '/DataScouting/' | grep -v '/FEDMonitor/' | grep -v '/LogMonitor/' | grep -v '/L1Accept/' | grep -v '/RPCMonitor/' | grep -v '/TestEnablesEcalHcalDT/' | grep -v '/TestEnablesTracker/' | grep -v '/DoubleMuParked/' | grep -v '/HTMHTParked/' | grep -v '/MuOniaParked/' | grep -v '/MultiJet1Parked/' | grep -v '/TauParked/' | grep -v '/BJetPlusX/' | grep -v '/DoubleElectron/' | grep -v '/ElectronHad/' | grep -v '/HTMHTParked/' | grep -v '/HcalHPDNoise/' | grep -v '/HcalNZS/' | grep -v '/JetHT/' | grep -v '/JetMon/' | grep -v '/MET/' | grep -v '/MuOnia/' | grep -v '/MultiJet/' | grep -v '/ParkingMonitor/' | grep -v '/SingleElectron/' | grep -v '/VBF1Parked/' | grep -v '/AlCaP0/' | grep -v '/AlCaPhiSym/' | grep -v '/BTag/' | grep -v '/Commissioning/' | grep -v '/Cosmics/' | grep -v '/DoubleMu/' | grep -v '/DoublePhoton/' | grep -v '/DoublePhotonHighPt/' | grep -v '/HTMHT/' | grep -v '/MinimumBias/' | grep -v '/MuEG/' | grep -v '/MuHad/' | grep -v '/NoBPTX/' | grep -v '/PhotonHad/' | grep -v '/SingleMu/' | grep -v '/SinglePhoton/' | grep -v '/Tau/' | grep -v '/TauPlusX/' | awk -F\/ '{print $2}' | sort | uniq
echo ""
echo "datasets not at FNAL"
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2012B*/* and site = T1_US_FNAL" | grep -v 'test/' | sort > datasets_fnal.list
echo ""
echo "PDs staying at CERN: AlCaLumiPixels, DataScouting, FEDMonitor, L1Accept, LogMonitor, RPCMonitor, TestEnablesEcalHcalDT, TestEnablesTracker"
echo ""
echo "PDs not going non-custodially to FNAL: DoubleMuParked, HTMHTParked, MuOniaParked, MultiJet1Parked, TauParked"
echo ""
echo "FNAL custodial for: BJetPlusX, DoubleElectron, ElectronHad, HTMHTParked, HcalHPDNoise, HcalNZS, JetHT, JetMon, MET, MuOnia, MultiJet, ParkingMonitor, SingleElectron, VBF1Parked"
echo ""
echo "missing:"
diff datasets.list datasets_fnal.list | grep '/BJetPlusX/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/DoubleElectron/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ElectronHad/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/HTMHTParked/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/HcalHPDNoise/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/HcalNZS/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/JetHT/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/JetMon/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MET/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MuOnia/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MultiJet/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/ParkingMonitor/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/SingleElectron/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/VBF1Parked/' | grep -vi 'preprod' | grep '<' | awk '{print $2}'
echo ""
echo "non-custodial kept at FNAL for AlCaP0, AlCaPhiSym, BTag, Commissioning, Cosmics, DoubleMu, DoublePhoton, DoublePhotonHighPt, HTMHT, MinimumBias, MuEG, MuHad, NoBPTX, PhotonHad, SingleMu, SinglePhoton, Tau, TauPlusX"
echo ""
echo "missing:"
diff datasets.list datasets_fnal.list | grep '/AlCaP0/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/AlCaPhiSym/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/BTag/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Commissioning/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Cosmics/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/DoubleMu/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/DoublePhoton/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/DoublePhotonHighPt/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/HTMHT/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MinimumBias/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MuEG/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/MuHad/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/NoBPTX/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/PhotonHad/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/SingleMu/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/SinglePhoton/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/Tau/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_fnal.list | grep '/TauPlusX/' | grep -v '/DQM' | grep -v '/ALCARECO' | grep '<' | awk '{print $2}'
echo ""