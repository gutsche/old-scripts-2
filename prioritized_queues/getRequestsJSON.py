#!/usr/bin/env python
import json
import urllib2,urllib, httplib, sys, re, os

url='vocms204.cern.ch'
conn  =  httplib.HTTPSConnection(url, cert_file = os.getenv('X509_USER_PROXY'), key_file = os.getenv('X509_USER_PROXY'))
r1=conn.request("GET",'/reqmgr/monitorSvc/requestmonitor', None, {"Accept": "application/json"})
r2=conn.getresponse()
requests = json.loads(r2.read())
good_status = ['running', 'acquired', 'assignment-approved', 'new']
good_requests = []
for request in requests:
    print request
    if 'status' not in request.keys():
        print request
        continue
    if request['status'] in good_status:
        url = 'cmsweb.cern.ch'
        workflow = request['request_name']
        conn  =  httplib.HTTPSConnection(url, cert_file = os.getenv('X509_USER_PROXY'), key_file = os.getenv('X509_USER_PROXY'))
        r1=conn.request("GET",'/couchdb/reqmgr_workload_cache/'+workflow, None, {"Accept": "application/json"})
        r2=conn.getresponse()
        details = json.loads(r2.read())
        request['details'] = details
        url = 'cmsweb.cern.ch'
        conn  =  httplib.HTTPSConnection(url, cert_file = os.getenv('X509_USER_PROXY'), key_file = os.getenv('X509_USER_PROXY'))
        r1=conn.request("GET",'/reqmgr/reqMgr/request/'+workflow, None, {"Accept": "application/json"})
        r2=conn.getresponse()
        details = json.loads(r2.read())
        request['details2'] = details
        url = 'cmsweb.cern.ch'
        conn  =  httplib.HTTPSConnection(url, cert_file = os.getenv('X509_USER_PROXY'), key_file = os.getenv('X509_USER_PROXY'))
        r1=conn.request("GET",'/reqmgr/reqMgr/outputDatasetsByRequestName?requestName=' + workflow)
        r2=conn.getresponse()
        datasets = json.loads(r2.read())
        request['OutputDatasets'] = datasets
        good_requests.append(request)

output_file = open('requests.json','w')
json.dump(good_requests,output_file)
output_file.close()
