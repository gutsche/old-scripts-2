#!/usr/bin/env python

import sys,os,urllib,json

input = open(sys.argv[1],'r')

phedexlist = sys.argv[1] + '.phedex'
command = "rm -f " + phedexlist
os.system(command)
phedexoutput = open(phedexlist,'w')
files = input.readlines()
for file in files:
    if file.count('/store/') > 0 :
            
        url = 'http://cmsweb.cern.ch/phedex/datasvc/json/prod/filereplicas?lfn=' + file.strip()
        result = json.load(urllib.urlopen(url))

        nodes = []

        for block in result['phedex']['block']:
            for filelist in block['file'] :
                for replica in filelist['replica']:
                    if replica['node'].count('FNAL') > 0 and replica['node'] not in nodes :
                        nodes.append(replica['node'])
        if len(nodes) > 0 :
            outputstring = file.strip() + " " + ','.join(nodes) + "\n"
            phedexoutput.write(outputstring)

phedexoutput.close()

