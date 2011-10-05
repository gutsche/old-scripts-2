#!/bin/bash
cd /data/relval/PAProd/T0LSF_0_12_18_patch5_PROD_1/
source start_prodagent.sh 0 1> /dev/null

cd /afs/cern.ch/user/r/relval/webpage/CustodialSummary

# Creating dir
dir=`date +"%Y/%m/%d"`
if [ -e $dir ]; then
    echo "This script already ran today. Skipping execution."
    return
fi
mkdir -p $dir

cd $dir

# Executing scripts
. /afs/cern.ch/user/r/relval/webpage/CustodialSummary/.scripts/queryPhEDEx.sh
#python /afs/cern.ch/user/r/relval/webpage/CustodialSummary/.scripts/parse.py
