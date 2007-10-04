#!/usr/bin/env python2.4

import sys, os

def pickleParameterSet(parameter_set,version):
    """

    pickle parameter set

    """

    import FWCore.ParameterSet.Config as cms
    import pickle

    # load parameter-set
    try:
        process = cms.include(parameter_set)
    except:
        print ''
        print 'ParameterSet: ',parameter_set,'could not be converted to python dictionary'
        print ''
        sys.exit(1)

    # pickle parameter-set by replacing cfg extension with pkl extension
    file = open(addCMSSWVersionToName(parameter_set,version)+".pkl",'w')
    pickle.dump(process,file)

def prepareWorkflow(parameter_set,events,speed_category,version,cms_path,cmssw_architecture,cmssw_version,name) :
    """

    prepareWorkflow for parameter-set

    """

    from xml.dom.minidom import Document, Element, Text
    
    topNode = Element("RelValSpec")

    element = Element("RelValTest")
    element.setAttribute("Name", name)

    SpeedCategoryElement = Element("SpeedCategory")
    SpeedCategoryElement.setAttribute("Value", speed_category)
    element.appendChild(SpeedCategoryElement)

    TotalEventsElement = Element("TotalEvents")
    TotalEventsElement.setAttribute("Value", str(events))
    element.appendChild(TotalEventsElement)

    pickle_file = os.path.join(os.getcwd(), addCMSSWVersionToName(parameter_set,version)+".pkl")

    PickleFileElement = Element("PickleFile")
    PickleFileElement.setAttribute("Value", pickle_file)
    element.appendChild(PickleFileElement)

    PickleFileElement = Element("CMSPath")
    PickleFileElement.setAttribute("Value", cms_path)
    element.appendChild(PickleFileElement)

    PickleFileElement = Element("CMSSWArchitecture")
    PickleFileElement.setAttribute("Value", cmssw_architecture)
    element.appendChild(PickleFileElement)

    PickleFileElement = Element("CMSSWVersion")
    PickleFileElement.setAttribute("Value", cmssw_version)
    element.appendChild(PickleFileElement)

    topNode.appendChild(element)
    
    doc = Document()
    doc.appendChild(topNode)
    handle = open(addCMSSWVersionToName(parameter_set,version)+".xml", "w")
    handle.write(doc.toprettyxml())
    handle.close()

def addCMSSWVersionToName(name,version) :
    """

    add CMSSW version tag to name starting with DevelopmentSample

    """

    array = name.split(".")[0].split("Sample")

    new_name = array[0] + "Sample" + str(version) + array[-1]

    return new_name

def main(argv) :
    """
    
    prepareWorkflow
    
    prepare PA workflow for cmssw parameter-set including parameter-set pickling
    requires setup'ed CMSSW user project area

    required parameters
    --parameter-set  <name>     : name and path of input parameter-set
    --events         <number>   : number of events to generate

    optional parameters         :
    --name                      : primary datasetname (default from parameter-set name)
    --speed-category <category> : speed category: Fast, Medium, Slow (default: Fast)
    --help (-h)                 : help
    --debug (-d)                : debug statements
    
    
    """

    # default
    try:
        cmssw_version = os.environ.get("CMSSW_VERSION")
    except:
        print ''
        print 'CMSSW version cannot be determined from $CMSSW_VERSION'
        sys.exit(2)
    parameter_set      = ''
    events             = 0
    speed_category     = "Slow"
    debug              = 0
    cms_path           = '/uscmst1/prod/sw/cms'
    cmssw_architecture = 'slc4_ia32_gcc345'
    name               = ''
    

    import getopt

    try:
        opts, args = getopt.getopt(argv, "", ["help", "debug", "parameter-set=", "events=", "speed-category=","name="])
    except getopt.GetoptError:
        print main.__doc__
        sys.exit(2)

    # check command line parameter
    for opt, arg in opts :
        if opt == "--help" :
            print main.__doc__
            sys.exit()
        elif opt == "--debug" :
            debug = 1
        elif opt == "--parameter-set" :
            parameter_set = arg
        elif opt == "--speed-category" :
            speed_category = arg
        elif opt == "--name" :
            name = arg
        elif opt == "--events" :
            try:
                events = int(arg)
            except:
                print ''
                print 'Events have to be given as a integer'
                print ''
                print main.__doc__
                sys.exit(2)

    if parameter_set == '' :
        print main.__doc__
        sys.exit(2)

    if events == 0 :
        print main.__doc__
        sys.exit(2)

    if speed_category != "Fast" and speed_category != "Medium" and speed_category != "Slow" :
        print ''
        print 'Unsupported speed category!'
        print ''
        print main.__doc__
        sys.exit(2)

    if os.path.exists(parameter_set) == False :
        print ''
        print 'Parameter-Set:',parameter_set,'cannot be found!'
        print ''
        print main.__doc__
        sys.exit(2)

    # prepare version tag
    version = cmssw_version.replace("CMSSW","").replace("_","")

    # prepare name
    if name == '':
        name = parameter_set.replace(".cfg","")

    # pickle parameter_set
    try:
        pickleParameterSet(parameter_set,version)
    except:
        print ''
        print 'Parameter-Set:',parameter_set,'could not be converted into a python dictionary and pickled!'
        print ''
        print main.__doc__
        sys.exit(1)
        
    # prepare workflow
    try:
        prepareWorkflow(parameter_set,events,speed_category,version,cms_path,cmssw_architecture,cmssw_version,name)
    except:
        print ''
        print 'Workflow for parameter-set:',parameter_set,'could not be created!'
        print ''
        print main.__doc__
        sys.exit(1)

    print 'Workflow:',addCMSSWVersionToName(parameter_set,version)+".xml",'created!'
    
if __name__ == '__main__' :
    main(sys.argv[1:])
