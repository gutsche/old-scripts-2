#!/bin/bash
./createRecontructionProject --project_name $1 --parameter_set reconstruction.cfg --events $2 --jobs $3 --dataset_cff RelVal120Higgs-ZZ-4Mu.cff
