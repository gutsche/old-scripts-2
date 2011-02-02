#!/usr/bin/env python

import sys, os, datetime, subprocess, shlex, tempfile, json, getopt

opts, args = getopt.getopt(sys.argv[1:], "", ["dataset=","storejson","lfns="])

dataset = None
storejson = False
lfnfile = None

for opt, arg in opts :
    if opt == "--dataset" :
        dataset = arg
    if opt == "--storejson" :
        storejson = True
    if opt == "--lfns" :
        lfnfile = arg
    
    
        
if dataset == None and lfnfile == None:
    print ''
    print 'Please define dataset to query for with --dataset or file with lfns with --lfns'
    print ''

def convertRange(runs):
    result = {}
    for run in runs.keys():
        tmp = []
        for lumirange in runs[run]:
            tmp.extend(range(lumirange[0],lumirange[1]+1))
        result[run] = tmp
    return result

def convertArray(runs):
    result = {}
    for run in runs.keys():
        lumis = runs[run]
        lumis.sort()
        endRange = lumis[0]
        startRange = lumis[0]
        lumiRanges = []
        for lumi in range(1,len(lumis)) :
            if endRange+1 == lumis[lumi] :
                endRange = lumis[lumi]
            else :
                lumiRanges.append([startRange,endRange])
                endRange = lumis[lumi]
                startRange = lumis[lumi]
        lumiRanges.append([startRange,endRange])
        result[run] = lumiRanges
    return result

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

def queryForRunsAndLumis(commandline):
    args = shlex.split(commandline)
    output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)

    runs = {}

    for line in output.communicate()[0].split('\n') :
        if len(line) > 0 :
            array = line.split()
            run = array[0]
            lumi = int(array[1])
            if run not in runs.keys():
                runs[run] = []
            if lumi not in runs[run]:
                runs[run].append(lumi)
    return runs


if lfnfile == None :

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
    # repare lumi json for runs
    json_runs = {}
    for run in all_runs :
        json_runs[run] = [[1,7500]]
else:
    runsnlumis = {}
    lfnfilehandle = open(lfnfile)
    for line in lfnfilehandle.readlines():
        commandline = "dbs search --production --query=\"find run,lumi where file = " + line.strip() + "\" --noheader"
        tmp = queryForRunsAndLumis(commandline)
        for run in tmp.keys():
            if run not in runsnlumis.keys():
                runsnlumis[run] = []
            for lumi in tmp[run]:
                if lumi not in runsnlumis[run]:
                    runsnlumis[run].append(lumi)
            
    json_runs = convertArray(runsnlumis)
    
if storejson == False :
    tmp = tempfile.mkstemp()
    tmp_handle = open(tmp[1],'w')
else :
    if lfnfile == None :
        tmpname = dataset
        tmpname = tmpname.replace('*','_STAR_',99)
        tmpname = tmpname.replace('/','_',99)
        tmpname = tmpname.replace('__','_',99)
        if tmpname[0] == '_' :
            tmpname = tmpname[1:]
        if tmpname[-1] == '_' :
            tmpname = tmpname[:-2]
        tmpname += '.json'
        tmp = ['',tmpname]
        tmp_handle = open(tmp[1],'w')
    else :
        tmpname = lfnfile.split('.')[0] + '.json'
        tmp = ['',tmpname]
        tmp_handle = open(tmp[1],'w')

json.dump(json_runs,tmp_handle)
tmp_handle.close()

commandline = 'lumiCalc.py -c frontier://LumiProd/CMS_LUMI_PROD -i ' + tmp[1] + ' overview'
# print ''
# print 'lumiCalc commandline:'
# print commandline

args = shlex.split(commandline)
output = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE)

if lfnfile == None :
    print ''
    print 'Lumi corresponding to all lumi sections in all runs in dataset',dataset
    print ''
else :
    print ''
    print 'Lumi corresponding to all lumi sections in all files in lfn list from input file',lfnfile
    print ''
    
print output.communicate()[0]
print ''
    
# print tmp[1]
if storejson == False :
    os.remove(tmp[1])