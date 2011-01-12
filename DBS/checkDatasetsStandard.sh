#!/bin/bash

tmpout=`mktemp`

for dataset in $*
do
dbs search --noheader --query="find dataset,sum(block.numevents),sum(block.size) where dataset = ${dataset}" >> $tmpout
done

cat $tmpout
echo ""
echo "Dataset:"
echo ""
for dataset in $*
do
echo "$dataset" 
done
python ~/scripts/DBS/parseDatasetsTimeRangeOutput.py $tmpout $*

rm $tmpout
