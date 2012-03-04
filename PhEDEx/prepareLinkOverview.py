#!/usr/bin/env python

import sys,os,urllib,json

url = 'https://cmsweb.cern.ch/phedex/datasvc/json/prod/links'
result = json.load(urllib.urlopen(url))

links = {}

for link in result['phedex']['link']:
    site_to = link['to']
    site_from = link['from']
    status = link['status']
    if status not in links.keys(): links[status] = []
    links[status].append({'to':site_to,'from':site_from})
    
for key in links.keys():
    print key,len(links[key])

print links['from_down']
