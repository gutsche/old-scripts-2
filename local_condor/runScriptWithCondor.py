#!/usr/bin/env python

import os,sys

scripts=sys.argv[1:]

for scriptname in scripts:
    name=os.path.splitext(scriptname)[0]
    jdl = open(name + '.jdl','w')
    jdl.write("universe              = vanilla\n")
    jdl.write("Executable            = " + scriptname + "\n")
    jdl.write("should_transfer_files = YES\n")
    jdl.write("WhenToTransferOutput  = ON_EXIT_OR_EVICT\n")
    jdl.write("Output                = " + name + ".out\n")
    jdl.write("Error                 = " + name + ".err\n")
    jdl.write("Log                   = " + name + ".condor\n")
    jdl.write("Requirements          = Memory >= 199 && OpSys == \"LINUX\" && (Arch != \"DUMMY\")\n")
    jdl.write("notification          = never\n")
    jdl.write("Queue 1\n")
    jdl.close()
    os.system("condor_submit " + name + ".jdl")
