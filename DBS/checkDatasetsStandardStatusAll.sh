#!/bin/bash
for dataset in $*
do
dbs search --noheader --production --query="find dataset,sum(block.numevents),sum(block.size) where dataset = ${dataset}"
done
