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

    --details           : print per job information to stdout
    --report            : produce ascii report file, one job per line: events,timePerEvent,averageMemory,maxMemory
    --input-dir         : override ProdAgent success archive directory
    --help              : help
    --debug             : debug statements

    """

    valid = ["help", "debug", "archives=", "report", "details", "input-dir="]

    debug     = 0
    archives  = None
    input_dir = None
    report    = 0
    details   = 0

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
    ArchiveFileList = [ archive for archive in ArchiveFileList if archive.count("merge") == 0 ]

    # jobs
    jobs = {}

    # extract performance information from archives
    for archive in ArchiveFileList :
        performance = ExtractPerformanceInformation(archive,ExtractDir,debug)
        #if performance != None :
        #    key = os.path.basename(archive).split('-')[1].replace('RelVal','')
        #    if key in jobs.keys() :
        #        jobs[key].append(performance)
        #    else :
        #        jobs[key] = [performance]

	step_num = 1
	for step in performance:
           if step != None :
               key = os.path.basename(archive).split('-')[1].replace('RelVal','') + '_step' + str(step_num) 
               if key in jobs.keys() :
                   jobs[key].append(step)
               else :
                   jobs[key] = [step]
	   step_num += 1


    if report == 1 :
        file = open('performance_report.txt','w')
        
    # prepare tables
    appTimeHeader1 = ''
    appTimeHeader2 = ''
    appTimeRow    = ''

    timeHeader1 = ''
    timeHeader2 = ''
    timeRow    = ''

    averageHeader1 = ''
    averageHeader2 = ''
    averageRow    = ''

    maxHeader1 = ''
    maxHeader2 = ''
    maxRow    = ''

    keys = jobs.keys()
    keys.sort()
    for key in keys :

        # detailed output and calculate averages
        appTime       = 0.
        appTimeError  = 0.
        events             = 0
        timePerEvent       = 0.
        timePerEventError  = 0.
        averageMemory      = 0.
        averageMemoryError = 0.
        maxMemory          = 0.
        maxMemoryError     = 0.
        if details == 1 :
            print ''
            print 'Performance summary per job for :',key
            print ''
        for job in jobs[key]:
            if details == 1 :
                print 'Job: Number of events: %d Time per Event: %.2f s Average Memory: %.2f MB Max. Memory: %.2f MB AppTime: %.2f' % (job['Events'],
                                                                                                                         job['TimePerEvent'],
                                                                                                                         job['AverageMemory']/1024.,
                                                                                                                         job['MaxMemory']/1024.,
                                                                                                                         job['AppTime'])

            appTime    += job['AppTime']
            appTimeError  += job['AppTime']*job['AppTime']
            timePerEvent       += job['TimePerEvent']
            timePerEventError  += job['TimePerEvent']*job['TimePerEvent']
            averageMemory      += job['AverageMemory']/1024.
            averageMemoryError += job['AverageMemory']/1024.*job['AverageMemory']/1024.
            maxMemory          += job['MaxMemory']/1024.
            maxMemoryError     += job['MaxMemory']/1024.*job['MaxMemory']/1024.
            events             += job['Events']

        appTime       /= len(jobs[key])
        appTimeError  /= len(jobs[key])
        timePerEvent       /= len(jobs[key])
        timePerEventError  /= len(jobs[key])
        averageMemory      /= len(jobs[key])
        averageMemoryError /= len(jobs[key])
        maxMemory          /= len(jobs[key])
        maxMemoryError     /= len(jobs[key])
        
        appTimeError  = math.sqrt(appTimeError - appTime*appTime)
        timePerEventError  = math.sqrt(timePerEventError - timePerEvent*timePerEvent)
        averageMemoryError = math.sqrt(averageMemoryError - averageMemory*averageMemory)
        maxMemoryError     = math.sqrt(maxMemoryError - maxMemory*maxMemory)
        
        appTimeHeader1 += ' ' + key + ' \" \"'
        appTimeHeader2 += ' \"Time [h]\" \"Error [h]\"'
        appTimeRow += ' %f %f' % (appTime,appTimeError)

        timeHeader1 += ' ' + key + ' \" \"'
        timeHeader2 += ' \"Time/Event [s]\" \"Error [s]\"'
        timeRow += ' %f %f' % (timePerEvent,timePerEventError)

        averageHeader1 += ' ' + key + ' \" \"'
        averageHeader2 += ' \"Average Memory/Event [MB]\" \"Error [MB]\"'
        averageRow += ' %f %f' % (averageMemory,averageMemoryError)

        maxHeader1 += ' ' + key + ' \" \"'
        maxHeader2 += ' \"Max Memory/Event [MB]\" \"Error [MB]\"'
        maxRow += ' %f %f' % (maxMemory,maxMemoryError)
        
        print ''
        print 'Average performance of:',key
        print 'Tot. Number of events: %d Time per Event: %.2f +- %.2f s Average Memory: %.2f +- %.2f MB Max. Memory: %.2f +- %.2f MB App time: %.2f +- %.2f h' % (events,
        timePerEvent,timePerEventError,
        averageMemory,averageMemoryError,
        maxMemory,maxMemoryError,
        appTime,appTimeError)

        if report == 1 :
            line = '%s %d %f %f %f %f %f %f %f %f\n' % (key,
            events,
            timePerEvent,timePerEventError,
            averageMemory,averageMemoryError,
            maxMemory,maxMemoryError,
            appTime,appTimeError)
            file.write(line)

        if details == 1 :
            detailfile = open(key+'.txt','w')
            for job in jobs[key]:
                line = '%d %f %f %f %f\n' % (job['Events'],
                                          job['TimePerEvent'],
                                          job['AverageMemory']/1024.,
                                          job['MaxMemory']/1024.,
                                           job['AppTime'])
                detailfile.write(line)
            detailfile.close()

    if report == 1 :
        file.close()

    print ''
    print appTimeHeader1
    print appTimeHeader2
    print appTimeRow
    print ''
    print timeHeader1
    print timeHeader2
    print timeRow
    print ''
    print averageHeader1
    print averageHeader2
    print averageRow
    print ''
    print maxHeader1
    print maxHeader2
    print maxRow
    print ''
    
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
def ExtractPerformanceInformation(archive,ExtractDir,debug):
  """
  open archive in ExtractDir and extract performance information 
  """ 

  # extract the FrameworkJobReport.xml
  if os.path.isfile(archive) and tarfile.is_tarfile(archive):
      jobtarfile   = tarfile.open(archive, 'r:gz')
      reportFileList = [tf for tf in jobtarfile.getnames() if tf.count("FrameworkJobReport.xml")]
      if len(reportFileList) > 0 :
          reportFile=reportFileList[0]
	  results = []   ### HERE!
          result = {}
          jobtarfile.extract(reportFile,ExtractDir)
          reportfilename = os.path.join(ExtractDir,reportFile)
          if os.path.isfile(reportfilename) :
              if debug:
                  print 'Opening FrameworkJobReport:',reportfilename,'from archive:',archive
              reports = readJobReport(reportfilename)
              for report in reports:
                  performanceReport = report.performance
                  # app time
                  try:
                      time = float(report.timing['AppEndTime']) - float(report.timing['AppStartTime'])
                      result['AppTime'] = time/3600.
                  except:
                      print 'Cannot read AppEndTime and AppStartTime from FrameworkJobReport.xml from',archive
                      result['AppTime'] = 0.

                  # average physical memory
                  try:
                      mem = performanceReport.summaries['RSSMemory']['AvgRSSMemory']
                      result['AverageMemory'] = float(mem)
                  except:
                      print 'Cannot read RSSMemory:AvgRSSMemory from FrameworkJobReport.xml from',archive
                      result['AverageMemory'] = 0.

                  # max physical memory
                  try:
                      mem = performanceReport.summaries['RSSMemory']['MaxRSSMemory']
                      result['MaxMemory'] = float(mem)
                  except:
                      print 'Cannot read RSSMemory:MaxRSSMemory from FrameworkJobReport.xml from',archive
                      result['MaxMemory'] = 0.

                  # events per job from trigger report
                  try:
                      events = performanceReport.summaries['TrigReport']['TotalEvents']
                      result['Events'] = int(events)
                  except:
                      try:
                          events = 0;
                          for inputFile in report.inputFiles:
                              events += int(inputFile['EventsRead'])
                          result['Events'] = events
                      except:
                          print 'Cannot read TrigReport:TotalEvents from FrameworkJobReport.xml from',archive
                          result['Events'] = 0

                  # time per event
                  try:
                      time = performanceReport.summaries['Timing']['RealPerEvent']
                      result['TimePerEvent'] = float(time)
                  except:
                      try:
                          timePerJob = float(report.timing['AppEndTime']) - float(report.timing['AppStartTime'])
                          result['TimePerEvent'] = timePerJob / float(result['Events'])
                      except:
                          print 'Cannot read Timing:RealPerEvent from FrameworkJobReport.xml from',archive
                          result['TimePerEvent'] = 0
		  
		  results.append(result)  ### HERE!
		  result = {}  ### HERE!


	  #return result  
          return results   ### HERE!
      else:
          print 'Archive:',archive,'does not contain a FrameworkJobReport.xml, skipping!'
          return None
          
  else:
      print 'Archive:',archive,'is not a gzipp\'ed tarball, skipping!'
      return None
      
################################################### 
if __name__ == '__main__':
    main(sys.argv[1:])
                                                                                                   
