#!/bin/bash

date=`echo $1 | awk -F'_' '{print $1}'`
number=`echo $1 | awk -F'_' '{print $2}'`

project=`echo "${date}_${number}"`
echo $project

create_ewksoup.sh $project 10 1

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

create_exoticsoup.sh $project 10 1

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

create_jets.sh $project 10 1

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

create_minbias.sh $project 10 1

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

create_softmuon.sh $project 10 1

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

create_ttbar.sh $project 10 1

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

create_wenu.sh $project 10 1

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

create_zmumu.sh $project 10 1

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

create_RelVal120BJets50-120.sh $project 10 1

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

create_RelVal120CJets50-120.sh $project 10 1

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

create_RelVal120Higgs-ZZ-4Mu.sh $project 10 1

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

create_RelVal120SingleMuPt100.sh $project 10 1

number=`expr $number + 1`
if [ $number -lt 10 ]; then
    number=`echo "0$number"`
fi
project=`echo "${date}_${number}"`
echo $project

create_RelVal120SingleMuPt10.sh $project 10 1
