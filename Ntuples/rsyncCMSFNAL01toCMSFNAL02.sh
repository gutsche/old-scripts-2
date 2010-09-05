#!/bin/bash
# execute on cmsfnal02 as cms1 in /storage/local/data2/cms1/cms2
rsync  -urLptgoD -v -h cmsfnal01.fnal.gov:/storage/local/data2/cms1/cms2/ .
