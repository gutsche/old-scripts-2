#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, json, getopt

opts, args = getopt.getopt(sys.argv[1:], "", ["dataset=","storejson"])

dataset = None
storejson = False

for opt, arg in opts :
    if opt == "--dataset" :
        dataset = arg
    if opt == "--storejson" :
        storejson = True
    
        
if dataset == None :
    print ''
    print 'Please define dataset to query for with --dataset'
    print ''

def queryForRunsAndTime(commandline):
    args = shlex.split(commandline)
    output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)

    runs = {}

    for line in output.communicate()[0].split('\n') :
        if len(line) > 0 :
            array = line.split()
            run = array[0]
            date = ' '.join(array[1:])
            runs[run] = date
    
    return runs

# collect run selection for last day
commandline = "dbs search --production --noheader --query=\"find dataset where dataset = " + dataset + " and dataset != *preprod* \""
args = shlex.split(commandline)
output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)
print ''
print 'Datasets:'
print ''
print output.communicate()[0]

commandline = "dbs search --production --query=\"find run,run.createdate where dataset = " + dataset + " and dataset != *preprod* \" --noheader"
runs = queryForRunsAndTime(commandline)

sorted_runs = runs.keys()
sorted_runs.sort()
all_runs = sorted_runs

# query for lumi

# repare lumi json for runs
json_runs = {}
for run in all_runs :
    json_runs[run] = [[1,7500]]
    
if storejson == False :
    tmp = tempfile.mkstemp()
    tmp_handle = open(tmp[1],'w')
else :
    tmpname = dataset
    tmpname = tmpname.replace('*','_STAR_',99)
    tmpname = tmpname.replace('/','_',99)
    tmpname = tmpname.replace('__','_',99)
    if tmpname[0] == '_' :
        tmpname = tmpname[1:]
    if tmpname[-1] == '_' :
        tmpname = tmpname[:-2]
    tmpname += '.json'
    print tmpname
    tmp = ['',tmpname]
    tmp_handle = open(tmp[1],'w')

json.dump(json_runs,tmp_handle)
tmp_handle.close()

commandline = 'lumiCalc.py -c frontier://LumiProd/CMS_LUMI_PROD -i ' + tmp[1] + ' overview'
print ''
print 'lumiCalc commandline:'
print commandline

args = shlex.split(commandline)
output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)

print ''
print 'Lumi corresponding to all lumi sections in all runs in dataset',dataset
print ''

print output.communicate()[0]
print ''
    
# os.remove(tmp[1])