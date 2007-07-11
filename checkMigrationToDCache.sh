#!/bin/bash

# check migration of development sample to dCache and recopy corrupt files
# input: projects in condor
# execute in condor

for project in $*
do
    echo ""
    echo "Migrating project $project"
    echo ""

    echo "changing to $project"
    cd $project
    echo ""

    echo "checking all .root files"
    echo ""
    for rootfile in `ls *.root 2>/dev/null`
    do
        blue=`ls -la $rootfile | awk '{print $5}'`
        dcache=`srm-get-metadata srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$rootfile | grep size | awk -F\: '{print $2}'`

        if [ $blue -ne $dcache ]; then
          echo "file: $rootfile blue: $blue dcache $dcache"
          echo "delete srm-advisory-delete srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$rootfile"
          srm-advisory-delete srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$rootfile
    	  echo "recopy srmcp file:////`pwd`/$rootfile srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$rootfile"
          srmcp file:////`pwd`/$rootfile srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$rootfile
        fi
    done
    echo ""

    echo "checking all .log.gz files"
    echo ""
    for loggzfile in `ls *.log.gz 2>/dev/null`
    do
        blue=`ls -la $loggzfile | awk '{print $5}'`
        dcache=`srm-get-metadata srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$loggzfile | grep size | awk -F\: '{print $2}'`

        if [ $blue -ne $dcache ]; then
          echo "file: $loggzfile blue: $blue dcache $dcache"
          echo "delete srm-advisory-delete srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$loggzfile"
          srm-advisory-delete srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$loggzfile
    	  echo "recopy srmcp file:////`pwd`/$loggzfile srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$loggzfile"
          srmcp file:////`pwd`/$loggzfile srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$loggzfile
        fi
    done
    echo ""

    cd ..

done
