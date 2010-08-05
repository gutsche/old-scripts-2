#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, getopt, json

if len(sys.argv[1:]) > 2:
    print ''
    print 'Please specify only 2 json files'
    print ''
    sys.exit(2)

diff = []
tmp1 = json.load(open(sys.argv[1]))
tmp2 = json.load(open(sys.argv[2]))
for run in tmp2:
    if run not in tmp1 :
        diff.append(run)
    
diff.sort()
name = "runs_" + str(diff[0]) + "_" + str(diff[-1]) + ".json"
tmp_handle = open(name,'w')
json.dump(diff,tmp_handle)
tmp_handle.close()
