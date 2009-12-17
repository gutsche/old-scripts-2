#! /usr/bin/env python

from optparse import OptionParser
import sys
import os 
import imp
import FWCore.ParameterSet.Config as cms

parser = OptionParser()
parser.usage = "%prog <configuration> <max events> <skip events>: manipulate max events and skip events in given configuration."

(options,args) = parser.parse_args()

if len(args)!=3:
    parser.print_help()
    sys.exit(1)

filename = args[0]
handle = open(filename, 'r')
max = int(args[1])
skip = int(args[2])
cfo = imp.load_source("pycfg", filename, handle)
cmsProcess = cfo.process
handle.close()

cmsProcess.maxEvents.input = cms.untracked.int32(max)
cmsProcess.source.skipEvents = cms.untracked.uint32(skip)

output = file('cmssw.py','w')
output.write('import FWCore.ParameterSet.Config as cms\n\n')
output.write(cmsProcess.dumpPython())
output.close()
