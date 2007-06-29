#!/bin/bash

./createSimulationProject --project_name 070628_01_01 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_1_minus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070628_01_04 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_10_minus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070628_01_06 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_100_minus.cff --seed 123 --events 1000 --jobs 25

./createSimulationProject --project_name 070628_01_11 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_1_plus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070628_01_14 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_10_plus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070628_01_16 --parameter_set simulation_gun.cfg --generator_cff single_mu_pt_100_plus.cff --seed 123 --events 1000 --jobs 25

./createSimulationProject --project_name 070628_01_41 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_1_minus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070628_01_44 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_10_minus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070628_01_46 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_100_minus.cff --seed 123 --events 1000 --jobs 25

./createSimulationProject --project_name 070628_01_51 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_1_plus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070628_01_54 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_10_plus.cff --seed 123 --events 1000 --jobs 25
./createSimulationProject --project_name 070628_01_56 --parameter_set simulation_gun.cfg --generator_cff single_pi_pt_100_plus.cff --seed 123 --events 1000 --jobs 25


./createSimulationProject --project_name 070628_01_73 --parameter_set simulation_pythia_lowlumipileup.cfg --pileup_cff cmssw_1_4_3_pileup.cff --generator_cff bjets_120_170.cff --seed 123 --events 100 --jobs 100
./createSimulationProject --project_name 070628_01_74 --parameter_set simulation_pythia_lowlumipileup.cfg --pileup_cff cmssw_1_4_3_pileup.cff --generator_cff ttbar.cff --seed 123 --events 100 --jobs 100

