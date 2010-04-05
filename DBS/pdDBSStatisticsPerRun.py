#!/usr/bin/env python

import sys, os, getopt, time

import ROOT

# from ROOT import TCanvas
# from ROOT import TH1D
# from ROOT import TStyle
# from ROOT import gROOT
# from ROOT import TDatime
# from ROOT import TPaveText

# defaults
debug   = 0

# time of execution
current = time.gmtime()
timestring = time.strftime("%Y-%m-%d %H:%M:%S UTC", current)
timefilestring = time.strftime("%Y_%m_%d_%H_%M_%S_UTC",current)

def main(argv) :
    """
    
    pdDBSStatistics
    
    query DBS for files in given list of PD and produce statistiscs plots

    required parameters
    --datasets <filename>                     :       file with dataset names, one dataset per line

    or

    --files <filename>                        :       file with list of files and properties per file from DBS query

    optional parameters                       :
    --help (-h)                               :       help
    --debug (-d)                              :       debug statements
    
    """
    # defauls
    datasets = None
    files    = None

    try:
        opts, args = getopt.getopt(argv, "", ["help", "debug", "datasets=", "files="])
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
        elif opt == "--datasets" :
            datasets = str(arg)
        elif opt == "--files" :
            files = str(arg)

    if datasets == None and files == None :
        print ''
        print '    Please at least specify --datasets or --files'
        print main.__doc__
        sys.exit(2)

    if datasets != None and files != None :
        print ''
        print '    Please specify only --datasets OR --files'
        print main.__doc__
        sys.exit(2)

    items = None
    plots = None

    if files != None:
        filelist_handle = open(files,'r')
        print ''
        print 'Working on given filelist'
        print ''
        plots = []
        plots.append(producePlots(filelist_handle,'filelist'))
        items = ['filelist']
    else :
        datasetlist_handle = open(datasets,'r')
        plots,items = queryDBS(datasetlist_handle)

    prepareHTML(plots,items)


def queryDBS(datasetlist_handle):
    """

    query DBS for datasets in handle list
    to collect information in dataset per file
    and then produce plots for them

    """
    plots = []
    datasets = []

    for line in datasetlist_handle.readlines():
        dataset = line.strip()
        if len(dataset.split()) < 1: 
            continue
        if len(dataset.split()) > 1:
            print 'Too many datasets in following line:',line
            print 'Skipping this line.'
            continue
        cmd = "python $DBSCMD_HOME/dbsCommandLine.py -c search --query=\"find file,file.size,file.numevents,run where dataset = " + dataset + "\" --noheader"
        filelist_handle_input,filelist_handle = os.popen2(cmd)
        print ''
        print 'Working on filelist from dataset:',dataset
        print ''
        plots.append(producePlots(filelist_handle,dataset))
        datasets.append(dataset)

    return plots,datasets

def producePlots(filelist_handle,identifier):
    """

    produce plots for filelist

    """

    runs = {}
    plots = []

    for line in filelist_handle.readlines():
        array = line.split()
        if len(array) > 3 :
            name = str(array[0])
            size = float(float(array[1])/1000000000000)
            events = int(array[2])
            run = int(array[3])
            if run in runs.keys():
                runs[run]['size'] += size
                runs[run]['events'] += events
            else :
                entry = {}
                entry['size'] = size
                entry['events'] = events
                runs[run] = entry

        if debug == 1 :
            for run in runs.keys():
                print run,'size:',runs[run]['size'],'events:',runs[run]['events']


    # define run axis
    sortedruns = runs.keys()
    sortedruns.sort()
    seen = set()
    runaxis = [ x for x in sortedruns if x not in seen and not seen.add(x)]

    ROOT.gROOT.SetBatch(1)

    myStyle = ROOT.TStyle("Default","Default");
    myStyle.cd();
    myStyle.SetFrameBorderMode(0);
    myStyle.SetCanvasBorderMode(0);
    myStyle.SetPadBorderMode(0);
    myStyle.SetPadColor(0);
    myStyle.SetCanvasColor(0);
    myStyle.SetTitleFillColor(0);
    myStyle.SetTitleBorderSize(1);
    myStyle.SetStatColor(0);
    myStyle.SetStatBorderSize(1);
    myStyle.SetOptStat(0);

    c = ROOT.TCanvas()

    c.SetLeftMargin(0.171)
    c.SetRightMargin(0.04)
    c.SetBottomMargin(0.093)
    c.SetTopMargin(0.08)
    c.SetGridx(1)
    c.SetGridy(1)

    # 6 digits in xaxis
    ROOT.TGaxis.SetMaxDigits(6);

    # events histogram
    print 'Drawing histograms for average number of events per run'
    h_events = ROOT.TH1D("NumberOfEvents" + identifier,"",runaxis[-1]-runaxis[0],runaxis[0],runaxis[-1])

    h_events.GetYaxis().SetTitle("Number of events [1/run]")
    h_events.GetYaxis().SetTitleSize(0.08)
    h_events.GetYaxis().SetTitleColor(4)
    h_events.GetYaxis().SetTitleOffset(1.14)
    h_events.GetYaxis().SetLabelSize(0.07)
    h_events.GetYaxis().SetLabelOffset(0.01)
    
    h_events.GetXaxis().SetLabelSize(0.05)
    h_events.GetXaxis().SetLabelOffset(0.035)

    h_events.SetLineColor(4)
    h_events.SetLineWidth(3)

    total_events = 0

    for run in runs.keys():
        total_events += runs[run]['events']
        h_events.Fill(run,runs[run]['events'])
    h_events.SetMaximum(h_events.GetMaximum()*1.3)
    h_events.Draw()

    t_events = ROOT.TPaveText(0.2,0.75,0.9,0.9,'brNDC')
    t_events.AddText('CMS 2010: %s' % identifier)
    t_events.AddText('Total number of events: %.2E' % (total_events))
    t_events.AddText('Last updated on: %s' % (timestring))
    t_events.SetFillColor(0)
    t_events.SetFillStyle(0)
    t_events.SetBorderSize(0)
    t_events.SetTextAlign(12)
    t_events.Draw()

    name = timefilestring + '_events' + identifier.replace('/','_') + '.png'
    plots.append(name)
    c.SaveAs(name)
    c.Clear()

    # size histogram
    print 'Drawing histograms for average size per day'
    h_size = ROOT.TH1D("Size"+identifier,"",runaxis[-1]-runaxis[0],runaxis[0],runaxis[-1])

    h_size.GetYaxis().SetTitle("Size [TB/run]")
    h_size.GetYaxis().SetTitleSize(0.08)
    h_size.GetYaxis().SetTitleColor(4)
    h_size.GetYaxis().SetTitleOffset(1.12)
    h_size.GetYaxis().SetLabelSize(0.07)
    h_size.GetYaxis().SetLabelOffset(0.01)

    h_size.GetXaxis().SetLabelSize(0.05)
    h_size.GetXaxis().SetLabelOffset(0.035)

    h_size.SetLineColor(4)
    h_size.SetLineWidth(3)

    total_size = 0.
    for run in runs.keys():
        total_size += runs[run]['size']
        h_size.Fill(run,runs[run]['size'])
    h_size.SetMaximum(h_size.GetMaximum()*1.3)
    h_size.Draw()

    t_size = ROOT.TPaveText(0.2,0.75,0.9,0.9,'brNDC')
    t_size.AddText('CMS 2010: %s' % identifier)
    t_size.AddText('Total size: %.2f TB' % (total_size))
    t_size.AddText('Last updated on: %s' % (timestring))
    t_size.SetFillColor(0)
    t_size.SetFillStyle(0)
    t_size.SetBorderSize(0)
    t_size.SetTextAlign(12)
    t_size.Draw()

    #raw_input('Press Enter...')
    name = timefilestring + '_size' + identifier.replace('/','_') + '.png'
    plots.append(name)
    c.SaveAs(name)
    c.Clear()
    return plots

def prepareHTML(plots,datasets):
    """

    prepare html page with all plots

    """

    html_file = open(timefilestring + '.html','w')
    html_file.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"\n')
    html_file.write('"http://www.w3.org/TR/html4/strict.dtd">\n')
    html_file.write('<html lang="en">\n')
    html_file.write('<head>\n')
    html_file.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n')
    html_file.write('<title>BeamCommissioning09</title>\n')
    html_file.write('<meta name="author" content="Oliver Gutsche">\n')
    html_file.write('</head>\n')
    html_file.write('<body>\n')
    for index in range(len(datasets)):
        html_file.write('<h1>' + datasets[index] + '</h1>\n')
        for plot in plots[index]:
            html_file.write('<a href="' + plot + '"><img src="' + plot + '" width=400></a>\n')
        html_file.write('<br><br>\n')
    html_file.write('<hr>\n')
    html_file.write('<p align="right">Last updated '+timestring+'</p>\n')
    html_file.write('</body>\n')
    html_file.write('</html>\n')
    html_file.close()

    index_file = open('index.html','w')
    index_file.write('<head>\n')
    index_file.write('<meta http-equiv="refresh" content="0; URL='+timefilestring+'.html">\n')
    index_file.write('</head>\n')
    index_file.write('<body>\n')
    index_file.write('</body>\n')
    index_file.close()


if __name__ == '__main__' :
    main(sys.argv[1:])

