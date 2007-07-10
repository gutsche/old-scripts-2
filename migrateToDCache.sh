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

    echo "copying all .root files"
    echo ""
    for rootfile in `ls *.root 2>/dev/null`
    do
	echo "copying $rootfile: srmcp file:////`pwd`/$rootfile srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$rootfile"
	srmcp file:////`pwd`/$rootfile srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$rootfile
    done
    echo ""

    echo "copying all .log.gz files"
    echo ""
    for loggzfile in `ls *.log.gz 2>/dev/null`
    do
	echo "copying $loggzfile: srmcp file:////`pwd`/$loggzfile srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$loggzfile"
	srmcp file:////`pwd`/$loggzfile srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$loggzfile
    done
    echo ""

    echo "zipping and copying all .log files"
    echo ""
    for logfile in `ls *.log 2>/dev/null`
    do
	echo "zipping $logfile"
	gzip $logfile
	echo "copying $logfile.gz: srmcp file:////`pwd`/$logfile.gz srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$logfile.gz"
	srmcp file:////`pwd`/$logfile.gz srm://cmssrm.fnal.gov:8443/srm/managerv1?SFN=/resilient/gutsche/condor/$project/$logfile.gz
    done
    echo ""
    
    cd ..

done
