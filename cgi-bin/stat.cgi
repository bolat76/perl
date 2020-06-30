#!/usr/bin/perl

print "Content-Type: text/html\n";
#######################################################################################
######### defining initial data
#######################################################################################
srand();

$b1 = '<b>'; $b2 = '</b>'; $u1 = '<u>'; $u2 = '<u2>';
$rf = '<font color = red>'; $f2 = '</font>'; $cnt = 0; $ac = "align = 'center'";
$ct1 = '</center>'; $ct2 = '</center>'; $hr = '<hr>'; $br = '<br>';
$yelclr = 'bgcolor = Khaki'; $yelclr1 = 'bgcolor = LemonChiffon';
$bluclr = 'bgcolor = skyblue'; $redclr = 'bgcolor = #8a8ac1;';
$timedatenow = scalar localtime;
$timedatenow =~s/  / /g;
($weekdaynow, $monthnow, $daynow, $timenow, $yearnow) = split(/ /, $timedatenow);
if($daynow < 10){$daynow = '0' . $daynow;}
($hournow, $minutenow, $secondnow) = split(/:/, $timenow);
$ai{'Jan'} = '01'; $ai{'Feb'} = '02'; $ai{'Mar'} = '03';
$ai{'Apr'} = '04'; $ai{'May'} = '05'; $ai{'Jun'} = '06';
$ai{'Jul'} = '07'; $ai{'Aug'} = '08'; $ai{'Sep'} = '09';
$ai{'Oct'} = '10'; $ai{'Nov'} = '11'; $ai{'Dec'} = '12';
####################### cookie part ###############################
$ai{'12'} = 'Jan'; $ai{'04'} = 'May'; $ai{'08'} = 'Sep';
$ai{'01'} = 'Feb'; $ai{'05'} = 'Jun'; $ai{'09'} = 'Oct';
$ai{'02'} = 'Mar'; $ai{'06'} = 'Jul'; $ai{'10'} = 'Nov';
$ai{'03'} = 'Apr'; $ai{'07'} = 'Aug'; $ai{'11'} = 'Dec';
@ailartizimi = ('01', '02', '03','04', '05', '06', '07', '08', '09', '10', '11', '12');
$ekiaialga = int($ai{$monthnow}) + 1; $ekiaialga = "$daynow.$ailartizimi[$ekiaialga].$yearnow";
$datenow = "$daynow.$ai{$monthnow}.$yearnow";
$shortyearnow = substr($yearnow, 2, 2);
$timestamp = $shortyearnow . $ai{$monthnow} . $daynow . $hournow . $minutenow . $secondnow;
$timestamp1 = $hournow . $minutenow . $secondnow;
$nxtmonth = $ai{$monthnow};
$nxtmonth = $ai{$nxtmonth};
#$live_time='Mon, 31-Jul-2009 12:00:00 GMT';
if($nxtmonth =~ /Jan/){$yearnow++;}
$live_time="$weekdaynow, $daynow\-$nxtmonth\-$yearnow $timenow GMT";
if($nxtmonth =~ /Jan/){$yearnow--;}
$userip = $ENV{'REMOTE_ADDR'};
 @getcookies = split (/; /,$ENV{'HTTP_COOKIE'});
 foreach(@getcookies){
        $hotcookie = $_;
        ($cookiekey, $cookieval) = split (/=/,$hotcookie);
        $cookies{$cookiekey} = $cookieval;
        if($cookiekey =~ /openenglishproject/){$gotcookie = $hotcookie; }
    }
#$gotcookie = $ENV{'HTTP_COOKIE'};
$cookie_file = '../oedata/cookies.txt';
$users_file = '../oedata/oe_usrdata.txt';
$accesslevel = 8;
$cookiemaxamount = 50;
###################### end of cookie part #########################
$oe_folder = '../oedata/';
$upload_folder = '../oedata/';
$groups_folder = '../oedata/groups/';
$oe_sl_balls_file = '../oedata/oe_sl_balls_data.txt';
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$glMonthPayValue = 5500;
$indexcgi = 'stat.cgi';
$students_file = $oe_folder . 'students.txt';
$leaders_file = $oe_folder . 'leaders.txt';
$adminText_file = $oe_folder . 'admin.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpgroupcgi = 'http://accelerator.kvadra.kz/cgi-bin/group.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Read lists';

open(INF, $cookie_file); @cookielist = <INF>; close(INF); foreach $i(@cookielist){
    chomp($i); #8<tab>8250732421875<tab>Tue Apr 23 14:16:01 2013<tab>172.28.113.66<tab>reserve
    ($clusrnum, $clusrrnd, $clusrdate, $clusrip, @other) = split (/<tab>/, $i);
    $oeusercookiernd{$clusrnum} = $clusrrnd;
    $oeusercookiedate{$clusrnum} = $clusrdate;
    $oeusercookieip{$clusrnum} = $clusrip;
}

open(INF, $leaders_file); @leaderslist = <INF>; close(INF); foreach $i(@leaderslist){
   # No<tab>Uniques ID<tab>1st name<tab>2nd name<tab>3rd name<tab>PWD<tab>School ID<tab>Group ID<tab>Phone Num<tab>Email<tab>Date<tab>Reserve
   #$ldrnum<tab>$ldrID<tab>$ldr1stname<tab>$ldr2ndname<tab>$ldr3rdname<tab>$ldrpwd<tab>$userschool<tab>$usergroup<tab>$other
   ($tldrnum, $tldrid, $tldrfirstnam, $tldrscndnam, $tldrthrdnam, $tldrpwd, $tldrschl, $tldrgrp, $tldrphn, $tldremail,
    $tldrdate, $tldrbrthday, $tldrgender, $tldrwrkplc, $tldrprsnid, $tldrindvdid, @other) = split (/<tab>/, $i);
   if ( $tldrnum ne '' && $tldrid ne '' ) { $glLastLeaderNumber = $tldrnum; $glLastLeaderCode = $tldrid; }
   if($tldrid ne ''){  $LeaderFullName{$tldrid} = "$tldrfirstnam $tldrscndnam $tldrthrdnam"; $tldremail = lc $tldremail;
      $LeaderUniqueId{$tldrid} = $tldrid; $LeaderFirstName{$tldrid} = $tldrfirstnam; $LeaderSecondName{$tldrid} = $tldrscndnam;
      $LeaderThirdName{$tldrid} = $tldrthrdnam; $LeaderPositionNum{$tldrid} = $tldrnum;   $LeaderSchoolNum{$tldrid} = $tldrschl;
      $LeaderGroupNum{$tldrid} = $tldrgrp; $LeaderPhoneNum{$tldrid} = $tldrphn; $LeaderEmail{$tldrid} = $tldremail; 
      $LeaderBirthDay{$tldrid} = $tldrbrthday; $LeaderGender{$tldrid} = $tldrgender; $LeaderWorkPlace{$tldrid} = $tldrwrkplc;
      $LeaderPersonId{$tldrid} = $tldrprsnid; $LeaderIndividId{$tldrid} = $tldrindvdid; $LeaderPassWord{$tldrid} = $tldrpwd;
   }
}  # $existSchool{$tldrschl}; $existGroup{$tldrgrp}; $GroupsPerSchool{$tldrschl}; $totalLeaders ;$totalSchools; $totalGroups

@uniqueSchoolNumList = "";  @uniqueGroupNumList = "";  @studentUniqueNumList = "";
open(INF, $students_file); @studentslist = <INF>;  close(INF); foreach $i(@studentslist){ 
   #1<tab>56BC4567<tab>Томирис<tab>Толенді<tab><tab>71<tab>71-1-M1
   #$usernum<tab>$userID<tab>$user1stname<tab>$user2ndname<tab>$user3rdname<tab>$userschool<tab>$usergroup<tab>$other
   ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp, @other) = split (/<tab>/, $i);
   if ( $tstudid =~ /56BC/ ) { $studentFullName{$tstudid} = "$tstudfirstnam $tstudthrdnam $tstudscndnam"; }
   if ( $tstudgrp ne '' && $tstudschl ne '' ) {
      $studentFirstName{$tstudid} = $tstudfirstnam; $studentSecondName{$tstudid} = $tstudscndnam;
      $studentThirdName{$tstudid} = $tstudthrdnam; $studentPositionNum{$tstudid} = $tstudnum; 
      $studentSchoolNum{$tstudid} = $tstudschl; $studentGroupNum{$tstudid} = $tstudgrp;     $existSchool{$tstudschl}++;  $existGroup{$tstudgrp}++; 
      if ( grep( /^$tstudschl$/, @uniqueSchoolNumList ) ) { $done = 1; } else { push(@uniqueSchoolNumList, $tstudschl); $totalSchools++; }
      if ( grep( /^$tstudgrp$/, @uniqueGroupNumList ) ) { $done = 1;} 
      else { $GroupsPerSchool{$tstudschl}++; $totalGroups++; push(@uniqueGroupNumList, $tstudgrp); $groupSchoolNum{$tstudgrp} = $tstudschl; }
      push(@studentUniqueNumList, $tstudid); $totalStudents++;
   }
}  # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents ;$totalSchools; $totalGroups

open(INF, $users_file); @userlist = <INF>; close(INF); foreach $i(@userlist){ 
          #1<tab>user1<tab>6<tab>777<tab>13.03.2013<tab>rest
          #$usernum<tab>$username<tab>$userlevel<tab>$userpwd<tab>$other
          ($tusrnum, $tusrnam, $tusrlvl, $tusrpwd, @other) = split (/<tab>/, $i);
          $username{$tusrnum} = $tusrnam; $userpwd{$tusrnum} = $tusrpwd;
          ($userfirstname{$tusrnum}, $userlastname{$tusrnum}) = split(/ /, $tusrnam);
          $userlevel{$tusrnum} = $tusrlvl; $usernumber{$tusrnum} = $tusrnum;
          $usernumber{$tusrnam} = $tusrnum;
          $userslist++;
          push(@loginuserslist, $tusrnam);
}
$cnt = 0;

open(INF, $oe_sl_balls_file); @OpEnSocLiftBallsList = <INF>; close(INF); 

#######################################################################################
######### getting Envirement queries
#######################################################################################

if($ENV{'REQUEST_METHOD'} eq 'GET'){$value=$ENV{'QUERY_STRING'};}
elsif($ENV{'REQUEST_METHOD'} eq 'POST'){sysread(STDIN,$value,$ENV{'CONTENT_LENGTH'});}

@values = split(/\&/, $value);
 foreach $i (@values) {
  ($varname, $mydata) = split(/=/,$i); 
  $mydata =~s/\+/ /g;
  $mydata =~s/%([0-9A-H]{2})/pack('C',hex($1))/ge;
  $whatis{$varname} = $mydata;
}

#######################################################################################
############### check COOKIES and LOG actions ###########################################
#######################################################################################
&checkcookies(); print "\n";
if($userbrowser eq 'desktop'){ &printfile($bas, $title);}
else {&printfile($basm, $title);}

if ( $whatis{'action'} ne '' ) { open(GURD,">>$log_file");
print GURD "Time: [$timedatenow] User ID: [$gotusrid] IP address: [$userip] User action: [$whatis{'action'}] Script: [$indexcgi] \n";
close(GURD); }

#####################################################################################
############################ LOGIN CHECK PART #######################################
#####################################################################################
print "<p>";
if($userlogged == 1){
    print "Hello $b1 $userfirstname{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>";
    if ( $whatis{'action'} eq 'get' && $whatis{'studid'} =~ /56BC/ ) { &getListOfGroupSub(); }
    elsif ( $whatis{'action'} eq 'show' && $whatis{'studid'} =~ /56BC/ && $whatis{'groupid'} ne '' ) { &showStudentStatsSub(); }
    &openBlankPageSub(); 
}
else{
    if($whatis{'action'} eq 'logout'){$donothing = 1;}
    print "$errorlogin<form method='post' action=\'$indexcgi\'><input type = 'hidden' name = 'action' value = 'login'>\n";
    print "<SELECT name = 'usernamenumber' CLASS = 'drop'><OPTION>Login</OPTION>\n";
    $tusernumber = 1; $userlogged = 0;
    @loginuserslist = sort(@loginuserslist);
    foreach $loggeduser (@loginuserslist){
        if(length($loggeduser) > 0){
             print "<OPTION VALUE=\'$usernumber{$loggeduser}\'>$loggeduser</OPTION>\n";
        }
    }
    print "</select><input type = 'password'  name = 'userpwd'>\n";
    print "$br<input type='reset' value = 'Reset'> <input type = 'submit' value = 'Enter'></form>\n";
}

#####################################################################################
######################### GET LIST OF GROUPS SUB ####################################
#####################################################################################
sub getListOfGroupSub { $glgStudId = $whatis{'studid'}; $glgCnt = 0; $myclr = $yelclr;
   foreach $glgGrpId (@uniqueGroupNumList) { $whatis{'groupid'} = $glgGrpId; &getLessonSub(); 
      # $glsUserID_GrpNm = $glsUserID . '_' . $glsgrpfile; $OEP_PartTxt{$glsUserID_GrpNm} = 'true';
      $glgStudId_GrpId = $glgStudId . '_' . $glgGrpId;
      if ( $OEP_PartTxt{$glgStudId_GrpId} eq 'true' ) { push (@glgFndGrpList, $glgGrpId); }
   }
   print "<p> </p><h2>Перечень групп ученика</h2><p> </p>
   <table><caption><h3>ID $glgStudId</h3></caption><tr $yelclr><td>No</td><td>Name</td><td>Student ID</td><td>Group ID</td></tr>\n";
   foreach $glgGrpId (@glgFndGrpList) { $glgCnt++;
      if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
      print "<tr $myclr><td>$glgCnt</td><td>$studentFullName{$glgStudId}</td><td $ac>[ $glgStudId ]</td>
      <td><a href = \'$httpindexcgi\?action=show\&studid\=$glgStudId\&groupid\=$glgGrpId\'>$glgGrpId</a></td></tr>\n";
   }
   print "</table>\n";
}

#####################################################################################
########################### OPEN BLANK PAGE SUB #####################################
#####################################################################################
sub openBlankPageSub { &printJavaScript();
   print "<p> </p><h3>Укажите номер ученика чтобы вывести статистику</h3><p> </p>
   <form method='post' action=\'$httpindexcgi\' onsubmit='return checkFunction();'>
   <input type = 'hidden' name = 'action' value = 'get'>
   <table><tr $yelclr><td>Введите номер ученика: </td>
   <td><input type = 'text' name = 'studid' value = ''></td></tr>
   <tr $yelclr1><td $ac><input type = 'reset' value = 'Reset'></td>
   <td $ac><input type = 'submit' value = 'Enter'></td></tr></table></form>\n";
}

#####################################################################################
########################### SHOW STUDENT STATS SUB ##################################
#####################################################################################
sub showStudentStatsSub { $sssStdId = $whatis{'studid'}; $sssGrpId = $whatis{'groupid'}; $sssCnt = 0;
   &getGroupSub(); $sssGrpCost = $glMonthPayValue * 2; $sssPayIndx = $sssStdId . '<tab>' . $sssGrpId; 
   if ( $sssGrpId =~ /M0/ ) { 
      if ( $glPayOneDate{$sssPayIndx} ne '' ) { $sssPayStat = '1. ' . $glPayOneDate{$sssPayIndx} . ' – 5 500 тг</br>'; }
      if ( $glPayTwoDate{$sssPayIndx} ne '' ) { $sssPayStat = $sssPayStat . '2. ' . $glPayTwoDate{$sssPayIndx} . ' – 5 500 тг</br>'; }
      $sssGrpCapTxt = 'Отчет по итогам модуля "StartUp"'; $sssGrpLssAmnt = 18; }
   elsif ( $sssGrpId =~ /M1/ ) { 
      if ( $glPayOneDate{$sssPayIndx} ne '' ) { $sssPayStat = '1. ' . $glPayOneDate{$sssPayIndx} . ' – 5 500 тг</br>'; }
      if ( $glPayTwoDate{$sssPayIndx} ne '' ) { $sssPayStat = $sssPayStat . '2. ' . $glPayTwoDate{$sssPayIndx} . ' – 5 500 тг</br>'; }
      $sssGrpCapTxt = 'Отчет по итогам 1-го модуля'; $sssGrpLssAmnt = 18; }
   elsif ( $sssGrpId =~ /M2/ ) { 
      if ( $glPayOneDate{$sssPayIndx} ne '' ) { $sssPayStat = '1. ' . $glPayOneDate{$sssPayIndx} . ' – 5 500 тг</br>'; }
      if ( $glPayTwoDate{$sssPayIndx} ne '' ) { $sssPayStat = $sssPayStat . '2. ' . $glPayTwoDate{$sssPayIndx} . ' – 5 500 тг</br>'; }
      if ( $glPayThreeDate{$sssPayIndx} ne '' ) { $sssPayStat = $sssPayStat .'3. ' . $glPayThreeDate{$sssPayIndx} . ' – 5 500 тг</br>'; }
      if ( $glPayFourDate{$sssPayIndx} ne '' ) { $sssPayStat = $sssPayStat . '4. ' . $glPayFourDate{$sssPayIndx} . ' – 5 500 тг</br>'; }
      $sssGrpCapTxt = 'Отчет по итогам 2-го модуля'; $sssGrpCost = $sssGrpCost * 2; $sssGrpLssAmnt = 30; }
   elsif ( $sssGrpId =~ /M3/ ) { 
      if ( $glPayOneDate{$sssPayIndx} ne '' ) { $sssPayStat = '1. ' . $glPayOneDate{$sssPayIndx} . ' – 5 500 тг</br>'; }
      if ( $glPayTwoDate{$sssPayIndx} ne '' ) { $sssPayStat = $sssPayStat . '2. ' . $glPayTwoDate{$sssPayIndx} . ' – 5 500 тг</br>'; }
      if ( $glPayThreeDate{$sssPayIndx} ne '' ) { $sssPayStat = $sssPayStat .'3. ' . $glPayThreeDate{$sssPayIndx} . ' – 5 500 тг</br>'; }
      if ( $glPayFourDate{$sssPayIndx} ne '' ) { $sssPayStat = $sssPayStat . '4. ' . $glPayFourDate{$sssPayIndx} . ' – 5 500 тг</br>'; }
      $sssGrpCapTxt = 'Отчет по итогам 3-го модуля'; $sssGrpCost = $sssGrpCost * 2; $sssGrpLssAmnt = 30; }
   
   print "<p> </p><h2>Статистика активности ученика</h2><p> </p>
   <table><caption><h3>$sssGrpCapTxt</h3></caption>
   <tr $yelclr><td>Ученик [$sssStdId]: </td><td>$studentFullName{$sssStdId}</td></tr>
   <tr $yelclr1><td>1-ый Волонтер-преподаватель: </td><td>$LeaderFullName{$OEP_VolunteerOneCode{$sssGrpId}}</td></tr>
   <tr $yelclr><td>2-ой Волонтер-преподаватель: </td><td>$LeaderFullName{$OEP_VolunteerTwoCode{$sssGrpId}}</td></tr>
   <tr $yelclr1><td>Тренер: </td><td>$OEP_Traineer{$sssGrpId}</td></tr>
   <tr $yelclr><td>Номер группы: </td><td>$sssGrpId</td></tr>
   <tr $yelclr1><td>Дата начала курса: </td><td>$OEP_StartDate{$sssGrpId}</td></tr>
   <tr $yelclr><td>Дата окончания: </td><td>$OEP_StartDate{$sssGrpId}</td></tr>
   <tr $yelclr1><td>Оплата за курс: </td><td>$sssGrpCost [$sssGrpLssAmnt занятий]</td></tr>
   <tr $yelclr><td>Оплата поступила: </td><td>$sssPayStat</td></tr>
   </table>\n<table><caption><b>Посещаемость:</b></caption>\n<tr $yelclr><td>№ Урока</td>";
   while ( $sssCnt < $sssGrpLssAmnt ) { $sssCnt++; print "<td>$sssCnt</td>"; } $sssCnt = 0;
   print "</tr>\n<tr $yelclr1><td>Посещение</td>"; &getLessonSub();    #@glsLessonNumList, "$i<tab>$glsprnum");
   foreach $sssLessIndx (@glsLessonNumList) { #$glsUserID_PRNum = $glsUserID . '_' . $glsprnum;  $OEP_Participation{$glsUserID_PRNum} = $glsUserPart;
      ($sssLessId, $sssPrjId) = split(/<tab>/, $sssLessIndx); $sssPartIndx = $sssStdId . '_' . $sssPrjId;
      if ( $OEP_Participation{$sssPartIndx} =~ /1/ ) { print "<td bgcolor = 'green'> $sssLessId </td>"; }
      else { print "<td bgcolor = 'red'> 0 </td>"; }
   }
   print "</tr></table>";
}

#####################################################################################
################################# GET GROUP SUB #####################################
#####################################################################################
sub getGroupSub {
   $ggsgrpfile = $groups_folder . $whatis{'groupid'} . '_data.txt'; $ggsid = $whatis{'groupid'};
   open(UPL, $ggsgrpfile);   @ggsprojectlist = <UPL>;   close(UPL);
   foreach $i (@ggsprojectlist){  chomp($i);  if($i =~ /<start of new project = /){ $donothing = 1; }
          elsif($i =~ /OEP_Created: /){$i =~ s/OEP_Created: //g; $OEP_Created{$ggsid} = $i;}
          elsif($i =~ /OEP_Editor: /){$i =~ s/OEP_Editor: //g; $OEP_Editor{$ggsid} = $i;}
          elsif($i =~ /OEP_School: /){$i =~ s/OEP_School: //g; $OEP_School{$ggsid} = $i;}
          elsif($i =~ /OEP_Group: /){$i =~ s/OEP_Group: //g; $OEP_Group{$ggsid} = $i;}
          elsif($i =~ /OEP_Traineer: /){$i =~ s/OEP_Traineer: //g; $OEP_Traineer{$ggsid} = $i;}
          elsif($i =~ /OEP_VolunteerOne: /){$i =~ s/OEP_VolunteerOne: //g; $OEP_VolunteerOne{$ggsid} = $i;}
          elsif($i =~ /OEP_VolunteerOneCode: /){$i =~ s/OEP_VolunteerOneCode: //g; $OEP_VolunteerOneCode{$ggsid} = $i;}
          elsif($i =~ /OEP_VolunteerTwo: /){$i =~ s/OEP_VolunteerTwo: //g; $OEP_VolunteerTwo{$ggsid} = $i;}
          elsif($i =~ /OEP_VolunteerTwoCode: /){$i =~ s/OEP_VolunteerTwoCode: //g; $OEP_VolunteerTwoCode{$ggsid} = $i;}
          elsif($i =~ /OEP_StartDate: /){$i =~ s/OEP_StartDate: //g; $OEP_StartDate{$ggsid} = $i;}
          elsif($i =~ /OEP_FinishDate: /){$i =~ s/OEP_FinishDate: //g; $OEP_FinishDate{$ggsid} = $i;}
          elsif($i =~ /OEP_Paid: /){$i =~ s/OEP_Paid: //g; $OEP_Paid{$ggsid} = $i;}
          elsif($i =~ /OEP_Status: /){$i =~ s/OEP_Status: //g; $OEP_Status{$ggsid} = $i;}
   }
   $gpsPayDataFile = $groups_folder . $whatis{'groupid'} . '_payments.txt'; $glGroupPaidValue{$ggsid} = 0;
   open(INF, $gpsPayDataFile);    @paymentslist = <INF>;    close(INF); 
   foreach $i(@paymentslist){ #1<tab>56BC4703<tab>99-10-M2<tab><tab><tab><tab><tab>reserve
      ($tpaynum, $tpaystudid, $tpaystudgrp, $tpayonedate, $tpaytwodate, $tpaytridate, $tpayfordate, 
      $tpaystatusone, $tpaystatustwo, $tpaystatustri, $tpaystatusfor, @other) = split (/<tab>/, $i);
      $glPayId = $tpaystudid . '<tab>' . $tpaystudgrp;  
      if ( $tpaystudid =~ /56BC/ && $tpaystudgrp ne '' ) {  
         $glPayOneDate{$glPayId} = $tpayonedate;  $glPayTwoDate{$glPayId} = $tpaytwodate;
         $glPayThreeDate{$glPayId} = $tpaytridate;  $glPayFourDate{$glPayId} = $tpayfordate; 
         $glPayStatusOne{$glPayId} = $tpaystatusone; $glPayStatusTwo{$glPayId} = $tpaystatustwo; 
         $glPayStatusTri{$glPayId} = $tpaystatustri; $glPayStatusFor{$glPayId} = $tpaystatusfor;
      }
   }
}

#####################################################################################
############################### GET LESSONS SUB #####################################
#####################################################################################
sub getLessonSub {
      foreach $stdid (@studentUniqueNumList){ if($studentGroupNum{$stdid} =~/$whatis{'groupid'}/){  push(@glsStudentsList, $stdid); } }
      $glsgrpfile = $groups_folder . $whatis{'groupid'} . '.txt';
      open(UPL, $glsgrpfile);
      @glsprojectlist = <UPL>;
      close(UPL);
      @glsProjectNumList = '';
      foreach $i (@glsprojectlist){
          chomp($i);
          if($i =~ /<start of new project = /){ 
             $glsprnum = $i;
             $glsprnum =~ s/<start of new project = //g;
             $glsprnum =~ s/>//g;
             $glsprnum =~ s/ //g;
             if($glsprnum =~ /\d/){
                if (grep(/$glsprnum/, @glsProjectNumList)) {$donothing = 1;}
                else{push(@glsProjectNumList, $glsprnum); $glsLessonsNum++;}
             }
          }
          elsif($i =~ /OEP_School: /){$i =~ s/OEP_School: //g; $OEP_School{$glsprnum} = $i;}
          elsif($i =~ /OEP_Group: /){$i =~ s/OEP_Group: //g; $OEP_Group{$glsprnum} = $i;}
          elsif($i =~ /OEP_Lesson: /){ $i =~ s/OEP_Lesson: //g; $OEP_Lesson{$glsprnum} = $i;  
             if ( $i ne '' ) { if ( length($i) == 1 ) { $i = '0' . $i; } push(@glsLessonNumList, "$i<tab>$glsprnum"); } }
          elsif($i =~ /OEP_Date: /){$i =~ s/OEP_Date: //g; $OEP_Date{$glsprnum} = $i;}
          elsif($i =~ /OEP_Topic: /){$i =~ s/OEP_Topic: //g; $OEP_Topic{$glsprnum} = $i;}
          elsif($i =~ /OEP_Comments: /){$i =~ s/OEP_Comments: //g; $OEP_Comments{$glsprnum} = $i;}
          elsif($i =~ /OEP_Participation_/){
              $i =~ s/OEP_Participation_//g; ($glsUserID, $glsUserPart) = split(/\: /, $i); 
              $glsUserID_GrpNm = $glsUserID . '_' . $whatis{'groupid'}; $OEP_PartTxt{$glsUserID_GrpNm} = 'true';
              $glsUserID_PRNum = $glsUserID . '_' . $glsprnum;  $OEP_Participation{$glsUserID_PRNum} = $glsUserPart;
          }
          elsif($i =~ /OEP_LateMinutes_/){
              $i =~ s/OEP_LateMinutes_//g;  ($glsUserID, $glsUserLate) = split(/\: /, $i); 
              $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $OEP_Late{$glsUserID_PRNum} = $glsUserLate;
          }
          elsif($i =~ /OEP_LiftMinus_/){
              $i =~ s/OEP_LiftMinus_//g; ($glsUserID, $glsUserLiftMinus) = split(/\: /, $i); 
              $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $OEP_LiftMinus{$glsUserID_PRNum} = $glsUserLiftMinus;
          }
          elsif($i =~ /OEP_Tests_/){
              $i =~ s/OEP_Tests_//g; ($glsUserID, $glsUserTest) = split(/\: /, $i); 
              $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $OEP_Test{$glsUserID_PRNum} = $glsUserTest;
          }
          elsif($i =~ /OEP_LiftPlus_/){
              $i =~ s/OEP_LiftPlus_//g; ($glsUserID, $glsUserLiftPlus) = split(/\: /, $i); 
              $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $OEP_LiftPlus{$glsUserID_PRNum} = $glsUserLiftPlus;
          }
          elsif($i =~ /OEP_TotalPoints_/){
              $i =~ s/OEP_TotalPoints_//g; ($glsUserID, $glsUserTotalPoints) = split(/\: /, $i); 
              $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $OEP_TotalPoints{$glsUserID_PRNum} = $glsUserTotalPoints;
          }
          elsif($i =~ /OEP_Eval_/){
              $i =~ s/OEP_Eval_//g; ($glsUserID, $glsUserEval) = split(/\: /, $i); 
              $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $OEP_Eval{$glsUserID_PRNum} = $glsUserEval;
          }
          elsif($i =~ /OEP_UserComment_/){
              $i =~ s/OEP_UserComment_//g; ($glsUserID, $glsUserComm) = split(/\: /, $i); 
              $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $OEP_UserComment{$glsUserID_PRNum} = $glsUserComm;
          }
          elsif($i =~ /OEP_HomeWork_/){
              $i =~ s/OEP_HomeWork_//g; ($glsUserID, $glsUserHome) = split(/\: /, $i); 
              $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $OEP_HomeWork{$glsUserID_PRNum} = $glsUserHome;
          }
      }
}

#####################################################################################
########################### FINISH END BODY #########################################
#####################################################################################

if($userbrowser eq 'desktop'){print "<p><a href=\'$httpindexcgi\?browser=mobile\'>MOBILE</a></p>\n";}
else{print "<p><a href=\'$httpindexcgi\?browser=desktop\'>DESKTOP</a></p>\n";}

if($userlogged == 1){
   if ( $gotusrid eq '6' || $gotusrid eq '8' || $gotusrid eq '3' ){
      open(INF, $adminText_file); @adminTextList = <INF>; close(INF); print @adminTextList; 
      &printfile($end, $title);
   }
}
else {print "</body></html>";}

#######################################################################################
########################### JAVASCRIPT PART ###########################################
#######################################################################################
sub printJavaScript {
print  <<EOT;
 <script>
 function checkFunction (){
    if(document.getElementsByName('studid')[0].value == ''){alert('Номер ученика?'); return false;}
 }
</script> 
EOT
}

##################################################################################################################
############################## Sub checkcookies ##################################################################
##################################################################################################################

sub checkcookies {
    #print "<br>i am in checkcookies\n";
    #7<tab>30569458007812<tab>Tue Sep 11 11:35:10 2012<tab>172.81.88.121<tab>reserve
    # $userid<tab>$randnum<tab>$timedatenow<tab>$userip<tab>future_reserve
    # $gotcookie = $ENV{'HTTP_COOKIE'};
    # $oeusercookiernd{$clusrnum} = $clusrrnd;
    # $oeusercookiedate{$clusrnum} = $clusrdate;
    # $oeusercookieip{$clusrnum} = $clusrip;
    ($gccontsupgrp, $gcusrnumrnd) = split(/=/, $gotcookie);
    ($gcusrnum, $gcusrrnd, $gcusrbrowser) = split(/_/, $gcusrnumrnd);
    $logindata = "User number: [$gcusrnum] User RND: [$gcusrrnd] User's RND: [$oeusercookiernd{$gcusrnum}]";
    if($gotcookie =~ /openenglishproject/ && $whatis{'action'} ne 'logout' && $whatis{'action'} ne 'login'){
       if($oeusercookiernd{$gcusrnum} eq $gcusrrnd){
            if($userlevel{$gcusrnum} < 7 || $userlevel{$gcusrnum} == $accesslevel){
                $userlogged = 1;  
                if($whatis{'browser'} eq 'mobile'){ $userbrowser = 'mobile'; }
                elsif($whatis{'browser'} eq 'desktop'){ $userbrowser = 'desktop'; }
                else{ $userbrowser = $gcusrbrowser; }
                $gotusrid = $gcusrnum;
                $newcookie = "openenglishproject\=$gcusrnum\_$gcusrrnd\_$userbrowser\; expires=$live_time\; path=/\;";
                print "Set-Cookie: " . $newcookie . "\n";
            }
       }
       else{$errorlogin = "$rf $b1 User not identified or no permission to access! $b2 $f2";}
       $iwashere = 1;
    }
    elsif($whatis{'action'} eq 'login' || $whatis{'action'} eq 'logout'){
        if($whatis{'action'} eq 'logout'){
            $userlogged = 0;
            $gotusrid = $gcusrnum;
            $oeusercookiernd{$gotusrid} = '12334567890';
            $oeusercookiedate{$gotusrid} = $timedatenow;
            $oeusercookieip{$gotusrid} = $userip;
            $iwashere = 2;
        }
        elsif($whatis{'action'} eq 'login'){
            if($whatis{'userpwd'} eq $userpwd{$whatis{'usernamenumber'}} && $whatis{'userpwd'} ne ''){
                  if($userlevel{$whatis{'usernamenumber'}} < 7 || $userlevel{$whatis{'usernamenumber'}} == $accesslevel){
                      if($whatis{'usernamenumber'} > 0){$gotusrid = $whatis{'usernamenumber'};}
                      else{$gotusrid = 0;}
                      $randnum = int(rand(10)*1000000000000);
                      $oeusercookiernd{$gotusrid} = $randnum;
                      $oeusercookiedate{$gotusrid} = $timedatenow;
                      $oeusercookieip{$gotusrid} = $userip;
                      $newcookie = "openenglishproject\=$gotusrid\_$randnum\_mobile\; expires=$live_time\; path=/\;";
                      print "Set-Cookie: " . $newcookie . "\n";
                      $userlogged = 1;
                      $iwashere = 3;
                  }  
            }
            else{$errorlogin = "$rf $b1 Wrong password! $b2 $f2";}
        }
        else{$errorlogin = "$rf $b1 Login error! Try again... $b2 $f2";}
        $cnt = 1;
        open(D,">$cookie_file");
        while ($cnt <= $cookiemaxamount){
            $cookie_file_data = "$cnt<tab>$oeusercookiernd{$cnt}<tab>$oeusercookiedate{$cnt}<tab>$oeusercookieip{$cnt}<tab>mobile";
            print D "$cookie_file_data\n";
            $cnt++;
        }
        close(D); 
        $cnt = 0;       
    }
    else{$userlogged = 0; $iwashere = 4;}
    $logindata = $logindata . "Got User ID: [$gotusrid]";
}


##################################################################################################################
################################### Sub printfile ################################################################
##################################################################################################################

sub printfile {
  my ($sfile, $stitle) = @_;
  open(INF, $sfile); 
  @filetoopen = <INF>; 
  close(INF);
  foreach $i (@filetoopen){
    chomp($i);
    if ($i=~/<title>/){$i = $i . $stitle;}
    print "$i\n";
  }
}