#!/bin/bash

./createSimulationProject --project_name 070727_01_01 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_1_minus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070727_01_02 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_2_minus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_03 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_5_minus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_04 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_10_minus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070727_01_05 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_25_minus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_06 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_100_minus.cff --seed 123 --events 1000 --jobs 25

./createSimulationProject --project_name 070727_01_11 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_1_plus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070727_01_12 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_2_plus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_13 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_5_plus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_14 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_10_plus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070727_01_15 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_25_plus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_16 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_100_plus.cff --seed 123 --events 1000 --jobs 25

./createSimulationProject --project_name 070727_01_21 --parameter_set simulation_gun.cfg --generator_cff single_e_pt_1_minus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_22 --parameter_set simulation_gun.cfg --generator_cff single_e_pt_2_minus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_23 --parameter_set simulation_gun.cfg --generator_cff single_e_pt_5_minus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_24 --parameter_set simulation_gun.cfg --generator_cff single_e_pt_10_minus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_25 --parameter_set simulation_gun.cfg --generator_cff single_e_pt_25_minus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_26 --parameter_set simulation_gun.cfg --generator_cff single_e_pt_100_minus.cff --seed 123 --events 1000 --jobs 5

./createSimulationProject --project_name 070727_01_31 --parameter_set simulation_gun.cfg --generator_cff single_e_pt_1_plus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_32 --parameter_set simulation_gun.cfg --generator_cff single_e_pt_2_plus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_33 --parameter_set simulation_gun.cfg --generator_cff single_e_pt_5_plus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_34 --parameter_set simulation_gun.cfg --generator_cff single_e_pt_10_plus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_35 --parameter_set simulation_gun.cfg --generator_cff single_e_pt_25_plus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_36 --parameter_set simulation_gun.cfg --generator_cff single_e_pt_100_plus.cff --seed 123 --events 1000 --jobs 5

./createSimulationProject --project_name 070727_01_41 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_1_minus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070727_01_42 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_2_minus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_43 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_5_minus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_44 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_10_minus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070727_01_45 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_25_minus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_46 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_100_minus.cff --seed 123 --events 1000 --jobs 25

./createSimulationProject --project_name 070727_01_51 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_1_plus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070727_01_52 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_2_plus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_53 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_5_plus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_54 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_10_plus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070727_01_55 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_25_plus.cff --seed 123 --events 1000 --jobs 5
./createSimulationProject --project_name 070727_01_56 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_100_plus.cff --seed 123 --events 1000 --jobs 25

./createSimulationProject --project_name 070727_01_61 --parameter_set simulation_pythia.cfg --generator_cff minbias.cff --seed 123 --events 100 --jobs 30

./createSimulationProject --project_name 070727_01_71 --parameter_set simulation_pythia.cfg --generator_cff bjets_120_170.cff --seed 123 --events 100 --jobs 30
./createSimulationProject --project_name 070727_01_72 --parameter_set simulation_pythia.cfg --generator_cff ttbar.cff --seed 123 --events 100 --jobs 30
./createSimulationProject --project_name 070727_01_73 --parameter_set simulation_pythia_lowlumipileup.cfg --pileup_cff cmssw_1_4_3_pileup.cff --generator_cff bjets_120_170.cff --seed 123 --events 100 --jobs 100
./createSimulationProject --project_name 070727_01_74 --parameter_set simulation_pythia_lowlumipileup.cfg --pileup_cff cmssw_1_4_3_pileup.cff --generator_cff ttbar.cff --seed 123 --events 100 --jobs 100

./createSimulationProject --project_name 070727_01_81 --parameter_set simulation_gun.cfg --generator_cff single_gamma_pt_5.cff --seed 123 --events 1000 --jobs 10
./createSimulationProject --project_name 070727_01_82 --parameter_set simulation_gun.cfg --generator_cff single_gamma_pt_10.cff --seed 123 --events 1000 --jobs 10
./createSimulationProject --project_name 070727_01_83 --parameter_set simulation_gun.cfg --generator_cff single_gamma_pt_55.cff --seed 123 --events 1000 --jobs 10
./createSimulationProject --project_name 070727_01_84 --parameter_set simulation_gun.cfg --generator_cff single_gamma_pt_100.cff --seed 123 --events 1000 --jobs 10

./createSimulationProject --project_name 070727_01_91 --parameter_set simulation_pythia.cfg --generator_cff zmumu.cff --seed 123 --events 100 --jobs 100
