#!/bin/bash

# migrate development sample to dCache
# input: projects in condor
# execute in condor

for project in $*
do
    echo ""
    echo "Migrating project $project to /pnfs/cms/WAX/resilient/gutsche/condor/$project"
    echo ""

    echo "changing to $project"
    cd $project
    echo ""

    echo "creating directory /pnfs/cms/WAX/resilient/gutsche/condor/$project"
    mkdir -p /pnfs/cms/WAX/resilient/gutsche/condor/$project
    echo ""

    echo "copying all .root files to /pnfs/cms/WAX/resilient/gutsche/condor/$project"
    echo ""
    for rootfile in `ls *.root 2>/dev/null`
    do
	echo "copying $rootfile to /pnfs/cms/WAX/resilient/gutsche/condor/$project/$rootfile"
	dccp $rootfile /pnfs/cms/WAX/resilient/gutsche/condor/$project/$rootfile
    done
    echo ""

    echo "copying all .log.gz files to /pnfs/cms/WAX/resilient/gutsche/condor/$project"
    echo ""
    for loggzfile in `ls *.log.gz 2>/dev/null`
    do
	echo "copying $loggzfile to /pnfs/cms/WAX/resilient/gutsche/condor/$project/$loggzfile"
	dccp $loggzfile /pnfs/cms/WAX/resilient/gutsche/condor/$project/$loggzfile
    done
    echo ""

    echo "zipping and copying all .log files to /pnfs/cms/WAX/resilient/gutsche/condor/$project"
    echo ""
    for logfile in `ls *.log 2>/dev/null`
    do
	echo "zipping $logfile"
	gzip $logfile
	echo "copying $logfile to /pnfs/cms/WAX/resilient/gutsche/condor/$project/$logfile"
	dccp $logfile /pnfs/cms/WAX/resilient/gutsche/condor/$project/$logfile
    done
    echo ""
    
    cd ..

done
