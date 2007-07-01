#!/bin/bash

# single mu minus

cd 070628_01_01
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_single_mu_pt_1_minus.cff
cd ..

cd 070628_01_04
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_single_mu_pt_10_minus.cff
cd ..

cd 070628_01_06
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_single_mu_pt_100_minus.cff
cd ..

# single mu plus

cd 070628_01_11
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_single_mu_pt_1_plus.cff
cd ..

cd 070628_01_14
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_single_mu_pt_10_plus.cff
cd ..

cd 070628_01_16
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_single_mu_pt_100_plus.cff
cd ..

# single pi minus

cd 070628_01_41
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_single_pi_pt_1_minus.cff
cd ..

cd 070628_01_44
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_single_pi_pt_10_minus.cff
cd ..

cd 070628_01_46
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_single_pi_pt_100_minus.cff
cd ..

# single pi plus

cd 070628_01_51
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_single_pi_pt_1_plus.cff
cd ..

cd 070628_01_54
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_single_pi_pt_10_plus.cff
cd ..

cd 070628_01_56
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_single_pi_pt_100_plus.cff
cd ..

# bjets

cd 070628_01_73
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_bjets_120_170_lowlumipileup.cff
cd ..

cd 070628_01_74
$CMSSW_BASE/src/GutSoftConfigurations/Scripts/generatePoolSourceFromFiles --file "*.root" --absolute > $CMSSW_BASE/src/GutSoftConfigurations/DataSets/cmssw_1_5_0_ttbar_lowlumipileup.cff
cd ..
