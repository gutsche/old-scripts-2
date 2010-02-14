python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/*" | grep -v 'test/' | sort > datasets.list
cat datasets.list | grep -i express > express.list
cat datasets.list | grep -vi express | grep '/RAW' | grep -v RAW-RECO > raw.list
cat datasets.list | grep -vi express | grep '/RECO' | grep -i prompt > prompt_reco.list
cat datasets.list | grep -vu express | grep '/Commissioning10-v1/RECO' >> prompt_reco.list
#cat datasets.list | grep -vi express | grep ALCA | grep v1 > alcareco_v1.list
#cat datasets.list | grep -vi express | grep ALCA | grep v2 > alcareco_v2.list
cat datasets.list | grep -vi express | grep ALCA > alcareco.list
#cat datasets.list | grep -vi express | grep SD | grep v1 | grep Prompt > sd_prompt_v1.list
#cat datasets.list | grep -vi express | grep SD | grep v2 | grep Prompt > sd_prompt_v2.list
#cat datasets.list | grep -vi express | grep SD | grep Prompt > sd_prompt.list
#cat datasets.list | grep -vi express | grep PromptSkim | grep -v SD | grep v1 > skims_prompt_v1.list
#cat datasets.list | grep -vi express | grep PromptSkim | grep -v SD > skims_prompt.list
#cat datasets.list | grep -iv express | grep 335p3 | grep SD > sd_335p3.list
#cat datasets.list | grep -iv express | grep 335p3 | grep -v SD > skims_335p3.list
cat datasets.list | grep -i 'test/' > test.list

cat express.list raw.list prompt_reco.list alcareco.list test.list | sort > done.list
echo ""
echo "inconsistencies"
echo ""
diff datasets.list done.list | grep '<' | awk '{print $2}'
echo ""
echo "datasets not at FNAL"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/* and site = *fnal.gov" | sort > datasets_fnal.list
diff datasets.list datasets_fnal.list | grep -vi express | grep -v '/Test' | grep -v '/RandomTriggersOpen' | grep '<' | awk '{print $2}'
echo ""
echo "custodial datasets not at CNAF"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/* and site = *cnaf.infn.it" | sort > datasets_cnaf.list
#diff datasets.list datasets_cnaf.list | grep '/ZeroBias/' | grep '<' | awk '{print $2}'
echo ""
echo "custodial datasets not at PIC"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/* and site = srmcms.pic.es" | sort > datasets_pic.list
#diff datasets.list datasets_pic.list | grep '/FEDMonitor/' | grep '<' | awk '{print $2}'
#diff datasets.list datasets_pic.list | grep '/RandomTriggers/' | grep '<' | awk '{print $2}'
#diff datasets.list datasets_pic.list | grep '/RPCMonitor/' | grep '<' | awk '{print $2}'
echo ""
echo "custodial datasets not at IN2P3"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/* and site = ccsrm.in2p3.fr" | sort > datasets_in2p3.list
diff datasets.list datasets_in2p3.list | grep '/TestEnables/' | grep -vi test | grep '<' | awk '{print $2}'
#diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep -vi test | grep '<' | awk '{print $2}'
echo ""
echo "custodial datasets not at RAL"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/* and site = srm-cms.gridpp.rl.ac.uk" | sort > datasets_ral.list
diff datasets.list datasets_ral.list | grep '/Cosmics/' | grep '<' | awk '{print $2}'
#diff datasets.list datasets_ral.list | grep '/AlCaP0/' | grep '<' | awk '{print $2}'
#diff datasets.list datasets_ral.list | grep '/AlCaPhiSymEcal/' | grep '<' | awk '{print $2}'
echo ""
echo "custodial datasets not at KIT"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Commissioning10*/* and site = cmssrm-fzk.gridka.de" | sort > datasets_kit.list
#diff datasets.list datasets_kit.list | grep '/ZeroBiasB/' | grep '<' | awk '{print $2}'
#diff datasets.list datasets_kit.list | grep '/Calo/' | grep '<' | awk '{print $2}'
