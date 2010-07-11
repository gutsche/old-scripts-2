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

    ExtractPerformanceReport.py

    Extract performance information from FrameworkJobreport.xml from jobs in JobCleanup success archive directory

    required parameters :
    
    --archives <names> : archive filename pattern in double-quotes, merge archives are automatically excluded

    optional parameters :

    --merge             : only look at merge jobs, if not set, merge jobs are excluded
    --details           : print per job information to stdout
    --report            : produce ascii report file, one job per line: events,timePerEvent,averageMemory,maxMemory
    --input-dir         : override ProdAgent success archive directory
    --help              : help
    --debug             : debug statements

    """

    valid = ["help", "debug", "archives=", "report", "details", "input-dir=", "merge"]

    debug     = 0
    archives  = None
    input_dir = None
    report    = 0
    details   = 0
    merge     = 0

    try:
        opts, args = getopt.getopt(argv, "", valid)
    except getopt.GetoptError, ex:
        print main.__doc__
        print ''
        print str(ex)
        print ''
        sys.exit(1)

    for opt, arg in opts:
        if opt == "--help" :
            print main.__doc__
            sys.exit()
        elif opt == "--debug" :
            debug = 1
        elif opt == "--report" :
            report = 1
        elif opt == "--details" :
            details = 1
        elif opt == "--archives" :
            archives = arg
        elif opt == "--input-dir" :
            input_dir = arg
        elif opt == "--merge" :
            merge = 1

    if archives == None :
        print main.__doc__
        sys.exit(2)
            
    # get archive directory for succeeded jobs from ProdAgent config
    SuccessDir = getSuccessArchiveDir()  # HERE!
    if input_dir != None :
        SuccessDir = input_dir

    # create temp directory
    ExtractDir = tempfile.mkdtemp()

    # prepare list of archives to process
    ArchiveFileList = glob.glob(os.path.join(SuccessDir,archives))

    # clean merge archives form list
    if merge == 1 :
        ArchiveFileList = [ archive for archive in ArchiveFileList if archive.count("merge") == 1 ]
    else :
        ArchiveFileList = [ archive for archive in ArchiveFileList if archive.count("merge") == 0 ]
        
    # extract information from archives
    jobs = ExtractOuputPerJob(ArchiveFileList,ExtractDir,debug)
    

    if len(jobs) > 0 :
        total   = 0   
        for job in jobs:
            total += job
        average = total / len(jobs)
        print ''
        print 'Average output MB/s: %.3f' % average
    else :
        print ''
        print 'No jobs extracted.'
 
    
    # remove temp directory
    os.system('rm -rf  %s ' % ExtractDir)
                                                                                                  
# ##########################
def getSuccessArchiveDir():
   """
   get the SuccessArchive dir from JobCleanup Component config
   """
   try:
     config = loadProdAgentConfiguration()
   except StandardError, ex:
     msg = "Error: error reading configuration:\n"
     msg += str(ex)
     print msg
     sys.exit(1)

   if not config.has_key("JobCleanup"):
      msg = "Error: Configuration block JobCleanup is missing from $PRODAGENT_CONFIG"
      print msg
      sys.exit(1)

   JCConfig       = config.getConfig("JobCleanup")
   successArchive = JCConfig.get("SuccessArchive", None)

   if not os.path.isdir(successArchive):
       cleanupDir    = JCConfig.get("ComponentDir",None)
       successArchive = os.path.join(cleanupDir,successArchive)

   return successArchive

# ##########################
def ExtractOuputPerJob(ArchiveFileList,ExtractDir,debug):
  """
  open archive in ExtractDir and extract performance information 
  """ 
  
  jobs = []

  counter = 0

  for archive in ArchiveFileList :

      # extract the FrameworkJobReport.xml
      if os.path.isfile(archive) and tarfile.is_tarfile(archive):
          counter += 1
          if counter%100 == 0:
              print 'Archive counter',counter
          jobtarfile   = tarfile.open(archive, 'r:gz')
          reportFileList = [tf for tf in jobtarfile.getnames() if tf.count("FrameworkJobReport.xml")]
          if len(reportFileList) > 0 :
              reportFile=reportFileList[0]
          jobtarfile.extract(reportFile,ExtractDir)
          reportfilename = os.path.join(ExtractDir,reportFile)
          if os.path.isfile(reportfilename) :
              if debug:
                  print 'Opening FrameworkJobReport:',reportfilename,'from archive:',archive
              reports = readJobReport(reportfilename)
              for report in reports:
                  size = 0
                  for file in report.files :
                      size += float(file['Size']) / 1024. / 1024.
                  timePerJob = float(report.timing['AppEndTime']) - float(report.timing['AppStartTime'])
                  if debug == 1 :
                      print timePerJob,size
                  jobs.append(size/timePerJob)
          else:
              print 'Archive:',archive,'does not contain a FrameworkJobReport.xml, skipping!'          
      else:
          print 'Archive:',archive,'is not a gzipp\'ed tarball, skipping!'
  
  return jobs  
          
      
################################################### 
if __name__ == '__main__':
    main(sys.argv[1:])
                                                                                                   
