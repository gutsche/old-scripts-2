#!/usr/bin/env python

import sys,os,urllib,json




url = 'https://cmsweb.cern.ch/phedex/datasvc/json/prod/nodes'
result = json.load(urllib.urlopen(url))

T0 = []
T1 = []
T2 = []
T3 = []

T1_US = []
T2_US = []
T3_US = []

T1_NON_US = []
T2_NON_US = []
T3_NON_US = []

for node in result['phedex']['node']:
    name = str(node['name'])
    if name.count('T0_') > 0 :
        if name.count('_MSS') <= 0 :
            name = name.replace('_Export','')
            T0.append(name)
    elif name.count('T1_') > 0 :
        if name.count('_MSS') <= 0 and name.count('_Disk') <= 0 :
            name = name.replace('_Buffer','')
            T1.append(name)
            if name.count('_US_') > 0 :
                T1_US.append(name)
            else :
                T1_NON_US.append(name)
    elif name.count('T2_') > 0 :
        T2.append(name)
        if name.count('_US_') > 0 :
            T2_US.append(name)
        else :
            T2_NON_US.append(name)
    elif name.count('T3_') > 0 :
        T3.append(name)
        if name.count('_US_') > 0 :
            T3_US.append(name)
        else :
            T3_NON_US.append(name)
    else:
        print 'error, cannot associate name:',name,'to site category'

#print len(T0)
#print len(T1),len(T1_US)
#print len(T2),len(T2_US)
#print len(T3),len(T3_US)

print ''
print 'T1 US'
print '|'.join(T1_US)
print ''
print 'T1 NON US'
print '|'.join(T1_NON_US)
print ''
print 'T2 US'
print '|'.join(T2_US)
print ''
print 'T2 NON US'
print '|'.join(T2_NON_US)
print ''
print 'T3 US'
print '|'.join(T3_US)
print ''
print 'T3 NON US'
print '|'.join(T3_NON_US)
print ''

