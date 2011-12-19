#!/bin/bash
dbs --query="find sum(block.size) where dataset = $1" | awk '{print $1/1000000000000}'
echo "RECO"
dbs --query="find sum(block.numevents) where dataset = $1/RECO"
echo "AOD"
dbs --query="find sum(block.numevents) where dataset = $1/AOD"
echo "DQM"
dbs --query="find sum(block.numevents) where dataset = $1/DQM"


