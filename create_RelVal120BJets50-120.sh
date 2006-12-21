#!/bin/bash
./createRecontructionProject --project_name $1 --parameter_set reconstruction.cfg --events $2 --jobs $3 --dataset_cff RelVal120BJets50-120.cff
