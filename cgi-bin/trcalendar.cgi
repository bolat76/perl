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
$grnclr = 'bgcolor = GreenYellow'; $redclr = 'bgcolor = #8a8ac1;';
$timedatenow = scalar localtime;
$timedatenow =~s/  / /g;
($weekdaynow, $monthnow, $daynow, $timenow, $yearnow) = split(/ /, $timedatenow);
if($daynow < 10){$daynow = '0' . $daynow;}
($hournow, $minutenow, $secondnow) = split(/:/, $timenow);
$ai{'Jan'} = '01'; $ai{'Feb'} = '02'; $ai{'Mar'} = '03';
$ai{'Apr'} = '04'; $ai{'May'} = '05'; $ai{'Jun'} = '06';
$ai{'Jul'} = '07'; $ai{'Aug'} = '08'; $ai{'Sep'} = '09';
$ai{'Oct'} = '10'; $ai{'Nov'} = '11'; $ai{'Dec'} = '12';
$argyai{'Jan'} = '02'; $argyai{'Feb'} = '03'; $argyai{'Mar'} = '04';
$argyai{'Apr'} = '05'; $argyai{'May'} = '06'; $argyai{'Jun'} = '07';
$argyai{'Jul'} = '08'; $argyai{'Aug'} = '09'; $argyai{'Sep'} = '10';
$argyai{'Oct'} = '11'; $argyai{'Nov'} = '12'; $argyai{'Dec'} = '01';
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
if($nxtmonth =~ /Jan/){$yearnow++; $datenextai = "28.$argyai{$monthnow}.$yearnow"; }
else { $datenextai = "28.$argyai{$monthnow}.$yearnow"; }
$live_time="$weekdaynow, $daynow\-$nxtmonth\-$yearnow $timenow GMT";
if($nxtmonth =~ /Jan/){$yearnow--;}
$userip = $ENV{'REMOTE_ADDR'};
 @getcookies = split (/; /,$ENV{'HTTP_COOKIE'});
 foreach(@getcookies){
        $hotcookie = $_;
        ($cookiekey, $cookieval) = split (/=/,$hotcookie);
        $cookies{$cookiekey} = $cookieval;
        if($cookiekey =~ /trainersproject/){$gotcookie = $hotcookie; }
    }
#$gotcookie = $ENV{'HTTP_COOKIE'};
$cookie_file = '../oedata/tr_cookies.txt';
$users_file = '../oedata/trainers.txt';
$leaders_file = '../oedata/leaders.txt';
$usersdata_file = '../oedata/trainersdata.txt';
###################### end of cookie part #########################
$oe_folder = '../oedata/';
$groups_folder = '../oedata/groups/';
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$glMonthPayValue = 5500;
$indexcgi = 'trcalendar.cgi';
$upd_user_file = $oe_folder . 'tr_upd_usr.txt';
$calendar_file = $oe_folder . 'calendar.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpcontrolcgi = 'http://accelerator.kvadra.kz/cgi-bin/control.cgi';
$httpmanagecgi = 'http://accelerator.kvadra.kz/cgi-bin/manage.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Read lists';

open(INF, $cookie_file); @cookielist = <INF>; close(INF);
foreach $i(@cookielist){
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
   if($tldrid ne ''){  $LeaderFullName{$tldrid} = "$tldrfirstnam $tldrscndnam $tldrthrdnam"; $tldremail = lc $tldremail;
      $LeaderUniqueId{$tldrid} = $tldrid; $LeaderFirstName{$tldrid} = $tldrfirstnam; $LeaderSecondName{$tldrid} = $tldrscndnam;
      $LeaderThirdName{$tldrid} = $tldrthrdnam; $LeaderPositionNum{$tldrid} = $tldrnum;   $LeaderSchoolNum{$tldrid} = $tldrschl;
      $LeaderGroupNum{$tldrid} = $tldrgrp; $LeaderPhoneNum{$tldrid} = $tldrphn; $LeaderEmail{$tldrid} = $tldremail; 
      $LeaderBirthDay{$tldrid} = $tldrbrthday; $LeaderGender{$tldrid} = $tldrgender; $LeaderWorkPlace{$tldrid} = $tldrwrkplc;
      $LeaderPersonId{$tldrid} = $tldrprsnid; $LeaderIndividId{$tldrid} = $tldrindvdid; $LeaderPassWord{$tldrid} = $tldrpwd;
   }
}  # $existSchool{$tldrschl}; $existGroup{$tldrgrp}; $GroupsPerSchool{$tldrschl}; $totalLeaders ;$totalSchools; $totalGroups

open(INF, $calendar_file); @calendar_list = <INF>;close(INF);
foreach $i(@calendar_list){ chomp($i); #12<tab>12.01.19<tab>Saturday
    ($tclndrnum, $tclndrdate, $tcndrweek, @other) = split (/<tab>/, $i);  
    $calendarweek{$tclndrnum} = $tcndrweek; $calendarweek{$tclndrdate} = $tcndrweek;
    $calendarnumber{$tclndrdate} = $tclndrnum;  $calendardate{$tclndrnum} = $tclndrdate;
}

open(INF, $users_file); 
@userlist = <INF>; 
close(INF); 
foreach $i(@userlist){ 
   #6<tab>44TR4706<tab>Болатхан<tab>Джайдаринов<tab><tab>1<tab>8 777 277 0326<tab>b.jaidarinov@gmail.com<tab>14.07.2019<tab>reserve
   ($tusrnum, $tusrid, $tusrfrstnam, $tusrscndnam, $tusrthrdnam, $tusrpwd, $tusrphnnum, $tusremail, $tusrdate, @other) = split (/<tab>/, $i);
   if ( $tusrid ne '' ) { $tusremail = lc $tusremail;
       $userFullName{$tusrid} = "$tusrfrstnam $tusrscndnam $tusrthrdnam"; $userpwd{$tusrid} = $tusrpwd; 
       $userFirstName{$tusrid} = $tusrfrstnam; $userSecondName{$tusrid} = $tusrscndnam; $userEmail{$tusrid} = $tusremail;
       $userThirdName{$tusrid} = $tusrthrdnam; $userCode{$tusrid} = $tusrid; $userCode{$tusremail} = $tusrid;
       push(@loginuserslist, $tusrid); $userPhoneNumber{$tusrid} = $tusrphnnum; 
       if ( $tusremail ne '' ) { $userEmailExist{$tusremail} = 1; $userpwd{$tusremail} = $tusrpwd; }
   }
}
$cnt = 0;

#@coins = ("Quarter","Dime","Nickel");
$moduleZeroText{'4'} = '<br>Обобщение занятий 1-3';  $moduleZeroText{'5'} = '<br>Коучинг сессия';  $moduleZeroText{'9'} = '<br>Обобщение занятий 6-8';
$moduleZeroText{'10'} = '<br>Промежуточное Тестирование';  $moduleZeroText{'14'} = '<br>Обобщение занятий 11-13';
$moduleZeroText{'17'} = '<br>Подготовка к итоговому тесту';  $moduleZeroText{'18'} = '<br>Итоговый тест';
$moduleOneText{'4'} = '<br>Обобщение занятий 1-3';  $moduleOneText{'5'} = '<br>Коучинг сессия';  $moduleOneText{'7'} = '<br>Speaking Club';
$moduleOneText{'8'} = '<br>Тест по Vocabulary и Рубежная встреча';  $moduleOneText{'12'} = '<br>Тест по Vocabulary и Коучинг сессия';
$moduleOneText{'16'} = '<br>Speaking Club';  $moduleOneText{'17'} = '<br>Обобщение занятий 13-16';  $moduleOneText{'18'} = '<br>Full File Test';
$moduleTwoText{'4'} = '<br>Обобщение занятий 1-3';  $moduleTwoText{'8'} = '<br>Обобщение занятий 5-7<br>1-2 Unit Test';  $moduleTwoText{'9'} = '<br>Коучинг сессия';
$moduleTwoText{'11'} = '<br>3-4 Unit Test';   $moduleTwoText{'12'} = '<br>Обобщение занятий 9-11<br>Progress  Test 1 (Unit 1-4)<br>Рубежная встреча с координатором'; 
$moduleTwoText{'16'} = '<br>Обобщение занятий 13-15<br>5-6 Unit Test';   $moduleTwoText{'17'} = '<br>Коучинг сессия';  $moduleTwoText{'20'} = '<br>7-8 Unit Test';
$moduleTwoText{'21'} = '<br>Обобщение занятий 17-20<br>Progress  Test 2 (Unit 5-8)<br>Рубежная встреча с координатором';  $moduleTwoText{'24'} = '<br>Коучинг сессия'; 
$moduleTwoText{'25'} = '<br>9-10 Unit Test';  $moduleTwoText{'29'} = '<br>11-12 Unit Test';   
$moduleTwoText{'30'} = '<br>Обобщение занятий 22-29<br>Progress  Test 3 (Unit 9-11)<br>Рубежная встреча с координатором'; 
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
if ( $whatis{'email'} ne '' ) { $whatis{'email'} = lc $whatis{'email'}; $whatis{'email'} =~s/ //g; }
&checkcookies();
print "\n";
if($userbrowser eq 'desktop'){ &printfile($bas, $title);}
else {&printfile($basm, $title);}

if ( $whatis{'action'} ne '' ) { open(GURD,">>$log_file");
print GURD "Time: [$timedatenow] User ID: [$gotusrid] IP address: [$userip] User action: [$whatis{'action'}] Script: [$indexcgi] \n";
close(GURD); }

#####################################################################################
############################ LOGIN CHECK PART #######################################
#####################################################################################
print "<p> </p>";
if ( $userlogged == 1 && $gotusrid =~ /44TR/ ) {
   print "<p>привет тренер $b1 $userFirstName{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a></p>";
   if ( $gotusrid eq '44TR4706' ) {
      open(CTRD, $upd_user_file);    $updatedTrainerId = <CTRD>;    close(CTRD); 
      print "<p> </p><form method='post' action=\'$indexcgi\'><select name='changeuser'>"; 
      if ( $whatis{'changeuser'} ne '' ) { print "<option value = \'$whatis{'changeuser'}\' selected>$userFullName{$whatis{'changeuser'}}</option>\n"; }
      foreach $i (@loginuserslist) { 
         if ( $updatedTrainerId eq $i && $whatis{'changeuser'} eq '' ) { print "<option value = \'$i\' selected>$userFullName{$i}</option>\n"; }
         else { print "<option value = \'$i\'>$userFullName{$i}</option>\n"; } }
      print "</select><input type = 'submit' value = 'Change User'></form>\n"; 
      if ( $whatis{'changeuser'} ne '' ) { open(CTRD,">$upd_user_file"); print CTRD $whatis{'changeuser'}; close(CTRD);
         $gotusrid = $whatis{'changeuser'}; print "<h3>User updated: [$gotusrid]</h3>\n";    }
      elsif ( $updatedTrainerId =~ /44TR/ ) { $gotusrid = $updatedTrainerId; print "<h3>User updated: [$gotusrid]</h3>\n"; }
   }   
}

#####################################################################################
########################### START MAIN BODY #########################################
#####################################################################################
if ( $userlogged == 1 && $gotusrid =~ /44TR/ ) {
   open(INF, $usersdata_file);    @usersDataList = <INF>;    close(INF);  foreach $tmpDataLine (@usersDataList) {
      #1<tab>44TR4701<tab>99-1-M1<tab>19.06.19<tab>reserve
      ($tmpUsrNum, $tmpUsrId, $tmpUsrGrpId, $tmpUsrDate, @other) = split (/<tab>/, $tmpDataLine);
      if ( $gotusrid eq $tmpUsrId ) { push(@userGroupNumList, $tmpUsrGrpId); $smbGrpActive{$gotusrid}++; }
   }
   if ( $smbGrpActive{$gotusrid} > 0 ) { &openBlankPage(); }
   print "<p> </p><p align = 'center'><a href=\'$httpcontrolcgi\'>HOME</a></p>\n";
}
else{
    if ( $whatis{'action'} eq 'login' && $userlogged != 1) { print "<p>$rf $errorlogin $f2</p>\n" ; }  
    print "<form method='post' action=\'$httpindexcgi\'><table><caption>Enter Login Data</caption><tr><td>Email: </td>
    <td><input type = 'text'  name = 'email'></td>  <td>Password: </td><td><input type = 'password'  name = 'userpwd'> </td>
    <td><input type = 'hidden' name = 'action' value = 'login'> <input type = 'submit' value = 'Enter'></td></tr></table></form>\n";
    print "<p><a href=\'$httpmanagecgi?action=email\'>Обновить Персональные Данные</a></p>";
}

#####################################################################################
############################ OPEN BLANK PAGE SUB ####################################
#####################################################################################
sub openBlankPage {
   if ( $whatis{'startdate'} eq '' ) { $bpsStartDate = $datenow ; } else { $bpsStartDate = $whatis{'startdate'}; }  
   if ( $whatis{'finishdate'} eq '' ) { $bpsFinishDate = $datenextai ; } else { $bpsFinishDate = $whatis{'finishdate'}; }  
   $bpsStartDayNum = $calendarnumber{$bpsStartDate}; $bpsFinishDayNum = $calendarnumber{$bpsFinishDate};  $bpsCnt = 0; $globalCont = 0 ;
   print "<h1>Список всех занятий на дату:</h1>
   <form method='post'  action=\'$httpindexcgi\'> Start Date: <input type='text' name='startdate' value=\'$bpsStartDate\' >
   Finish Date: <input type='text' name='finishdate' value=\'$bpsFinishDate\' > <input type = 'submit' value = 'Show Calendar'>
   </form><table>\n";
   foreach $grpid (@userGroupNumList){ $whatis{'groupid'} = $grpid;  $bpsCnt++;
      if ( $grpid =~ /M/){ &openGroupSub($bpsStartDayNum, $bpsFinishDayNum, $bpsCnt);  }
   }
   print "</table><p> </p>\n"; 
}

#####################################################################################
############################### OPEN GROUP SUB ######################################
#####################################################################################
sub openGroupSub {   ($ogsDayStart, $ogsDayEnd, $ogsShowDays) = @_;  $ogsCalendarListLastValue = 0; 
   ( $whatis{'schoolid'}, @rest ) = split ( /-/, $whatis{'groupid'} ); &getGroupDataSub(); $ogsClCnt = 0;
   $ogsid = $whatis{'groupid'};  &getLessonSub(); if ( $OEP_Status{$ogsid} !~ /Active/ ) { return; }
   (@ogsCalendarList) = split(/\, /, $OEP_Calendar{$ogsid});  (@ogsTimeList) = split(/<tab>/, $OEP_TimeList{$ogsid});  $ogsCheckLoop = 0; 
   $cnt = $ogsDayStart;  $ogsClndLine = ""; $ogsWeekLine = ''; $ogsGraphLine = ''; $ogsLessLine = ''; $ogsVisitLine = '';   $ogsCnt = 0;
   foreach $i ( @ogsCalendarList ) { if ($ogsCalendarListLastValue < $i) { $ogsCalendarListLastValue = $i; } 
        $ogsGrpId = $ogsid . '<tab>' . $i;  $ogsCalendarDayValue{$ogsGrpId} = $i; $ogsCalendarDayPlace{$ogsGrpId} = $ogsClCnt; 
        $ogsClCnt++;   }
   if ( $ogsDayStart <= $ogsCalendarListLastValue && $ogsDayEnd > $ogsCalendarList[0] ) { $donothing = 1 ; }
   else { return; }   if ( $ogsShowDays != 1 && $globalCont == 0 ) { $ogsShowDays = 1 ; }    #$existGroup{$tstudgrp};
   print "<tr $yelclr id = $ogsShowDays><td $ac>$whatis{'schoolid'} ___________ <br>[$ogsid]<br>($existGroup{$ogsid})</td>\n";    
   while ( $cnt < $ogsDayEnd ) { $ogsFactLessPartTextLine = ""; #$tcnt = $ogsCnt + 1; 
      if ( $ogsShowDays == 1 ) { $ogsClndLine = $ogsClndLine . "<td>$calendardate{$cnt}</td>"; 
         $ogsWeekLine = $ogsWeekLine . "<td>$calendarweek{$cnt}</td>"; } 
      else { $ogsClndLine = $ogsClndLine . "<td></td>";  $ogsWeekLine = $ogsWeekLine . "<td></td>"; }
      $ogsGrpId = $ogsid . '<tab>' . $cnt;
      if ( $glsGroupDateLessonNumber{$ogsGrpId} > 0 ){ $ogsFactLessPartTextLine = "<br>$rf $b1 Урок:[$glsGroupDateLessonNumber{$ogsGrpId}]";
         $ogsFactLessPartTextLine = $ogsFactLessPartTextLine . "<br>Пришло:[$glsGroupParticipation{$ogsGrpId}\/$existGroup{$ogsid}] $b2 $f2</br>"; 
      }
      if ( $ogsCalendarDayValue{$ogsGrpId} > 0 && $ogsCalendarDayValue{$ogsGrpId} ne '' ) {
         $tcnt = $ogsCalendarDayPlace{$ogsGrpId} + 1;
         if ( $OEP_Group{$ogsid} =~ /M0/ ){ $ogsAddTxt = $moduleZeroText{$tcnt}; }       
         elsif ( $OEP_Group{$ogsid} =~ /M1/ ){ $ogsAddTxt = $moduleOneText{$tcnt}; }
         elsif ( $OEP_Group{$ogsid} =~ /M2/ ){ $ogsAddTxt = $moduleTwoText{$tcnt}; }           
         else { $ogsAddTxt = ''; }
         $ogsGraphLine = $ogsGraphLine . "<td>$ogsTimeList[$tcnt]</td>" ;  
         $ogsLessLine = $ogsLessLine . "<td $ac>$tcnt $ogsAddTxt $ogsFactLessPartTextLine</td>";
         $ogsCnt++;
      }
      else { $ogsAddTxt = '';  $ogsGraphLine = $ogsGraphLine . "<td></td>"; 
         $ogsLessLine =  $ogsLessLine . "<td> $ogsFactLessPartTextLine</td>"; }
      if($ogsCheckLoop > 300){last;}
      $ogsCheckLoop++;  $cnt++;  $globalCont++;
   }
   if ( $ogsShowDays == 1 ) { print "$ogsWeekLine</tr>\n<tr $yelclr1 id='dates'><td>Date</td>$ogsClndLine</tr>
   <tr $yelclr id='second'> <td>Time of lesson</td>"; }
   print "$ogsGraphLine</tr>\n<tr $yelclr1 id='lessons'><td>Number of lesson</td>$ogsLessLine</tr>\n";
}

#####################################################################################
################################# GET GROUP SUB #####################################
#####################################################################################
sub getGroupDataSub {
   #foreach $stdid (@studentUniqueNumList){ if($studentGroupNum{$stdid} =~ $whatis{'groupid'}){  push(@glsStudentsList, $stdid); } }
   $ggsgrpfile = $groups_folder . $whatis{'groupid'} . '_data.txt'; $ggsid = $whatis{'groupid'};
   open(UPL, $ggsgrpfile);       @ggsprojectlist = <UPL>;       close(UPL);
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
      elsif($i =~ /OEP_Calendar: /){$i =~ s/OEP_Calendar: //g; $OEP_Calendar{$ggsid} = $i;}
      elsif($i =~ /OEP_TimeList: /){$i =~ s/OEP_TimeList: //g; $OEP_TimeList{$ggsid} = $i;}
      elsif($i =~ /OEP_MondayTime: /){$i =~ s/OEP_MondayTime: //g; $OEP_MondayTime{$ggsid} = $i;}
      elsif($i =~ /OEP_TuesdayTime: /){$i =~ s/OEP_TuesdayTime: //g; $OEP_TuesdayTime{$ggsid} = $i;}
      elsif($i =~ /OEP_WednesdayTime: /){$i =~ s/OEP_WednesdayTime: //g; $OEP_WednesdayTime{$ggsid} = $i;}
      elsif($i =~ /OEP_ThursdayTime: /){$i =~ s/OEP_ThursdayTime: //g; $OEP_ThursdayTime{$ggsid} = $i;}
      elsif($i =~ /OEP_FridayTime: /){$i =~ s/OEP_FridayTime: //g; $OEP_FridayTime{$ggsid} = $i;}
      elsif($i =~ /OEP_SaturdayTime: /){$i =~ s/OEP_SaturdayTime: //g; $OEP_SaturdayTime{$ggsid} = $i;}
      elsif($i =~ /OEP_SundayTime: /){$i =~ s/OEP_SundayTime: //g; $OEP_SundayTime{$ggsid} = $i;}
      elsif($i =~ /OEP_Monday: /){$i =~ s/OEP_Monday: //g; $OEP_Monday{$ggsid} = $i;}
      elsif($i =~ /OEP_Tuesday: /){$i =~ s/OEP_Tuesday: //g; $OEP_Tuesday{$ggsid} = $i;}
      elsif($i =~ /OEP_Wednesday: /){$i =~ s/OEP_Wednesday: //g; $OEP_Wednesday{$ggsid} = $i;}
      elsif($i =~ /OEP_Thursday: /){$i =~ s/OEP_Thursday: //g; $OEP_Thursday{$ggsid} = $i;}
      elsif($i =~ /OEP_Friday: /){$i =~ s/OEP_Friday: //g; $OEP_Friday{$ggsid} = $i;}
      elsif($i =~ /OEP_Saturday: /){$i =~ s/OEP_Saturday: //g; $OEP_Saturday{$ggsid} = $i;}
      elsif($i =~ /OEP_Sunday: /){$i =~ s/OEP_Sunday: //g; $OEP_Sunday{$ggsid} = $i;}
   }
}
#####################################################################################
############################### GET LESSONS SUB #####################################
#####################################################################################
sub getLessonSub {
    #foreach $stdid (@studentUniqueNumList){ if($studentGroupNum{$stdid} =~/$whatis{'groupid'}/){  push(@glsStudentsList, $stdid); } }
    $glsgrpfile = $groups_folder . $whatis{'groupid'} . '.txt'; 
    open(UPL, $glsgrpfile);     @glsprojectlist = <UPL>;    close(UPL);    @glsProjectNumList = '';
    foreach $i (@glsprojectlist){        chomp($i);
        if ( $i =~ /<start of new project = / ) { 
           $glsprnum = $i;
           $glsprnum =~ s/<start of new project = //g;
           $glsprnum =~ s/>//g;
           $glsprnum =~ s/ //g;
           if ( $glsprnum =~ /\d/ ) {
              if (grep(/$glsprnum/, @glsProjectNumList)) {$donothing = 1;}
              else{push(@glsProjectNumList, $glsprnum); $glsLessonsNum++;}
           }
        }# $glsGroupDateLessonNumber{$glsGroupLessonDateArgument} # $glsGroupParticipation{$glsGroupLessonDateArgument};
        elsif($i =~ /OEP_School: /){$i =~ s/OEP_School: //g; $GLS_School{$glsprnum} = $i;}
        elsif($i =~ /OEP_Group: /){$i =~ s/OEP_Group: //g; $GLS_Group{$glsprnum} = $i;}
        elsif($i =~ /OEP_Lesson: /){$i =~ s/OEP_Lesson: //g; $GLS_Lesson{$glsprnum} = $i;}
        elsif($i =~ /OEP_Date: /){
           $i =~ s/OEP_Date: //g; $GLS_Date{$glsprnum} = $i; #$calendarnumber{$tclndrdate}
           $glsGroupLessonDateArgument = $whatis{'groupid'} . '<tab>' . $calendarnumber{$GLS_Date{$glsprnum}};
           $glsGroupDateLessonNumber{$glsGroupLessonDateArgument} = $GLS_Lesson{$glsprnum}; 
        }
        elsif($i =~ /OEP_Topic: /){$i =~ s/OEP_Topic: //g; $GLS_Topic{$glsprnum} = $i;}
        elsif($i =~ /OEP_Comments: /){$i =~ s/OEP_Comments: //g; $GLS_Comments{$glsprnum} = $i;}
        elsif($i =~ /OEP_Participation_/){
           $i =~ s/OEP_Participation_//g; ($glsUserID, $glsUserPart) = split(/\: /, $i); 
           $glsUserID_PRNum = $glsUserID . '_' . $glsprnum;  $GLS_Participation{$glsUserID_PRNum} = $glsUserPart;
           if ( $glsUserPart =~/1/ ) { $glsGroupParticipation{$glsGroupLessonDateArgument}++; }
        }# $glsGroupDateLessonNumber{$glsGroupLessonDateArgument} # $glsGroupParticipation{$glsGroupLessonDateArgument};
        elsif($i =~ /OEP_LateMinutes_/){
           $i =~ s/OEP_LateMinutes_//g;  ($glsUserID, $glsUserLate) = split(/\: /, $i); 
           $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $GLS_Late{$glsUserID_PRNum} = $glsUserLate;
        }
        elsif($i =~ /OEP_LiftMinus_/){
           $i =~ s/OEP_LiftMinus_//g; ($glsUserID, $glsUserLiftMinus) = split(/\: /, $i); 
           $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $GLS_LiftMinus{$glsUserID_PRNum} = $glsUserLiftMinus;
        }
        elsif($i =~ /OEP_Tests_/){
           $i =~ s/OEP_Tests_//g; ($glsUserID, $glsUserTest) = split(/\: /, $i); 
           $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $GLS_Test{$glsUserID_PRNum} = $glsUserTest;
        }
        elsif($i =~ /OEP_LiftPlus_/){
           $i =~ s/OEP_LiftPlus_//g; ($glsUserID, $glsUserLiftPlus) = split(/\: /, $i); 
           $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $GLS_LiftPlus{$glsUserID_PRNum} = $glsUserLiftPlus;
        }
        elsif($i =~ /OEP_TotalPoints_/){
           $i =~ s/OEP_TotalPoints_//g; ($glsUserID, $glsUserTotalPoints) = split(/\: /, $i); 
           $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $GLS_TotalPoints{$glsUserID_PRNum} = $glsUserTotalPoints;
        }
        elsif($i =~ /OEP_Eval_/){
           $i =~ s/OEP_Eval_//g; ($glsUserID, $glsUserEval) = split(/\: /, $i); 
           $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $GLS_Eval{$glsUserID_PRNum} = $glsUserEval;
        }
        elsif($i =~ /OEP_UserComment_/){
           $i =~ s/OEP_UserComment_//g; ($glsUserID, $glsUserComm) = split(/\: /, $i); 
           $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $GLS_UserComment{$glsUserID_PRNum} = $glsUserComm;
        }
        elsif($i =~ /OEP_HomeWork_/){
           $i =~ s/OEP_HomeWork_//g; ($glsUserID, $glsUserHome) = split(/\: /, $i); 
           $glsUserID_PRNum = $glsUserID . '_' . $glsprnum; $GLS_HomeWork{$glsUserID_PRNum} = $glsUserHome;
        }
    }
}

#####################################################################################
########################### FINISH END BODY #########################################
#####################################################################################

if($userbrowser eq 'desktop'){print "<p><a href=\'$httpindexcgi\?browser=mobile\'>MOBILE</a></p>\n";}
else{print "<p><a href=\'$httpindexcgi\?browser=desktop\'>DESKTOP</a></p>\n";}

print "</center></body></html>";

##################################################################################################################
############################## Sub checkcookies ##################################################################
##################################################################################################################

sub checkcookies {
    #print "<br>i am in checkcookies\n";
    #7<tab>30569458007812<tab>Tue Sep 11 11:35:10 2012<tab>172.81.88.121<tab>reserve
    # $userid<tab>$randnum<tab>$timedatenow<tab>$userip<tab>future_reserve
    # $gotcookie = $ENV{'HTTP_COOKIE'};    # $oeusercookiernd{$clusrnum} = $clusrrnd;    
    # $oeusercookiedate{$clusrnum} = $clusrdate;    # $oeusercookieip{$clusrnum} = $clusrip;
    ($gccontsupgrp, $gcusrnumrnd) = split(/=/, $gotcookie);
    ($gcusrnum, $gcusrrnd, $gcusrbrowser) = split(/_/, $gcusrnumrnd);
    $logindata = "User number: [$gcusrnum] User RND: [$gcusrrnd] User's RND: [$oeusercookiernd{$gcusrnum}]";
    if ( $gotcookie =~ /trainersproject/ && $whatis{'action'} ne 'logout' && $whatis{'action'} ne 'login' ) { $iwashere = 1;
       if ( $oeusercookiernd{$gcusrnum} eq $gcusrrnd && $userip eq $oeusercookieip{$gcusrnum} && $userip ne '' ) {  
          $userlogged = 1;   $gotusrid = $gcusrnum;
          if($whatis{'browser'} eq 'mobile'){ $userbrowser = 'mobile'; }
          elsif($whatis{'browser'} eq 'desktop'){ $userbrowser = 'desktop'; }
          else{ $userbrowser = $gcusrbrowser; }
          $newcookie = "trainersproject\=$gcusrnum\_$gcusrrnd\_$userbrowser\; expires=$live_time\; path=/\;";
          print "Set-Cookie: " . $newcookie . "\n";
       }
       else { $errorlogin = "$rf $b1 User not identified or no permission to access! $b2 $f2"; }
    } #$userpwd{$tusrid} = $tusrpwd; $userpwd{$tusremail} = $tusrpwd;
      #$userFirstName{$tusrid} = $tusrfrstnam; $userCode{$tusrid} = $tusrid; $userCode{$tusremail} = $tusrid;
      #$userSchoolId{$tusrid} = $tusrsclid; $userGroupId{$tusrid} = $tusrgrpid; 
    elsif ( $whatis{'action'} eq 'login' || $whatis{'action'} eq 'logout' ) {
       if ( $whatis{'action'} eq 'logout' ) {
          $userlogged = 0;   $gotusrid = $gcusrnum;     $oeusercookiernd{$gotusrid} = '1234567890';
          $oeusercookiedate{$gotusrid} = $timedatenow;  $oeusercookieip{$gotusrid} = $userip;
          $newcookie = "trainersproject=0_1234567890_desktop\; expires=$live_time\; path=/\;";
          print "Set-Cookie: " . $newcookie . "\n";  $iwashere = 2;
       }
       elsif ( $whatis{'action'} eq 'login' ) {
          if ( $whatis{'userpwd'} eq $userpwd{$whatis{'email'}} && $whatis{'userpwd'} ne '' ) {
              $ccUserNumber = $userCode{$whatis{'email'}};
              if ( $ccUserNumber =~ /44TR/ ) { $gotusrid = $ccUserNumber; }  else { $gotusrid = 0; }
              $randnum = int(rand(10)*1000000000000);       $oeusercookiernd{$gotusrid} = $randnum;
              $oeusercookiedate{$gotusrid} = $timedatenow;  $oeusercookieip{$gotusrid} = $userip;
              $newcookie = "trainersproject\=$gotusrid\_$randnum\_desktop\; expires=$live_time\; path=/\;";
              print "Set-Cookie: " . $newcookie . "\n";       $userlogged = 1;    $iwashere = 3;
              $ccDataLine = "$gotusrid<tab>$randnum<tab>$timedatenow<tab>$userip<tab>desktop";
          }
          else { $errorlogin = "$rf $b1 Wrong email or password! $b2 $f2"; }
       }
       else { $errorlogin = "$rf $b1 Login error! Try again... $b2 $f2"; }
       $cnt = 999999;
       open(INF, $cookie_file); @cookie_list = <INF>; close(INF);
       foreach $i (@cookie_list){
          chomp($i);
          ($tclusrnum, $tclusrrnd, $tclusrdate, $tclusrip, @other) = split (/<tab>/, $i);
          if($tclusrnum eq $userCode{$whatis{'email'}} && $tclusrnum ne '' ) { $donothing = 1; }
          else { push(@ccNewCookieList, $i); }
       }
       open(D,">$cookie_file");
       foreach $i (@ccNewCookieList){ if ( $i ne '' ) { print D "$i\n"; } }
       if ( $ccDataLine ne '' ) { print D "$ccDataLine\n"; }
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