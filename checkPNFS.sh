#!/bin/sh

#directories='/store/user/ibloch/QCD_Pt_0_15/CMSSW_1_6_12-fakeSkim_CMS2_V00_05_01_v1/'
#directories='/store/user/ibloch/QCD_Pt_15_20/CMSSW_1_6_12-fakeSkim_CMS2_V00_05_01_v1/'
#directories='/store/user/ibloch/QCD_Pt_20_30/CMSSW_1_6_12-fakeSkim_CMS2_V00_05_01_v1/'
#directories='/store/user/ibloch/QCD_Pt_30_50/CMSSW_1_6_12-fakeSkim_CMS2_V00_05_01_v1/'
#directories='/store/user/ibloch/QCD_Pt_50_80/CMSSW_1_6_12-fakeSkim_CMS2_V00_05_01_v1/'
directories='/store/user/ibloch/QCD_Pt_80_120/CMSSW_1_6_12-fakeSkim_CMS2_V00_05_01_v1/'
#directories='/store/user/gutsche/QCD_Pt_120_170/CMSSW_1_6_12-fakeSkim_CMS2_V00_05_01_v1/'
#directories='/store/user/gutsche/QCD_Pt_170_230/CMSSW_1_6_12-fakeSkim_CMS2_V00_05_01_v1/'
#directories='/store/user/gutsche/QCD_Pt_230_300/CMSSW_1_6_12-fakeSkim_CMS2_V00_05_01_v1/'
#directories='/store/user/gutsche/QCD_Pt_300_380/CMSSW_1_6_12-fakeSkim_CMS2_V00_05_01_v1/'
#directories='/store/user/gutsche/QCD_Pt_380_470/CMSSW_1_6_12-fakeSkim_CMS2_V00_05_01_v1/'
#directories='/store/user/gutsche/QCD_Pt_470_600/CMSSW_1_6_12-fakeSkim_CMS2_V00_05_01_v1/'

for dir in $directories
do
	files=`ls -1 /pnfs/cms/WAX/11/$dir | grep root`
	for file in $files
	do
		command=`echo "edmFileUtil -f $dir/$file"`
		echo $command 
	done
done

