#!/usr/bin/env python

import sys,os
import subprocess




result = {}

command="""condor_status -any -const 'MyType=="glideresource"' -format '%s ' Name -format '%i ' GlideFactoryMonitorStatusHeld -format '%i ' GlideFactoryMonitorStatusPending -format "%i\n" GlideFactoryMonitorStatusRunning"""
proc = subprocess.Popen(command, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
out, err = proc.communicate()
for line in out.split('\n') :
    if line == "" : continue
    array = line.split()
    if array[0].startswith('CMS') :
        site = '_'.join(array[0].split('_')[1:4])
        if site.endswith('GRIF') or site.endswith('London') or site.endswith('RRC') or site.endswith('SGrid') or (site.startswith('T3') and site.endswith('ScotGrid')):
            site += '_' + array[0].split('_')[4]
        if site.count('_PT_') >= 1:
            site += '_' + array[0].split('_')[4]
        site = site.split('@')[0]
        held = int(array[-3])
        pend = int(array[-2])
        run  = int(array[-1])
        if site not in result.keys():
            result[site] = {"held":0,"pend":0,"run":0}
        result[site]["held"]+=held
        result[site]["pend"]+=pend
        result[site]["run"]+=run
    

sortedsites = result.keys()
sortedsites.sort()

print '------------------------------------------------------'
print '| %20s | %7s | %7s | %7s |' % ('Site','Held','Pending','Running')
print '------------------------------------------------------'

tot_held = 0
tot_pend = 0
tot_run = 0

for site in sortedsites:
    tot_held+=result[site]["held"]
    tot_pend+=result[site]["pend"]
    tot_run+=result[site]["run"]    
    print '| %20s | %7d | %7d | %7d |' % (site,result[site]["held"],result[site]["pend"],result[site]["run"])

print '------------------------------------------------------'
print '| %20s | %7d | %7d | %7d |' % ('All Sites',tot_held,tot_pend,tot_run)
print '------------------------------------------------------'
