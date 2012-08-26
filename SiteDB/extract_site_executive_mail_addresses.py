#!/usr/bin/env python2.4

import json
import urllib2,urllib, httplib, sys, re, os

def fetch(url,api):
	conn  =  httplib.HTTPSConnection(url, cert_file = os.getenv('X509_USER_PROXY'), key_file = os.getenv('X509_USER_PROXY'))
	r1=conn.request("GET",api, None, {"Accept": "application/json"})
	r2=conn.getresponse()
	result = json.loads(r2.read())
	return result
	
jr = fetch('cmsweb.cern.ch','/sitedb/data/prod/site-responsibilities')
jn = fetch('cmsweb.cern.ch','/sitedb/data/prod/site-names')
jp = fetch('cmsweb.cern.ch','/sitedb/data/prod/people')

sites = {}
sites ['T2_AT_Vienna'] = []
sites ['T2_BE_IIHE'] = []
sites ['T2_BE_UCL'] = []
sites ['T2_BR_SPRACE'] = []
sites ['T2_BR_UERJ'] = []
sites ['T2_CH_CSCS'] = []
sites ['T2_CN_Beijing'] = []
sites ['T2_DE_DESY'] = []
sites ['T2_DE_RWTH'] = []
sites ['T2_EE_Estonia'] = []
sites ['T2_ES_CIEMAT'] = []
sites ['T2_ES_IFCA'] = []
sites ['T2_FI_HIP'] = []
sites ['T2_FR_CCIN2P3'] = []
sites ['T2_FR_GRIF_IRFU'] = []
sites ['T2_FR_GRIF_LLR'] = []
sites ['T2_FR_IPHC'] = []
sites ['T2_HU_Budapest'] = []
sites ['T2_IN_TIFR'] = []
sites ['T2_IT_Bari'] = []
sites ['T2_IT_Legnaro'] = []
sites ['T2_IT_Pisa'] = []
sites ['T2_IT_Rome'] = []
sites ['T2_KR_KNU'] = []
sites ['T2_PL_Warsaw'] = []
sites ['T2_PT_LIP_Lisbon'] = []
sites ['T2_PT_NCG_Lisbon'] = []
sites ['T2_RU_IHEP'] = []
sites ['T2_RU_INR'] = []
sites ['T2_RU_ITEP'] = []
sites ['T2_RU_JINR'] = []
sites ['T2_RU_PNPI'] = []
sites ['T2_RU_RRC_KI'] = []
sites ['T2_TR_METU'] = []
sites ['T2_TW_Taiwan'] = []
sites ['T2_UA_KIPT'] = []
sites ['T2_UK_London_Brunel'] = []
sites ['T2_UK_London_IC'] = []
sites ['T2_UK_SGrid_RALPP'] = []
sites ['T2_US_Caltech'] = []
sites ['T2_US_Florida'] = []
sites ['T2_US_MIT'] = []
sites ['T2_US_Nebraska'] = []
sites ['T2_US_Purdue'] = []
sites ['T2_US_UCSD'] = []
sites ['T2_US_Vanderbilt'] = []
sites ['T2_US_Wisconsin'] = []



for i in jn['result']:
    if i[jn['desc']['columns'].index('type')]=='phedex':
        phedexname=i[jn['desc']['columns'].index('alias')]
        phedexname=re.sub('_(Export|Buffer|Disk|MSS|Stage)$','',phedexname)
        sitedbname=i[jn['desc']['columns'].index('site_name')]
        if phedexname not in sites.keys(): continue
        for k in jr['result']:
            if k[jr['desc']['columns'].index('role')]=='Site Executive' or k[jr['desc']['columns'].index('role')]=='Site Admin':
                if k[jr['desc']['columns'].index('site_name')]==sitedbname:
                    contactname=k[jr['desc']['columns'].index('username')]
                    for z in jp['result']:
                        if z[jp['desc']['columns'].index('username')]==contactname:
                            email=z[jp['desc']['columns'].index('email')]
                            if email not in sites[phedexname]: sites[phedexname].append(email)

for site in sites.keys():
    print site,','.join(sites[site])

