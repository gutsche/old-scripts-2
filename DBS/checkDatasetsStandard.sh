#!/bin/bash
for dataset in $*
do
dbs search --noheader --query="find dataset,sum(file.numevents),sum(file.size) where dataset = ${dataset}"
done
