#!/usr/bin/env python

import os,sys

sites = [ 'T0_CH_CERN', 'T1_CH_CERN', 'T1_DE_KIT', 'T1_IT_CNAF', 'T1_ES_PIC', 'T1_FR_CCIN2P3', 'T1_UK_RAL', 'T1_US_FNAL', 'T1_TW_ASGC',]
data_tiers = ['RAW','RECO','ALCARECO','RAW-RECO','USER']
mc_tiers = ['GEN-SIM-RAW','GEN-SIM-RECO','AODSIM','GEN-SIM_RAWDEBUG','GEN-SIM_RECODEBUG']

mc_acq = ['Summer08','Fall08','Winter09','Summer09','Spring10','Summer10','Fall10']
data_acq = ['GlobalMar08','CRUZET1','CRUZET2','CRUZET3','CRUZET4','EW35','CRUZET09','CRAFT09','BeamCommissioning08','Commissioning08','BeamCommissioning09','Commissioning09','Commissioning10','Run2010A','Run2010B']

special_acq = ['StoreResults','JobRobot']

data = {}
mc = {}
special_data = {}
special_mc = {}

def parseFile(file,site):
    data[site] = {}
    mc[site] = {}
    special_data[site] = {}
    special_mc[site] = {}
    
    for line in file.readlines() :
        array = line.split(',')
        if len(array) != 8 :
            continue
        if array[0].count('Acquisition') > 0 :
            continue
        acq = array[0].strip()
        tier = array[1].strip()
        data_total = float(array[2])
        data_cust = float(array[3])
        data_non_cust = float(array[4])
        mc_total = float(array[5])
        mc_cust = float(array[6])
        mc_non_cust = float(array[7])
        if acq in mc_acq :
            if acq not in mc[site].keys():
                mc[site][acq] = {}
            if tier not in mc[site][acq].keys():
                mc[site][acq][tier] = {}
            if 'custodial' not in mc[site][acq][tier].keys() :
                mc[site][acq][tier]['custodial'] = 0
            if 'non-custodial' not in mc[site][acq][tier].keys() :
                mc[site][acq][tier]['non-custodial'] = 0
            mc[site][acq][tier]['custodial'] += mc_cust
            mc[site][acq][tier]['non-custodial'] += mc_non_cust
        elif acq in data_acq :
            if acq not in data[site].keys():
                data[site][acq] = {}
            if tier not in data[site][acq].keys():
                data[site][acq][tier] = {}
            if 'custodial' not in data[site][acq][tier].keys() :
                data[site][acq][tier]['custodial'] = 0
            if 'non-custodial' not in data[site][acq][tier].keys() :
                data[site][acq][tier]['non-custodial'] = 0
            data[site][acq][tier]['custodial'] += data_cust
            data[site][acq][tier]['non-custodial'] += data_non_cust
        else :
            if acq not in special_data[site].keys():
                special_data[site][acq] = {}
            if tier not in special_data[site][acq].keys():
                special_data[site][acq][tier] = {}
            if 'custodial' not in special_data[site][acq][tier].keys() :
                special_data[site][acq][tier]['custodial'] = 0
            if 'non-custodial' not in special_data[site][acq][tier].keys() :
                special_data[site][acq][tier]['non-custodial'] = 0

            special_data[site][acq][tier]['custodial'] += data_cust
            special_data[site][acq][tier]['non-custodial'] += data_non_cust

            if acq not in special_mc[site].keys():
                special_mc[site][acq] = {}
            if tier not in special_mc[site][acq].keys():
                special_mc[site][acq][tier] = {}
            if 'custodial' not in special_mc[site][acq][tier].keys() :
                special_mc[site][acq][tier]['custodial'] = 0
            if 'non-custodial' not in special_mc[site][acq][tier].keys() :
                special_mc[site][acq][tier]['non-custodial'] = 0
            special_mc[site][acq][tier]['custodial'] += data_cust
            special_mc[site][acq][tier]['non-custodial'] += data_non_cust
            

# do something

parseFile(open('T1DataSummary_T0_CH_CERN.txt'),'T0_CH_CERN')
parseFile(open('T1DataSummary_T1_CH_CERN.txt'),'T1_CH_CERN')
parseFile(open('T1DataSummary_T1_DE_KIT.txt'),'T1_DE_KIT')
parseFile(open('T1DataSummary_T1_ES_PIC.txt'),'T1_ES_PIC')
parseFile(open('T1DataSummary_T1_FR_CCIN2P3.txt'),'T1_FR_CCIN2P3')
parseFile(open('T1DataSummary_T1_IT_CNAF.txt'),'T1_IT_CNAF')
parseFile(open('T1DataSummary_T1_TW_ASGC.txt'),'T1_TW_ASGC')
parseFile(open('T1DataSummary_T1_UK_RAL.txt'),'T1_UK_RAL')
parseFile(open('T1DataSummary_T1_US_FNAL.txt'),'T1_US_FNAL')

# print data table

data_detailed_output = open('data_detailed_output.csv','w')

sum = {}
for site in sites:
    sum[site] = {}
    for tier in data_tiers :
        sum[site][tier] = {}
        for cust in ['custodial','non-custodial'] :
            sum[site][tier][cust] = 0
sitestring = ','.join(sites)
data_detailed_output.write('Acquisition era,Data Tier,Cust./Non-Cust.,' + sitestring + ',All sites\n')
for acq in data_acq:
    for tier in data_tiers :
        for cust in ['custodial','non-custodial'] :
            line = ''
            line += acq + ',' + tier + ',' + cust + ','
            tmp = 0
            for site in sites :
                line += str(data[site][acq][tier][cust]) + ','
                sum[site][tier][cust] += data[site][acq][tier][cust]
                tmp += data[site][acq][tier][cust]
            line += str(tmp)
            data_detailed_output.write(line + '\n')
for tier in data_tiers :
    for cust in ['custodial','non-custodial'] :
        data_detailed_output.write('Total,' + tier + ',' + cust + ',')
        tmp = 0
        for site in sites:
            data_detailed_output.write(str(sum[site][tier][cust]) + ',')
            tmp +=sum[site][tier][cust]
        data_detailed_output.write(str(tmp) + '\n')
data_detailed_output.write('Total,,,')
tmp2 = 0
for site in sites:
    tmp = 0
    for tier in data_tiers :
        for cust in ['custodial','non-custodial'] :
            tmp += sum[site][tier][cust]
            tmp2 += sum[site][tier][cust]
    data_detailed_output.write(str(tmp) + ',')
data_detailed_output.write(str(tmp2) + '\n')
data_detailed_output.close()
print 'Wrote data_detailed_output.csv'

# output for only acq and cust/non-cust

data_acq_output = open('data_acq_output.csv','w')

sum = {}
for site in sites:
    sum[site] = {}
    sum[site]['custodial'] = 0
    sum[site]['non-custodial'] = 0
sitestring = ','.join(sites)
data_acq_output.write('Acquisition era,Cust./Non-Cust.,' + sitestring + ',All sites\n')
for acq in data_acq:
    for cust in ['custodial','non-custodial'] :
        line = ''
        line += acq + ',' + cust + ','
        tmp2 = 0
        for site in sites :
            tmp = 0
            for tier in data_tiers :
                tmp += data[site][acq][tier][cust]                    
            line += str(tmp) + ','
            sum[site][cust] += tmp
            tmp2 += tmp
        line += str(tmp2)    
        data_acq_output.write(line + '\n')
data_acq_output.write('Total,custodial,')
tmp = 0
for site in sites:
    data_acq_output.write(str(sum[site]['custodial']) + ',')
    tmp += sum[site]['custodial']
data_acq_output.write(str(tmp) + '\n')
data_acq_output.write('Total,non-custodial,')
tmp = 0
for site in sites:
    data_acq_output.write(str(sum[site]['non-custodial']) + ',')
    tmp += sum[site]['non-custodial']
data_acq_output.write(str(tmp) + '\n')
data_acq_output.write('Total,,')
tmp = 0
for site in sites:
    data_acq_output.write(str(sum[site]['custodial']+sum[site]['non-custodial']) + ',')
    tmp += sum[site]['custodial']+sum[site]['non-custodial']
data_acq_output.write(str(tmp) + '\n')
data_acq_output.close()
print 'Wrote data_acq_output.csv'


# output for only acq and tier

data_tier_output = open('data_tier_output.csv','w')

sum = {}
for site in sites:
    sum[site] = {}
    for tier in data_tiers :
        sum[site][tier] = 0
sitestring = ','.join(sites)
data_tier_output.write('Acquisition era,Data tier,' + sitestring + ',All sites\n')
for acq in data_acq:
    for tier in data_tiers :
        line = ''
        line += acq + ',' + tier + ','
        tmp2 = 0
        for site in sites :
            tmp = 0
            for cust in ['custodial','non-custodial'] :
                tmp += data[site][acq][tier][cust]                    
            line += str(tmp) + ','
            sum[site][tier] += tmp
            tmp2 += tmp
        line += str(tmp2)    
        data_tier_output.write(line + '\n')
for tier in data_tiers:
    data_tier_output.write('Total,' + tier + ',')
    tmp = 0 
    for site in sites:
        data_tier_output.write(str(sum[site][tier]) + ',')
        tmp += sum[site][tier]   
    data_tier_output.write(str(tmp) + '\n')
data_tier_output.write('Total,,')
tmp2 = 0
for site in sites:
    tmp = 0
    for tier in data_tiers:
        tmp += sum[site][tier]
        tmp2 += sum[site][tier]
    data_tier_output.write(str(tmp) + ',')
data_tier_output.write(str(tmp2) + '\n')
data_tier_output.close()
print 'Wrote data_tier_output.csv'

# print mc table

mc_detailed_output = open('mc_detailed_output.csv','w')

sum = {}
for site in sites:
    sum[site] = {}
    for tier in mc_tiers :
        sum[site][tier] = {}
        for cust in ['custodial','non-custodial'] :
            sum[site][tier][cust] = 0
sitestring = ','.join(sites)
mc_detailed_output.write('Acquisition era,Data Tier,Cust./Non-Cust.,' + sitestring + ',All sites\n')
for acq in mc_acq:
    for tier in mc_tiers :
        for cust in ['custodial','non-custodial'] :
            line = ''
            line += acq + ',' + tier + ',' + cust + ','
            tmp = 0
            for site in sites :
                line += str(mc[site][acq][tier][cust]) + ','
                sum[site][tier][cust] += mc[site][acq][tier][cust]
                tmp += mc[site][acq][tier][cust]
            line += str(tmp)
            mc_detailed_output.write(line + '\n')
for tier in mc_tiers :
    for cust in ['custodial','non-custodial'] :
        mc_detailed_output.write('Total,' + tier + ',' + cust + ',')
        tmp = 0
        for site in sites:
            mc_detailed_output.write(str(sum[site][tier][cust]) + ',')
            tmp +=sum[site][tier][cust]
        mc_detailed_output.write(str(tmp) + '\n')
mc_detailed_output.write('Total,,,')
tmp2 = 0
for site in sites:
    tmp = 0
    for tier in mc_tiers :
        for cust in ['custodial','non-custodial'] :
            tmp += sum[site][tier][cust]
            tmp2 += sum[site][tier][cust]
    mc_detailed_output.write(str(tmp) + ',')
mc_detailed_output.write(str(tmp2) + '\n')
mc_detailed_output.close()
print 'Wrote mc_detailed_output.csv'

# output for only acq and cust/non-cust

mc_acq_output = open('mc_acq_output.csv','w')

sum = {}
for site in sites:
    sum[site] = {}
    sum[site]['custodial'] = 0
    sum[site]['non-custodial'] = 0
sitestring = ','.join(sites)
mc_acq_output.write('Acquisition era,Cust./Non-Cust.,' + sitestring + ',All sites\n')
for acq in mc_acq:
    for cust in ['custodial','non-custodial'] :
        line = ''
        line += acq + ',' + cust + ','
        tmp2 = 0
        for site in sites :
            tmp = 0
            for tier in mc_tiers :
                tmp += mc[site][acq][tier][cust]                    
            line += str(tmp) + ','
            sum[site][cust] += tmp
            tmp2 += tmp
        line += str(tmp2)    
        mc_acq_output.write(line + '\n')
mc_acq_output.write('Total,custodial,')
tmp = 0
for site in sites:
    mc_acq_output.write(str(sum[site]['custodial']) + ',')
    tmp += sum[site]['custodial']
mc_acq_output.write(str(tmp) + '\n')
mc_acq_output.write('Total,non-custodial,')
tmp = 0
for site in sites:
    mc_acq_output.write(str(sum[site]['non-custodial']) + ',')
    tmp += sum[site]['non-custodial']
mc_acq_output.write(str(tmp) + '\n')
mc_acq_output.write('Total,,')
tmp = 0
for site in sites:
    mc_acq_output.write(str(sum[site]['custodial']+sum[site]['non-custodial']) + ',')
    tmp += sum[site]['custodial']+sum[site]['non-custodial']
mc_acq_output.write(str(tmp) + '\n')
mc_acq_output.close()
print 'Wrote mc_acq_output.csv'


# output for only acq and tier

mc_tier_output = open('mc_tier_output.csv','w')

sum = {}
for site in sites:
    sum[site] = {}
    for tier in mc_tiers :
        sum[site][tier] = 0
sitestring = ','.join(sites)
mc_tier_output.write('Acquisition era,Data tier,' + sitestring + ',All sites\n')
for acq in mc_acq:
    for tier in mc_tiers :
        line = ''
        line += acq + ',' + tier + ','
        tmp2 = 0
        for site in sites :
            tmp = 0
            for cust in ['custodial','non-custodial'] :
                tmp += mc[site][acq][tier][cust]                    
            line += str(tmp) + ','
            sum[site][tier] += tmp
            tmp2 += tmp
        line += str(tmp2)    
        mc_tier_output.write(line + '\n')
for tier in mc_tiers:
    mc_tier_output.write('Total,' + tier + ',')
    tmp = 0 
    for site in sites:
        mc_tier_output.write(str(sum[site][tier]) + ',')
        tmp += sum[site][tier]   
    mc_tier_output.write(str(tmp) + '\n')
mc_tier_output.write('Total,,')
tmp2 = 0
for site in sites:
    tmp = 0
    for tier in mc_tiers:
        tmp += sum[site][tier]
        tmp2 += sum[site][tier]
    mc_tier_output.write(str(tmp) + ',')
mc_tier_output.write(str(tmp2) + '\n')
mc_tier_output.close()
print 'Wrote mc_tier_output.csv'
