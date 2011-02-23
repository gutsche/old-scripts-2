#!/bin/sh
export couchUrl="http://dmwmwriter:purpl3Pants@cms-xen41.fnal.gov:5984"
export database_name="gutsche_configcache"
export user_name="gutsche"
export group_name="DataOps"

inject-to-config-cache $couchUrl $database_name $user_name $group_name REDIGI_DIGI_L1_DIGI2RAW_HLT_RECODEBUGCONTENT.py Winter10RedigiRerecoStep1DebugContent "Winter10 Redigi/ReReco pass: Step1 Debug Content" | grep DocID | awk '{print "REDIGI_DIGI_L1_DIGI2RAW_HLT_RECODEBUGCONTENT.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name REDIGI_DIGI_L1_DIGI2RAW_HLT_RECODEBUGCONTENT_PU.py Winter10RedigiRerecoStep1DebugContentPU "Winter10 Redigi/ReReco pass: Step1 Debug Content with PU" | grep DocID | awk '{print "REDIGI_DIGI_L1_DIGI2RAW_HLT_RECODEBUGCONTENT_PU.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name REDIGI_DIGI_L1_DIGI2RAW_HLT_RECOSIMCONTENT.py Winter10RedigiRerecoStep1 "Winter10 Redigi/ReReco pass: Step1" | grep DocID | awk '{print "REDIGI_DIGI_L1_DIGI2RAW_HLT_RECOSIMCONTENT.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name REDIGI_DIGI_L1_DIGI2RAW_HLT_RECOSIMCONTENT_2011PU.py Winter10RedigiRerecoStep1PU2011 "Winter10 Redigi/ReReco pass: Step1 with PU 2011" | grep DocID | awk '{print "REDIGI_DIGI_L1_DIGI2RAW_HLT_RECOSIMCONTENT_2011PU.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name REDIGI_DIGI_L1_DIGI2RAW_HLT_RECOSIMCONTENT_PU.py Winter10RedigiRerecoStep1PU "Winter10 Redigi/ReReco pass: Step1 with PU" | grep DocID | awk '{print "REDIGI_DIGI_L1_DIGI2RAW_HLT_RECOSIMCONTENT_PU.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name aodsim_prod.py Winter10RedigiRerecoAODSIM "Winter10 Redigi/ReReco pass: AODSIM" | grep DocID | awk '{print "aodsim_prod.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name step2_RAW2DIGI_L1Reco_RECO_VALIDATION_RECODEBUGCONTENT.py Winter10RedigiRerecoStep2DebugContent "Winter10 Redigi/ReReco pass: Step2 Debug Content" | grep DocID | awk '{print "step2_RAW2DIGI_L1Reco_RECO_VALIDATION_RECODEBUGCONTENT.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name step2_RAW2DIGI_L1Reco_RECO_VALIDATION_RECOSIMCONTENT.py Winter10RedigiRerecoStep2 "Winter10 Redigi/ReReco pass: Step2" | grep DocID | awk '{print "step2_RAW2DIGI_L1Reco_RECO_VALIDATION_RECOSIMCONTENT.py "$2}'

inject-to-config-cache $couchUrl $database_name $user_name $group_name rereco_Electron_pp.py Dec22ReRecoElectronPD "Dec22 ReReco pass: Electron PD" | grep DocID | awk '{print "rereco_Electron_pp.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name rereco_MuOnia_pp.py Dec22ReRecoMuOniaPD "Dec22 ReReco pass: MuOnia PD" | grep DocID | awk '{print "rereco_MuOnia_pp.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name rereco_Mu_pp.py Dec22ReRecoMu "Dec22 ReReco pass: Mu PD" | grep DocID | awk '{print "rereco_Mu_pp.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name rereco_pp.py Dec22ReRecoPP "Dec22 ReReco pass: generic pp" | grep DocID | awk '{print "rereco_pp.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name skim_BTau.py Dec22SkimBTauPD "Dec22 ReReco pass: skim for BTau PD" | grep DocID | awk '{print "skim_BTau.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name skim_Electron.py Dec22SkimElectronPD "Dec22 ReReco pass: skim for Electron PD" | grep DocID | awk '{print "skim_Electron.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name skim_Jet.py Dec22SkimJetPD "Dec22 ReReco pass: skim for Jet PD" | grep DocID | awk '{print "skim_Jet.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name skim_METFwd.py Dec22SkimMETFwdPD "Dec22 ReReco pass: skim for METFwd PD" | grep DocID | awk '{print "skim_METFwd.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name skim_Mu.py Dec22SkimMuPD "Dec22 ReReco pass: skim for Mu PD" | grep DocID | awk '{print "skim_Mu.py "$2}'
inject-to-config-cache $couchUrl $database_name $user_name $group_name skim_Photon.py Dec22SkimPhotonPD "Dec22 ReReco pass: skim for Photon PD" | grep DocID | awk '{print "skim_Photon.py "$2}'
