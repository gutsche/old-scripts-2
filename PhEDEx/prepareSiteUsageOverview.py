#!/usr/bin/env python

import sys,os,urllib,json




url = 'https://cmsweb.cern.ch/phedex/datasvc/json/prod/nodeusage?node=T?_*'
result = json.load(urllib.urlopen(url))

T0 = {}
T1 = {}
T2 = {}
T3 = {}

T1_US = {}
T2_US = {}
T3_US = {}

T1_NON_US = {}
T2_NON_US = {}
T3_NON_US = {}

for node in result['phedex']['node']:
    name = str(node['name'])

    cust_node_files = int(node['cust_node_files'])
    noncust_node_files = int(node['noncust_node_files'])
    src_node_files = int(node['src_node_files'])
    nonsrc_node_files = int(node['nonsrc_node_files'])
    
    files = (cust_node_files + noncust_node_files + src_node_files + nonsrc_node_files)

    cust_node_bytes = int(node['cust_node_bytes'])
    noncust_node_bytes = int(node['noncust_node_bytes'])
    src_node_bytes = int(node['src_node_bytes'])
    nonsrc_node_bytes = int(node['nonsrc_node_bytes'])

    bytes = (cust_node_bytes + noncust_node_bytes + src_node_bytes + nonsrc_node_bytes)/1000000000000
    
    tmp = {'files':files,'bytes':bytes}
    
    if name.count('T0_') > 0 :
        if name.count('_MSS') <= 0 :
            name = name.replace('_Export','')
            T0[name] = tmp
    elif name.count('T1_') > 0 :
        if name.count('_MSS') <= 0 and name.count('_Disk') <= 0 :
            name = name.replace('_Buffer','')
            T1[name] = tmp
            if name.count('_US_') > 0 :
                T1_US[name] = tmp
            else :
                T1_NON_US[name] = tmp
    elif name.count('T2_') > 0 :
        T2[name] = tmp
        if name.count('_US_') > 0 :
            T2_US[name] = tmp
        else :
            T2_NON_US[name] = tmp
    elif name.count('T3_') > 0 :
        T3[name] = tmp
        if name.count('_US_') > 0 :
            T3_US[name] = tmp
        else :
            T3_NON_US[name] = tmp
    else:
        print 'error, cannot associate name:',name,'to site category'

#print len(T0)
#print len(T1),len(T1_US)
#print len(T2),len(T2_US)
#print len(T3),len(T3_US)

# print ''
# print 'T1 US'
# print '|'.join(T1_US)
# print ''
# print 'T1 NON US'
# print '|'.join(T1_NON_US)
# print ''
# print 'T2 US'
# print '|'.join(T2_US)
# print ''
# print 'T2 NON US'
# print '|'.join(T2_NON_US)
# print ''
# print 'T3 US'
# print '|'.join(T3_US)
# print ''
# print 'T3 NON US'
# print '|'.join(T3_NON_US)
# print ''
# 

for site in T0.keys():
    print "site: %20s files: %15d bytes: %7.1f TB" % (site,T0[site]['files'],T0[site]['bytes'])
for site in T1.keys():
    print "site: %20s files: %15d bytes: %7.1f TB" % (site,T1[site]['files'],T1[site]['bytes'])
for site in T2.keys():
    print "site: %20s files: %15d bytes: %7.1f TB" % (site,T2[site]['files'],T2[site]['bytes'])
for site in T3.keys():
    print "site: %20s files: %15d bytes: %7.1f TB" % (site,T3[site]['files'],T3[site]['bytes'])
