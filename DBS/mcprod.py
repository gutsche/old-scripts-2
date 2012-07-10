#!/usr/bin/env python

import sys,os,subprocess,shlex,locale
locale.setlocale(locale.LC_ALL, 'en_US')

def queryForDifferentCampaigns(era,tier):
    campaigns = []
    commandline = "dbs search --query=\"find dataset where dataset = *"+era+"*"+tier+"\" --noheader --production"
    localargs = shlex.split(commandline)
    output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
    lines = output.communicate()[0].split('\n')
    for line in lines:
        if line == '': continue
        array = line.split('/')
        array2 = array[2].split('-')
        if array2[1] not in campaigns: campaigns.append(array2[1])
    return campaigns
    

def queryDBS(title,dataset_query):
    result = {}

    commandline = "dbs search --query=\"find dataset.status,sum(block.numevents) where dataset = "+dataset_query+"\" --noheader --production"
    localargs = shlex.split(commandline)
    output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
    lines = output.communicate()[0].split('\n')
    for line in lines:
        if line == '': continue
        array = line.split()
        result[array[0]] = int(array[1])
    
    print ""
    print title
    print "----------------------------------"
    print "(DBS query string: " + dataset_query + ")"
    print "----------------------------------"
    print ""
    total = 0
    if 'PRODUCTION' in result.keys():
        print "%s: %s" % ("PRODUCTION".ljust(12),locale.format("%d", result['PRODUCTION'], grouping=True).rjust(20))
        total += result['PRODUCTION']
    if 'VALID' in result.keys():
        print "%s: %s" % ("VALID".ljust(12),locale.format("%d", result['VALID'], grouping=True).rjust(20))
        total += result['VALID']
    print "----------------------------------"
    print "%s: %s" % ("TOTAL".ljust(12),locale.format("%d", total, grouping=True).rjust(20))
    print ""

# campaigns = queryForDifferentCampaigns("Summer12","AODSIM")
queryDBS("Summer12 GEN-SIM","*Summer12*GEN-SIM")
# queryDBS("Summer12 DR51X AODSIM","*Summer12-PU_S7_START50*AODSIM")
# queryDBS("Summer12 DR51X NOPU AODSIM","*Summer12-NoPileUp_START50*AODSIM")
queryDBS("Summer12 DR52X AODSIM","*Summer12-PU_S7_START52_V*AODSIM")
# queryDBS("Summer12 DR52X LowPU AODSIM","*Summer12-PU_S8_START52_V*AODSIM")
# queryDBS("Summer12 DR52X TSG GEN-SIM-RECO","*Summer12-PU_S9_START52_V*GEN-SIM-RECO")
# for campaign in campaigns:
    # if campaign == "PU_S7_START50_V15": continue
    # if campaign == "PU_S7_START52_V5": continue
    # if campaign == 'NoPileUp_START50_V15' : continue
    # dataset_query = '*Summer12-' + campaign + '*AODSIM'
    # queryDBS("Summer12 AODSIM",dataset_query)
    # print campaign
queryDBS("Summer12 DR53X AODSIM","*Summer12_DR53X*AODSIM")
