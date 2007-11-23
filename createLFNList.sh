ret=`cat $1`

for aline in $ret; do
       echo "List for dataset $aline"
       python2.4 $DBSCMD_HOME/dbsCommandLine.py -c lsf --url=http://cmssrv46.fnal.gov:8080/DBS/servlet/DBSServlet --path=$aline | grep store | awk '{print $1}'
done
