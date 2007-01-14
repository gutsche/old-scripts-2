#!/bin/bash

date=`echo $1 | awk -F'_' '{print $1}'`
number=`echo $1 | awk -F'_' '{print $2}'`

project=`echo "${date}_${number}"`
echo $project

./createRecontructionProject --project_name $project --parameter_set reconstruction.cfg --events 100 --jobs 100 --dataset_cff cmssw_1_2_0_hzz4e_digis.cff

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

./createRecontructionProject --project_name $project --parameter_set reconstruction.cfg --events 100 --jobs 100 --dataset_cff cmssw_1_2_0_hzz4mu_digis.cff

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

./createRecontructionProject --project_name $project --parameter_set reconstruction.cfg --events 10 --jobs 997 --dataset_cff cmssw_1_2_0_jets_digis.cff

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

./createRecontructionProject --project_name $project --parameter_set reconstruction.cfg --events 10 --jobs 992 --dataset_cff cmssw_1_2_0_minbias_digis.cff

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

./createRecontructionProject --project_name $project --parameter_set reconstruction.cfg --events 100 --jobs 100 --dataset_cff cmssw_1_2_0_single_mu_100_digis.cff

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

./createRecontructionProject --project_name $project --parameter_set reconstruction.cfg --events 100 --jobs 100 --dataset_cff cmssw_1_2_0_single_mu_10_digis.cff

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

./createRecontructionProject --project_name $project --parameter_set reconstruction.cfg --events 100 --jobs 100 --dataset_cff cmssw_1_2_0_single_mu_1_digis.cff

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

./createRecontructionProject --project_name $project --parameter_set reconstruction.cfg --events 10 --jobs 995 --dataset_cff cmssw_1_2_0_ttbar_digis.cff
