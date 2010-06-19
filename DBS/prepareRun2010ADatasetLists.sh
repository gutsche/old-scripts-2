python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/*" | grep -v 'test/' | sort > complete_datasets.list

cat complete_datasets.list | grep -i express > express.list
cat complete_datasets.list | grep -i preproduction > preproduction.list
cat complete_datasets.list | grep -- '-Error' > error.list

cat complete_datasets.list | grep -vi express | grep -vi preproduction | grep -v -- '-Error' > datasets.list

cat datasets.list | grep '/RAW' | grep -v RAW-RECO | grep v1 > raw_v1.list

cat datasets.list | grep '/RECO' | grep -i prompt | grep v1 > prompt_reco_v1.list
cat datasets.list | grep '/RECO' | grep -i prompt | grep v2 > prompt_reco_v2.list

cat datasets.list | grep ALCA | grep v1 > alcareco_v1.list
cat datasets.list | grep ALCA | grep v2 > alcareco_v2.list
cat datasets.list | grep ALCA | grep v3 > alcareco_v3.list

cat datasets.list | grep '/RAW-RECO' | grep v2 > dpg_skims_v2.list

cat datasets.list | grep 'CollisionRecoSequence' | grep v1 > collision_reco_sequence_v1.list
cat datasets.list | grep 'CollisionRecoSequence' | grep v2 > collision_reco_sequence_v2.list

# cat datasets.list | grep 'SD_' | grep v1  > sd_v1.list

cat datasets.list | grep 'CS_' | grep v1  > cs_v1.list
cat datasets.list | grep 'CS_' | grep v2  > cs_v2.list

cat datasets.list | grep May27thReReco > rereco_May27thReReco.list
cat datasets.list | grep May27thSkim > rereco_May27thSkim.list


cat express.list error.list preproduction.list raw_v1.list prompt_reco_v1.list alcareco_v1.list collision_reco_sequence_v1.list cs_v1.list prompt_reco_v2.list alcareco_v2.list collision_reco_sequence_v2.list cs_v2.list alcareco_v3.list dpg_skims_v2.list rereco_May27thReReco.list rereco_May27thSkim.list | sort > done.list

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
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_US_FNAL" | grep -v 'test/' | sort > datasets_fnal.list
diff datasets.list datasets_fnal.list | grep -v '/Test' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at CNAF"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_IT_CNAF" | sort > datasets_cnaf.list

diff datasets.list datasets_cnaf.list | grep '/MuMonitor/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep '/RandomTriggers/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep '/FEDMonitor/' | grep '<' | awk '{print $2}'

diff datasets.list datasets_cnaf.list | grep 'JetMETTauMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep 'JetMETTau/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep 'EGMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep 'EG/' | grep 'RAW' | grep 'v1' | grep -v 'RAW-RECO' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_cnaf.list | grep 'MuMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep 'Mu/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep 'MinimumBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep 'Cosmics/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep 'ZeroBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep 'Commissioning/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at PIC"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_ES_PIC" | sort > datasets_pic.list

diff datasets.list datasets_pic.list | grep '/Mu/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep '/LogMonitor/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep '/RPCMonitor/' | grep '<' | awk '{print $2}'

diff datasets.list datasets_pic.list | grep 'JetMETTauMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep 'JetMETTau/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep 'EGMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep 'EG/' | grep 'RAW' | grep 'v1' | grep -v 'RAW-RECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep 'MuMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_pic.list | grep 'Mu/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep 'MinimumBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep 'Cosmics/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep 'ZeroBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep 'Commissioning/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at IN2P3"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_FR_CCIN2P3" | sort > datasets_in2p3.list

diff datasets.list datasets_in2p3.list | grep '/EGMonitor/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/TestEnables/' | grep '<' | awk '{print $2}'

diff datasets.list datasets_in2p3.list | grep 'JetMETTauMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep 'JetMETTau/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_in2p3.list | grep 'EGMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep 'EG/' | grep 'RAW' | grep 'v1' | grep -v 'RAW-RECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep 'MuMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep 'Mu/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep 'MinimumBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep 'Cosmics/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep 'ZeroBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep 'Commissioning/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at RAL"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_UK_RAL" | sort > datasets_ral.list

diff datasets.list datasets_ral.list | grep '/EG/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_ral.list | grep '/AlCaP0/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_ral.list | grep '/AlCaPhiSymEcal/' | grep '<' | awk '{print $2}'

diff datasets.list datasets_ral.list | grep 'JetMETTauMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_ral.list | grep 'JetMETTau/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_ral.list | grep 'EGMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_ral.list | grep 'EG/' | grep 'RAW' | grep 'v1' | grep -v 'RAW-RECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_ral.list | grep 'MuMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_ral.list | grep 'Mu/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_ral.list | grep 'MinimumBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_ral.list | grep 'Cosmics/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_ral.list | grep 'ZeroBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_ral.list | grep 'Commissioning/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at KIT"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_DE_KIT" | sort > datasets_kit.list

diff datasets.list datasets_kit.list | grep '/MinimumBias/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep '/ZeroBias/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep '/Commissioning/' | grep '<' | awk '{print $2}'

diff datasets.list datasets_kit.list | grep 'JetMETTauMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep 'JetMETTau/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep 'EGMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep 'EG/' | grep 'RAW' | grep 'v1' | grep -v 'RAW-RECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep 'MuMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep 'Mu/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_kit.list | grep 'MinimumBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep 'Cosmics/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_kit.list | grep 'ZeroBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_kit.list | grep 'Commissioning/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at ASGC"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_TW_ASGC" | sort > datasets_asgc.list

diff datasets.list datasets_asgc.list | grep '/Cosmics/' | grep '<' | awk '{print $2}'

diff datasets.list datasets_asgc.list | grep 'JetMETTauMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_asgc.list | grep 'JetMETTau/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_asgc.list | grep 'EGMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_asgc.list | grep 'EG/' | grep 'RAW' | grep 'v1' | grep -v 'RAW-RECO' | grep '<' | awk '{print $2}'
diff datasets.list datasets_asgc.list | grep 'MuMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_asgc.list | grep 'Mu/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_asgc.list | grep 'MinimumBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_asgc.list | grep 'Cosmics/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_asgc.list | grep 'ZeroBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_asgc.list | grep 'Commissioning/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
