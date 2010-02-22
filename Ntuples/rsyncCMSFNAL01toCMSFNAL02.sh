#!/bin/bash
# execute on cmsfnal02 as cms1 in /storage/local/data2/cms1/cms2
rsync -a -i --ignore-existing cmsfnal01.fnal.gov:/storage/local/data2/cms1/cms2/ .
