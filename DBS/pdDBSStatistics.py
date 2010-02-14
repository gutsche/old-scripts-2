#!/usr/bin/env python

import sys, os, getopt, time

from ROOT import TCanvas
from ROOT import TH1D
from ROOT import TStyle
from ROOT import gROOT
from ROOT import TDatime
from ROOT import TPaveText

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
        cmd = "python $DBSCMD_HOME/dbsCommandLine.py -c search --query=\"find file,file.size,file.numevents,run,lumi,file.createdate where dataset = " + dataset + "\" --noheader"
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

    files = {}
    plots = []
    failures = []

    for line in filelist_handle.readlines():
        array = line.split()
        if len(array) > 3 :
            name = str(array[0])
            size = float(float(array[1])/1000000000000)
            events = int(array[2])
            run = int(array[3])
            lumi = int(array[4])
            if array[-1] != 'GMT' :
                failures.append(line)
            else :
                thetime = int(time.mktime(time.strptime(' '.join(array[5:]),'%a, %d %b %Y %H:%M:%S %Z')))
                if name in files.keys():
                    files[name]['lumi'].append(lumi)
                else :
                    entry = {}
                    entry['size'] = size
                    entry['events'] = events
                    entry['run'] = [run]
                    entry['lumi'] = [lumi]
                    entry['time'] = thetime
                    files[name] = entry

        if debug == 1 :
            for name in files.keys():
                print name,'size:',files[name]['size'],'events:',files[name]['events'],'runs:',','.join(map(str,files[name]['run'])),'lumis:',','.join(map(str,files[name]['lumi'])),'date:',files[name]['time']


    # print failures
    if len(failures) > 0 :
        print ""
        print "failures:"
        for line in failures :
            print line

    # define time axis
    times = [ files[name]['time'] for name in files ]
    times.sort()
    first_day = times[0]-times[0]%86400
    last_day  = times[len(times)-1]+(86400-times[len(times)-1]%86400)
    days = int((last_day - first_day)/86400.)

    # determine x axis division
    if days%10 == 0:
        bigdiv = 10
        smalldiv = days/10
    elif days%9 == 0:
        bigdiv = 9
        smalldiv = days/9
    elif days%8 == 0:
        bigdiv = 8
        smalldiv = days/8
    elif days%7 == 0:
        bigdiv = 7
        smalldiv = days/7
    elif days%6 == 0:
        bigdiv = 6
        smalldiv = days/6
    elif days%5 == 0:
        bigdiv = 5
        smalldiv = days/5
    elif days%4 == 0:
        bigdiv = 4
        smalldiv = days/4
    elif days%3 == 0:
        bigdiv = 3
        smalldiv = days/3
    elif days%2 == 0:
        bigdiv = 2
        smalldiv = days/2
    else :
        bigdiv = 1
        smalldiv = days


    gROOT.SetBatch(1)

    myStyle = TStyle("Default","Default");
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
    myStyle.SetTimeOffset(first_day+86400)

    c = TCanvas()

    c.SetLeftMargin(0.171)
    c.SetRightMargin(0.04)
    c.SetBottomMargin(0.093)
    c.SetTopMargin(0.08)
    c.SetGridx(1)
    c.SetGridy(1)

    # events histogram
    print 'Drawing histograms for average number of events per day'
    h_events = TH1D("NumberOfEvents" + identifier,"",days,0.,days*86400.)

    h_events.GetYaxis().SetTitle("Number of events [1/24h]")
    h_events.GetYaxis().SetTitleSize(0.08)
    h_events.GetYaxis().SetTitleColor(4)
    h_events.GetYaxis().SetTitleOffset(1.14)
    h_events.GetYaxis().SetLabelSize(0.07)
    h_events.GetYaxis().SetLabelOffset(0.01)
    
    h_events.GetXaxis().SetTimeDisplay(1)
    h_events.GetXaxis().SetTimeFormat("%m/%d")
    h_events.GetXaxis().SetLabelSize(0.05)
    h_events.GetXaxis().SetLabelOffset(0.035)
    h_events.GetXaxis().SetNdivisions(smalldiv * 100 + bigdiv,0)

    h_events.SetLineColor(4)
    h_events.SetLineWidth(3)

    total_events = 0

    for name in files.keys():
        total_events += files[name]['events']
        h_events.Fill(files[name]['time']-first_day,files[name]['events'])
    h_events.SetMaximum(h_events.GetMaximum()*1.3)
    h_events.Draw()

    t_events = TPaveText(0.2,0.75,0.9,0.9,'brNDC')
    t_events.AddText('CMS 2009: %s' % identifier)
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

    # rate histogram
    print 'Drawing histograms for average rate per day'
    h_rate = TH1D("Rate" + identifier,"",days,0.,days*86400.)
    h_rate.GetYaxis().SetTitle("Average Rate [Hz/24h]")
    h_rate.GetYaxis().SetTitleSize(0.08)
    h_rate.GetYaxis().SetTitleColor(4)
    h_rate.GetYaxis().SetTitleOffset(1.14)
    h_rate.GetYaxis().SetLabelSize(0.07)
    h_rate.GetYaxis().SetLabelOffset(0.01)
    
    h_rate.GetXaxis().SetTimeDisplay(1)
    h_rate.GetXaxis().SetTimeFormat("%m/%d")
    h_rate.GetXaxis().SetLabelSize(0.05)
    h_rate.GetXaxis().SetLabelOffset(0.035)
    h_rate.GetXaxis().SetNdivisions(smalldiv * 100 + bigdiv,0)

    h_rate.SetLineColor(4)
    h_rate.SetLineWidth(3)

    h_rate_max = 0.

    for bin in range(days):
        rate = h_events.GetBinContent(bin+1)/24./3600.
        if rate > h_rate_max :
            h_rate_max = rate
        h_rate.SetBinContent(bin+1,rate)

    h_rate.SetMaximum(h_rate_max*1.3)
    h_rate.Draw()

    t_rate = TPaveText(0.2,0.75,0.9,0.9,'brNDC')
    t_rate.AddText('CMS 2009: %s' % identifier)
    t_rate.AddText('Average rate: %.2f Hz' % (float(total_events)/float(days)/24./3600.))
    t_rate.AddText('Last updated on: %s' % (timestring))
    t_rate.SetFillColor(0)
    t_rate.SetFillStyle(0)
    t_rate.SetBorderSize(0)
    t_rate.SetTextAlign(12)
    t_rate.Draw()

    name = timefilestring + '_rate' + identifier.replace('/','_') + '.png'
    plots.append(name)
    c.SaveAs(name)
    c.Clear()

    # size histogram
    print 'Drawing histograms for average size per day'
    h_size = TH1D("Size"+identifier,"",days,0.,days*86400.)

    h_size.GetYaxis().SetTitle("Size [TB/24h]")
    h_size.GetYaxis().SetTitleSize(0.08)
    h_size.GetYaxis().SetTitleColor(4)
    h_size.GetYaxis().SetTitleOffset(1.12)
    h_size.GetYaxis().SetLabelSize(0.07)
    h_size.GetYaxis().SetLabelOffset(0.01)

    h_size.GetXaxis().SetTimeDisplay(1)
    h_size.GetXaxis().SetTimeFormat("%m/%d")
    h_size.GetXaxis().SetLabelSize(0.05)
    h_size.GetXaxis().SetLabelOffset(0.035)
    h_size.GetXaxis().SetNdivisions(smalldiv * 100 + bigdiv,0)

    h_size.SetLineColor(4)
    h_size.SetLineWidth(3)

    total_size = 0.
    for name in files.keys():
        total_size += files[name]['size']
        h_size.Fill(files[name]['time']-first_day,files[name]['size'])
    h_size.SetMaximum(h_size.GetMaximum()*1.3)
    h_size.Draw()

    t_size = TPaveText(0.2,0.75,0.9,0.9,'brNDC')
    t_size.AddText('CMS 2009: %s' % identifier)
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
    html_file.write('<p align="right">Last updated blablabla</p>\n')
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

