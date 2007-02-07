#!/bin/bash

./createRecontructionProject --project_name 070206_01 --parameter_set reconstruction.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_single_mu_1_digis.cff
./createRecontructionProject --project_name 070206_02 --parameter_set reconstruction.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_single_mu_10_digis.cff
./createRecontructionProject --project_name 070206_03 --parameter_set reconstruction.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_single_mu_100_digis.cff
./createRecontructionProject --project_name 070206_04 --parameter_set reconstruction.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_minbias_digis.cff
./createRecontructionProject --project_name 070206_05 --parameter_set reconstruction.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_hzz4e_digis.cff
./createRecontructionProject --project_name 070206_06 --parameter_set reconstruction.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_hzz4mu_digis.cff
./createRecontructionProject --project_name 070206_07 --parameter_set reconstruction.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_ttbar_digis.cff
./createRecontructionProject --project_name 070206_08 --parameter_set reconstruction.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_jets_digis.cff

./createRecontructionProject --project_name 070206_11 --parameter_set reconstruction_pt09.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_single_mu_1_digis.cff
./createRecontructionProject --project_name 070206_12 --parameter_set reconstruction_pt09.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_single_mu_10_digis.cff
./createRecontructionProject --project_name 070206_13 --parameter_set reconstruction_pt09.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_single_mu_100_digis.cff
./createRecontructionProject --project_name 070206_14 --parameter_set reconstruction_pt09.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_minbias_digis.cff
./createRecontructionProject --project_name 070206_15 --parameter_set reconstruction_pt09.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_hzz4e_digis.cff
./createRecontructionProject --project_name 070206_16 --parameter_set reconstruction_pt09.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_hzz4mu_digis.cff
./createRecontructionProject --project_name 070206_17 --parameter_set reconstruction_pt09.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_ttbar_digis.cff
./createRecontructionProject --project_name 070206_18 --parameter_set reconstruction_pt09.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_jets_digis.cff

./createRecontructionProject --project_name 070206_22 --parameter_set reconstruction_extras_off.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_single_mu_10_digis.cff
./createRecontructionProject --project_name 070206_24 --parameter_set reconstruction_extras_off.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_minbias_digis.cff
./createRecontructionProject --project_name 070206_27 --parameter_set reconstruction_extras_off.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_ttbar_digis.cff

./createRecontructionProject --project_name 070206_32 --parameter_set reconstruction_rphi.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_single_mu_10_digis.cff
./createRecontructionProject --project_name 070206_34 --parameter_set reconstruction_rphi.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_minbias_digis.cff
./createRecontructionProject --project_name 070206_37 --parameter_set reconstruction_rphi.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_ttbar_digis.cff

./createRecontructionProject --project_name 070206_42 --parameter_set reconstruction_mergeLast25.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_single_mu_10_digis.cff
./createRecontructionProject --project_name 070206_44 --parameter_set reconstruction_mergeLast25.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_minbias_digis.cff
./createRecontructionProject --project_name 070206_47 --parameter_set reconstruction_mergeLast25.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_ttbar_digis.cff

./createRecontructionProject --project_name 070206_52 --parameter_set reconstruction_noMerging.cfg --events 500 --jobs 20 --dataset_cff cmssw_1_2_0_single_mu_10_digis.cff
./createRecontructionProject --project_name 070206_54 --parameter_set reconstruction_noMerging.cfg --events 250 --jobs 40 --dataset_cff cmssw_1_2_0_minbias_digis.cff
./createRecontructionProject --project_name 070206_57 --parameter_set reconstruction_noMerging.cfg --events 50  --jobs 200 --dataset_cff cmssw_1_2_0_ttbar_digis.cff







