#!/usr/bin/env perl

##H Prints a summary of the space usage on any given site, separated into different release cycles.
##H If no site is given, it will display the summary for all T1 MSS nodes.
##H
##H Usage:
##H   T1CustodialSummary.pl -db DBCONFIG --site=T1_SITE_NAME --datatier=DATATIER
##H
##H Examples:
##H   T1CustodialSummary.pl -db /data/DBAccessInfo/DBParam:Prod/Reader --site=T1_US_FNAL_MSS --datatier=GEN-SIM-RECO
##H

# Process command line arguments.
use Getopt::Long;
use PHEDEX::Core::Help;
use PHEDEX::Core::DB;
use PHEDEX::Core::Timing;
&GetOptions ("db=s"          => \$args{DBCONFIG},
	     "site=s" => \$args{SITE},
	     "datatier=s" => \$args{DATATIER},
	     "help|h"        => sub { &usage() });

unless ($args{DBCONFIG}) {
    die "Error: The database was not specified. \n";
}

my $site = "T%_MSS";
if ($args{SITE}) {
    $site = $args{SITE};
}

my $datatier = "";
if ($args{DATATIER}) {
    $datatier = $args{DATATIER};
}

##############################################################################
#LFN string match
##############################################################################
my $lfnPattern = "/store/data";
#my $lfnPattern = "/store/mc";

##############################################################################
#Create List of release cycles / dataset sample types 
##############################################################################
my @releaseCycles;

# #MC
push(@releaseCycles,"Summer08");
push(@releaseCycles,"Fall08");
push(@releaseCycles,"Winter09");
push(@releaseCycles,"Summer09");
push(@releaseCycles,"Spring10");
push(@releaseCycles,"Summer10");
push(@releaseCycles,"Fall10");
push(@releaseCycles,"Winter10");
push(@releaseCycles,"Spring11");
push(@releaseCycles,"Summer11");
push(@releaseCycles,"Fall11");
push(@releaseCycles,"StoreResults");
push(@releaseCycles,"JobRobot");

#Cosmics
push(@releaseCycles,"GlobalMar08");
push(@releaseCycles,"CRUZET1");
push(@releaseCycles,"CRUZET2");
push(@releaseCycles,"CRUZET3");
push(@releaseCycles,"CRUZET4");
push(@releaseCycles,"EW35");
push(@releaseCycles,"CRUZET09");
push(@releaseCycles,"CRAFT09");

#DATA
push(@releaseCycles,"BeamCommissioning08");
push(@releaseCycles,"Commissioning08");
push(@releaseCycles,"BeamCommissioning09");
push(@releaseCycles,"Commissioning09");
push(@releaseCycles,"Commissioning10");
push(@releaseCycles,"Run2010A");
push(@releaseCycles,"Run2010B");
push(@releaseCycles,"HIRun2010");
push(@releaseCycles,"Run2011A");
push(@releaseCycles,"Run2011B");


for($releaseCycleIndex=0; $releaseCycleIndex < scalar(@releaseCycles); $releaseCycleIndex++) {
    print "@releaseCycles[$releaseCycleIndex]", "\n";
}

##############################################################################
#Create List of datatiers 
##############################################################################
my @datatierList;
if ($datatier eq "") {
    push(@datatierList, "RAW");
    push(@datatierList, "RECO");
    push(@datatierList, "ALCARECO");
    push(@datatierList, "DQM");
    push(@datatierList, "RAW-RECO");
    push(@datatierList, "USER");
    push(@datatierList, "GEN-SIM");
    push(@datatierList, "GEN-RAW");
    push(@datatierList, "GEN-SIM-RAW");
    push(@datatierList, "GEN-SIM-RECO");
    push(@datatierList, "AODSIM");
    push(@datatierList, "GEN-SIM-RAWDEBUG");
    push(@datatierList, "GEN-SIM-RECODEBUG");
} else {
    push(@datatierList, $datatier);
}
print "DataTier = $datatier\n";

my $self = { DBCONFIG => $args{DBCONFIG} };
my $dbh = &connectToDatabase ($self);
my $sql;

##############################################################################
#Get List of sites matching the string given
##############################################################################
my @sites;

my $sql_findSites = qq{ select T_ADM_NODE.NAME from T_ADM_NODE where 
			    T_ADM_NODE.NAME like '$site' };

my $q = &dbprep($dbh, $sql_findSites);
chomp;
&dbbindexec($q);

#add all existing datasets
while ($data = $q->fetchrow()) {
    push(@sites,$data);
}

for ($siteIndex=0; $siteIndex < scalar(@sites); $siteIndex++) {
    print "***********************************************************************\n";
    print "SITE : @sites[$siteIndex]", "\n";
    print "***********************************************************************\n";
    print "Acquisition Era, DataTier , TotalData [TB] , CustodialData [TB], nonCustodialData [TB] , TotalMC [TB] , CustodialMC [TB], nonCustodialMC [TB] \n";

    for($releaseCycleIndex=0; $releaseCycleIndex < scalar(@releaseCycles); $releaseCycleIndex++) {
	
	for($datatierIndex=0; $datatierIndex < scalar(@datatierList); $datatierIndex++) {
	    
	    #declare variables
	    my $totalDataTB = 0;
	    my $custodialDataTB = 0;
	    my $totalMCTB = 0;
	    my $custodialMCTB = 0;


	    my $regExpression = '%' . $releaseCycles[$releaseCycleIndex] . '%/' . $datatierList[$datatierIndex] . '#%';

	    my $sql_findBlockSubscriptions = qq{ select T_DPS_BLOCK.BYTES, T_DPS_BLOCK.NAME, T_DPS_BLOCK_REPLICA.IS_CUSTODIAL from T_DPS_BLOCK, T_DPS_BLOCK_REPLICA, T_ADM_NODE, T_DPS_SUBS_BLOCK where 
					 T_ADM_NODE.NAME = ? 
					 and T_DPS_BLOCK_REPLICA.NODE = T_ADM_NODE.ID 
					 and T_DPS_BLOCK_REPLICA.BLOCK = T_DPS_BLOCK.ID 
					 and T_DPS_SUBS_BLOCK.BLOCK = T_DPS_BLOCK.ID
					 and T_DPS_SUBS_BLOCK.DESTINATION = T_ADM_NODE.ID
					 and T_DPS_BLOCK.NAME like ? };

	    my $q = &dbprep($dbh, $sql_findBlockSubscriptions);

	    $q->bind_param(1 , @sites[$siteIndex]);
	    $q->bind_param(2 , $regExpression);

	    chomp;
	    &dbbindexec($q);

	    
	    while (@data = $q->fetchrow_array()) {
		#$totalTB = $totalTB + $data[0] / (1000*1000*1000*1000);
		#print "$pass : BLOCK : $data[0] : $data[1] , custodial : $data[2]      ,  $totalTB \n";
		my $sql_matchLFN = qq{ select T_DPS_FILE.LOGICAL_NAME from T_DPS_BLOCK, T_DPS_FILE where 
					   T_DPS_FILE.INBLOCK = T_DPS_BLOCK.ID  
					   and T_DPS_BLOCK.NAME = ? and ROWNUM < 2 };

		my $q1 = &dbprep($dbh, $sql_matchLFN);
		$q1->bind_param(1 , $data[1]);
		chomp;
		&dbbindexec($q1);

		my $class = -1;	    
		while ($result = $q1->fetchrow_array()) {
		    #print "MATCH : $result \n";
		    if ($result =~ "/store/data/" || $result =~ "/store/hidata/") {
			$class = 1;
		    } elsif ($result =~ "/store/mc/") {
			$class = 2;
		    }
		    last;
		}
		if ($class == 1) {
		    $totalDataTB = $totalDataTB + $data[0] / (1000*1000*1000*1000);
		    if ($data[2] eq "y") {
			$custodialDataTB = $custodialDataTB + $data[0] / (1000*1000*1000*1000);
		    }
		    #print "Data : BLOCK : $data[0] : $data[1] \n";
		} elsif ($class == 2) {
		    $totalMCTB = $totalMCTB + $data[0] / (1000*1000*1000*1000);
		    if ($data[2] eq "y") {
			$custodialMCTB = $custodialMCTB + $data[0] / (1000*1000*1000*1000);
		    }
		    #print "MC : BLOCK : $data[0] : $data[1] \n";
		}
	    }



# 	    my $sql_findCustodialBlocks = qq{ select T_DPS_BLOCK.BYTES, T_DPS_BLOCK.NAME from T_DPS_BLOCK, T_DPS_BLOCK_REPLICA, T_ADM_NODE where 
# 						  T_ADM_NODE.NAME = '@sites[$siteIndex]' 
# 						  and T_DPS_BLOCK_REPLICA.NODE = T_ADM_NODE.ID 
# 						  and T_DPS_BLOCK_REPLICA.BLOCK = T_DPS_BLOCK.ID 
# 						  and T_DPS_BLOCK_REPLICA.IS_CUSTODIAL = 'y'
# 						  and T_DPS_BLOCK.NAME like '%$releaseCycles[$releaseCycleIndex]%$datatierList[$datatierIndex]%'};

# 	    my $q = &dbprep($dbh, $sql_findCustodialBlocks);
# 	    chomp;
# 	    &dbbindexec($q);

	    
# 	    while (@data = $q->fetchrow_array()) {
# 		#$custodialTB = $custodialTB + $data[0] / (1000*1000*1000*1000);
# 		#print "$pass : BLOCK : $data[0] : $data[1]         ,  $custodialTB \n";
# 		my $sql_matchLFN2 = qq{ select T_DPS_FILE.LOGICAL_NAME from T_DPS_BLOCK, T_DPS_FILE where 
# 					    T_DPS_FILE.INBLOCK = T_DPS_BLOCK.ID
# 					    and T_DPS_BLOCK.NAME = ?  
# 					    and T_DPS_FILE.LOGICAL_NAME like '%$lfnPattern%' and ROWNUM < 2 };
		
# 		my $q2 = &dbprep($dbh, $sql_matchLFN2);
# 		$q2->bind_param(1 , $data[1]); 
# 		chomp;
# 		&dbbindexec($q2);
		

# 		my $class = -1;	    
# 		while ($result = $q2->fetchrow_array()) {
# 		    #print "MATCH : $result \n";
# 		    if ($result =~ "/store/data/") {
# 			$class = 1;
# 		    } elsif ($result =~ "/store/mc/") {
# 			$class = 2;
# 		    }
# 		    last;
# 		}
# 		if ($class == 1) {
# 		    $custodialDataTB = $custodialDataTB + $data[0] / (1000*1000*1000*1000);
# 		    #print "Data : BLOCK : $data[0] : $data[1] \n";
# 		} elsif ($class == 2) {
# 		    $custodialMCTB = $custodialMCTB + $data[0] / (1000*1000*1000*1000);
# 		    #print "MC : BLOCK : $data[0] : $data[1] \n";
# 		}	    
# 	    }

	    my $nonCustodialDataTB =  $totalDataTB - $custodialDataTB;
	    my $nonCustodialMCTB =  $totalMCTB - $custodialMCTB;

	    my $totalDataString = sprintf('%.3f', $totalDataTB);
	    my $custodialTotalDataString = sprintf('%.3f', $custodialDataTB);
	    my $nonCustodialTotalDataString = sprintf('%.3f', $nonCustodialDataTB);
	    my $totalMCString = sprintf('%.3f', $totalMCTB);
	    my $custodialTotalMCString = sprintf('%.3f', $custodialMCTB);
	    my $nonCustodialTotalMCString = sprintf('%.3f', $nonCustodialMCTB);

	    print "$releaseCycles[$releaseCycleIndex], $datatierList[$datatierIndex] , $totalDataString , $custodialTotalDataString , $nonCustodialTotalDataString, $totalMCString, $custodialTotalMCString , $nonCustodialTotalMCString \n";	    
	}
    }
    print "\n\n";
}

&disconnectFromDatabase ($self, $dbh, 1);
