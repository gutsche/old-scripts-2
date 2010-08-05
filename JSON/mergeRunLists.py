#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, getopt, json

runs = []
for filename in sys.argv[1:]:
    tmp = json.load(open(filename))
    for run in tmp:
        if run not in runs:
            runs.append(run)

runs.sort()
name = "runs_" + str(runs[0]) + "_" + str(runs[-1]) + ".json"
if os.path.isfile(name):
    name = name[:-5] + '_new.json'

tmp_handle = open(name,'w')
json.dump(runs,tmp_handle)
tmp_handle.close()
