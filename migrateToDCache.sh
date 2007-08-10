#!/bin/bash

# migrate development sample to dCache
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

    echo "create copyjob file"
    rm -f copy.job
    touch copy.job

    echo "copying all .root files"
    echo ""
    for rootfile in `ls *.root 2>/dev/null`
    do
	echo "adding $rootfile to copyjob file: file:////`pwd`/$rootfile srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$rootfile"
	echo "file:////`pwd`/$rootfile srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$rootfile" >> copy.job
    done
    echo ""

    echo "copying all .log.gz files"
    echo ""
    for loggzfile in `ls *.log.gz 2>/dev/null`
    do
	echo "adding $loggzfile to copyjob file: file:////`pwd`/$loggzfile srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$loggzfile"
	echo "file:////`pwd`/$loggzfile srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$loggzfile" >> copy.job
    done
    echo ""

    echo "zipping and copying all .log files"
    echo ""
    for logfile in `ls *.log 2>/dev/null`
    do
	echo "zipping $logfile"
	gzip $logfile
	echo "adding $logfile.gz to copyjob file: file:////`pwd`/$logfile.gz srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$logfile.gz"
	echo "file:////`pwd`/$logfile.gz srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$logfile.gz" >> copy.job
    done
    echo ""    

    echo "execute srmcp -copyjobfile=copy.job"
    srmcp -debug=true -copyjobfile=copy.job

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