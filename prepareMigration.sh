#!/bin/sh

cat $1 | awk '{print $6}' | sort | awk '{print "python2.4 $PRODAGENT_ROOT/util/publish.py DBSInterface:MigrateDatasetToGlobal "$1"\npython2.4 $PRODAGENT_ROOT/util/publish.py PhEDExInjectDataset "$1}'
