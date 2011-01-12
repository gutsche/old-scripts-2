dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RAW* and block.createdate >= 2010-01-01 and block.createdate < 2010-02-01" > mc_2010_jan_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM and block.createdate >= 2010-01-01 and block.createdate < 2010-02-01" >> mc_2010_jan_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RECO* and block.createdate >= 2010-01-01 and block.createdate < 2010-02-01" > mc_2010_jan_reco.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = AODSIM and block.createdate >= 2010-01-01 and block.createdate < 2010-02-01" > mc_2010_jan_aod.blocks

dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RAW* and block.createdate >= 2010-02-01 and block.createdate < 2010-03-01" > mc_2010_feb_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM and block.createdate >= 2010-02-01 and block.createdate < 2010-03-01" >> mc_2010_feb_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RECO* and block.createdate >= 2010-02-01 and block.createdate < 2010-03-01" > mc_2010_feb_reco.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = AODSIM and block.createdate >= 2010-02-01 and block.createdate < 2010-03-01" > mc_2010_feb_aod.blocks

dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RAW* and block.createdate >= 2010-03-01 and block.createdate < 2010-04-01" > mc_2010_mar_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM and block.createdate >= 2010-03-01 and block.createdate < 2010-04-01" >> mc_2010_mar_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RECO* and block.createdate >= 2010-03-01 and block.createdate < 2010-04-01" > mc_2010_mar_reco.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = AODSIM and block.createdate >= 2010-03-01 and block.createdate < 2010-04-01" > mc_2010_mar_aod.blocks

dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RAW* and block.createdate >= 2010-04-01 and block.createdate < 2010-05-01" > mc_2010_apr_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM and block.createdate >= 2010-04-01 and block.createdate < 2010-05-01" >> mc_2010_apr_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RECO* and block.createdate >= 2010-04-01 and block.createdate < 2010-05-01" > mc_2010_apr_reco.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = AODSIM and block.createdate >= 2010-04-01 and block.createdate < 2010-05-01" > mc_2010_apr_aod.blocks

dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RAW* and block.createdate >= 2010-05-01 and block.createdate < 2010-06-01" > mc_2010_may_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM and block.createdate >= 2010-05-01 and block.createdate < 2010-06-01" >> mc_2010_may_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RECO* and block.createdate >= 2010-05-01 and block.createdate < 2010-06-01" > mc_2010_may_reco.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = AODSIM and block.createdate >= 2010-05-01 and block.createdate < 2010-06-01" > mc_2010_may_aod.blocks

dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RAW* and block.createdate >= 2010-06-01 and block.createdate < 2010-07-01" > mc_2010_jun_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM and block.createdate >= 2010-06-01 and block.createdate < 2010-07-01" >> mc_2010_jun_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RECO* and block.createdate >= 2010-06-01 and block.createdate < 2010-07-01" > mc_2010_jun_reco.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = AODSIM and block.createdate >= 2010-06-01 and block.createdate < 2010-07-01" > mc_2010_jun_aod.blocks

dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RAW* and block.createdate >= 2010-07-01 and block.createdate < 2010-08-01" > mc_2010_jul_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM and block.createdate >= 2010-07-01 and block.createdate < 2010-08-01" >> mc_2010_jul_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RECO* and block.createdate >= 2010-07-01 and block.createdate < 2010-08-01" > mc_2010_jul_reco.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = AODSIM and block.createdate >= 2010-07-01 and block.createdate < 2010-08-01" > mc_2010_jul_aod.blocks

dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RAW* and block.createdate >= 2010-08-01 and block.createdate < 2010-09-01" > mc_2010_aug_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM and block.createdate >= 2010-08-01 and block.createdate < 2010-09-01" >> mc_2010_aug_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RECO* and block.createdate >= 2010-08-01 and block.createdate < 2010-09-01" > mc_2010_aug_reco.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = AODSIM and block.createdate >= 2010-08-01 and block.createdate < 2010-09-01" > mc_2010_aug_aod.blocks

dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RAW* and block.createdate >= 2010-09-01 and block.createdate < 2010-10-01" > mc_2010_sep_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM and block.createdate >= 2010-09-01 and block.createdate < 2010-10-01" >> mc_2010_sep_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RECO* and block.createdate >= 2010-09-01 and block.createdate < 2010-10-01" > mc_2010_sep_reco.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = AODSIM and block.createdate >= 2010-09-01 and block.createdate < 2010-10-01" > mc_2010_sep_aod.blocks

dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RAW* and block.createdate >= 2010-10-01 and block.createdate < 2010-11-01" > mc_2010_oct_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM and block.createdate >= 2010-10-01 and block.createdate < 2010-11-01" >> mc_2010_oct_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RECO* and block.createdate >= 2010-10-01 and block.createdate < 2010-11-01" > mc_2010_oct_reco.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = AODSIM and block.createdate >= 2010-10-01 and block.createdate < 2010-11-01" > mc_2010_oct_aod.blocks

dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RAW* and block.createdate >= 2010-11-01 and block.createdate < 2010-12-01" > mc_2010_nov_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM and block.createdate >= 2010-11-01 and block.createdate < 2010-12-01" >> mc_2010_nov_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RECO* and block.createdate >= 2010-11-01 and block.createdate < 2010-12-01" > mc_2010_nov_reco.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = AODSIM and block.createdate >= 2010-11-01 and block.createdate < 2010-12-01" > mc_2010_nov_aod.blocks

dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RAW* and block.createdate >= 2010-12-01 and block.createdate < 2011-01-01" > mc_2010_dec_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM and block.createdate >= 2010-12-01 and block.createdate < 2011-01-01" >> mc_2010_dec_raw.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = GEN-SIM-RECO* and block.createdate >= 2010-12-01 and block.createdate < 2011-01-01" > mc_2010_dec_reco.blocks
dbs search --noheader --production --query="find block,block.size,block.numevents,block.createdate where tier = AODSIM and block.createdate >= 2010-12-01 and block.createdate < 2011-01-01" > mc_2010_dec_aod.blocks








# cat mc_2010_oct_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | awk -F\/ '{print $3}' | sort -u
# cat mc_2010_oct_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | awk -F\/ '{print $3}' | sort -u
# cat mc_2010_oct_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | awk -F\/ '{print $3}' | sort -u
# 
# 
# cat mc_2010_oct_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -vi rereco | grep -v 'V10-v' | grep -v 'V10A-v' | grep -v 'V9-v' | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024" Events: "SUM2}'
# 


cat mc_2010_jan_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | awk -F\/ '{print $3}' | sort -u
cat mc_2010_jan_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | awk -F\/ '{print $3}' | sort -u
cat mc_2010_jan_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | awk -F\/ '{print $3}' | sort -u

cat mc_2010_jan_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_jan_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_jan_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'

cat mc_2010_feb_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | awk -F\/ '{print $3}' | sort -u
cat mc_2010_feb_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v V16 | awk -F\/ '{print $3}' | sort -u
cat mc_2010_feb_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v V16 | awk -F\/ '{print $3}' | sort -u

cat mc_2010_feb_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_feb_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v V16 | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_feb_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v V16 | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'

cat mc_2010_mar_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | awk -F\/ '{print $3}' | sort -u
cat mc_2010_mar_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -vi rereco | awk -F\/ '{print $3}' | sort -u
cat mc_2010_mar_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -vi rereco | awk -F\/ '{print $3}' | sort -u

cat mc_2010_mar_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_mar_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -vi rereco | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_mar_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -vi rereco | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'

cat mc_2010_apr_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | awk -F\/ '{print $3}' | sort -u
cat mc_2010_apr_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -vi rereco | awk -F\/ '{print $3}' | sort -u
cat mc_2010_apr_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -vi rereco | awk -F\/ '{print $3}' | sort -u

cat mc_2010_apr_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_apr_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -vi rereco | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_apr_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -vi rereco | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'

cat mc_2010_may_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | awk -F\/ '{print $3}' | sort -u
cat mc_2010_may_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -vi rereco | awk -F\/ '{print $3}' | sort -u
cat mc_2010_may_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -vi rereco | awk -F\/ '{print $3}' | sort -u

cat mc_2010_may_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_may_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -vi rereco | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_may_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -vi rereco | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'

cat mc_2010_jun_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -v SP10 | awk -F\/ '{print $3}' | sort -u
cat mc_2010_jun_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -v SP10 | grep -vi rereco | awk -F\/ '{print $3}' | sort -u
cat mc_2010_jun_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -v SP10 | grep -vi rereco | awk -F\/ '{print $3}' | sort -u

cat mc_2010_jun_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -v SP10 | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_jun_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -v SP10 | grep -vi rereco | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_jun_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -v SP10 | grep -vi rereco | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'

cat mc_2010_jul_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -v SP10 | awk -F\/ '{print $3}' | sort -u
cat mc_2010_jul_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -v SP10 | grep -vi rereco | awk -F\/ '{print $3}' | sort -u
cat mc_2010_jul_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -v SP10 | grep -vi rereco | awk -F\/ '{print $3}' | sort -u

cat mc_2010_jul_raw.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -v SP10 | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_jul_reco.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -v SP10 | grep -vi rereco | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
cat mc_2010_jul_aod.blocks | grep -v '/CMSSW_' | grep -vi test | grep -vi preprod | grep -v Jan29 | grep -v S09 | grep -v SP10 | grep -vi rereco | awk '{SUM1+=$2} {SUM2+=$3} END {print "October 2010: Size [TiB]: "SUM1/1024/1024/1024/1024" Events: "SUM2}'
