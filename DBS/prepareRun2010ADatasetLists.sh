python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/*" | grep -v 'test/' | sort > complete_datasets.list

cat complete_datasets.list | grep -i express > express.list
cat complete_datasets.list | grep -i preprod > preproduction.list
cat complete_datasets.list | grep -- '-Error' > error.list

cat complete_datasets.list | grep -vi express | grep -vi preproduction | grep -v -- '-Error' > datasets.list

cat datasets.list | grep '/RAW' | grep -v RAW-RECO | grep v1 > raw_v1.list

cat datasets.list | grep '/RECO' | grep -i prompt | grep v1 > prompt_reco_v1.list
cat datasets.list | grep '/RECO' | grep -i prompt | grep v2 > prompt_reco_v2.list
cat datasets.list | grep '/RECO' | grep -i prompt | grep v4 > prompt_reco_v4.list
cat datasets.list | grep '/RECO' | grep -i prompt | grep v5 > prompt_reco_v5.list
cat datasets.list | grep '/RECO' | grep -i prompt | grep v6 > prompt_reco_v6.list

cat datasets.list | grep ALCA | grep v1 > alcareco_v1.list
cat datasets.list | grep ALCA | grep v2 > alcareco_v2.list
cat datasets.list | grep ALCA | grep v3 > alcareco_v3.list
cat datasets.list | grep ALCA | grep v4 > alcareco_v4.list
cat datasets.list | grep ALCA | grep v5 > alcareco_v5.list
cat datasets.list | grep ALCA | grep v6 > alcareco_v6.list

cat datasets.list | grep '/RAW-RECO' | grep v2 > dpg_skims_v2.list
cat datasets.list | grep '/RAW-RECO' | grep v4 > dpg_skims_v4.list
cat datasets.list | grep '/USER' | grep v4 >> dpg_skims_v4.list
cat datasets.list | grep '/RAW-RECO' | grep v5 > dpg_skims_v5.list
cat datasets.list | grep '/USER' | grep v5 >> dpg_skims_v5.list
cat datasets.list | grep '/RAW-RECO' | grep v6 > dpg_skims_v6.list
cat datasets.list | grep '/USER' | grep v6 >> dpg_skims_v6.list

cat datasets.list | grep 'CollisionRecoSequence' | grep v1 > collision_reco_sequence_v1.list
cat datasets.list | grep 'CollisionRecoSequence' | grep v2 > collision_reco_sequence_v2.list
cat datasets.list | grep 'CollisionRecoSequence' | grep v4 > collision_reco_sequence_v4.list
cat datasets.list | grep 'CollisionRecoSequence' | grep v5 > collision_reco_sequence_v5.list
cat datasets.list | grep 'CollisionRecoSequence' | grep v6 > collision_reco_sequence_v6.list

# template to add to consistency check
#  prompt_reco_v4.list alcareco_v4.list collision_reco_sequence_v4.list cs_v4.list alcareco_v4.list dpg_skims_v4.list 

cat datasets.list | grep 'HLTtest' > rereco_hltest.list

cat datasets.list | grep 'SD_' | grep v6  > sd_v6.list

cat datasets.list | grep 'CS_' | grep v1  > cs_v1.list
cat datasets.list | grep 'CS_' | grep v2  > cs_v2.list
cat datasets.list | grep 'CS_' | grep v4  > cs_v4.list
cat datasets.list | grep 'CS_' | grep v5  > cs_v5.list
cat datasets.list | grep 'CS_' | grep v6  > cs_v6.list

cat datasets.list | grep May27thReReco > rereco_May27thReReco.list
cat datasets.list | grep May27thSkim > rereco_May27thSkim.list

cat datasets.list | grep Jun9thReReco > rereco_Jun9thReReco.list
cat datasets.list | grep Jun9thSkim > rereco_Jun9thSkim.list

cat datasets.list | grep Jun14thReReco > rereco_Jun14thReReco.list
cat datasets.list | grep Jun14thSkim > rereco_Jun14thSkim.list

cat datasets.list | grep Jul6thReReco > rereco_Jul6thReReco.list
cat datasets.list | grep Jul6thSkim > rereco_Jul6thSkim.list

cat datasets.list | grep Jul15thReReco > rereco_Jul15thReReco.list
cat datasets.list | grep Jul15thSkim > rereco_Jul15thSkim.list

cat datasets.list | grep Jul16thReReco > rereco_Jul16thReReco.list
cat datasets.list | grep Jul16thSkim > rereco_Jul16thSkim.list

cat datasets.list | grep Jul23ReReco > rereco_Jul23ReReco.list
cat datasets.list | grep Jul23Skim > rereco_Jul23Skim.list

cat datasets.list | grep Jul26thReReco > rereco_Jul26thReReco.list
cat datasets.list | grep Jul26thSkim > rereco_Jul26thSkim.list

cat datasets.list | grep 'Sep17ReReco' | grep v2 > rereco_sep17_v2.list

cat datasets.list | grep 'Sep17Skim' | grep v1 > skim_sep17_v1.list
cat datasets.list | grep 'Sep17Skim' | grep v2 > skim_sep17_v2.list

cat datasets.list | grep 'Nov4ReReco' | grep v1 > rereco_nov4_v1.list
cat datasets.list | grep 'Nov4Skim' | grep v1 > skim_nov4_v1.list

cat datasets.list | grep 'Dec4ReReco' | grep v1 > rereco_dec4_v1.list
cat datasets.list | grep 'Dec4Skim' | grep v1 > skim_dec4_v1.list

cat datasets.list | grep 'Dec22ReReco' | grep v1 > rereco_dec22_v1.list
cat datasets.list | grep 'Dec22Skim' | grep v2 > skim_dec22_v2.list

cat express.list error.list preproduction.list raw_v1.list prompt_reco_v1.list alcareco_v1.list collision_reco_sequence_v1.list cs_v1.list prompt_reco_v2.list alcareco_v2.list collision_reco_sequence_v2.list cs_v2.list alcareco_v3.list dpg_skims_v2.list rereco_May27thReReco.list rereco_May27thSkim.list prompt_reco_v4.list alcareco_v4.list collision_reco_sequence_v4.list cs_v4.list alcareco_v4.list dpg_skims_v4.list rereco_Jun9thReReco.list rereco_Jun9thSkim.list rereco_Jun14thReReco.list rereco_Jun14thSkim.list rereco_hltest.list  prompt_reco_v5.list alcareco_v5.list collision_reco_sequence_v5.list cs_v5.list alcareco_v5.list dpg_skims_v5.list  prompt_reco_v6.list alcareco_v6.list collision_reco_sequence_v6.list cs_v6.list alcareco_v6.list dpg_skims_v6.list sd_v6.list rereco_Jul6thReReco.list rereco_Jul6thSkim.list rereco_Jul15thReReco.list rereco_Jul15thSkim.list rereco_Jul16thReReco.list rereco_Jul16thSkim.list rereco_Jul23ReReco.list rereco_Jul23Skim.list rereco_Jul26thReReco.list rereco_Jul26thSkim.list rereco_sep17_v2.list skim_sep17_v1.list skim_sep17_v2.list rereco_nov4_v1.list skim_nov4_v1.list rereco_dec4_v1.list skim_dec4_v1.list rereco_dec22_v1.list skim_dec22_v2.list | sort > done.list

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
echo "FNAL custodial for: JetMETTauMonitor, JetMETTau, JetMET, CastorTest, HcalHPDNoise, HcalNZS"
echo "non-custodial kept at FNAL for BTau, EG, EGMonitor. MinimumBias, Mu, MuOnia, ZeroBias: currently only Nov4 and Dec22"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_US_FNAL" | grep -v 'test/' | sort > datasets_fnal.list
diff datasets.list datasets_fnal.list | grep -v '/Test' | grep -v 'HeavyIonTest' | grep -v '/DQM' | grep -v 'NanoDST' | grep -vi preprod | grep -v L1Accept | grep -v ALCARECO | grep -v Dec4 | grep -v Jul15 | grep -v Jul26 | grep -v Jul6 | grep -v Jun9 | grep -v May27 | grep -v CollisionRecoSequence | grep -v '/Commissioning' | grep '<' | awk '{print $2}'

# echo ""
# echo "datasets not at CNAF"
# echo ""
# python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_IT_CNAF" | sort > datasets_cnaf.list
# 
# diff datasets.list datasets_cnaf.list | grep '/MuMonitor/' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_cnaf.list | grep '/RandomTriggers/' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_cnaf.list | grep '/FEDMonitor/' | grep '<' | awk '{print $2}'
# 
# diff datasets.list datasets_cnaf.list | grep 'JetMETTauMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_cnaf.list | grep 'JetMETTau/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_cnaf.list | grep 'EGMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_cnaf.list | grep 'EG/' | grep 'RAW' | grep 'v1' | grep -v 'RAW-RECO' | grep '<' | awk '{print $2}'
# # diff datasets.list datasets_cnaf.list | grep 'MuMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_cnaf.list | grep 'Mu/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_cnaf.list | grep 'MinimumBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_cnaf.list | grep 'Cosmics/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_cnaf.list | grep 'ZeroBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_cnaf.list | grep 'Commissioning/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# 
# echo ""
# echo "datasets not at PIC"
# echo ""
# python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_ES_PIC" | sort > datasets_pic.list
# 
# diff datasets.list datasets_pic.list | grep '/Mu/' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_pic.list | grep '/LogMonitor/' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_pic.list | grep '/RPCMonitor/' | grep '<' | awk '{print $2}'
# 
# diff datasets.list datasets_pic.list | grep 'JetMETTauMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_pic.list | grep 'JetMETTau/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_pic.list | grep 'EGMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_pic.list | grep 'EG/' | grep 'RAW' | grep 'v1' | grep -v 'RAW-RECO' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_pic.list | grep 'MuMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# # diff datasets.list datasets_pic.list | grep 'Mu/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_pic.list | grep 'MinimumBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_pic.list | grep 'Cosmics/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_pic.list | grep 'ZeroBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_pic.list | grep 'Commissioning/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# 
# echo ""
# echo "datasets not at IN2P3"
# echo ""
# python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_FR_CCIN2P3" | sort > datasets_in2p3.list
# 
# diff datasets.list datasets_in2p3.list | grep '/EGMonitor/' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_in2p3.list | grep '/TestEnables/' | grep '<' | awk '{print $2}'
# 
# diff datasets.list datasets_in2p3.list | grep 'JetMETTauMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_in2p3.list | grep 'JetMETTau/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# # diff datasets.list datasets_in2p3.list | grep 'EGMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_in2p3.list | grep 'EG/' | grep 'RAW' | grep 'v1' | grep -v 'RAW-RECO' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_in2p3.list | grep 'MuMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_in2p3.list | grep 'Mu/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_in2p3.list | grep 'MinimumBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_in2p3.list | grep 'Cosmics/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_in2p3.list | grep 'ZeroBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_in2p3.list | grep 'Commissioning/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# 
# echo ""
# echo "datasets not at RAL"
# echo ""
# python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_UK_RAL" | sort > datasets_ral.list
# 
# diff datasets.list datasets_ral.list | grep '/EG/' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_ral.list | grep '/AlCaP0/' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_ral.list | grep '/AlCaPhiSymEcal/' | grep '<' | awk '{print $2}'
# 
# diff datasets.list datasets_ral.list | grep 'JetMETTauMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_ral.list | grep 'JetMETTau/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_ral.list | grep 'EGMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# # diff datasets.list datasets_ral.list | grep 'EG/' | grep 'RAW' | grep 'v1' | grep -v 'RAW-RECO' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_ral.list | grep 'MuMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_ral.list | grep 'Mu/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_ral.list | grep 'MinimumBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_ral.list | grep 'Cosmics/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_ral.list | grep 'ZeroBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_ral.list | grep 'Commissioning/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# 
# echo ""
# echo "datasets not at KIT"
# echo ""
# python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_DE_KIT" | sort > datasets_kit.list
# 
# diff datasets.list datasets_kit.list | grep '/MinimumBias/' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_kit.list | grep '/ZeroBias/' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_kit.list | grep '/Commissioning/' | grep '<' | awk '{print $2}'
# 
# diff datasets.list datasets_kit.list | grep 'JetMETTauMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_kit.list | grep 'JetMETTau/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_kit.list | grep 'EGMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_kit.list | grep 'EG/' | grep 'RAW' | grep 'v1' | grep -v 'RAW-RECO' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_kit.list | grep 'MuMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_kit.list | grep 'Mu/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# # diff datasets.list datasets_kit.list | grep 'MinimumBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_kit.list | grep 'Cosmics/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# # diff datasets.list datasets_kit.list | grep 'ZeroBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# # diff datasets.list datasets_kit.list | grep 'Commissioning/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# 
# echo ""
# echo "datasets not at ASGC"
# echo ""
# python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010A*/* and site = T1_TW_ASGC" | sort > datasets_asgc.list
# 
# diff datasets.list datasets_asgc.list | grep '/Cosmics/' | grep '<' | awk '{print $2}'
# 
# diff datasets.list datasets_asgc.list | grep 'JetMETTauMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_asgc.list | grep 'JetMETTau/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_asgc.list | grep 'EGMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_asgc.list | grep 'EG/' | grep 'RAW' | grep 'v1' | grep -v 'RAW-RECO' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_asgc.list | grep 'MuMonitor/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_asgc.list | grep 'Mu/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_asgc.list | grep 'MinimumBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# # diff datasets.list datasets_asgc.list | grep 'Cosmics/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_asgc.list | grep 'ZeroBias/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
# diff datasets.list datasets_asgc.list | grep 'Commissioning/' | grep 'RAW' | grep -v 'RAW-RECO' | grep 'v1' | grep '<' | awk '{print $2}'
