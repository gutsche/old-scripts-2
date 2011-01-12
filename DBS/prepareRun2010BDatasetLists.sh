python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010B*/*" | grep -v 'test/' | sort > complete_datasets.list

cat complete_datasets.list | grep -i express > express.list
cat complete_datasets.list | grep -i preprod > preproduction.list
cat complete_datasets.list | grep -- '-Error' > error.list

cat complete_datasets.list | grep -vi express | grep -vi preprod | grep -v -- '-Error' > datasets.list

cat datasets.list | grep '/RAW' | grep -v RAW-RECO | grep v1 > raw_v1.list

cat datasets.list | grep '/RECO' | grep -i prompt | grep v1 > prompt_reco_v1.list
cat datasets.list | grep '/RECO' | grep -i prompt | grep v2 > prompt_reco_v2.list

cat datasets.list | grep '/AOD' | grep -i prompt | grep v1 > prompt_aod_v1.list
cat datasets.list | grep '/AOD' | grep -i prompt | grep v2 > prompt_aod_v2.list

cat datasets.list | grep '/DQM' | grep -i prompt | grep v1 > prompt_dqm_v1.list
cat datasets.list | grep '/DQM' | grep -i prompt | grep v2 > prompt_dqm_v2.list

cat datasets.list | grep ALCA | grep v1 > alcareco_v1.list
cat datasets.list | grep ALCA | grep v2 > alcareco_v2.list

cat datasets.list | grep -i skim | grep v1 > dpg_skims_v1.list
cat datasets.list | grep '/RAW-RECO' | grep v1 >> dpg_skims_v1.list
cat datasets.list | grep -i skim | grep v2 > dpg_skims_v2.list
cat datasets.list | grep '/RAW-RECO' | grep v2 >> dpg_skims_v2.list
cat datasets.list | grep '/USER' | grep v2 >> dpg_skims_v2.list


cat datasets.list | grep 'SD_' | grep v1  > sd_v1.list
cat datasets.list | grep 'SD_' | grep v2  > sd_v2.list

# cat datasets.list | grep 'CS_' | grep v1  > cs_v1.list

cat datasets.list | grep 'Sep17ReReco' | grep v2 > rereco_sep17_v2.list

cat datasets.list | grep 'Nov4ReReco' | grep v1 > rereco_nov4_v1.list
cat datasets.list | grep 'Nov4ReReco' | grep v2 > rereco_nov4_v2.list
cat datasets.list | grep 'Nov4Skim' | grep v1 > skim_nov4_v1.list

cat datasets.list | grep 'Dec4ReReco' | grep v1 > rereco_dec4_v1.list
cat datasets.list | grep 'Dec4Skim' | grep v1 > skim_dec4_v1.list

cat datasets.list | grep 'Dec22ReReco' | grep v1 > rereco_dec22_v1.list
cat datasets.list | grep 'Dec22Skim' | grep v2 > skim_dec22_v2.list

cat datasets.list | grep 'TRKFailureScenario' | grep v1 > trkfailurescenario_v1.list

cat express.list error.list preproduction.list raw_v1.list prompt_reco_v1.list prompt_aod_v1.list prompt_dqm_v1.list alcareco_v1.list sd_v1.list dpg_skims_v1.list prompt_reco_v2.list prompt_aod_v2.list prompt_dqm_v2.list alcareco_v2.list sd_v2.list dpg_skims_v2.list rereco_sep17_v2.list trkfailurescenario_v1.list rereco_nov4_v1.list skim_nov4_v1.list rereco_nov4_v2.list rereco_dec4_v1.list skim_dec4_v1.list rereco_dec22_v1.list skim_dec22_v2.list | sort > done.list

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
echo "FNAL custodial for: EGMonitor, Electron, MinimumBias, Cosmics, HCALHPDNoise, HCALNZS, ForwardTest, HeavyIonTest"
echo "non-custodial kept at FNAL for BTau, Jet, MetMETTauMonitor, MetFwd, Mu, MuMonitor, MuOnia, Photon: currently only Nov4 and Dec22"
echo ""
python $DBSCMD_HOME/dbsCommandLine.py -c search --noheader --query="find dataset where dataset = /*/Run2010B*/* and site = T1_US_FNAL" | grep -v 'test/' | sort > datasets_fnal.list
diff datasets.list datasets_fnal.list | grep -v '/DQM' | grep -v '/ALCARECO' | grep -v '/MiniDaq/' | grep -v 'L1Accept' | grep -v 'HeavyIonTestPlayback' | grep -v 'EcalHcalCalibrationHI' | grep -v Dec4 | grep -v Jul15 | grep -v Jul26 | grep -v Jul6 | grep -v Jun9 | grep -v May27 | grep -v CollisionRecoSequence | grep -v '/Commissioning' | grep '<' | awk '{print $2}'
