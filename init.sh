#echo "CMS2 CMSSW_1_6_12 configuration INGO"
#orig=`echo $PWD`
#. /uscmst1/prod/sw/cms/shrc prod
#
#cd /uscms/home/ibloch/FakeE_Ntuples_1_6_12/CMSSW_1_6_12/src
#eval `scramv1 runtime -sh`
#cd /uscms/home/gutsche/work/software/TAS/fakeSkims
#source /uscms/home/gutsche/work/software/CRAB/CRAB/crab.sh
#export DBS_CLIENT_CONFIG=/uscms/home/gutsche/work/software/CRAB/CRAB/external/DBSAPI/DBSAPI/dbs.config
#export X509_USER_PROXY=/uscms/home/gutsche/tmp.txt
#cd $orig

echo "CMS2 CMSSW_1_6_12 configuration"
. /uscmst1/prod/sw/cms/shrc prod
cd /uscms/home/gutsche/work/software/TAS/CMSSW_1_6_12/src
eval `scramv1 runtime -sh`

