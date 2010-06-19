python $DBSCMD_HOME/dbsCommandLine.py -c search --query="find dataset where dataset = /*/Commissioning10*/*" --noheader | grep -v 'test/' | sort > datasets.list

cat datasets.list | grep -i express > express.list

cat datasets.list | grep -vi express | grep -vi preproduction | grep -vi preproduction | grep -- '-Error' > error.list

cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RAW' | grep -v RAW-RECO | grep v1 > raw_v1.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RAW' | grep -v RAW-RECO | grep v2 > raw_v2.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RAW' | grep -v RAW-RECO | grep v3 > raw_v3.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RAW' | grep -v RAW-RECO | grep v4 > raw_v4.list

cat datasets.list | grep -vi express | grep -vi preproduction | grep '/Commissioning10-v1/RECO' > prompt_reco_v1.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RECO' | grep -i prompt | grep v2 > prompt_reco_v2.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RECO' | grep -i prompt | grep v3 > prompt_reco_v3.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RECO' | grep -i prompt | grep v4 > prompt_reco_v4.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RECO' | grep -i prompt | grep v5 > prompt_reco_v5.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RECO' | grep -i prompt | grep v6 > prompt_reco_v6.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RECO' | grep -i prompt | grep v7 > prompt_reco_v7.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RECO' | grep -i prompt | grep v8 > prompt_reco_v8.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RECO' | grep -i prompt | grep v9 > prompt_reco_v9.list

cat datasets.list | grep -vi express | grep -vi preproduction | grep ALCA | grep v1 > alcareco_v1.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep ALCA | grep v2 > alcareco_v2.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep ALCA | grep v3 > alcareco_v3.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep ALCA | grep v4 > alcareco_v4.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep ALCA | grep v5 > alcareco_v5.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep ALCA | grep v6 > alcareco_v6.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep ALCA | grep v7 > alcareco_v7.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep ALCA | grep v8 > alcareco_v8.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep ALCA | grep v9 > alcareco_v9.list

cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RAW-RECO' | grep v5 > raw-reco_v5.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RAW-RECO' | grep v6 > raw-reco_v6.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RAW-RECO' | grep v7 > raw-reco_v7.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RAW-RECO' | grep v8 > raw-reco_v8.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep '/RAW-RECO' | grep v9 > raw-reco_v9.list

cat datasets.list | grep -vi express | grep -vi preproduction | grep 'CollisionRecoSequence' | grep v5 > collision_reco_sequence_v5.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep 'CollisionRecoSequence' | grep v6 > collision_reco_sequence_v6.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep 'CollisionRecoSequence' | grep v7 > collision_reco_sequence_v7.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep 'CollisionRecoSequence' | grep v8 > collision_reco_sequence_v8.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep 'CollisionRecoSequence' | grep v9 > collision_reco_sequence_v9.list

cat datasets.list | grep -vi express | grep -vi preproduction | grep Mar1rstReReco > rereco_Mar1rstReReco.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep Apr1ReReco > rereco_Apr1ReReco.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep Apr20ReReco > rereco_Apr20ReReco.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep May6thReReco > rereco_May6thReReco.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep May27thReReco > rereco_May27thReReco.list

cat datasets.list | grep -vi express | grep -vi preproduction | grep Apr1Skim > rereco_Apr1Skim.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep Abr8Skim > rereco_Abr8Skim.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep Apr20Skim > rereco_Apr20Skim.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep -i GR_R_35X_V7A >> rereco_Apr20Skim.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep May6thPDSkim > rereco_May6thSkim.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep May6thSkim >> rereco_May6thSkim.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep May27thSkim > rereco_May27thSkim.list

cat datasets.list | grep -i preproduction > preproduction.list

cat datasets.list | grep -vi express | grep -vi preproduction | grep 'SD_' | grep v1  > sd_v1.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep 'SD_' | grep v9  > sd_v9.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep 'CS_' | grep v1  > cs_v9.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep 'CS_' | grep v8  > cs_v8.list
cat datasets.list | grep -vi express | grep -vi preproduction | grep 'CS_' | grep v9  > cs_v9.list



cat express.list error.list raw_v1.list raw_v2.list raw_v3.list raw_v4.list prompt_reco_v1.list prompt_reco_v2.list prompt_reco_v3.list prompt_reco_v4.list prompt_reco_v5.list prompt_reco_v6.list prompt_reco_v7.list prompt_reco_v8.list alcareco_v1.list alcareco_v2.list alcareco_v3.list alcareco_v4.list alcareco_v5.list alcareco_v6.list alcareco_v7.list alcareco_v8.list rereco_Mar1rstReReco.list raw-reco_v5.list raw-reco_v6.list raw-reco_v7.list raw-reco_v8.list collision_reco_sequence_v5.list collision_reco_sequence_v6.list collision_reco_sequence_v7.list collision_reco_sequence_v8.list rereco_Apr1ReReco.list rereco_Apr1Skim.list prompt_reco_v9.list alcareco_v9.list raw-reco_v9.list collision_reco_sequence_v9.list preproduction.list sd_v1.list cs_v1.list cs_v8.list rereco_Apr20ReReco.list rereco_Abr8Skim.list rereco_Apr20Skim.list sd_v9.list cs_v9.list rereco_May6thReReco.list rereco_May6thSkim.list rereco_May27thReReco.list rereco_May27thSkim.list | sort > done.list

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
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --query="find dataset where dataset = /*/Commissioning10*/* and site = *fnal.gov" --noheader | grep -v 'test/' | sort > datasets_fnal.list
diff datasets.list datasets_fnal.list | grep -vi express | grep -vi preproduction | grep -v '/Test' | grep -vi -- '-Error' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at CNAF"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --query="find dataset where dataset = /*/Commissioning10*/* and site = *cnaf.infn.it" --noheader | sort > datasets_cnaf.list

diff datasets.list datasets_cnaf.list | grep '/ZeroBias/' | grep 'RAW' | grep 'v4' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep '/ZeroBias/' | grep 'RECO' | grep 'v5' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep '/ZeroBias/' | grep 'RECO' | grep 'v6' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep '/ZeroBias/' | grep 'RECO' | grep 'v7' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep '/ZeroBias/' | grep 'RECO' | grep 'v8' | grep '<' | awk '{print $2}'

diff datasets.list datasets_cnaf.list | grep '/MinimumBias/Commissioning10-v4/RAW' | grep '<' | awk '{print $2}'

diff datasets.list datasets_cnaf.list | grep '/ZeroBias/' | grep 'Apr1' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at PIC"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --query="find dataset where dataset = /*/Commissioning10*/* and site = srmcms.pic.es" --noheader | sort > datasets_pic.list

diff datasets.list datasets_pic.list | grep '/MinimumBias/' | grep 'RAW' | grep 'v4' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at IN2P3"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --query="find dataset where dataset = /*/Commissioning10*/* and site = ccsrm.in2p3.fr" --noheader | sort > datasets_in2p3.list

diff datasets.list datasets_in2p3.list | grep '/TestEnables/' | grep -vi test | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/AlCaP0/' | grep -vi test | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/AlCaPhiSymEcal/' | grep -vi test | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/FEDMonitor/' | grep -vi test | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/LogMonitor/' | grep -vi test | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/RPCMonitor/' | grep -vi test | grep '<' | awk '{print $2}'

diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep '/RAW ' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep '/RAW ' | grep 'v2' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep '/RAW ' | grep 'v3' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep 'PromptReco' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep 'PromptReco' | grep 'v2' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep 'PromptReco' | grep 'v3' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep 'PromptReco' | grep 'v4' | grep '<' | awk '{print $2}'

diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep '/RAW ' | grep 'v4' | grep '<' | awk '{print $2}'


echo ""
echo "datasets not at RAL"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --query="find dataset where dataset = /*/Commissioning10*/* and site = srm-cms.gridpp.rl.ac.uk" --noheader | sort > datasets_ral.list

diff datasets.list datasets_ral.list | grep '/Cosmics/' | grep '<' | awk '{print $2}'

diff datasets.list datasets_ral.list | grep '/MinimumBias/' | grep 'RAW' | grep 'v4' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at KIT"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --query="find dataset where dataset = /*/Commissioning10*/* and site = cmssrm-fzk.gridka.de" --noheader | sort > datasets_kit.list

diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/ZeroBias/' | grep 'RAW' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/ZeroBias/' | grep 'RAW' | grep 'v2' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/ZeroBias/' | grep 'RAW' | grep 'v3' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/ZeroBias/' | grep 'PromptReco' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/ZeroBias/' | grep 'PromptReco' | grep 'v2' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/ZeroBias/' | grep 'PromptReco' | grep 'v3' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/ZeroBias/' | grep 'PromptReco' | grep 'v4' | grep '<' | awk '{print $2}'

diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/MinimumBias/' | grep 'RAW' | grep 'v4' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/MinimumBias/' | grep 'RECO' | grep 'v5' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/MinimumBias/' | grep 'RECO' | grep 'v6' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/MinimumBias/' | grep 'RECO' | grep 'v7' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/MinimumBias/' | grep 'RECO' | grep 'v8' | grep '<' | awk '{print $2}'

diff datasets.list datasets_kit.list | grep -vi preproduction | grep '/MinimumBias/' | grep 'Apr1' | grep '<' | awk '{print $2}'