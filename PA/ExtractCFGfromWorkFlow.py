#!/usr/bin/env python

import os
import pickle
from ProdCommon.CMSConfigTools.ConfigAPI.CMSSWAPILoader import CMSSWAPILoader
from ProdCommon.MCPayloads.WorkflowSpec import WorkflowSpec
from ProdCommon.MCPayloads.DatasetTools import getOutputDatasetsWithPSet


specfile = "/uscms/home/gutsche/CSA08-JetET110-CSA08_S43_S43_rereco_may19_PIC_v1-Workflow.xml"

rawCfgFile = "%s.raw.cfg" % os.path.basename(specfile)
origCfgFile = "%s.orig.cfg" % os.path.basename(specfile)
dbsCfgFile = "%s.dbs.cfg" % os.path.basename(specfile)

spec = WorkflowSpec()
spec.load(specfile)


rawCfg = spec.payload.cfgInterface.rawCfg
originalCfg = spec.payload.cfgInterface.originalCfg

dbsDatasets = getOutputDatasetsWithPSet(spec.payload)

handle = open(dbsCfgFile, 'w')
handle.write(
    dbsDatasets[0]['PSetContent']
    )
handle.close()

handle = open(origCfgFile, 'w')
handle.write(originalCfg)
handle.close()

loader = CMSSWAPILoader(
    os.environ['SCRAM_ARCH'],
    spec.payload.application['Version'],
    os.environ['CMS_PATH']
    )


loader.load()


cmsProcess = pickle.loads(rawCfg)
handle = open(rawCfgFile, 'w')
handle.write(cmsProcess.dumpConfig())
handle.close()

loader.unload()
