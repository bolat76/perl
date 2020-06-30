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
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$indexcgi = 'calendar.cgi';
$students_file = $oe_folder . 'students.txt';
$calendar_file = $oe_folder . 'calendar.txt';
$adminText_file = $oe_folder . 'admin.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpreadcgi = 'http://accelerator.kvadra.kz/cgi-bin/read.cgi';
$httpgroupcgi = 'http://accelerator.kvadra.kz/cgi-bin/group.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Group Details';

open(INF, $cookie_file); @cookielist = <INF>; close(INF); foreach $i(@cookielist){
    chomp($i); #8<tab>8250732421875<tab>Tue Apr 23 14:16:01 2013<tab>172.28.113.66<tab>reserve
    ($clusrnum, $clusrrnd, $clusrdate, $clusrip, @other) = split (/<tab>/, $i);
    $oeusercookiernd{$clusrnum} = $clusrrnd;
    $oeusercookiedate{$clusrnum} = $clusrdate;
    $oeusercookieip{$clusrnum} = $clusrip;
}

@uniqueSchoolNumList = "";  @uniqueGroupNumList = "";  @studentUniqueNumList = "";
open(INF, $students_file); @studentslist = <INF>; close(INF); foreach $i(@studentslist){ 
      #1<tab>56BC4567<tab>Томирис<tab>Толенді<tab><tab>71<tab>71-1-M1
      #$usernum<tab>$userID<tab>$user1stname<tab>$user2ndname<tab>$user3rdname<tab>$userschool<tab>$usergroup<tab>$other
      ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp, @other) = split (/<tab>/, $i);
      if ( length( $tstudgrp ) > 0 && length ( $tstudschl ) > 0 ){
             $studentFirstName{$tstudid} = $tstudfirstnam; $studentSecondName{$tstudid} = $tstudscndnam;
             $studentThirdName{$tstudid} = $tstudthrdnam; $studentPositionNum{$tstudid} = $tstudnum; 
             $studentSchoolNum{$tstudid} = $tstudschl; $studentGroupNum{$tstudid} = $tstudgrp;     $existSchool{$tstudschl}++;  $existGroup{$tstudgrp}++; 
             if ( grep( /^$tstudschl$/, @uniqueSchoolNumList ) ) { $done = 1; } else { push(@uniqueSchoolNumList, $tstudschl); $totalSchools++; }
             if ( grep( /^$tstudgrp$/, @uniqueGroupNumList ) ){ $done = 1;} 
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
          $usernumber{$tusrnam} = $tusrnum; $userslist++; push(@loginuserslist, $tusrnam);
}
$cnt = 0;

open(INF, $calendar_file); @calendar_list = <INF>; close(INF); foreach $i(@calendar_list){ chomp($i); 
    ($tclndrnum, $tclndrdate, $tcndrweek, @other) = split (/<tab>/, $i);  #12<tab>12.01.19<tab>Saturday
    $calendarweek{$tclndrnum} = $tcndrweek; $calendardate{$tclndrnum} = $tclndrdate;
    $calendarweek{$tclndrdate} = $tcndrweek;  $calendarnumber{$tclndrdate} = $tclndrnum;
    ($clndrDay, $clndrMonth, $clndrYear) = split(/\./, $tclndrdate);  if ( $i ne '' ) { $myCalendarLastLine = $i; }
} $myNextYear = $yearnow + 1; if ( $clndrYear < $myNextYear && $clndrYear > 2000 ) { &addNewCalendarDays($myNextYear); }

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
############### check COOKIES and LOG actions #########################################
#######################################################################################
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
print "<p>";
if($userlogged == 1){
    print "Hello $b1 $userfirstname{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>";
    &blankPageSub();
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
############################### OPEN GROUP SUB ######################################
#####################################################################################
sub blankPageSub {
   if ( $whatis{'startdate'} eq '' ) { $bpsStartDate = $datenow ; } else { $bpsStartDate = $whatis{'startdate'}; }  
   if ( $whatis{'finishdate'} eq '' ) { $bpsFinishDate = $datenextai ; } else { $bpsFinishDate = $whatis{'finishdate'}; }  
   $bpsStartDayNum = $calendarnumber{$bpsStartDate}; $bpsFinishDayNum = $calendarnumber{$bpsFinishDate};  $bpsCnt = 0; $globalCont = 0 ;
   print "<h1>Список всех школ на дату:</h1>
   <form method='post'  action=\'$httpindexcgi\'> Start Date: <input type='text' name='startdate' value=\'$bpsStartDate\' >
   Finish Date: <input type='text' name='finishdate' value=\'$bpsFinishDate\' > <input type = 'submit' value = 'Show Calendar'></form><table>\n";
   foreach $sclid (@uniqueSchoolNumList){
      if( length( $sclid ) > 0){  #if($myclr eq $yelclr){$myclr = $yelclr1;} else{$myclr = $yelclr;}
         # $cnt++; # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents; $totalSchools; $totalGroups
         foreach $grpid (@uniqueGroupNumList){
            $whatis{'schoolid'} = $sclid;   $whatis{'groupid'} = $grpid;  $bpsCnt++;
            if($groupSchoolNum{$grpid} eq $sclid){ &openGroupSub($bpsStartDayNum, $bpsFinishDayNum, $bpsCnt);  }
         }
      }
   }
   print "</table><p> </p>\n"; 
}
#####################################################################################
############################### OPEN GROUP SUB ######################################
#####################################################################################
sub openGroupSub {
   ($ogsDayStart, $ogsDayEnd, $ogsShowDays) = @_; $ogsClCnt = 0; $ogsCalendarListLastValue = 0; #$ogsDayEnd = $ogsDayStart + 31;
   &getGroupDataSub(); $ogsid = $whatis{'groupid'};  &getLessonSub();  # if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
   if ( $OEP_Status{$ogsid} !~ /Active/ ) { return; }
   (@ogsCalendarList) = split(/\, /, $OEP_Calendar{$ogsid});  (@ogsTimeList) = split(/<tab>/, $OEP_TimeList{$ogsid});  $ogsCheckLoop = 0; 
   $cnt = $ogsDayStart;  $ogsClndLine = ""; $ogsWeekLine = ''; $ogsGraphLine = ''; $ogsLessLine = ''; $ogsVisitLine = '';   $ogsCnt = 0;
   foreach $i ( @ogsCalendarList ) { 
        if ($ogsCalendarListLastValue < $i) { $ogsCalendarListLastValue = $i; } 
        $ogsGrpId = $ogsid . '<tab>' . $i;  $ogsCalendarDayValue{$ogsGrpId} = $i; $ogsCalendarDayPlace{$ogsGrpId} = $ogsClCnt; $ogsClCnt++;
   }
   #LOOP:  for (0 .. $#ogsCalendarList) {  if ($ogsCalendarList[$_] eq $ogsDayStart) {  $ogsCnt = $_ ;   last LOOP;   }   }
   if ( $ogsDayStart <= $ogsCalendarListLastValue && $ogsDayEnd > $ogsCalendarList[0] ) { $donothing = 1 ; }
   else { return; }   if ( $ogsShowDays != 1 && $globalCont == 0 ) { $ogsShowDays = 1 ; }    #$existGroup{$tstudgrp};
   # $glsGroupLessonDateArgument = $whatis{'groupid'} . '<tab>' . $calendarnumber{$GLS_Date{$glsprnum}};
   # $glsGroupDateLessonNumber{$glsGroupLessonDateArgument} # $glsGroupParticipation{$glsGroupLessonDateArgument};
   print "<tr $yelclr id = $ogsShowDays><td $ac>$whatis{'schoolid'} ___________ <br>[$ogsid]<br>($existGroup{$ogsid})</td>\n";    
   while($cnt < $ogsDayEnd){ $ogsFactLessPartTextLine = ""; #$tcnt = $ogsCnt + 1; 
      if ( $ogsShowDays == 1 ) { $ogsClndLine = $ogsClndLine . "<td>$calendardate{$cnt}</td>";   $ogsWeekLine = $ogsWeekLine . "<td>$calendarweek{$cnt}</td>";  } 
      else { $ogsClndLine = $ogsClndLine . "<td></td>";  $ogsWeekLine = $ogsWeekLine . "<td></td>"; }
      $ogsGrpId = $ogsid . '<tab>' . $cnt;
      if($glsGroupDateLessonNumber{$ogsGrpId} > 0 ){ 
  $ogsFactLessPartTextLine = "<br>$rf $b1 Урок:[$glsGroupDateLessonNumber{$ogsGrpId}]<br>Пришло:[$glsGroupParticipation{$ogsGrpId}\/$existGroup{$ogsid}] $b2 $f2</br>"; 
      }
      #print "<!-- ogsGrpId:[$ogsGrpId] glsGroupDateLessonNumber{$ogsGrpId}:[$glsGroupDateLessonNumber{$ogsGrpId}] glsGroupDateLessonParticipation{$ogsGrpId}:[$glsGroupDateLessonParticipation{$ogsGrpId}]-->\n";
      if ( $ogsCalendarDayValue{$ogsGrpId} > 0 && $ogsCalendarDayValue{$ogsGrpId} ne '' ) {
         $tcnt = $ogsCalendarDayPlace{$ogsGrpId} + 1;
         if ( $OEP_Group{$ogsid} =~ /M0/ ){ $ogsAddTxt = $moduleZeroText{$tcnt}; }       
         elsif ( $OEP_Group{$ogsid} =~ /M1/ ){ $ogsAddTxt = $moduleOneText{$tcnt}; }
         elsif ( $OEP_Group{$ogsid} =~ /M2/ ){ $ogsAddTxt = $moduleTwoText{$tcnt}; }           
         else { $ogsAddTxt = ''; }
         $ogsGraphLine = $ogsGraphLine . "<td>$ogsTimeList[$tcnt]</td>" ;  $ogsLessLine = $ogsLessLine . "<td $ac>$tcnt $ogsAddTxt $ogsFactLessPartTextLine</td>";
         $ogsCnt++;
      }
      else { $ogsAddTxt = '';  $ogsGraphLine = $ogsGraphLine . "<td></td>"; $ogsLessLine =  $ogsLessLine . "<td> $ogsFactLessPartTextLine</td>"; }
      if($ogsCheckLoop > 300){last;}
      $ogsCheckLoop++;  $cnt++;  $globalCont++;
   }
   if ( $ogsShowDays == 1 ) { print "$ogsWeekLine</tr>\n<tr $yelclr1 id='dates'><td>Date</td>$ogsClndLine</tr>\n<tr $yelclr id='second'> <td>Time of lesson</td>"; }
   print "$ogsGraphLine</tr>\n<tr $yelclr1 id='lessons'><td>Number of lesson</td>$ogsLessLine</tr>\n";
   # print "</table>\n";
   # $calendarweek{$tclndrnum} = $tcndrweek; $calendardate{$tclndrnum} = $tclndrdate;
   # $calendarweek{$tclndrdate} = $tcndrweek;  $calendarnumber{$tclndrdate} = $tclndrnum;
}
#####################################################################################
################################# GET GROUP SUB #####################################
#####################################################################################
sub getGroupDataSub {
      #foreach $stdid (@studentUniqueNumList){ if($studentGroupNum{$stdid} =~ $whatis{'groupid'}){  push(@glsStudentsList, $stdid); } }
      $ggsgrpfile = $groups_folder . $whatis{'groupid'} . '_data.txt'; $ggsid = $whatis{'groupid'};
      open(UPL, $ggsgrpfile);
      @ggsprojectlist = <UPL>;
      close(UPL);
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
          #$newline = $newline . "GLS_UserComment\_$stdid: $whatis{$rlscomm}\n";    $newline = $newline . "GLS_HomeWork\_$stdid: $whatis{$rlshome}\n";

      }
}

#####################################################################################
########################## ADD NEW CALENDAR DAYS SUB ################################
#####################################################################################
sub addNewCalendarDays {  ($ancNextYear, @others) = @_;
   @aptatizimi = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday');
   $apta{'Monday'} = 1; $apta{'Tuesday'} = 2; $apta{'Wednesday'} = 3; $apta{'Thursday'} = 4;
   $apta{'Friday'} = 5; $apta{'Saturday'} = 6; $apta{'Sunday'} = 7;
   $aisan{'01'} = 31; $aisan{'02'} = 28; $aisan{'03'} = 31; $aisan{'04'} = 30; 
   $aisan{'05'} = 31; $aisan{'06'} = 30; $aisan{'07'} = 31; $aisan{'08'} = 31; 
   $aisan{'09'} = 30; $aisan{'10'} = 31; $aisan{'11'} = 30; $aisan{'12'} = 31;
   $ancIntIndx = int ( $ancNextYear / 4 ); $ancFltIndx = $ancNextYear / 4;
   if ( $ancIntIndx == $ancFltIndx ) { $aisan{'02'}++; }
   # @ailartizimi = ('01', '02', '03','04', '05', '06', '07', '08', '09', '10', '11', '12');
   ($ancClndrNum, $ancClndrDate, $ancClndrWeek, @other) = split (/<tab>/, $myCalendarLastLine);  
   $ancWeekDayNum = $apta{$ancClndrWeek};
   foreach $ancAi (@ailartizimi) { $ancDay = 0;   #12<tab>12.01.19<tab>Saturday
      while ( $ancDay < $aisan{$ancAi} ) { $ancDay++; $ancClndrNum++;
         $ancWeekDay = $aptatizimi[$ancWeekDayNum]; $ancWeekDayNum++;
         if ( $ancWeekDayNum == 7 ) { $ancWeekDayNum = 0; }
         if ( $ancDay < 10 ) { $ancDayTxt = '0' . $ancDay; } else { $ancDayTxt = $ancDay; }
         $ancNewLineTxt = "$ancClndrNum<tab>$ancDayTxt\.$ancAi\.$ancNextYear<tab>$ancWeekDay";
         push(@ancNewCalendarDaysList, $ancNewLineTxt);
      }
   }
   #$calendar_file = $oe_folder . 'nextYearCalendar.txt';
   open(CLNDR,">>$calendar_file");
   foreach $i (@ancNewCalendarDaysList) { print CLNDR "\n$i"; }
   close(CLNDR);
}

#####################################################################################
############################ FINISH END BODY ########################################
#####################################################################################

#print "<p>.</p><p><a href=\'$httpindexcgi\'>Список всех школ</a></p>\n";
#print "<p>.</p><p><a href=\'$httpreadcgi?list=groups\&schoolid=$whatis{'schoolid'}\'>Список групп школы № $whatis{'schoolid'}</a></p>\n";
#print "<p>.</p><p><a href=\'$httpreadcgi?list=all\'>Общий список в основной таблице</a></p>\n";
if($userlogged == 1){
   if ( $gotusrid eq '6' || $gotusrid eq '8' || $gotusrid eq '3' || $gotusrid eq '9' ){
      open(INF, $adminText_file); @adminTextList = <INF>; close(INF); print @adminTextList; 
      &printfile($end, $title);
   }
}
else {print "</body></html>";}
#if($userbrowser eq 'desktop'){print "<p><a href=\'$httpindexcgi\?browser=mobile\'>MOBILE</a></p>\n";}
#else{print "<p><a href=\'$httpindexcgi\?browser=desktop\'>DESKTOP</a></p>\n";}



##################################################################################################################
################################# Sub checkcookies ###############################################################
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