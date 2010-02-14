#!/bin/bash
# execute from /store/local/data2/cms1/cms2
dirs=`find /pnfs/cms/WAX/resilient/gutsche/ -name "merge*.root" | sed -e 's/\/pnfs\/cms\/WAX\/resilient\/gutsche\///g' | sed -e 's/\/merged.*.root//g' | sort | uniq`
for dir in $dirs
do
echo "mkdir -p $dir"
mkdir -p $dir
done
files=`find /pnfs/cms/WAX/resilient/gutsche/ -name "merge*.root"`
for file in $files
do
dir=`echo $file | sed -e 's/\/pnfs\/cms\/WAX\/resilient\/gutsche\///g' | sed -e 's/\/merged.*.root//g'` 
echo "dccp $file $dir"
dccp $file $dir
done

