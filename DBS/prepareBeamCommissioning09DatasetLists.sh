python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/BeamCommissioning09*/*" | sort > datasets.list
cat datasets.list | grep -i express > express.list
cat datasets.list | grep -vi express | grep '/RAW' | grep -v RAW-RECO > raw.list
cat datasets.list | grep -vi express | grep '/RECO' | grep -i prompt > prompt_reco.list
cat datasets.list | grep -vi express | grep ALCA | grep -v 18th | grep v1 > alcareco_v1.list
cat datasets.list | grep -vi express | grep ALCA | grep -v 18th | grep v2 > alcareco_v2.list
cat datasets.list | grep -vi express | grep ALCA | grep -v 18th > alcareco.list
cat datasets.list | grep -vi express | grep SD | grep v1 | grep Prompt > sd_prompt_v1.list
cat datasets.list | grep -vi express | grep SD | grep v2 | grep Prompt > sd_prompt_v2.list
cat datasets.list | grep -vi express | grep SD | grep Prompt > sd_prompt.list
cat datasets.list | grep -vi express | grep PromptSkim | grep -v SD | grep v1 > skims_prompt_v1.list
cat datasets.list | grep -vi express | grep PromptSkim | grep -v SD > skims_prompt.list
cat datasets.list | grep -iv express | grep 335p3 | grep SD > sd_335p3.list
cat datasets.list | grep -iv express | grep 335p3 | grep -v SD > skims_335p3.list
cat datasets.list | grep -iv express | grep GR09_P_V7 | grep '/RECO' > rereco_GR09_P_V7.list
cat datasets.list | grep -iv express | grep GR09_P_V7 | grep -v '/RECO' | grep SD > sd_rereco_GR09_P_V7.list
cat datasets.list | grep -iv express | grep GR09_P_V7 | grep -v '/RECO' | grep -v SD > skims_rereco_GR09_P_V7.list
cat datasets.list | grep test > test.list
cat datasets.list | grep FIRSTCOLL > rereco_FIRSTCOLL.list
cat datasets.list | grep -iv express | grep Dec9thReReco | grep '/RECO' > rereco_Dec9thReReco.list
cat datasets.list | grep -iv express | grep Dec9thReReco | grep -v '/RECO' | grep SD > sd_rereco_Dec9thReReco.list
cat datasets.list | grep -iv express | grep Dec9thReReco | grep -v '/RECO' | grep -v SD > skims_rereco_Dec9thReReco.list
cat datasets.list | grep -iv express | grep Dec14thReReco | grep '/RECO' > rereco_Dec14thReReco.list
cat datasets.list | grep -iv express | grep Dec14thSkim | grep -v '/RECO' | grep SD > sd_rereco_Dec14thReReco.list
cat datasets.list | grep -iv express | grep Dec14thSkim | grep -v '/RECO' | grep -v SD > skims_rereco_Dec14thReReco.list

cat datasets.list | grep -iv express | grep Dec19thReReco_336p3 | grep '/RECO' > rereco_Dec19thReReco_336p3.list
cat datasets.list | grep -iv express | grep Dec19thSkim_336p3 | grep -v '/RECO' | grep SD > sd_rereco_Dec19thReReco_336p3.list
cat datasets.list | grep -iv express | grep Dec19thSkim_336p3 | grep -v '/RECO' | grep -v SD > skims_rereco_Dec19thReReco_336p3.list

cat datasets.list | grep -iv express | grep Dec19thReReco_341 | grep '/RECO' > rereco_Dec19thReReco_341.list
cat datasets.list | grep -iv express | grep Dec19thSkim_341 | grep -v '/RECO' | grep SD > sd_rereco_Dec19thReReco_341.list
cat datasets.list | grep -iv express | grep Dec19thSkim_341 | grep -v '/RECO' | grep -v SD > skims_rereco_Dec19thReReco_341.list

cat datasets.list | grep -iv express | grep Jan21stPreProd_336p3 | grep '/RECO' > rereco_Jan21stPreProd_336p3.list
# rereco_Jan21stPreProd_336p3.list

cat datasets.list | grep -iv express | grep Jan23ReReco | grep '/RECO' > rereco_Jan23ReReco.list
cat datasets.list | grep -iv express | grep Jan23Skim | grep -v '/RECO' | grep SD > sd_rereco_Jan23ReReco.list
cat datasets.list | grep -iv express | grep Jan23Skim | grep -v '/RECO' | grep -v SD > skims_rereco_Jan23ReReco.list
# rereco_Jan23ReReco.list sd_rereco_Jan23ReReco.list skims_rereco_Jan23ReReco.list 

cat datasets.list | grep -iv express | grep Jan29ReReco | grep '/RECO' > rereco_Jan29ReReco.list
cat datasets.list | grep -iv express | grep Jan29Skim | grep -v '/RECO' | grep SD > sd_rereco_Jan29ReReco.list
cat datasets.list | grep -iv express | grep Jan29Skim | grep -v '/RECO' | grep -v SD > skims_rereco_Jan29ReReco.list
# rereco_Jan29ReReco.list sd_rereco_Jan29ReReco.list skims_rereco_Jan29ReReco.list 

cat datasets.list | grep -iv express | grep Feb9ReReco | grep '/RECO' > rereco_Feb9ReReco.list
cat datasets.list | grep -iv express | grep Feb9Skim | grep -v '/RECO' | grep SD > sd_rereco_Feb9ReReco.list
cat datasets.list | grep -iv express | grep Feb9Skim | grep -v '/RECO' | grep -v SD > skims_rereco_Feb9ReReco.list
# rereco_Feb9ReReco.list sd_rereco_Feb9ReReco.list skims_rereco_Feb9ReReco.list 

cat datasets.list | grep -iv express | grep 18thFebPreProd > preprod_18thFebPreProd.list #custodial at PIC

cat test.list express.list raw.list prompt_reco.list alcareco.list sd_prompt.list skims_prompt.list sd_335p3.list skims_335p3.list rereco_GR09_P_V7.list sd_rereco_GR09_P_V7.list skims_rereco_GR09_P_V7.list rereco_Dec9thReReco.list sd_rereco_Dec9thReReco.list skims_rereco_Dec9thReReco.list rereco_FIRSTCOLL.list rereco_Dec14thReReco.list sd_rereco_Dec14thReReco.list skims_rereco_Dec14thReReco.list rereco_Dec19thReReco_336p3.list sd_rereco_Dec19thReReco_336p3.list skims_rereco_Dec19thReReco_336p3.list rereco_Dec19thReReco_341.list sd_rereco_Dec19thReReco_341.list skims_rereco_Dec19thReReco_341.list rereco_Jan23ReReco.list sd_rereco_Jan23ReReco.list skims_rereco_Jan23ReReco.list rereco_Jan29ReReco.list sd_rereco_Jan29ReReco.list skims_rereco_Jan29ReReco.list rereco_Feb9ReReco.list sd_rereco_Feb9ReReco.list skims_rereco_Feb9ReReco.list rereco_Jan21stPreProd_336p3.list preprod_18thFebPreProd.list | sort > done.list
echo ""
echo "inconsistencies"
echo ""
diff datasets.list done.list | grep '<' | awk '{print $2}'
echo ""
echo "datasets not at FNAL"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/BeamCommissioning09*/* and site = *fnal.gov" | sort > datasets_fnal.list
diff datasets.list datasets_fnal.list | grep -vi express | grep -v '/Test' | grep -v '/RandomTriggersOpen' | grep -v '/ZeroBiasBnotT0' | grep '<' | awk '{print $2}'
echo ""
echo "custodial datasets not at CNAF"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/BeamCommissioning09*/* and site = *cnaf.infn.it" | sort > datasets_cnaf.list
diff datasets.list datasets_cnaf.list | grep '/ZeroBias/' | grep '<' | awk '{print $2}'
echo ""
echo "custodial datasets not at PIC"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/BeamCommissioning09*/* and site = srmcms.pic.es" | sort > datasets_pic.list
diff datasets.list datasets_pic.list | grep '/FEDMonitor/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep '/RandomTriggers/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep '/RPCMonitor/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_pic.list | grep '/MinimumBias/' | grep '18thFebPreProd' | grep '<' | awk '{print $2}'
echo ""
echo "custodial datasets not at IN2P3"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/BeamCommissioning09*/* and site = ccsrm.in2p3.fr" | sort > datasets_in2p3.list
diff datasets.list datasets_in2p3.list | grep '/MinimumBias/' | grep -vi test | grep -v '18thFebPreProd' | grep '<' | awk '{print $2}'
echo ""
echo "custodial datasets not at RAL"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/BeamCommissioning09*/* and site = srm-cms.gridpp.rl.ac.uk" | sort > datasets_ral.list
diff datasets.list datasets_ral.list | grep '/AlCaP0/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_ral.list | grep '/AlCaPhiSymEcal/' | grep '<' | awk '{print $2}'
echo ""
echo "custodial datasets not at KIT"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/BeamCommissioning09*/* and site = cmssrm-fzk.gridka.de" | sort > datasets_kit.list
diff datasets.list datasets_kit.list | grep '/ZeroBiasB/' | grep '<' | awk '{print $2}'
diff datasets.list datasets_kit.list | grep '/Calo/' | grep '<' | awk '{print $2}'
