#!/bin/bash
for dataset in $*
do
	dbs search --noheader --query="find dataset,sum(block.numevents),sum(block.size) where dataset = ${dataset} and block.createdate > 2010-11-1 00:00:00 GMT and file.createdate < 2010-11-2 00:00:00 GMT" >> 01.txt
	dbs search --noheader --query="find dataset,sum(block.numevents),sum(block.size) where dataset = ${dataset} and block.createdate > 2010-11-2 00:00:00 GMT and file.createdate < 2010-11-3 00:00:00 GMT" >> 02.txt
	dbs search --noheader --query="find dataset,sum(block.numevents),sum(block.size) where dataset = ${dataset} and block.createdate > 2010-11-3 00:00:00 GMT and file.createdate < 2010-11-4 00:00:00 GMT" >> 03.txt
	dbs search --noheader --query="find dataset,sum(block.numevents),sum(block.size) where dataset = ${dataset} and block.createdate > 2010-11-4 00:00:00 GMT and file.createdate < 2010-11-5 00:00:00 GMT" >> 04.txt
	dbs search --noheader --query="find dataset,sum(block.numevents),sum(block.size) where dataset = ${dataset} and block.createdate > 2010-11-5 00:00:00 GMT and file.createdate < 2010-11-6 00:00:00 GMT" >> 05.txt
	dbs search --noheader --query="find dataset,sum(block.numevents),sum(block.size) where dataset = ${dataset} and block.createdate > 2010-11-6 00:00:00 GMT and file.createdate < 2010-11-7 00:00:00 GMT" >> 06.txt
	dbs search --noheader --query="find dataset,sum(block.numevents),sum(block.size) where dataset = ${dataset} and block.createdate > 2010-11-7 00:00:00 GMT and file.createdate < 2010-11-8 00:00:00 GMT" >> 07.txt
	dbs search --noheader --query="find dataset,sum(block.numevents),sum(block.size) where dataset = ${dataset} and block.createdate > 2010-11-8 00:00:00 GMT and file.createdate < 2010-11-9 00:00:00 GMT" >> 08.txt
    dbs search --noheader --query="find dataset,sum(block.numevents),sum(block.size) where dataset = ${dataset} and block.createdate > 2010-11-9 00:00:00 GMT and file.createdate < 2010-11-10 00:00:00 GMT" >> 09.txt
    dbs search --noheader --query="find dataset,sum(block.numevents),sum(block.size) where dataset = ${dataset} and block.createdate > 2010-11-10 00:00:00 GMT and file.createdate < 2010-11-11 00:00:00 GMT" >> 10.txt
done
