#!/usr/bin/env python

import sys,os

inputfile = open(sys.argv[1])

users = {}

for line in inputfile.readlines():
    array = line.split()
    file = array[0]
    size = float(array[3])
    user = '/'.join(file.split('/')[:6])
    if user not in users.keys() : users[user] = 0.
    users[user] += size
    
users_sorted = users.keys()
users_sorted.sort()

for user in users_sorted:
    print "{userfield:<40s}: {sizefield:10.2f} GB".format(userfield=user,sizefield=users[user]/1000000000)