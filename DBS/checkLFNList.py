#!/usr/bin/env python

import sys,os

input = open(sys.argv[1],'r')

dbslist = sys.argv[1] + '.dbs'
files = input.readlines()
command = "rm -f " + dbslist
os.system(command)
for file in files:
    if file.count('/store/') > 0 :
        command = 'python $DBSCMD_HOME/dbsCommandLine.py -c search --query=\"find dataset,dataset.status,file where file = ' + file.strip() + ' and site=*.fnal.gov\" --noheader --production >> ' + dbslist
        os.system(command)
