#!/bin/bash

for tar in $*
do
name=`echo $tar | sed -e 's/.tar.gz//'`
mkdir $name
cd $name
tar xzf ../$tar
cd ..
done
