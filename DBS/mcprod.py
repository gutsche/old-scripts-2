#!/usr/bin/env python

import sys,os,subprocess,shlex,locale
locale.setlocale(locale.LC_ALL, 'en_US')

result = {}

commandline = "dbs search --query=\"find dataset.status,sum(block.numevents) where dataset = *Summer12*GEN-SIM\" --noheader --production"
localargs = shlex.split(commandline)
output = subprocess.Popen(localargs, shell=False, stdout=subprocess.PIPE)
lines = output.communicate()[0].split('\n')
for line in lines:
    if line == '': continue
    array = line.split()
    result[array[0]] = int(array[1])
    
print ""
print "%s: %s" % ("PRODUCTION".ljust(12),locale.format("%d", result['PRODUCTION'], grouping=True).rjust(20))
print "%s: %s" % ("VALID".ljust(12),locale.format("%d", result['VALID'], grouping=True).rjust(20))
print "----------------------------------"
print "%s: %s" % ("TOTAL".ljust(12),locale.format("%d", result['VALID']+result['PRODUCTION'], grouping=True).rjust(20))
print ""
