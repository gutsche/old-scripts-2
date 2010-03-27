python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/*" | grep -v 'test/' | sort > datasets.list

cat datasets.list | grep -i express > express.list

cat datasets.list | grep -vi express | grep -- '-Error' > error.list

cat datasets.list | grep -vi express | grep '/RAW' | grep -v RAW-RECO | grep v1 > raw_v1.list
cat datasets.list | grep -vi express | grep '/RAW' | grep -v RAW-RECO | grep v2 > raw_v2.list
cat datasets.list | grep -vi express | grep '/RAW' | grep -v RAW-RECO | grep v3 > raw_v3.list
cat datasets.list | grep -vi express | grep '/RAW' | grep -v RAW-RECO | grep v4 > raw_v4.list

cat datasets.list | grep -vi express | grep '/Commissioning10-v1/RECO' > prompt_reco_v1.list
cat datasets.list | grep -vi express | grep '/RECO' | grep -i prompt | grep v2 > prompt_reco_v2.list
cat datasets.list | grep -vi express | grep '/RECO' | grep -i prompt | grep v3 > prompt_reco_v3.list
cat datasets.list | grep -vi express | grep '/RECO' | grep -i prompt | grep v4 > prompt_reco_v4.list
cat datasets.list | grep -vi express | grep '/RECO' | grep -i prompt | grep v5 > prompt_reco_v5.list

cat datasets.list | grep -vi express | grep ALCA | grep v1 > alcareco_v1.list
cat datasets.list | grep -vi express | grep ALCA | grep v2 > alcareco_v2.list
cat datasets.list | grep -vi express | grep ALCA | grep v3 > alcareco_v3.list
cat datasets.list | grep -vi express | grep ALCA | grep v4 > alcareco_v4.list
cat datasets.list | grep -vi express | grep ALCA | grep v5 > alcareco_v5.list

cat datasets.list | grep -vi express | grep Mar1rstReReco > rereco_Mar1rstReReco.list

cat express.list error.list raw_v1.list raw_v2.list raw_v3.list raw_v4.list prompt_reco_v1.list prompt_reco_v2.list prompt_reco_v3.list prompt_reco_v4.list prompt_reco_v5.list alcareco_v1.list alcareco_v2.list alcareco_v3.list alcareco_v4.list alcareco_v5.list rereco_Mar1rstReReco.list | sort > done.list

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
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/* and site = *fnal.gov" | grep -v 'test/' | sort > datasets_fnal.list
diff datasets.list datasets_fnal.list | grep -vi express | grep -v '/Test' | grep -vi -- '-Error' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at CNAF"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/* and site = *cnaf.infn.it" | sort > datasets_cnaf.list

diff datasets.list datasets_cnaf.list | grep '/ZeroBias/' | grep 'RAW' | grep 'v4' | grep '<' | awk '{print $2}'
diff datasets.list datasets_cnaf.list | grep '/ZeroBias/' | grep 'RECO' | grep 'v5' | grep '<' | awk '{print $2}'

diff datasets.list datasets_cnaf.list | grep '/MinimumBias/Commissioning10-v4/RAW' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at PIC"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/* and site = srmcms.pic.es" | sort > datasets_pic.list

diff datasets.list datasets_pic.list | grep '/MinimumBias/' | grep 'RAW' | grep 'v4' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at IN2P3"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/* and site = ccsrm.in2p3.fr" | sort > datasets_in2p3.list

diff datasets.list datasets_in2p3.list | grep '/TestEnables/' | grep -vi test | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/AlCaP0/' | grep -vi test | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/AlCaPhiSymEcal/' | grep -vi test | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/FEDMonitor/' | grep -vi test | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/LogMonitor/' | grep -vi test | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/RPCMonitor/' | grep -vi test | grep '<' | awk '{print $2}'

diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep 'RAW' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep 'RAW' | grep 'v2' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep 'RAW' | grep 'v3' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep 'RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep 'RECO' | grep 'v2' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep 'RECO' | grep 'v3' | grep '<' | awk '{print $2}'
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep 'RECO' | grep 'v4' | grep '<' | awk '{print $2}'

diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep 'RAW' | grep 'v4' | grep '<' | awk '{print $2}'


echo ""
echo "datasets not at RAL"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/* and site = srm-cms.gridpp.rl.ac.uk" | sort > datasets_ral.list

diff datasets.list datasets_ral.list | grep '/Cosmics/' | grep '<' | awk '{print $2}'

diff datasets.list datasets_ral.list | grep '/MinimumBias/' | grep 'RAW' | grep 'v4' | grep '<' | awk '{print $2}'

echo ""
echo "datasets not at KIT"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/* and site = cmssrm-fzk.gridka.de" | sort > datasets_kit.list

diff datasets.list datasets_kit.list | grep '/ZeroBias/' | grep 'RAW' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep '/ZeroBias/' | grep 'RAW' | grep 'v2' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep '/ZeroBias/' | grep 'RAW' | grep 'v3' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep '/ZeroBias/' | grep 'RECO' | grep 'v1' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep '/ZeroBias/' | grep 'RECO' | grep 'v2' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep '/ZeroBias/' | grep 'RECO' | grep 'v3' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep '/ZeroBias/' | grep 'RECO' | grep 'v4' | grep '<' | awk '{print $2}'

diff datasets.list datasets_kit.list | grep '/MinimumBias/' | grep 'RAW' | grep 'v4' | grep '<' | awk '{print $2}'
