#!/usr/bin/env python

import httplib
import urllib
import sys

def makeRequest(url,params):

    encodedParams = urllib.urlencode(params)
    headers  =  {"Content-type": "application/x-www-form-urlencoded",
                 "Accept": "text/plain"}

    conn  =  httplib.HTTPConnection(url)
    conn.request("POST",  "/create/makeSchema", encodedParams, headers)
    response = conn.getresponse()
    data = response.read()
    if response.status != 303:
        print 'could not post request with following parameters:'
        for item in params.keys():
            print item + ": " + str(params[item])
        print 'Response from http call:'
        print 'Status:',response.status,'Reason:',response.reason
        print 'Explanation:'
        print data
        print "Exiting!"
        sys.exit(1)
    workflow=data.split('/')[5].split("'")[0]
    print 'Injected workflow:',workflow
    conn.close()
    return workflow
    
def approveRequest(url,workflow):
    params = {"action": "Approve",
              "checkbox"+workflow: "checked"}

    encodedParams = urllib.urlencode(params)
    headers  =  {"Content-type": "application/x-www-form-urlencoded",
                 "Accept": "text/plain"}

    conn  =  httplib.HTTPConnection(url)
    conn.request("POST",  "/reqmgr/approve/handleApprovalPage", encodedParams, headers)
    response = conn.getresponse()
    if response.status != 200:
        print 'could not approve request with following parameters:'
        for item in params.keys():
            print item + ": " + str(params[item])
        print 'Response from http call:'
        print 'Status:',response.status,'Reason:',response.reason
        print 'Explanation:'
        data = response.read()
        print data
        print "Exiting!"
        sys.exit(1)
    conn.close()
    print 'Approved workflow:',workflow
    return
    
def assignRequest(url,workflow,team,site,era,procversion):
    params = {"action": "Assign",
              "Team"+team: "checked",
              "SiteWhitelist": site,
              "SiteBlacklist": "",
              "MergedLFNBase": "/store/backfill/1",
              "UnmergedLFNBase": "/store/unmerged",
              "MinMergeSize": 500000000,
              "MaxMergeSize": 4294967296,
              "MaxMergeEvents": 50000,
              "AcquisitionEra": era,
              "ProcessingVersion": procversion,
              "checkbox"+workflow: "checked"}

    encodedParams = urllib.urlencode(params)

    headers  =  {"Content-type": "application/x-www-form-urlencoded",
                 "Accept": "text/plain"}

    conn  =  httplib.HTTPConnection(url)
    conn.request("POST",  "/assign/handleAssignmentPage", encodedParams, headers)
    response = conn.getresponse()
    if response.status != 200:
        print 'could not approve request with following parameters:'
        for item in params.keys():
            print item + ": " + str(params[item])
        print 'Response from http call:'
        print 'Status:',response.status,'Reason:',response.reason
        print 'Explanation:'
        data = response.read()
        print data
        print "Exiting!"
        sys.exit(1)
    conn.close()
    print 'Assigned workflow:',workflow,'to site:',site,'with processing version',procversion
    return

# read configs.txt
config = {}
configsfile = open('configs.txt')
for line in configsfile.readlines():
    array = line.split()
    if len(array) == 2:
        config[array[0]] = array[1]
    else :
        print 'Following line in configs.txt could not be decoded:',line
        
        
# define some global parameters
url = "cmssrv98.fnal.gov:8687"
release = "CMSSW_3_9_7"
globaltag = "FT_R_39X_V4A::All"
scramarch = "slc5_ia32_gcc434"
era='Backfill'
team='cmsdataops'

# define parameters to be changed everytime!!!
identifier = "110218"
counter = 3
repititions = 8

# workflow definition per site
workflows = {}

# T1_DE_KIT	 /BTau/Run2010B-v1/RAW	 cmssrm-fzk.gridka.de	 rereco_pp.py	 skim_BTau.py
params = { 
"inputdataset": "/BTau/Run2010B-v1/RAW",
"recoconfig": config["rereco_pp.py"],
"recoconfigoutputmodule": "RECOoutput",
"skimname": "BTauSkim",
"skimconfig": config["skim_BTau.py"],
}
# workflows['T1_DE_KIT'] = params

# T1_ES_PIC	 /Photon/Run2010B-v1/RAW	 srmcms.pic.es	 rereco_pp.py	 skim_Photon.py
params = { 
"inputdataset": "/Photon/Run2010B-v1/RAW",
"recoconfig": config["rereco_pp.py"],
"recoconfigoutputmodule": "RECOoutput",
"skimname": "PhotonSkim",
"skimconfig": config["skim_Photon.py"],
}
# workflows['T1_ES_PIC'] = params

# T1_FR_CCIN2P3	 /METFwd/Run2010B-v1/RAW	 ccsrm.in2p3.fr	 rereco_pp.py	 skim_METFwd.py
params = { 
"inputdataset": "/METFwd/Run2010B-v1/RAW",
"recoconfig": config["rereco_pp.py"],
"recoconfigoutputmodule": "RECOoutput",
"skimname": "METFwdSkim",
"skimconfig": config["skim_METFwd.py"],
}
# workflows['T1_FR_CCIN2P3'] = params

# T1_IT_CNAF	 /Mu/Run2010B-v1/RAW	 storm-fe-cms.cr.cnaf.infn.it	 rereco_Mu_pp.py	 skim_Mu.py
params = { 
"inputdataset": "/Mu/Run2010B-v1/RAW",
"recoconfig": config["rereco_Mu_pp.py"],
"recoconfigoutputmodule": "RECOoutput",
"skimname": "MuSkim",
"skimconfig": config["skim_Mu.py"],
}
# workflows['T1_IT_CNAF'] = params

# T1_UK_RAL	 /Jet/Run2010B-v1/RAW	 srm-cms.gridpp.rl.ac.uk	 rereco_pp.py	 skim_Jet.py
params = { 
"inputdataset": "/Jet/Run2010B-v1/RAW",
"recoconfig": config["rereco_pp.py"],
"recoconfigoutputmodule": "RECOoutput",
"skimname": "JetSkim",
"skimconfig": config["skim_Jet.py"],
}
# workflows['T1_UK_RAL'] = params

# T1_US_FNAL	 /Electron/Run2010B-v1/RAW	 cmssrm.fnal.gov	 rereco_Electron_pp.py	 skim_Electron.py
params = { 
"inputdataset": "/Electron/Run2010B-v1/RAW",
"recoconfig": config["rereco_Electron_pp.py"],
"recoconfigoutputmodule": "RECOoutput",
"skimname": "ElectronSkim",
"skimconfig": config["skim_Electron.py"],
}
workflows['T1_US_FNAL'] = params

# T1_TW_ASGC	 /MuOnia/Run2010B-v1/RAW	 srm2.grid.sinica.edu.tw	 rereco_MuOnia_pp.py
params = { 
"inputdataset": "/MuOnia/Run2010B-v1/RAW",
"recoconfig": config["rereco_MuOnia_pp.py"],
"recoconfigoutputmodule": "RECOoutput",
}
# workflows['T1_TW_ASGC'] = params

for rep in range(repititions):
    for site in workflows.keys():
        procversion = identifier + "_%02i" % counter + '_' + site + '_' + workflows[site]['inputdataset'].split('/')[1]
        params = {"CMSSWVersion": release,
                  "ProdConfigCacheID": workflows[site]['recoconfig'],
                  "InputDataset": workflows[site]['inputdataset'],
                  "RunWhitelist": [],
                  "RunBlacklist": [],
                  "BlockWhitelist": [],
                  "BlockBlacklist": [],
                  "GlobalTag": globaltag,
                  "RequestString": 'Backfill_' + procversion,
                  "RequestPriority": 1,
                  "ScramArch": scramarch,
                  "DbsUrl": "http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet",
                  "inputMode": "couchDB",
                  "Scenario": "pp",
                  "RequestType": "ReReco",
                  "Group": team}
        if "skimconfig" in workflows[site].keys():
          params["SkimName1"] =  workflows[site]['skimname']
          params["SkimInput1"] =  workflows[site]['recoconfigoutputmodule']
          params["SkimConfig1"] =  workflows[site]['skimconfig']
          params["nskims"] =  1,
        
                  
        workflow = makeRequest(url,params)
        approveRequest(url,workflow)
        assignRequest(url,workflow,team,site,era,procversion+'-v1')
    counter += 1