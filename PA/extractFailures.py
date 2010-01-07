#!/usr/bin/env python
from MessageService.MessageService import MessageService
from ProdAgentCore.Configuration import loadProdAgentConfiguration
from ProdAgentDB.Config import defaultConfig as dbConfig
from ProdCommon.FwkJobRep.ReportParser import readJobReport

import sys,os,getopt,glob,math
import time,tarfile,tempfile

# ##########################
def main(argv) :
    """

    extractFailures.py

    Extract logArchive tarball LFN and FrameworkError from last FrameworkJobReport.xml of failure tarball

	Parameters: list of failure tarballs

    """

    debug = 0

    # create temp directory
    ExtractDir = tempfile.mkdtemp()

    # extract performance information from archives
    failures = []
    for archive in argv :
        failure = ExtractFailureInformation(archive,ExtractDir,debug)
        if failure != None :
            failures.append(failure)

    print ""
    print "Failures:"

    for failure in failures:
        for lfn in failure.keys():
            if lfn != None :
                if failure[lfn] != None :
                    print ""
                    print "logArchive tarball at CERN:"
                    print ""
                    print lfn
                    print ""
                    print "Failure description:"
                    print ""
                    print failure[lfn]

    print ""
    print "Failures without error, rfcp commands to copy LFN's into local directory:"
    print ""

    for failure in failures:
        for lfn in failure.keys():
            if lfn != None :
                if failure[lfn] == None :
                    print "rfcp /castor/cern.ch/cms" + lfn + " ."

    counter = 0
    for failure in failures:
        for lfn in failure.keys():
            if lfn == None :
                counter += 1
    if counter > 0 :
        print ""
        print "Number of Failures without error and logArchive LFN:",counter

    print ""
    
    # remove temp directory
    os.system('rm -rf  %s ' % ExtractDir)
                                                                                                  
# ##########################
def ExtractFailureInformation(archive,ExtractDir,debug):
  """
  open archive in ExtractDir and extract failure information
  use first description and LFN found, ignore following
  """ 
  
  # extract the FrameworkJobReport.xml
  if os.path.isfile(archive) and tarfile.is_tarfile(archive):
      jobtarfile   = tarfile.open(archive, 'r:gz')
      reportFileList = [tf for tf in jobtarfile.getnames() if tf.count("FrameworkJobReport")]
      reportFileList.sort()
      result = {}
      if len(reportFileList) > 0 :
          reportFile=reportFileList[-1]
          jobtarfile.extract(reportFile,ExtractDir)
          reportfilename = os.path.join(ExtractDir,reportFile)
          if os.path.isfile(reportfilename) :
              if debug:
                  print 'Opening FrameworkJobReport:',reportfilename,'from archive:',archive
              reports = readJobReport(reportfilename)
              for report in reports:
                  logfile = None
                  failure = None
                  if len(report.logFiles) > 0 :
                      logfile = report.logFiles.keys()[0]
                  if len(report.errors) > 0 :
                      failure = report.errors[0]['Description'].replace('\t','')
                  result[logfile] = failure
                                    
      else:
          print 'Archive:',archive,'does not contain a FrameworkJobReport*.xml, skipping!'

      return result
  else:
      print 'Archive:',archive,'is not a gzipp\'ed tarball, skipping!'
      return None
      
################################################### 
if __name__ == '__main__':
    main(sys.argv[1:])
