#!/usr/bin/env python

import os,sys,datetime

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import colorConverter
from operator import add

# Make a list of colors cycling through the rgbcmyk series.
colors = [colorConverter.to_rgba(c) for c in ('r','g','m','c','y','b','k')]
now = datetime.datetime.utcnow()
date = now.strftime("%Y-%m-%d")
fulldate = now.strftime("%A, %d. %B %Y %H:%M UTC")

types = [
'custodial data',
'non-custodial data',
'custodial MC',
'non-custodial MC'
]

sites = [
'T1_DE_KIT',
'T1_ES_PIC',
'T1_FR_CCIN2P3',
'T1_IT_CNAF',
'T1_UK_RAL',
'T1_US_FNAL',
'T1_TW_ASGC',
]

tiers_data = [
'RAW',
'RECO',
'DQM',
'ALCARECO',
'RAW-RECO',
'USER',
]

eras_data  = [
'GlobalMar08',
'CRUZET1',
'CRUZET2',
'CRUZET3',
'CRUZET4',
'EW35',
'CRUZET09',
'CRAFT09',
'BeamCommissioning08',
'Commissioning08',
'BeamCommissioning09',
'Commissioning09',
'Commissioning10',
'Run2010A',
'Run2010B',
'HIRun2010',
'Run2011A',
'Run2011B'
]

tiers_mc   = [
'GEN-SIM',
'GEN-RAW',
'GEN-SIM-RAW',
'GEN-SIM-RECO',
'AODSIM',
'DQM',
'GEN-SIM-RAWDEBUG',
'GEN-SIM-RECODEBUG',
]

eras_mc    = [
'Summer08',
'Fall08',
'Winter09',
'Summer09',
'Spring10',
'Summer10',
'Fall10',
'Winter10',
'Spring11',
'Summer11',
'Fall11'
]

ignore_eras = [
'JobRobot',
'StoreResults',
]

ignore_tiers = [
]


def main(argv) :
    """
    tape storage statistics
    parameters: <previous date> <current date>
    execute from top directory
    """
    
    print 'Execute at',fulldate

    if len(argv) != 2:
        print main.__doc__
        sys.exit(2)
        
    previous_date = argv[0]
    current_date  = argv[1]
        
    current                  = {}
    current['T1_DE_KIT']     = parseFile(current_date + '/T1DataSummary_T1_DE_KIT.txt')
    current['T1_ES_PIC']     = parseFile(current_date + '/T1DataSummary_T1_ES_PIC.txt')
    current['T1_FR_CCIN2P3'] = parseFile(current_date + '/T1DataSummary_T1_FR_CCIN2P3.txt')
    current['T1_IT_CNAF']    = parseFile(current_date + '/T1DataSummary_T1_IT_CNAF.txt')
    current['T1_TW_ASGC']    = parseFile(current_date + '/T1DataSummary_T1_TW_ASGC.txt')
    current['T1_UK_RAL']     = parseFile(current_date + '/T1DataSummary_T1_UK_RAL.txt')
    current['T1_US_FNAL']    = parseFile(current_date + '/T1DataSummary_T1_US_FNAL.txt')

    previous                  = {}
    previous['T1_DE_KIT']     = parseFile(previous_date + '/T1DataSummary_T1_DE_KIT.txt')
    previous['T1_ES_PIC']     = parseFile(previous_date + '/T1DataSummary_T1_ES_PIC.txt')
    previous['T1_FR_CCIN2P3'] = parseFile(previous_date + '/T1DataSummary_T1_FR_CCIN2P3.txt')
    previous['T1_IT_CNAF']    = parseFile(previous_date + '/T1DataSummary_T1_IT_CNAF.txt')
    previous['T1_TW_ASGC']    = parseFile(previous_date + '/T1DataSummary_T1_TW_ASGC.txt')
    previous['T1_UK_RAL']     = parseFile(previous_date + '/T1DataSummary_T1_UK_RAL.txt')
    previous['T1_US_FNAL']    = parseFile(previous_date + '/T1DataSummary_T1_US_FNAL.txt')

    completeCategories(current)
    completeCategories(previous)

    checkCategories(current)
    checkCategories(previous)
    
    delta = subtract(current,previous)
    
    detailedDictDataCurrent = createDetailedDictData(current)
    eraCustDictDataCurrent = createEraCustDictData(current)
    eraTierDictDataCurrent = createEraTierDictData(current)
    tierDictDataCurrent = createTierDictData(current)
    tierDictCustDataCurrent = createTierDictCustData(current)
    tierDictNonCustDataCurrent = createTierDictNonCustData(current)
    eraDictDataCurrent = createEraDictData(current)
    eraDictCustDataCurrent = createEraDictCustData(current)
    eraDictNonCustDataCurrent = createEraDictNonCustData(current)

    detailedArrayDataCurrent = createDetailedArrayData(detailedDictDataCurrent)
    eraCustArrayDataCurrent = createEraCustArrayData(eraCustDictDataCurrent)
    eraTierArrayDataCurrent = createEraTierArrayData(eraTierDictDataCurrent)
    tierArrayDataCurrent = createTierArrayData(tierDictDataCurrent)
    tierArrayCustDataCurrent = createTierArrayCustData(tierDictCustDataCurrent)
    tierArrayNonCustDataCurrent = createTierArrayNonCustData(tierDictNonCustDataCurrent)
    eraArrayDataCurrent = createEraArrayData(eraDictDataCurrent)
    eraArrayCustDataCurrent = createEraArrayCustData(eraDictCustDataCurrent)
    eraArrayNonCustDataCurrent = createEraArrayNonCustData(eraDictNonCustDataCurrent)

    detailedDictMCCurrent = createDetailedDictMC(current)
    eraCustDictMCCurrent = createEraCustDictMC(current)
    eraTierDictMCCurrent = createEraTierDictMC(current)
    tierDictMCCurrent = createTierDictMC(current)
    tierDictCustMCCurrent = createTierDictCustMC(current)
    tierDictNonCustMCCurrent = createTierDictNonCustMC(current)
    eraDictMCCurrent = createEraDictMC(current)
    eraDictCustMCCurrent = createEraDictCustMC(current)
    eraDictNonCustMCCurrent = createEraDictNonCustMC(current)

    detailedArrayMCCurrent = createDetailedArrayMC(detailedDictMCCurrent)
    eraCustArrayMCCurrent = createEraCustArrayMC(eraCustDictMCCurrent)
    eraTierArrayMCCurrent = createEraTierArrayMC(eraTierDictMCCurrent)
    tierArrayMCCurrent = createTierArrayMC(tierDictMCCurrent)
    tierArrayCustMCCurrent = createTierArrayCustMC(tierDictCustMCCurrent)
    tierArrayNonCustMCCurrent = createTierArrayNonCustMC(tierDictNonCustMCCurrent)
    eraArrayMCCurrent = createEraArrayMC(eraDictMCCurrent)
    eraArrayCustMCCurrent = createEraArrayCustMC(eraDictCustMCCurrent)
    eraArrayNonCustMCCurrent = createEraArrayNonCustMC(eraDictNonCustMCCurrent)

    createHTMLfromArray(detailedArrayDataCurrent,'tape_storage_overview_current_data_detailed.html','Current Week Tape Storage Overview: Detailed View for Data',3)
    createHTMLfromArray(eraTierArrayDataCurrent,'tape_storage_overview_current_data_era_tier.html','Current Week Tape Storage Overview: Era/Tier View for Data',2)
    createHTMLfromArray(eraCustArrayDataCurrent,'tape_storage_overview_current_data_era_cust.html','Current Week Tape Storage Overview: Era/Cust./Non-Cust. View for Data',2)
    createHTMLfromArray(eraArrayDataCurrent,'tape_storage_overview_current_data_era.html','Current Week Tape Storage Overview: Era View for Data',1)
    createHTMLfromArray(eraArrayCustDataCurrent,'tape_storage_overview_current_cust_data_era.html','Current Week Tape Storage Overview: Era View for Custodial Data',1)
    createHTMLfromArray(eraArrayNonCustDataCurrent,'tape_storage_overview_current_non_cust_data_era.html','Current Week Tape Storage Overview: Era View for Non-Custodial Data',1)
    createHTMLfromArray(tierArrayDataCurrent,'tape_storage_overview_current_data_tier.html','Current Week Tape Storage Overview: Tier View for Data',1)
    createHTMLfromArray(tierArrayCustDataCurrent,'tape_storage_overview_current_cust_data_tier.html','Current Week Tape Storage Overview: Tier View for Custodial Data',1)
    createHTMLfromArray(tierArrayNonCustDataCurrent,'tape_storage_overview_current_non_cust_data_tier.html','Current Week Tape Storage Overview: Tier View for Non-Custodial Data',1)

    createHTMLfromArray(detailedArrayMCCurrent,'tape_storage_overview_current_mc_detailed.html','Current Week Tape Storage Overview: Detailed View for MC',3)
    createHTMLfromArray(eraTierArrayMCCurrent,'tape_storage_overview_current_mc_era_tier.html','Current Week Tape Storage Overview: Era/Tier View for MC',2)
    createHTMLfromArray(eraCustArrayMCCurrent,'tape_storage_overview_current_mc_era_cust.html','Current Week Tape Storage Overview: Era/Cust./Non-Cust. View for MC',2)
    createHTMLfromArray(eraArrayMCCurrent,'tape_storage_overview_current_mc_era.html','Current Week Tape Storage Overview: Era View for MC',1)
    createHTMLfromArray(eraArrayCustMCCurrent,'tape_storage_overview_current_cust_mc_era.html','Current Week Tape Storage Overview: Era View for Custodial MC',1)
    createHTMLfromArray(eraArrayNonCustMCCurrent,'tape_storage_overview_current_non_cust_mc_era.html','Current Week Tape Storage Overview: Era View for Non-Custodial MC',1)
    createHTMLfromArray(tierArrayMCCurrent,'tape_storage_overview_current_mc_tier.html','Current Week Tape Storage Overview: Tier View for MC',1)
    createHTMLfromArray(tierArrayCustMCCurrent,'tape_storage_overview_current_cust_mc_tier.html','Current Week Tape Storage Overview: Tier View for Custodial MC',1)
    createHTMLfromArray(tierArrayNonCustMCCurrent,'tape_storage_overview_current_non_cust_mc_tier.html','Current Week Tape Storage Overview: Tier View for Non-Custodial MC',1)

    detailedDictDataPrevious = createDetailedDictData(previous)
    eraCustDictDataPrevious = createEraCustDictData(previous)
    eraTierDictDataPrevious = createEraTierDictData(previous)
    tierDictDataPrevious = createTierDictData(previous)
    tierDictCustDataPrevious = createTierDictCustData(previous)
    tierDictNonCustDataPrevious = createTierDictNonCustData(previous)
    eraDictDataPrevious = createEraDictData(previous)
    eraDictCustDataPrevious = createEraDictCustData(previous)
    eraDictNonCustDataPrevious = createEraDictNonCustData(previous)

    detailedArrayDataPrevious = createDetailedArrayData(detailedDictDataPrevious)
    eraCustArrayDataPrevious = createEraCustArrayData(eraCustDictDataPrevious)
    eraTierArrayDataPrevious = createEraTierArrayData(eraTierDictDataPrevious)
    tierArrayDataPrevious = createTierArrayData(tierDictDataPrevious)
    tierArrayCustDataPrevious = createTierArrayCustData(tierDictCustDataPrevious)
    tierArrayNonCustDataPrevious = createTierArrayNonCustData(tierDictNonCustDataPrevious)
    eraArrayDataPrevious = createEraArrayData(eraDictDataPrevious)
    eraArrayCustDataPrevious = createEraArrayCustData(eraDictCustDataPrevious)
    eraArrayNonCustDataPrevious = createEraArrayNonCustData(eraDictNonCustDataPrevious)

    detailedDictMCPrevious = createDetailedDictMC(previous)
    eraCustDictMCPrevious = createEraCustDictMC(previous)
    eraTierDictMCPrevious = createEraTierDictMC(previous)
    tierDictMCPrevious = createTierDictMC(previous)
    tierDictCustMCPrevious = createTierDictCustMC(previous)
    tierDictNonCustMCPrevious = createTierDictNonCustMC(previous)
    eraDictMCPrevious = createEraDictMC(previous)
    eraDictCustMCPrevious = createEraDictCustMC(previous)
    eraDictNonCustMCPrevious = createEraDictNonCustMC(previous)

    detailedArrayMCPrevious = createDetailedArrayMC(detailedDictMCPrevious)
    eraCustArrayMCPrevious = createEraCustArrayMC(eraCustDictMCPrevious)
    eraTierArrayMCPrevious = createEraTierArrayMC(eraTierDictMCPrevious)
    tierArrayMCPrevious = createTierArrayMC(tierDictMCPrevious)
    tierArrayCustMCPrevious = createTierArrayCustMC(tierDictCustMCPrevious)
    tierArrayNonCustMCPrevious = createTierArrayNonCustMC(tierDictNonCustMCPrevious)
    eraArrayMCPrevious = createEraArrayMC(eraDictMCPrevious)
    eraArrayCustMCPrevious = createEraArrayCustMC(eraDictCustMCPrevious)
    eraArrayNonCustMCPrevious = createEraArrayNonCustMC(eraDictNonCustMCPrevious)

    createHTMLfromArray(detailedArrayDataPrevious,'tape_storage_overview_previous_data_detailed.html','Previous Week Tape Storage Overview: Detailed View for Data',3)
    createHTMLfromArray(eraTierArrayDataPrevious,'tape_storage_overview_previous_data_era_tier.html','Previous Week Tape Storage Overview: Era/Tier View for Data',2)
    createHTMLfromArray(eraCustArrayDataPrevious,'tape_storage_overview_previous_data_era_cust.html','Previous Week Tape Storage Overview: Era/Cust./Non-Cust. View for Data',2)
    createHTMLfromArray(eraArrayDataPrevious,'tape_storage_overview_previous_data_era.html','Previous Week Tape Storage Overview: Era View for Data',1)
    createHTMLfromArray(eraArrayCustDataPrevious,'tape_storage_overview_previous_cust_data_era.html','Previous Week Tape Storage Overview: Era View for Custodial Data',1)
    createHTMLfromArray(eraArrayNonCustDataPrevious,'tape_storage_overview_previous_non_cust_data_era.html','Previous Week Tape Storage Overview: Era View for Non-Custodial Data',1)
    createHTMLfromArray(tierArrayDataPrevious,'tape_storage_overview_previous_data_tier.html','Previous Week Tape Storage Overview: Tier View for Data',1)
    createHTMLfromArray(tierArrayCustDataPrevious,'tape_storage_overview_previous_cust_data_tier.html','Previous Week Tape Storage Overview: Tier View for Custodial Data',1)
    createHTMLfromArray(tierArrayNonCustDataPrevious,'tape_storage_overview_previous_non_cust_data_tier.html','Previous Week Tape Storage Overview: Tier View for Non-Custodial Data',1)

    createHTMLfromArray(detailedArrayMCPrevious,'tape_storage_overview_previous_mc_detailed.html','Previous Week Tape Storage Overview: Detailed View for MC',3)
    createHTMLfromArray(eraTierArrayMCPrevious,'tape_storage_overview_previous_mc_era_tier.html','Previous Week Tape Storage Overview: Era/Tier View for MC',2)
    createHTMLfromArray(eraCustArrayMCPrevious,'tape_storage_overview_previous_mc_era_cust.html','Previous Week Tape Storage Overview: Era/Cust./Non-Cust. View for MC',2)
    createHTMLfromArray(eraArrayMCPrevious,'tape_storage_overview_previous_mc_era.html','Previous Week Tape Storage Overview: Era View for MC',1)
    createHTMLfromArray(eraArrayCustMCPrevious,'tape_storage_overview_previous_cust_mc_era.html','Previous Week Tape Storage Overview: Era View for Custodial MC',1)
    createHTMLfromArray(eraArrayNonCustMCPrevious,'tape_storage_overview_previous_non_cust_mc_era.html','Previous Week Tape Storage Overview: Era View for Non-Custodial MC',1)
    createHTMLfromArray(tierArrayMCPrevious,'tape_storage_overview_previous_mc_tier.html','Previous Week Tape Storage Overview: Tier View for MC',1)
    createHTMLfromArray(tierArrayCustMCPrevious,'tape_storage_overview_previous_cust_mc_tier.html','Previous Week Tape Storage Overview: Tier View for Custodial MC',1)
    createHTMLfromArray(tierArrayNonCustMCPrevious,'tape_storage_overview_previous_non_cust_mc_tier.html','Previous Week Tape Storage Overview: Tier View for Non-Custodial MC',1)

    detailedDictDataDelta = createDetailedDictData(delta)
    eraCustDictDataDelta = createEraCustDictData(delta)
    eraTierDictDataDelta = createEraTierDictData(delta)
    tierDictDataDelta = createTierDictData(delta)
    tierDictCustDataDelta = createTierDictCustData(delta)
    tierDictNonCustDataDelta = createTierDictNonCustData(delta)
    eraDictDataDelta = createEraDictData(delta)
    eraDictCustDataDelta = createEraDictCustData(delta)
    eraDictNonCustDataDelta = createEraDictNonCustData(delta)

    detailedArrayDataDelta = createDetailedArrayData(detailedDictDataDelta)
    eraCustArrayDataDelta = createEraCustArrayData(eraCustDictDataDelta)
    eraTierArrayDataDelta = createEraTierArrayData(eraTierDictDataDelta)
    tierArrayDataDelta = createTierArrayData(tierDictDataDelta)
    tierArrayCustDataDelta = createTierArrayCustData(tierDictCustDataDelta)
    tierArrayNonCustDataDelta = createTierArrayNonCustData(tierDictNonCustDataDelta)
    eraArrayDataDelta = createEraArrayData(eraDictDataDelta)
    eraArrayCustDataDelta = createEraArrayCustData(eraDictCustDataDelta)
    eraArrayNonCustDataDelta = createEraArrayNonCustData(eraDictNonCustDataDelta)

    detailedDictMCDelta = createDetailedDictMC(delta)
    eraCustDictMCDelta = createEraCustDictMC(delta)
    eraTierDictMCDelta = createEraTierDictMC(delta)
    tierDictMCDelta = createTierDictMC(delta)
    tierDictCustMCDelta = createTierDictCustMC(delta)
    tierDictNonCustMCDelta = createTierDictNonCustMC(delta)
    eraDictMCDelta = createEraDictMC(delta)
    eraDictCustMCDelta = createEraDictCustMC(delta)
    eraDictNonCustMCDelta = createEraDictNonCustMC(delta)

    detailedArrayMCDelta = createDetailedArrayMC(detailedDictMCDelta)
    eraCustArrayMCDelta = createEraCustArrayMC(eraCustDictMCDelta)
    eraTierArrayMCDelta = createEraTierArrayMC(eraTierDictMCDelta)
    tierArrayMCDelta = createTierArrayMC(tierDictMCDelta)
    tierArrayCustMCDelta = createTierArrayCustMC(tierDictCustMCDelta)
    tierArrayNonCustMCDelta = createTierArrayNonCustMC(tierDictNonCustMCDelta)
    eraArrayMCDelta = createEraArrayMC(eraDictMCDelta)
    eraArrayCustMCDelta = createEraArrayCustMC(eraDictCustMCDelta)
    eraArrayNonCustMCDelta = createEraArrayNonCustMC(eraDictNonCustMCDelta)

    createHTMLfromArray(detailedArrayDataDelta,'tape_storage_overview_delta_data_detailed.html','Delta Week Tape Storage Overview: Detailed View for Data',3)
    createHTMLfromArray(eraTierArrayDataDelta,'tape_storage_overview_delta_data_era_tier.html','Delta Week Tape Storage Overview: Era/Tier View for Data',2)
    createHTMLfromArray(eraCustArrayDataDelta,'tape_storage_overview_delta_data_era_cust.html','Delta Week Tape Storage Overview: Era/Cust./Non-Cust. View for Data',2)
    createHTMLfromArray(eraArrayDataDelta,'tape_storage_overview_delta_data_era.html','Delta Week Tape Storage Overview: Era View for Data',1)
    createHTMLfromArray(eraArrayCustDataDelta,'tape_storage_overview_delta_cust_data_era.html','Delta Week Tape Storage Overview: Era View for Custodial Data',1)
    createHTMLfromArray(eraArrayNonCustDataDelta,'tape_storage_overview_delta_non_cust_data_era.html','Delta Week Tape Storage Overview: Era View for Non-Custodial Data',1)
    createHTMLfromArray(tierArrayDataDelta,'tape_storage_overview_delta_data_tier.html','Delta Week Tape Storage Overview: Tier View for Data',1)
    createHTMLfromArray(tierArrayCustDataDelta,'tape_storage_overview_delta_cust_data_tier.html','Delta Week Tape Storage Overview: Tier View for Custodial Data',1)
    createHTMLfromArray(tierArrayNonCustDataDelta,'tape_storage_overview_delta_non_cust_data_tier.html','Delta Week Tape Storage Overview: Tier View for Non-Custodial Data',1)

    createHTMLfromArray(detailedArrayMCDelta,'tape_storage_overview_delta_mc_detailed.html','Delta Week Tape Storage Overview: Detailed View for MC',3)
    createHTMLfromArray(eraTierArrayMCDelta,'tape_storage_overview_delta_mc_era_tier.html','Delta Week Tape Storage Overview: Era/Tier View for MC',2)
    createHTMLfromArray(eraCustArrayMCDelta,'tape_storage_overview_delta_mc_era_cust.html','Delta Week Tape Storage Overview: Era/Cust./Non-Cust. View for MC',2)
    createHTMLfromArray(eraArrayMCDelta,'tape_storage_overview_delta_mc_era.html','Delta Week Tape Storage Overview: Era View for MC',1)
    createHTMLfromArray(eraArrayCustMCDelta,'tape_storage_overview_delta_cust_mc_era.html','Delta Week Tape Storage Overview: Era View for Custodial MC',1)
    createHTMLfromArray(eraArrayNonCustMCDelta,'tape_storage_overview_delta_non_cust_mc_era.html','Delta Week Tape Storage Overview: Era View for Non-Custodial MC',1)
    createHTMLfromArray(tierArrayMCDelta,'tape_storage_overview_delta_mc_tier.html','Delta Week Tape Storage Overview: Tier View for MC',1)
    createHTMLfromArray(tierArrayCustMCDelta,'tape_storage_overview_delta_cust_mc_tier.html','Delta Week Tape Storage Overview: Tier View for Custodial MC',1)
    createHTMLfromArray(tierArrayNonCustMCDelta,'tape_storage_overview_delta_non_cust_mc_tier.html','Delta Week Tape Storage Overview: Tier View for Non-Custodial MC',1)

    overviewDictCurrent = createOverviewDict(current)
    overviewDictPrevious = createOverviewDict(previous)
    overviewDictDelta = createOverviewDict(delta)
    
    overviewArrayCurrent = createOverviewArray(overviewDictCurrent)
    overviewArrayPrevious = createOverviewArray(overviewDictPrevious)
    overviewArrayDelta = createOverviewArray(overviewDictDelta)
    
    createHTMLfromArray(overviewArrayCurrent,'tape_storage_overview_current.html','Current Week Tape Storage Overview',1)
    createHTMLfromArray(overviewArrayPrevious,'tape_storage_overview_previous.html','Previous Week Tape Storage Overview',1)
    createHTMLfromArray(overviewArrayDelta,'tape_storage_overview_delta.html','Delta between Current and Previous Week Tape Storage Overview',1)
    
    overviewArray = {}
    for site in sites:
        overviewArray[site]= createSiteOverviewArray(current,delta,site)
        createHTMLfromArray(overviewArray[site],'tape_storage_overview_'+site+'.html','Tape Storage Overview ' + site,1)
    
    createOverviewPlots(overviewDictCurrent,'Total Tape Storage Overview','total_tape_storage_overview.png')
    createOverviewPlots(overviewDictDelta,'Delta Tape Storage Overview','delta_tape_storage_overview.png')
    createOverviewPieGraphs(overviewDictCurrent,'','Custodial Tape Storage Overview','custodial_tape_storage_pie.png')
    createOverviewPieGraphs(overviewDictCurrent,'data','Custodial Data Tape Storage Overview','custodial_data_tape_storage_pie.png')
    createOverviewPieGraphs(overviewDictCurrent,'mc','Custodial MC Tape Storage Overview','custodial_mc_tape_storage_pie.png')

    createMainHTML(overviewArrayCurrent,overviewArrayDelta,'Tape Storage Overview')
    

def createDetailedDictData(input):

    result = {}

    for era in eras_data:
        if era not in result.keys():
            result[era] = {}
        for tier in tiers_data:
            if tier not in result[era].keys():
                result[era][tier] = {}
            if 'cust' not in result[era][tier].keys():
                result[era][tier]['cust'] = {}
            if 'non_cust' not in result[era][tier].keys():
                result[era][tier]['non_cust'] = {}
            for site in sites:
                value = input[site][era][tier]['data']['cust']
                result[era][tier]['cust'][site] = value
            for site in sites:
                value = input[site][era][tier]['data']['non_cust']
                result[era][tier]['non_cust'][site] = value

    print 'Created detailed dict for data'

    return result


def createEraCustDictData(input):

    result = {}

    for era in eras_data:
        if era not in result.keys():
            result[era] = {}
        if 'cust' not in result[era].keys():
            result[era]['cust'] = {}
        if 'non_cust' not in result[era].keys():
            result[era]['non_cust'] = {}
        for site in sites:
            value = 0
            for tier in tiers_data:
                value += input[site][era][tier]['data']['cust']
            result[era]['cust'][site] = value
            value = 0
            for tier in tiers_data:
                value += input[site][era][tier]['data']['non_cust']
            result[era]['non_cust'][site] = value
            
    print 'Created era/cust dict for data'

    return result

def createEraTierDictData(input):

    result = {}

    for era in eras_data:
        if era not in result.keys():
            result[era] = {}
        for tier in tiers_data:
			if tier not in result[era].keys():
				result[era][tier] = {}
			for site in sites:
				value = input[site][era][tier]['data']['cust']
				value += input[site][era][tier]['data']['non_cust']
				result[era][tier][site] = value

    print 'Created era/tier dict for data'

    return result

def createTierDictData(input):

    result = {}

    for tier in tiers_data:
		if tier not in result.keys():
			result[tier] = {}
		for site in sites:
			value = 0
			for era in eras_data:
				value += input[site][era][tier]['data']['cust']
				value += input[site][era][tier]['data']['non_cust']
			result[tier][site] = value

    print 'Created tier dict for data'

    return result

def createTierDictCustData(input):

    result = {}

    for tier in tiers_data:
		if tier not in result.keys():
			result[tier] = {}
		for site in sites:
			value = 0
			for era in eras_data:
				value += input[site][era][tier]['data']['cust']
			result[tier][site] = value

    print 'Created tier dict for cust data'

    return result

def createTierDictNonCustData(input):

    result = {}

    for tier in tiers_data:
		if tier not in result.keys():
			result[tier] = {}
		for site in sites:
			value = 0
			for era in eras_data:
				value += input[site][era][tier]['data']['non_cust']
			result[tier][site] = value

    print 'Created tier array for non-cust data'

    return result

def createEraDictData(input):

    result = {}

    for era in eras_data:
		if era not in result.keys():
			result[era] = {}
		for site in sites:
			value = 0
			for tier in tiers_data:
				value += input[site][era][tier]['data']['cust']
				value += input[site][era][tier]['data']['non_cust']
			result[era][site] = value

    print 'Created era dict for data'

    return result

def createEraDictCustData(input):

    result = {}

    for era in eras_data:
		if era not in result.keys():
			result[era] = {}
		for site in sites:
			value = 0
			for tier in tiers_data:
				value += input[site][era][tier]['data']['cust']
			result[era][site] = value

    print 'Created era dict for cust data'

    return result

def createEraDictNonCustData(input):

    result = {}

    for era in eras_data:
		if era not in result.keys():
			result[era] = {}
		for site in sites:
			value = 0
			for tier in tiers_data:
				value += input[site][era][tier]['data']['non_cust']
			result[era][site] = value

    print 'Created era dict for non-cust data'

    return result

def createDetailedArrayData(input):

    result = []

    line = []
    line.append('Acquisition era')
    line.append('Data Tier')
    line.append('Cust./Non-Cust.')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for era in eras_data:
        for tier in tiers_data:
            line = []
            line.append(era)
            line.append(tier)
            line.append('custodial')
            local_total = 0
            for site in sites:
                value = input[era][tier]['cust'][site]
                line.append("%.3f" % value)
                local_total += value
                total[site] += value
            line.append("%.3f" % local_total)
            result.append(line)
            line = []
            line.append(era)
            line.append(tier)
            line.append('non-custodial')
            local_total = 0
            for site in sites:
                value = input[era][tier]['non_cust'][site]
                line.append("%.3f" % value)
                local_total += value
                total[site] += value
            line.append("%.3f" % local_total)
            result.append(line)
    line = []
    line.append('Total')
    line.append('')
    line.append('')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created detailed array for data'

    return result

def createEraCustArrayData(input):

    result = []

    line = []
    line.append('Acquisition era')
    line.append('Cust./Non-Cust.')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for era in eras_data:
        line = []
        line.append(era)
        line.append('custodial')
        local_total = 0
        for site in sites:
            value = input[era]['cust'][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
        line = []
        line.append(era)
        line.append('non-custodial')
        local_total = 0
        for site in sites:
            value = input[era]['non_cust'][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
    line = []
    line.append('Total')
    line.append('')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created era/cust array for data'

    return result

def createEraTierArrayData(input):

    result = []

    line = []
    line.append('Acquisition era')
    line.append('Data Tier')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for era in eras_data:
        for tier in tiers_data:
            line = []
            line.append(era)
            line.append(tier)
            local_total = 0
            for site in sites:
                value = input[era][tier][site]
                line.append("%.3f" % value)
                local_total += value
                total[site] += value
            line.append("%.3f" % local_total)
            result.append(line)
    line = []
    line.append('Total')
    line.append('')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created era/tier array for data'

    return result

def createTierArrayData(input):

	result = []

	line = []
	line.append('Data Tier')
	for site in sites:
		line.append(site+' [TB]')
	line.append('All sites [TB]')
	result.append(line)
	total = {}
	for site in sites:
		total[site] = 0
	for tier in tiers_data:
		line = []
		line.append(tier)
		local_total = 0
		for site in sites:
			value = input[tier][site]
			line.append("%.3f" % value)
			local_total += value
			total[site] += value
		line.append("%.3f" % local_total)
		result.append(line)
	line = []
	line.append('Total')
	local_total = 0
	for site in sites:
		line.append("%.3f" % total[site])
		local_total += total[site]
	line.append("%.3f" % local_total)
	result.append(line)

	print 'Created tier array for data'

	return result

def createTierArrayCustData(input):

    result = []

    line = []
    line.append('Data Tier')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for tier in tiers_data:
        line = []
        line.append(tier)
        local_total = 0
        for site in sites:
            value = input[tier][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
    line = []
    line.append('Total')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created tier array for cust data'

    return result

def createTierArrayNonCustData(input):

    result = []

    line = []
    line.append('Data Tier')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for tier in tiers_data:
        line = []
        line.append(tier)
        local_total = 0
        for site in sites:
            value = input[tier][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
    line = []
    line.append('Total')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created tier array for non-cust data'

    return result

def createEraArrayData(input):

    result = []

    line = []
    line.append('Acquisition era')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for era in eras_data:
        line = []
        line.append(era)
        local_total = 0
        for site in sites:
            value = input[era][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
    line = []
    line.append('Total')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created era array for data'

    return result

def createEraArrayCustData(input):

    result = []

    line = []
    line.append('Acquisition era')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for era in eras_data:
        line = []
        line.append(era)
        local_total = 0
        for site in sites:
            value = input[era][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
    line = []
    line.append('Total')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created era array for cust data'

    return result

def createEraArrayNonCustData(input):

    result = []

    line = []
    line.append('Acquisition era')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for era in eras_data:
        line = []
        line.append(era)
        local_total = 0
        for site in sites:
            value = input[era][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
    line = []
    line.append('Total')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created era array for non-cust data'

    return result

def createDetailedDictMC(input):

    result = {}

    for era in eras_mc:
        if era not in result.keys():
            result[era] = {}
        for tier in tiers_mc:
            if tier not in result[era].keys():
                result[era][tier] = {}
            if 'cust' not in result[era][tier].keys():
                result[era][tier]['cust'] = {}
            if 'non_cust' not in result[era][tier].keys():
                result[era][tier]['non_cust'] = {}
            for site in sites:
                value = input[site][era][tier]['mc']['cust']
                result[era][tier]['cust'][site] = value
            for site in sites:
                value = input[site][era][tier]['mc']['non_cust']
                result[era][tier]['non_cust'][site] = value

    print 'Created detailed dict for mc'

    return result


def createEraCustDictMC(input):

    result = {}

    for era in eras_mc:
        if era not in result.keys():
            result[era] = {}
        if 'cust' not in result[era].keys():
            result[era]['cust'] = {}
        if 'non_cust' not in result[era].keys():
            result[era]['non_cust'] = {}
        for site in sites:
            value = 0
            for tier in tiers_mc:
                value += input[site][era][tier]['mc']['cust']
            result[era]['cust'][site] = value
            value = 0
            for tier in tiers_mc:
                value += input[site][era][tier]['mc']['non_cust']
            result[era]['non_cust'][site] = value
            
    print 'Created era/cust dict for mc'

    return result

def createEraTierDictMC(input):

    result = {}

    for era in eras_mc:
        if era not in result.keys():
            result[era] = {}
        for tier in tiers_mc:
			if tier not in result[era].keys():
				result[era][tier] = {}
			for site in sites:
				value = input[site][era][tier]['mc']['cust']
				value += input[site][era][tier]['mc']['non_cust']
				result[era][tier][site] = value

    print 'Created era/tier dict for mc'

    return result

def createTierDictMC(input):

    result = {}

    for tier in tiers_mc:
		if tier not in result.keys():
			result[tier] = {}
		for site in sites:
			value = 0
			for era in eras_mc:
				value += input[site][era][tier]['mc']['cust']
				value += input[site][era][tier]['mc']['non_cust']
			result[tier][site] = value

    print 'Created tier dict for mc'

    return result

def createTierDictCustMC(input):

    result = {}

    for tier in tiers_mc:
		if tier not in result.keys():
			result[tier] = {}
		for site in sites:
			value = 0
			for era in eras_mc:
				value += input[site][era][tier]['mc']['cust']
			result[tier][site] = value

    print 'Created tier dict for cust mc'

    return result

def createTierDictNonCustMC(input):

    result = {}

    for tier in tiers_mc:
		if tier not in result.keys():
			result[tier] = {}
		for site in sites:
			value = 0
			for era in eras_mc:
				value += input[site][era][tier]['mc']['non_cust']
			result[tier][site] = value

    print 'Created tier array for non-cust mc'

    return result

def createEraDictMC(input):

    result = {}

    for era in eras_mc:
		if era not in result.keys():
			result[era] = {}
		for site in sites:
			value = 0
			for tier in tiers_mc:
				value += input[site][era][tier]['mc']['cust']
				value += input[site][era][tier]['mc']['non_cust']
			result[era][site] = value

    print 'Created era dict for mc'

    return result

def createEraDictCustMC(input):

    result = {}

    for era in eras_mc:
		if era not in result.keys():
			result[era] = {}
		for site in sites:
			value = 0
			for tier in tiers_mc:
				value += input[site][era][tier]['mc']['cust']
			result[era][site] = value

    print 'Created era dict for cust mc'

    return result

def createEraDictNonCustMC(input):

    result = {}

    for era in eras_mc:
		if era not in result.keys():
			result[era] = {}
		for site in sites:
			value = 0
			for tier in tiers_mc:
				value += input[site][era][tier]['mc']['cust']
			result[era][site] = value

    print 'Created era dict for non-cust mc'

    return result

def createDetailedArrayMC(input):

    result = []

    line = []
    line.append('Acquisition era')
    line.append('MC Tier')
    line.append('Cust./Non-Cust.')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for era in eras_mc:
        for tier in tiers_mc:
            line = []
            line.append(era)
            line.append(tier)
            line.append('custodial')
            local_total = 0
            for site in sites:
                value = input[era][tier]['cust'][site]
                line.append("%.3f" % value)
                local_total += value
                total[site] += value
            line.append("%.3f" % local_total)
            result.append(line)
            line = []
            line.append(era)
            line.append(tier)
            line.append('non-custodial')
            local_total = 0
            for site in sites:
                value = input[era][tier]['non_cust'][site]
                line.append("%.3f" % value)
                local_total += value
                total[site] += value
            line.append("%.3f" % local_total)
            result.append(line)
    line = []
    line.append('Total')
    line.append('')
    line.append('')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created detailed array for mc'

    return result

def createEraCustArrayMC(input):

    result = []

    line = []
    line.append('Acquisition era')
    line.append('Cust./Non-Cust.')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for era in eras_mc:
        line = []
        line.append(era)
        line.append('custodial')
        local_total = 0
        for site in sites:
            value = input[era]['cust'][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
        line = []
        line.append(era)
        line.append('non-custodial')
        local_total = 0
        for site in sites:
            value = input[era]['non_cust'][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
    line = []
    line.append('Total')
    line.append('')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created era/cust array for mc'

    return result

def createEraTierArrayMC(input):

    result = []

    line = []
    line.append('Acquisition era')
    line.append('MC Tier')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for era in eras_mc:
        for tier in tiers_mc:
            line = []
            line.append(era)
            line.append(tier)
            local_total = 0
            for site in sites:
                value = input[era][tier][site]
                line.append("%.3f" % value)
                local_total += value
                total[site] += value
            line.append("%.3f" % local_total)
            result.append(line)
    line = []
    line.append('Total')
    line.append('')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created era/tier array for mc'

    return result

def createTierArrayMC(input):

	result = []

	line = []
	line.append('MC Tier')
	for site in sites:
		line.append(site+' [TB]')
	line.append('All sites [TB]')
	result.append(line)
	total = {}
	for site in sites:
		total[site] = 0
	for tier in tiers_mc:
		line = []
		line.append(tier)
		local_total = 0
		for site in sites:
			value = input[tier][site]
			line.append("%.3f" % value)
			local_total += value
			total[site] += value
		line.append("%.3f" % local_total)
		result.append(line)
	line = []
	line.append('Total')
	local_total = 0
	for site in sites:
		line.append("%.3f" % total[site])
		local_total += total[site]
	line.append("%.3f" % local_total)
	result.append(line)

	print 'Created tier array for mc'

	return result

def createTierArrayCustMC(input):

    result = []

    line = []
    line.append('MC Tier')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for tier in tiers_mc:
        line = []
        line.append(tier)
        local_total = 0
        for site in sites:
            value = input[tier][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
    line = []
    line.append('Total')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created tier array for cust mc'

    return result

def createTierArrayNonCustMC(input):

    result = []

    line = []
    line.append('MC Tier')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for tier in tiers_mc:
        line = []
        line.append(tier)
        local_total = 0
        for site in sites:
            value = input[tier][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
    line = []
    line.append('Total')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created tier array for non-cust mc'

    return result

def createEraArrayMC(input):

    result = []

    line = []
    line.append('Acquisition era')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for era in eras_mc:
        line = []
        line.append(era)
        local_total = 0
        for site in sites:
            value = input[era][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
    line = []
    line.append('Total')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created era array for mc'

    return result

def createEraArrayCustMC(input):

    result = []

    line = []
    line.append('Acquisition era')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for era in eras_mc:
        line = []
        line.append(era)
        local_total = 0
        for site in sites:
            value = input[era][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
    line = []
    line.append('Total')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created era array for cust mc'

    return result

def createEraArrayNonCustMC(input):

    result = []

    line = []
    line.append('Acquisition era')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    for era in eras_mc:
        line = []
        line.append(era)
        local_total = 0
        for site in sites:
            value = input[era][site]
            line.append("%.3f" % value)
            local_total += value
            total[site] += value
        line.append("%.3f" % local_total)
        result.append(line)
    line = []
    line.append('Total')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created era array for non-cust mc'

    return result

def createOverviewDict(input):

    result = {}
    result['data'] = {}
    result['data']['cust'] = {}
    result['data']['non_cust'] = {}
    result['mc'] = {}
    result['mc']['cust'] = {}
    result['mc']['non_cust'] = {}

    for site in sites:
        data_cust_value = 0
        data_non_cust_value = 0
        for era in eras_data:
            for tier in tiers_data:
                data_cust_value += input[site][era][tier]['data']['cust']
                data_non_cust_value += input[site][era][tier]['data']['non_cust']
        result['data']['cust'][site] = data_cust_value
        result['data']['non_cust'][site] = data_non_cust_value

    for site in sites:
        mc_cust_value = 0
        mc_non_cust_value = 0
        for era in eras_mc:
            for tier in tiers_mc:
                mc_cust_value += input[site][era][tier]['mc']['cust']
                mc_non_cust_value += input[site][era][tier]['mc']['non_cust']
        result['mc']['cust'][site] = mc_cust_value
        result['mc']['non_cust'][site] = mc_non_cust_value

    print 'Created overview dict'

    return result

def createOverviewArray(input):

    result = []

    line = []
    line.append('')
    for site in sites:
        line.append(site+' [TB]')
    line.append('All sites [TB]')
    result.append(line)
    total = {}
    for site in sites:
        total[site] = 0
    line = []
    line.append('custodial data')
    local_total = 0
    for site in sites:
        value = input['data']['cust'][site]
        line.append("%.3f" % value)
        local_total += value
        total[site] += value
    line.append("%.3f" % local_total)
    result.append(line)
    line = []
    line.append('non-custodial data')
    local_total = 0
    for site in sites:
        value = input['data']['non_cust'][site]
        line.append("%.3f" % value)
        local_total += value
        total[site] += value
    line.append("%.3f" % local_total)
    result.append(line)
    line = []
    line.append('custodial mc')
    local_total = 0
    for site in sites:
        value = input['mc']['cust'][site]
        line.append("%.3f" % value)
        local_total += value
        total[site] += value
    line.append("%.3f" % local_total)
    result.append(line)
    line = []
    line.append('non-custodial mc')
    local_total = 0
    for site in sites:
        value = input['mc']['non_cust'][site]
        line.append("%.3f" % value)
        local_total += value
        total[site] += value
    line.append("%.3f" % local_total)
    result.append(line)
    line = []
    line.append('custodial')
    local_total = 0
    for site in sites:
        value = input['data']['cust'][site]
        value += input['mc']['cust'][site]
        line.append("%.3f" % value)
        local_total += value
    line.append("%.3f" % local_total)
    result.append(line)
    line = []
    line.append('non-custodial')
    local_total = 0
    for site in sites:
        value = input['data']['non_cust'][site]
        value += input['mc']['non_cust'][site]
        line.append("%.3f" % value)
        local_total += value
    line.append("%.3f" % local_total)
    result.append(line)
    line = []
    line.append('Total')
    local_total = 0
    for site in sites:
        line.append("%.3f" % total[site])
        local_total += total[site]
    line.append("%.3f" % local_total)
    result.append(line)

    print 'Created overview array'

    return result

def createSiteOverviewArray(currentInput,deltaInput,site):

    result = []

    line = []
    line.append('Overview for: ' + site)
    line.append('Custodial Delta [TB]')
    line.append('Custodial Total [TB]')
    line.append('Non-Custodial Delta [TB]')
    line.append('Non-Custodial Total [TB]')
    line.append('Total Delta [TB]')
    line.append('Total Total [TB]')
    result.append(line)

    data_delta_total = 0
    data_total_total = 0
    mc_delta_total   = 0
    mc_total_total   = 0
    delta_total   = 0
    total_total   = 0

    line = []
    line.append('Data')
    value = 0
    for era in eras_data:
        for tier in tiers_data:
            value += deltaInput[site][era][tier]['data']['cust']
    line.append("%.3f" % value)
    data_delta_total += value
    value = 0
    for era in eras_data:
        for tier in tiers_data:
            value += currentInput[site][era][tier]['data']['cust']
    line.append("%.3f" % value)
    data_total_total += value
    value = 0
    for era in eras_data:
        for tier in tiers_data:
            value += deltaInput[site][era][tier]['data']['non_cust']
    line.append("%.3f" % value)
    data_delta_total += value
    value = 0
    for era in eras_data:
        for tier in tiers_data:
            value += currentInput[site][era][tier]['data']['non_cust']
    line.append("%.3f" % value)
    data_total_total += value
    line.append("%.3f" % data_delta_total)
    line.append("%.3f" % data_total_total)
    result.append(line)

    line = []
    line.append('MC')
    value = 0
    for era in eras_mc:
        for tier in tiers_mc:
            value += deltaInput[site][era][tier]['mc']['cust']
    line.append("%.3f" % value)
    mc_delta_total += value
    value = 0
    for era in eras_mc:
        for tier in tiers_mc:
            value += currentInput[site][era][tier]['mc']['cust']
    line.append("%.3f" % value)
    mc_total_total += value
    value = 0
    for era in eras_mc:
        for tier in tiers_mc:
            value += deltaInput[site][era][tier]['mc']['non_cust']
    line.append("%.3f" % value)
    mc_delta_total += value
    value = 0
    for era in eras_mc:
        for tier in tiers_mc:
            value += currentInput[site][era][tier]['mc']['non_cust']
    line.append("%.3f" % value)
    mc_total_total += value
    line.append("%.3f" % mc_delta_total)
    line.append("%.3f" % mc_total_total)
    result.append(line)

    line = []
    line.append('Total')
    value = 0
    for era in eras_data:
        for tier in tiers_data:
            value += deltaInput[site][era][tier]['data']['cust']
    for era in eras_mc:
        for tier in tiers_mc:
            value += deltaInput[site][era][tier]['mc']['cust']
    line.append("%.3f" % value)
    delta_total += value
    value = 0
    for era in eras_data:
        for tier in tiers_data:
            value += currentInput[site][era][tier]['data']['cust']
    for era in eras_mc:
        for tier in tiers_mc:
            value += currentInput[site][era][tier]['mc']['cust']
    line.append("%.3f" % value)
    total_total += value
    value = 0
    for era in eras_data:
        for tier in tiers_data:
            value += deltaInput[site][era][tier]['data']['non_cust']
    for era in eras_mc:
        for tier in tiers_mc:
            value += deltaInput[site][era][tier]['mc']['non_cust']
    line.append("%.3f" % value)
    delta_total += value
    value = 0
    for era in eras_data:
        for tier in tiers_data:
            value += currentInput[site][era][tier]['data']['non_cust']
    for era in eras_mc:
        for tier in tiers_mc:
            value += currentInput[site][era][tier]['mc']['non_cust']
    line.append("%.3f" % value)
    total_total += value
    line.append("%.3f" % delta_total)
    line.append("%.3f" % total_total)
    result.append(line)

    print 'Created overview array for site',site

    return result

def parseFile(filename):
    #
    # create structure from file from Si's TMDB query script
    #
    # era 
    #   |-> tier
    #          |-> data/mc
    #                    |-> cust/non_cust

    localfile = open(filename)

    result = {}
    counter = 0
    for line in localfile.readlines() :
        array = line.split(',')
        if len(array) != 8 :
            continue
        if array[0].count('Acquisition') > 0 :
            continue
        counter += 1
        era = array[0].strip()
        tier = array[1].strip()
        tier = tier.replace('GEN-SIM_RAWDEBUG','GEN-SIM-RAWDEBUG')
        tier = tier.replace('GEN-SIM_RECODEBUG','GEN-SIM-RECODEBUG')
        cust_data = float(array[3])
        non_cust_data = float(array[4])
        cust_mc = float(array[6])
        non_cust_mc = float(array[7])
        if era not in result.keys():
            result[era] = {}
        if tier not in result[era].keys():
            result[era][tier] = {}
        if 'data' not in result[era][tier].keys():
            result[era][tier]['data'] = {}
        if 'mc' not in result[era][tier].keys():
            result[era][tier]['mc'] = {}
        result[era][tier]['data']['cust'] = cust_data
        result[era][tier]['data']['non_cust'] = non_cust_data
        result[era][tier]['mc']['cust'] = cust_mc
        result[era][tier]['mc']['non_cust'] = non_cust_mc

    print 'Parsed',counter,'lines from',filename

    return result

def subtract(current,previous):
    delta = {}
    for site in current.keys() :
        if site not in delta.keys():
            delta[site] = {}
        for era in current[site].keys() :
            if era not in delta[site].keys():
                delta[site][era] = {}
            for tier in current[site][era].keys():
                if tier not in delta[site][era].keys():
                    delta[site][era][tier] = {}
                for item in current[site][era][tier].keys():
                    if item not in delta[site][era][tier].keys():
                        delta[site][era][tier][item] = {}
                    for cust in current[site][era][tier][item]:
                        # if site not in previous.keys() or era not in previous[site].keys() or tier not in previous[site][era].keys() or item not in previous[site][era][tier].keys() or cust not in previous[site][era][tier][item].keys() :
                        #     delta[site][era][tier][item][cust] = current[site][era][tier][item][cust]
                        # else :
                        delta[site][era][tier][item][cust] = current[site][era][tier][item][cust] - previous[site][era][tier][item][cust]

    print 'Calculated delta between current and previous.'

    return delta

def checkCategories(input):
    """
    check if list of data tiers and acquisition eras are still valid or if we have additional entries
    """

    new_tiers = []
    new_eras = []

    for site in input.keys():
        for era in input[site].keys():
            if era not in eras_data and era not in eras_mc:
                if era not in new_eras and era not in ignore_eras:
                    new_eras.append(era)
            for tier in input[site][era].keys():
                if tier not in tiers_data and tier not in tiers_mc:
                    if tier not in new_tiers and tier not in ignore_tiers:
                        new_tiers.append(tier)

    if len(new_tiers) > 0:
        print 'New tiers:',','.join(new_tiers)
    if len(new_eras) > 0:
        print 'New eras:',','.join(new_eras)
    if len(new_tiers) > 0 or len(new_eras) > 0:
        sys.exit(1)

    print 'No new eras or data tiers found during parsing.'

def createHTMLfromArray(array,filename,title,numberOfDescColumn):

    localfile = open(filename,'w')

    localfile.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"')
    localfile.write('"http://www.w3.org/TR/html4/strict.dtd">')

    localfile.write('<html lang="en">')
    localfile.write('<head>')
    localfile.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
    localfile.write('<title>'+title+'</title>')
    localfile.write('<meta name="author" content="Oliver Gutsche">')
    localfile.write('<!-- Date: '+date+' -->')
    localfile.write('</head>')
    localfile.write('<body>')
    localfile.write('<h1>'+title+'</h1>')


    localfile.write(createHTMLTablefromArray(array,numberOfDescColumn))

    localfile.write('<hr>')
    localfile.write(fulldate)

    localfile.write('</body>')
    localfile.write('</html>')

    localfile.close()

    print 'Created html file:',filename,'with title:',title



def createHTMLTablefromArray(array,numberOfDescColumn):

    result = ""

    result += '<table border="1" cellspacing="0" cellpadding="2">\n'
    result += '<tr>\n'
    for cell in array[0]:
        result += '<th>'+cell+'</th>'
    result += '</tr>\n'
    for line in array[1:]:
        result += '<tr>'
        for cell in line[:numberOfDescColumn]:
            result += '<td>'+cell+'</td>'
        for cell in line[numberOfDescColumn:]:
            result += '<td align="right">'+cell+'</td>'
        result += '</tr>\n'
    result += '</table>\n'

    return result
    
def calculateStackOffsets(previous,current,positive,negative):
    result = []
    for item in range(len(current)):
        result.append(0)

    for item in range(len(previous)):
        if previous[item] < 0:
            negative[item] = negative[item] + previous[item]
        else :
            positive[item] = positive[item] + previous[item]
        if current[item] < 0:
            result[item] = negative[item]
        else :
            result[item] = positive[item]

    return (result,positive,negative)

def createHorizontalStackedBarPlot(filename,title,labels,legends,data) :

    plt.figure(figsize=(16,6),dpi=300)

    N = len(labels)
    ind = np.arange(N)+.5 
    width = 0.5

    plots = []
    left_edge = []
    left_edge_negative = []
    left_edge_positive = []
    for index in range(N):
        left_edge.append(0.)
        left_edge_negative.append(0.)
        left_edge_positive.append(0.)
    plots.append(plt.barh(ind, data[0], width, color=colors[0], align='center', left=left_edge))
    for index in range(len(legends)-1):
        (left_edge,left_edge_positive,left_edge_negative) = calculateStackOffsets(data[index],data[index+1],left_edge_positive,left_edge_negative)
        plots.append(plt.barh(ind, data[index+1], width, color=colors[index+1], align='center', left=left_edge))

    fontsize = 20
    plt.title(title,fontsize=fontsize)
    plt.yticks(ind, labels)
    plt.xlabel('TB',fontsize=fontsize)
    plt.legend( [ plot[0] for plot in plots], legends, loc='center left', bbox_to_anchor=(1.05, .5) )
    plt.grid(True)
    ax = plt.gca()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(fontsize)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(fontsize)
    leg = ax.get_legend()
    ltext  = leg.get_texts()
    plt.setp(ltext, fontsize=fontsize)

    plt.subplots_adjust(left=.2,right=0.75)

    plt.savefig(filename,format='png')
    plt.close()

def createOverviewPlots(input,title,filename):
    """
    types = [
    'custodial data',
    'non-custodial data',
    'custodial MC',
    'non-custodial MC'
    ]
    """



    # data1[sites][types]
    data1 = []
    for site in sites:
        data1.append([
        input['data']['cust'][site],
        input['data']['non_cust'][site],
        input['mc']['cust'][site],
        input['mc']['non_cust'][site],
        ])

    createHorizontalStackedBarPlot(filename.replace('.png','_by_type.png'),title,types,sites,data1)

    # data1[sites][types]
    data2 = []
    tmp = []
    for site in sites:
        tmp.append(input['data']['cust'][site])
    data2.append(tmp)
    tmp = []
    for site in sites:
        tmp.append(input['data']['non_cust'][site])
    data2.append(tmp)
    tmp = []
    for site in sites:
        tmp.append(input['mc']['cust'][site])
    data2.append(tmp)
    tmp = []
    for site in sites:
        tmp.append(input['mc']['non_cust'][site])
    data2.append(tmp)
    
    createHorizontalStackedBarPlot(filename.replace('.png','_by_site.png'),title,sites,types,data2)

    print 'Created overview plots'

def createOverviewPieGraphs(input,mode,title,filename):
    plt.figure(figsize=(10,7.5), dpi=300)
    plt.axes([0.15, 0., 0.7, 0.933])

    data = []
    for site in sites:
        if mode == 'data' :
            data.append(input['data']['cust'][site])
        elif mode == 'mc' :
            data.append(input['mc']['cust'][site])
        else :
            data.append(input['data']['cust'][site]+input['mc']['cust'][site])

    fontsize = 25
    myPie = plt.pie(data, labels=sites, autopct='%1.f%%', shadow=False, colors=colors)
    for x in myPie[2]:
        x.set_color('w')
        x.set_fontsize(fontsize)
    for x in myPie[1]:
        x.set_fontsize(fontsize-5)
    plt.title(title, fontsize=fontsize+5)
    plt.savefig(filename,format='png')
    plt.close()

    print 'Created overview pie plot'

def createMainHTML(totalArray,deltaArray,title):

    localfile = open('main.html','w')

    localfile.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"')
    localfile.write('"http://www.w3.org/TR/html4/strict.dtd">')

    localfile.write('<html lang="en">')
    localfile.write('<head>')
    localfile.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">')
    localfile.write('<title>'+title+'</title>')
    localfile.write('<meta name="author" content="Oliver Gutsche">')
    localfile.write('<!-- Date: '+date+' -->')
    localfile.write('</head>')
    localfile.write('<body>')
    localfile.write('<h1>'+title+'</h1>')

    localfile.write('<h2>Current week Overview</h2>')
    localfile.write('<a href=\"total_tape_storage_overview_by_site.png\" target=\"_blank\"><img src=\"total_tape_storage_overview_by_site.png\" height=\"200\"><a><a href=\"total_tape_storage_overview_by_type.png\" target=\"_blank\"><img src=\"total_tape_storage_overview_by_type.png\" height=\"200\"><a><br>')
    localfile.write(createHTMLTablefromArray(totalArray,1))
    localfile.write('<h2>Delta between Current and Previous week Overview</h2>')
    localfile.write('<a href=\"delta_tape_storage_overview_by_site.png\" target=\"_blank\"><img src=\"delta_tape_storage_overview_by_site.png\" height=\"200\"><a><a href=\"delta_tape_storage_overview_by_type.png\" target=\"_blank\"><img src=\"delta_tape_storage_overview_by_type.png\" height=\"200\"><a><br>')
    localfile.write(createHTMLTablefromArray(deltaArray,1))
    pie_size = 250
    localfile.write('<br><a href=\"custodial_tape_storage_pie.png\" target=\"_blank\"><img src=\"custodial_tape_storage_pie.png\" height=\"'+str(pie_size)+'\"><a><a href=\"custodial_data_tape_storage_pie.png\" target=\"_blank\"><img src=\"custodial_data_tape_storage_pie.png\" height=\"'+str(pie_size)+'\"><a><a href=\"custodial_mc_tape_storage_pie.png\" target=\"_blank\"><img src=\"custodial_mc_tape_storage_pie.png\" height=\"'+str(pie_size)+'\"><a><br>')


    localfile.write('<h2>Tables</h2>')
    localfile.write('<table border="1" cellspacing="0" cellpadding="2">')
    localfile.write('<tr>')
    localfile.write('<th>Description</th>')
    localfile.write('<th>Tables</th>')
    localfile.write('</tr>')

    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview</td>')
    localfile.write('<td><a href="tape_storage_overview_current.html">Current week</a>, <a href="tape_storage_overview_previous.html">Previous week</a>, <a href="tape_storage_overview_delta.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')

    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview per site</td>')
    column = ""
    for site in sites:
        column = column + '<a href="tape_storage_overview_'+site+'.html">' + site + '</a> '
    localfile.write('<td>' + column + '</td>')
    localfile.write('</tr>')

    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Detailed View for Data</td>')
    localfile.write('<td><a href="tape_storage_overview_current_data_detailed.html">Current week</a>, <a href="tape_storage_overview_previous_data_detailed.html">Previous week</a>, <a href="tape_storage_overview_delta_data_detailed.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Era/Tier View for Data</td>')
    localfile.write('<td><a href="tape_storage_overview_current_data_era_tier.html">Current week</a>, <a href="tape_storage_overview_previous_data_era_tier.html">Previous week</a>, <a href="tape_storage_overview_delta_data_era_tier.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Era/Cust./Non-Cust. View for Data</td>')
    localfile.write('<td><a href="tape_storage_overview_current_data_era_cust.html">Current week</a>, <a href="tape_storage_overview_previous_data_era_cust.html">Previous week</a>, <a href="tape_storage_overview_delta_data_era_cust.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Era View for Data</td>')
    localfile.write('<td><a href="tape_storage_overview_current_data_era.html">Current week</a>, <a href="tape_storage_overview_previous_data_era.html">Previous week</a>, <a href="tape_storage_overview_delta_data_era.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Era View for Custodial Data</td>')
    localfile.write('<td><a href="tape_storage_overview_current_cust_data_era.html">Current week</a>, <a href="tape_storage_overview_previous_cust_data_era.html">Previous week</a>, <a href="tape_storage_overview_delta_cust_data_era.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Era View for Non-Custodial Data</td>')
    localfile.write('<td><a href="tape_storage_overview_current_non_cust_data_era.html">Current week</a>, <a href="tape_storage_overview_previous_non_cust_data_era.html">Previous week</a>, <a href="tape_storage_overview_delta_non_cust_data_era.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Tier View for Data</td>')
    localfile.write('<td><a href="tape_storage_overview_current_data_tier.html">Current week</a>, <a href="tape_storage_overview_previous_data_tier.html">Previous week</a>, <a href="tape_storage_overview_delta_data_tier.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Tier View for Custodial Data</td>')
    localfile.write('<td><a href="tape_storage_overview_current_cust_data_tier.html">Current week</a>, <a href="tape_storage_overview_previous_cust_data_tier.html">Previous week</a>, <a href="tape_storage_overview_delta_cust_data_tier.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Tier View for Non-Custodial Data</td>')
    localfile.write('<td><a href="tape_storage_overview_current_non_cust_data_tier.html">Current week</a>, <a href="tape_storage_overview_previous_non_cust_data_tier.html">Previous week</a>, <a href="tape_storage_overview_delta_non_cust_data_tier.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Detailed View for MC</td>')
    localfile.write('<td><a href="tape_storage_overview_current_mc_detailed.html">Current week</a>, <a href="tape_storage_overview_previous_mc_detailed.html">Previous week</a>, <a href="tape_storage_overview_delta_mc_detailed.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Era/Tier View for MC</td>')
    localfile.write('<td><a href="tape_storage_overview_current_mc_era_tier.html">Current week</a>, <a href="tape_storage_overview_previous_mc_era_tier.html">Previous week</a>, <a href="tape_storage_overview_delta_mc_era_tier.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Era/Cust./Non-Cust. View for MC</td>')
    localfile.write('<td><a href="tape_storage_overview_current_mc_era_cust.html">Current week</a>, <a href="tape_storage_overview_previous_mc_era_cust.html">Previous week</a>, <a href="tape_storage_overview_delta_mc_era_cust.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Era View for MC</td>')
    localfile.write('<td><a href="tape_storage_overview_current_mc_era.html">Current week</a>, <a href="tape_storage_overview_previous_mc_era.html">Previous week</a>, <a href="tape_storage_overview_delta_mc_era.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Era View for Custodial MC</td>')
    localfile.write('<td><a href="tape_storage_overview_current_cust_mc_era.html">Current week</a>, <a href="tape_storage_overview_previous_cust_mc_era.html">Previous week</a>, <a href="tape_storage_overview_delta_cust_mc_era.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Era View for Non-Custodial MC</td>')
    localfile.write('<td><a href="tape_storage_overview_current_non_cust_mc_era.html">Current week</a>, <a href="tape_storage_overview_previous_non_cust_mc_era.html">Previous week</a>, <a href="tape_storage_overview_delta_non_cust_mc_era.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Tier View for MC</td>')
    localfile.write('<td><a href="tape_storage_overview_current_mc_tier.html">Current week</a>, <a href="tape_storage_overview_previous_mc_tier.html">Previous week</a>, <a href="tape_storage_overview_delta_mc_tier.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Tier View for Custodial MC</td>')
    localfile.write('<td><a href="tape_storage_overview_current_cust_mc_tier.html">Current week</a>, <a href="tape_storage_overview_previous_cust_mc_tier.html">Previous week</a>, <a href="tape_storage_overview_delta_cust_mc_tier.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')
    localfile.write('<tr>')
    localfile.write('<td>Tape Storage Overview: Tier View for Non-Custodial MC</td>')
    localfile.write('<td><a href="tape_storage_overview_current_non_cust_mc_tier.html">Current week</a>, <a href="tape_storage_overview_previous_non_cust_mc_tier.html">Previous week</a>, <a href="tape_storage_overview_delta_non_cust_mc_tier.html">Delta between Current and Previous week</a></td>')
    localfile.write('</tr>')

    localfile.write('<tr>')
    localfile.write('<td></td>')
    localfile.write('<td><a href</td>')
    localfile.write('</tr>')

    localfile.write('</table>')

    localfile.write('<hr>')
    localfile.write(fulldate)

    localfile.write('</body>')
    localfile.write('</html>')

    localfile.close()

    print 'Created html file: main.html with title:',title
    
def completeCategories(input):
    local_eras = []
    local_eras.extend(eras_data)
    local_eras.extend(eras_mc)
    local_eras.extend(ignore_eras)
    local_tiers = []
    local_tiers.extend(tiers_data)
    local_tiers.extend(tiers_mc)
    local_tiers.extend(ignore_tiers)
    
    for site in input.keys():
        for era in local_eras:
            if era not in input[site].keys():
                input[site][era] = {}
            for tier in local_tiers:
                if tier not in input[site][era].keys():
                    input[site][era][tier] = {}
                if 'data' not in input[site][era][tier].keys():
                    input[site][era][tier]['data'] = {}
                if 'mc' not in input[site][era][tier].keys():
                    input[site][era][tier]['mc'] = {}
                if 'cust' not in input[site][era][tier]['data'].keys():
                    input[site][era][tier]['data']['cust'] = 0
                if 'non_cust' not in input[site][era][tier]['data'].keys():
                    input[site][era][tier]['data']['non_cust'] = 0
                if 'cust' not in input[site][era][tier]['mc'].keys():
                    input[site][era][tier]['mc']['cust'] = 0
                if 'non_cust' not in input[site][era][tier]['mc'].keys():
                    input[site][era][tier]['mc']['non_cust'] = 0
    
if __name__ == '__main__' :
    main(sys.argv[1:])
