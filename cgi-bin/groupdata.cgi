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
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$indexcgi = 'groupdata.cgi';
$students_file = $oe_folder . 'students.txt';
$leaders_file = $oe_folder . 'leaders.txt';
$calendar_file = $oe_folder . 'calendar.txt';
$adminText_file = $oe_folder . 'admin.txt';
$trainers_file = $oe_folder . 'trainers.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpreadcgi = 'http://accelerator.kvadra.kz/cgi-bin/read.cgi';
$httpgroupcgi = 'http://accelerator.kvadra.kz/cgi-bin/group.cgi';
$httpstudentcgi = 'http://accelerator.kvadra.kz/cgi-bin/student.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Group Details';

open(INF, $cookie_file); 
@cookielist = <INF>;
close(INF);
foreach $i(@cookielist){
    chomp($i); #8<tab>8250732421875<tab>Tue Apr 23 14:16:01 2013<tab>172.28.113.66<tab>reserve
    ($clusrnum, $clusrrnd, $clusrdate, $clusrip, @other) = split (/<tab>/, $i);
    $oeusercookiernd{$clusrnum} = $clusrrnd;
    $oeusercookiedate{$clusrnum} = $clusrdate;
    $oeusercookieip{$clusrnum} = $clusrip;
}

open(INF, $trainers_file); @trainerslist = <INF>;  close(INF);  foreach $i(@trainerslist){
   # No<tab>Uniques ID<tab>1st name<tab>2nd name<tab>3rd name<tab>PWD<tab>Phone Num<tab>Email<tab>Date<tab>Reserve
   #$trnrnum<tab>$trnrID<tab>$trnr1stname<tab>$trnr2ndname<tab>$trnr3rdname<tab>$trnrpwd<tab>$usergroup<tab>$other
   ($ttrnrnum, $ttrnrid, $ttrnrfirstnam, $ttrnrscndnam, $ttrnrthrdnam, $ttrnrpwd, $ttrnrphn, $ttrnremail, @other) = split (/<tab>/, $i);
   if($ttrnrid ne ''){  $TrainerFullName{$ttrnrid} = "$ttrnrfirstnam $ttrnrscndnam $ttrnrthrdnam"; $ttrnremail = lc $ttrnremail;
      $TrainerUniqueId{$ttrnrid} = $ttrnrid; $TrainerFirstName{$ttrnrid} = $ttrnrfirstnam; $TrainerSecondName{$ttrnrid} = $ttrnrscndnam;
      $TrainerThirdName{$ttrnrid} = $ttrnrthrdnam; $TrainerPositionNum{$ttrnrid} = $ttrnrnum; $TrainerPhoneNum{$ttrnrid} = $ttrnrphn; 
      $TrainerEmail{$ttrnrid} = $ttrnremail; $TrainerPwd{$ttrnrid} = $ttrnrpwd; push(@globalTrainersList, $ttrnrid); $totalTrainers++;
   }
}

open(INF, $leaders_file); @leaderslist = <INF>; close(INF); foreach $i(@leaderslist){
   # No<tab>Uniques ID<tab>1st name<tab>2nd name<tab>3rd name<tab>PWD<tab>School ID<tab>Group ID<tab>Phone Num<tab>Email<tab>Date<tab>Reserve
   #$ldrnum<tab>$ldrID<tab>$ldr1stname<tab>$ldr2ndname<tab>$ldr3rdname<tab>$ldrpwd<tab>$userschool<tab>$usergroup<tab>$other
   ($tldrnum, $tldrid, $tldrfirstnam, $tldrscndnam, $tldrthrdnam, $tldrpwd, $tldrschl, $tldrgrp, $tldrphn, $tldremail, @other) = split (/<tab>/, $i);
   if ( $tldrnum ne '' && $tldrid ne '' ) { $glLastLeaderNumber = $tldrnum; $glLastLeaderCode = $tldrid; }
   if($tldrid ne ''){  $LeaderFullName{$tldrid} = "$tldrfirstnam $tldrscndnam $tldrthrdnam";
      $LeaderUniqueId{$tldrid} = $tldrid; $LeaderFirstName{$tldrid} = $tldrfirstnam; $LeaderSecondName{$tldrid} = $tldrscndnam;
      $LeaderThirdName{$tldrid} = $tldrthrdnam; $LeaderPositionNum{$tldrid} = $tldrnum;   $LeaderSchoolNum{$tldrid} = $tldrschl;
      $LeaderGroupNum{$tldrid} = $tldrgrp; $LeaderPhoneNum{$tldrid} = $tldrphn; $LeaderEmail{$tldrid} = $tldremail; 
      push(@globalLeadersIdList, $tldrid); $totalLeaders++;
   }
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
    ($tclndrnum, $tclndrdate, $tcndrweek, @other) = split (/<tab>/, $i);   #12<tab>12.01.19<tab>Saturday
    $calendarweek{$tclndrnum} = $tcndrweek; $calendardate{$tclndrnum} = $tclndrdate;
    $calendarweek{$tclndrdate} = $tcndrweek;  $calendarnumber{$tclndrdate} = $tclndrnum;
}

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
&checkcookies();
print "\n";
if($userbrowser eq 'desktop'){ &printfile($bas, $title);}
else {&printfile($basm, $title);}

if ( $whatis{'action'} ne '' ) { open(GURD,">>$log_file");
print GURD "Time: [$timedatenow] User ID: [$gotusrid] IP address: [$userip] User action: [$whatis{'action'}] Script: [$indexcgi] \n";
close(GURD); }

#######################################################################################
########################## JAVASCRIPT PART ###########################################
#######################################################################################
sub printjavascript {
print  <<EOT;
 <script>
function showTableRaws(ShowId) {
    var my_disply = document.getElementById(ShowId).style.display;
    if(my_disply == "block"){document.getElementById(ShowId).style.display = "none";}
    else{document.getElementById(ShowId).style.display = "block";}
}
 function checkAllFunction (){ var x = 0;
        if(document.getElementsByName('schoolid')[0].value == ''){alert('Выберите номер школы!'); return false;}
        if(document.getElementsByName('groupid')[0].value == ''){alert('Укажите номер группы!'); return false;}
        if(document.getElementsByName('traineer')[0].value == ''){alert('Выберите тренера!'); return false;}
        if(document.getElementsByName('volunteerone')[0].value == ''){alert('Укажите 1-го волонтера!'); return false;}
        if(document.getElementsByName('volunteertwo')[0].value == ''){alert('Укажите 2-го волонтера!'); return false;}
        if(isValidDate(document.getElementsByName('datestart')[0].value)){} else {
        alert('Неверный формат даты: [' + document.getElementsByName('datestart')[0].value + ']!'); return false;}
        if(isValidDate(document.getElementsByName('dateend')[0].value)){} else {
        alert('Неверный формат даты: [' + document.getElementsByName('dateend')[0].value + ']!'); return false;}
        if(document.getElementsByName('paid')[0].value == ''){alert('Выберите тип модуля!'); return false;}
        if(document.getElementsByName('status')[0].value == ''){alert('Выберите статус группы!'); return false;}
        if(document.getElementsByName('monday')[0].checked || document.getElementsByName('tuesday')[0].checked
        || document.getElementsByName('wednesday')[0].checked || document.getElementsByName('thursday')[0].checked
        || document.getElementsByName('friday')[0].checked || document.getElementsByName('saturday')[0].checked
        || document.getElementsByName('sunday')[0].checked){x = 1;} else{alert('Укажите дни недели!'); return false;}
        if(document.getElementsByName('mondaytime')[0].value == '' && document.getElementsByName('tuesdaytime')[0].value == ''
        && document.getElementsByName('wednesdaytime')[0].value == '' && document.getElementsByName('thursdaytime')[0].value == ''
        && document.getElementsByName('fridaytime')[0].value == '' && document.getElementsByName('saturdaytime')[0].value == ''
        && document.getElementsByName('sundaytime')[0].value == ''){alert('Укажите время уроков!'); return false;}
 }
 function checkEditFunction (){ var x = 0;
        if(document.getElementsByName('traineer')[0].value == ''){alert('Выберите тренера!'); return false;}
        if(document.getElementsByName('volunteerone')[0].value == ''){alert('Укажите 1-го волонтера!'); return false;}
        if(document.getElementsByName('volunteertwo')[0].value == ''){alert('Укажите 2-го волонтера!'); return false;}
        if(isValidDate(document.getElementsByName('datestart')[0].value)){} else {
        alert('Неверный формат даты: [' + document.getElementsByName('datestart')[0].value + ']!'); return false;}
        if(isValidDate(document.getElementsByName('dateend')[0].value)){} else {
        alert('Неверный формат даты: [' + document.getElementsByName('dateend')[0].value + ']!'); return false;}
        if(document.getElementsByName('paid')[0].value == ''){alert('Выберите тип модуля!'); return false;}
        if(document.getElementsByName('status')[0].value == ''){alert('Выберите статус группы!'); return false;}
        
 }
 function isValidDate(dateString) {
    if(!/^\\d{1,2}\\.\\d{1,2}\\.\\d{4}\$/.test(dateString)) {return false;} var parts = dateString.split(".");
    var day = parseInt(parts[0], 10); var month = parseInt(parts[1], 10); var year = parseInt(parts[2], 10);
    if(year < 1000 || year > 3000 || month == 0 || month > 12) { return false; }
    var monthLength = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];
    if(year % 400 == 0 || (year % 100 != 0 && year % 4 == 0)) {  monthLength[1] = 29; }
    return day > 0 && day <= monthLength[month - 1];
 }
</script> 
EOT
}
#####################################################################################
########################## LOGIN CHECK PART #######################################
#####################################################################################
print "<p>";
if($userlogged == 1){
    print "Hello $b1 $userfirstname{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>";
    if($whatis{'action'} eq 'create'){&createGroupSub();}
    elsif($whatis{'action'} eq 'biglist' ){&printGroupList();}
    elsif($whatis{'action'} eq 'write' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' ){ &writeGroupSub(); }
    elsif($whatis{'action'} eq 'record' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){ &recordGroupSub(); }
    elsif($whatis{'action'} eq 'edit' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){ &editGroupSub(); }
    elsif($whatis{'action'} eq 'open' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){ &printjavascript(); &openGroupSub(); }
    else{&blankPageSub();}
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
      print "<p> </p><h1><a href=\'$httpindexcgi?action=biglist\'>Open all groups</a></h1>\n";
      print "<p> </p>"; $myclr = $yelclr; $cnt = 0;
      print "<table><caption>Список всех школ</caption>\n";
      print "<tr $myclr><td>№</td><td>Школа №</td><td>Кол-во учеников</td><td>Группа-1</td><td>Группа-2</td>
      <td>Группа-3</td><td>Группа-4</td><td>Группа-5</td><td>Группа-6</td></tr>\n";
      foreach $sclid (@uniqueSchoolNumList){
          if( length( $sclid ) > 0){
                if($myclr eq $yelclr){$myclr = $yelclr1;} else{$myclr = $yelclr;}
                $cnt++; # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents; $totalSchools; $totalGroups
                print "<tr $myclr><td>$cnt</td><td  align='center'>$sclid</td><td  align='center'>$existSchool{$sclid}</td>";
                foreach $grpid (@uniqueGroupNumList){
                    if($groupSchoolNum{$grpid} eq $sclid){ 
                    print "<td><a href=\'$httpindexcgi?action=open\&groupid=$grpid\&schoolid=$sclid\'>$grpid</a> [$existGroup{$grpid}]</td>";  }
                }
                print "</tr>\n";
          }
      }
      if($myclr eq $yelclr){$myclr = $yelclr1;} else{$myclr = $yelclr;}
      print "<tr $myclr><td>Sum:</td><td  align='center'>$totalSchools</td><td  align='center'>$totalStudents</td></tr></table><p> </p>\n"; 
      print "<h2><a href=\'$httpindexcgi?action=create'>Create New Group Header</a> </h2>";

}
#####################################################################################
############################### OPEN GROUP SUB ######################################
#####################################################################################
sub openGroupSub {
   &getGroupSub(); $ogsid = $whatis{'groupid'};  $ogsUserId = $OEP_Editor{$ogsid};  
   $ogsMaxLess = 21;  if($ogsid =~ /M2/ || $ogsid =~ /M3/){$ogsMaxLess = 33;} 
   print "<p> </p><table>
   <caption><a href=\'$httpreadcgi?list=groups\&schoolid=$whatis{'schoolid'}\'>$whatis{'schoolid'}-ая</a> Школа [Группа № $whatis{'groupid'}]</caption>
   <tr $yelclr><td>Created</td><td $ac>$OEP_Created{$ogsid}</td></tr> 
   <tr $yelclr1><td>Editor</td><td>$userfirstname{$ogsUserId} $userlastname{$ogsUserId}</td></tr> 
   <tr $yelclr><td>Группа №</td><td $ac>$OEP_Group{$ogsid} [$existGroup{$ogsid}]</td></tr> 
   <tr $yelclr1><td>Traineer</td><td $ac>$OEP_Traineer{$ogsid}</td></tr>
   <tr $yelclr><td>First Volonteer</td><td $ac>$LeaderFullName{$OEP_VolunteerOneCode{$ogsid}}</td></tr> 
   <tr $yelclr1><td>Second Volonteer</td><td $ac>$LeaderFullName{$OEP_VolunteerTwoCode{$ogsid}}</td></tr>
   <tr $yelclr><td>Start Date</td><td $ac>$OEP_StartDate{$ogsid}</td></tr> 
   <tr $yelclr1><td>Finish Date</td><td $ac>$OEP_FinishDate{$ogsid}</td></tr>
   <tr $yelclr><td>Status of the group</td><td $ac>$OEP_Status{$ogsid}</td></tr></table>";
   print "<p><a href=\'javascript:showTableRaws(\"$whatis{'groupid'}\");' >Подробный план занятий группы [$whatis{'groupid'}]</a></p>
   <table style='display: none\;' id=\'$whatis{'groupid'}\'> <tr $yelclr><td>Day of week</td>\n";  
     #if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
     
   if($OEP_Calendar{$ogsid} ne ''){
      (@ogsCalendarList) = split(/\, /, $OEP_Calendar{$ogsid});  (@ogsTimeList) = split(/<tab>/, $OEP_TimeList{$ogsid});  $ogsCheckLoop = 0;
      $cnt = 0;  $ogsWeekLine = ''; $ogsGraphLine = ''; $ogsLessLine = ''; $ogsVisitLine = '';   $ogsCalDay = $ogsCalendarList[0]; 
      while($cnt < $ogsMaxLess){
         print "<td id = \'$ogsCheckLoop\' name = 'checkLoop'>$calendarweek{$ogsCalDay}</td>";   
         $ogsWeekLine = $ogsWeekLine . "<td>$calendardate{$ogsCalDay}</td>";  $tcnt = $cnt + 1;
         if ( $OEP_Group{$ogsid} =~ /M0/ ){ $ogsAddTxt = $moduleZeroText{$tcnt}; }
         elsif ( $OEP_Group{$ogsid} =~ /M1/ ){ $ogsAddTxt = $moduleOneText{$tcnt}; }
         elsif ( $OEP_Group{$ogsid} =~ /M2/ ){ $ogsAddTxt = $moduleTwoText{$tcnt}; }
         else { $ogsAddTxt = ''; }
         if ( $ogsCalendarList[$cnt] =~/$ogsCalDay/){
            $ogsGraphLine = $ogsGraphLine . "<td  id = \'$cnt\' name = 'cnt'>$ogsTimeList[$cnt]</td>" ; 
            $cnt++; $ogsLessLine = $ogsLessLine . "<td $ac>$cnt $ogsAddTxt</td>";
         }
         else{ $ogsGraphLine = $ogsGraphLine . "<td id = \'$cnt\' name = 'cnt'></td>"; 
         $ogsLessLine =  $ogsLessLine . "<td></td>"; }
         if($ogsCheckLoop > 100){last;}
         $ogsCalDay++;   $ogsCheckLoop++;
      }
   }
   print "</tr>\n<tr $yelclr1><td>Date</td>$ogsWeekLine</tr><tr $yelclr><td>Lessons Graph</td>$ogsGraphLine</tr>
   <tr $yelclr1><td>Lesson number</td>$ogsLessLine</tr></table>\n
   <h1><a href=\'$httpindexcgi?action=edit&schoolid=$whatis{'schoolid'}\&groupid=$whatis{groupid}\'>Редактировать данные группы [$whatis{groupid}]</a></h1>";
   # $calendarweek{$tclndrnum} = $tcndrweek; $calendardate{$tclndrnum} = $tclndrdate;
   # $calendarweek{$tclndrdate} = $tcndrweek;  $calendarnumber{$tclndrdate} = $tclndrnum;
}
#####################################################################################
################################# GET GROUP SUB ######################################
#####################################################################################
sub getGroupSub {
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
########################## PRINT LIST OF LESSONS SUB ##################################
#####################################################################################
sub printGroupList {    
    &printjavascript();    #print "<p>@uniqueGroupNumList</p>\n";
    foreach $pglGrpID (@uniqueGroupNumList){
       if ( length ( $pglGrpID ) > 0 ){
          ($whatis{'schoolid'}, @rest) = split(/-/, $pglGrpID);
          $whatis{'groupid'} = $pglGrpID;  &openGroupSub();  
       }
    }
}
#####################################################################################
################################ EDIT GROUP SUB #####################################
#####################################################################################
sub editGroupSub {  #$LeaderFirstName{$tldrid} = $tldrfirstnam; $LeaderSecondName{$tldrid} = $tldrscndnam;
    &printjavascript();  &getGroupSub();  $egsid =  $whatis{'groupid'};  #@uniqueSchoolNumList
    #$egsVolOneCode = $whatis{'volunteerone'}; $egsVolOneName = $LeaderFullName{$egsVolOneCode};
    #$egsVolTwoCode = $whatis{'volunteertwo'}; $egsVolTwoName = $LeaderFullName{$egsVolTwoCode};
    print "<p> </p><form method='post' action=\'$indexcgi\' name = 'editgroup' onsubmit='return checkEditFunction();'> 
    <input type = 'hidden' name = 'action' value = 'write'>\n";
    print "<table><tr $yelclr1><td>№ школы:</td> <td>$whatis{'schoolid'} 
    <input type = 'hidden' name = 'schoolid' value = \'$whatis{'schoolid'}\'></td></tr>\n"; # School number
    print "<tr $yelclr><td>№ группы:</td> <td>$whatis{'groupid'} 
    <input type = 'hidden' name = 'groupid' value = \'$whatis{'groupid'}\'></td></tr>\n";  # Group number
    print "<tr $yelclr1><td>Выберите тренера:</td> 
    <td><select name ='traineer'><option value=\'$OEP_Traineer{$egsid}\' selected>$OEP_Traineer{$egsid}</option>";
    foreach $egsUser (@globalTrainersList) { # @globalTrainersList $TrainerFullName{$egsUser}
       print "<option value = \'$TrainerFullName{$egsUser}\'>$TrainerFullName{$egsUser}</option>\n"; }    # Traineer
    print "</select></td></tr>\n<tr $yelclr><td>1-ый волонтер:</td> <td><select name ='volunteerone'>";
    if ($OEP_VolunteerOne{$egsid} ne '') { 
    print "<option value = \'$OEP_VolunteerOneCode{$egsid}\' selected>$LeaderFullName{$OEP_VolunteerOneCode{$egsid}}</option>"; }
    foreach $egsUser (@globalLeadersIdList){ print "<option value = \'$egsUser\'>$LeaderFullName{$egsUser}</option>\n"; }    # Volunteer 1
    print "</select></td></tr>\n<tr $yelclr1><td>2-ой волонтер:</td><td><select name ='volunteertwo'>\n";
    if ($OEP_VolunteerTwo{$egsid} ne '') { 
    print "<option value=\'$OEP_VolunteerTwoCode{$egsid}\' selected>$LeaderFullName{$OEP_VolunteerTwoCode{$egsid}}</option>"; }
    foreach $egsUser (@globalLeadersIdList){ print "<option value=\'$egsUser\'>$LeaderFullName{$egsUser}</option>\n"; }    # Volunteer 2
    print "</select></td></tr>\n"; 
    if ( $OEP_StartDate{$egsid} eq '' ) { $OEP_StartDate{$egsid} = $datenow; } 
    if ( $OEP_FinishDate{$egsid} eq '' ) { $OEP_FinishDate{$egsid} = $datenow; }
    print "<tr $yelclr><td>Дата начала уроков:</td> 
    <td><input type='text' name='datestart' value=\'$OEP_StartDate{$egsid}\'></td></tr>\n"; #Start Date
    print "<tr $yelclr1><td>Дата завершения уроков:</td> 
    <td><input type='text' name='dateend' value=\'$OEP_FinishDate{$egsid}\'></td></tr>\n"; # Finish Date
    print "<tr $yelclr><td>Модуль платный? :</td><td> <select name ='paid'>
    <option value=\'$OEP_Paid{$egsid}\' selected>$OEP_Paid{$egsid}</option>
    <option value='Paid'>Paid</option>\n<option value='Pilot'>Pilot</option>\n</select> </td></tr>
    <tr $yelclr1><td>Текущий статус группы:</td>       <td><select name ='status'>
    <option value=\'$OEP_Status{$egsid}\' selected>$OEP_Status{$egsid}</option>
    <option value='Active'>Active</option>  <option value='Frozen'>Frozen</option>
    <option value='Finished'>Finished</option>\n<option value='Cancelled'>Cancelled</option>\n</select></td></tr></table>
    <p><input type = 'hidden' name = 'mondaytime' value = \'$OEP_MondayTime{$egsid}\'> 
    <input type = 'hidden' name = 'tuesdaytime' value = \'$OEP_TuesdayTime{$egsid}\'>
    <input type = 'hidden' name = 'wednesdaytime' value = \'$OEP_WednesdayTime{$egsid}\'> 
    <input type = 'hidden' name = 'thursdaytime' value = \'$OEP_ThursdayTime{$egsid}\'>
    <input type = 'hidden' name = 'fridaytime' value = \'$OEP_FridayTime{$egsid}\'> 
    <input type = 'hidden' name = 'saturdaytime' value = \'$OEP_SaturdayTime{$egsid}\'>
    <input type = 'hidden' name = 'sundaytime' value = \'$OEP_SundayTime{$egsid}\'> 
    <input type = 'hidden' name = 'monday' value = \'$OEP_Monday{$egsid}\'>
    <input type = 'hidden' name = 'tuesday' value = \'$OEP_Tuesday{$egsid}\'> 
    <input type = 'hidden' name = 'wednesday' value = \'$OEP_Wednesday{$egsid}\'>
    <input type = 'hidden' name = 'thursday' value = \'$OEP_Thursday{$egsid}\'> 
    <input type = 'hidden' name = 'friday' value = \'$OEP_Friday{$egsid}\'>
    <input type = 'hidden' name = 'saturday' value = \'$OEP_Saturday{$egsid}\'> 
    <input type = 'hidden' name = 'sunday' value = \'$OEP_Sunday{$egsid}\'></p>\n";  
    # $egsMaxLess = 18;  if($egsid =~ /M2/){$egsMaxLess = 30;} 
    if($OEP_Calendar{$egsid} ne ''){   
 #  $calendarweek{$tclndrnum} = $tcndrweek; $calendardate{$tclndrnum} = $tclndrdate; 
 # $calendarweek{$tclndrdate} = $tcndrweek;  $calendarnumber{$tclndrdate} = $tclndrnum;
       print "<table><caption>Edit dates and time of each lessons</caption><tr><td>№ урока</td><td>Дата урока</td><td>Время урока</td></tr>\n";  
       (@egsCalendarList) = split(/\, /, $OEP_Calendar{$egsid});  (@egsTimeList) = split(/<tab>/, $OEP_TimeList{$egsid});  
       $egsCheckLoop = 0;    $cnt = 0;    $egsCalDay = $egsCalendarList[0]; 
       foreach $egsId (@egsCalendarList){   $tcnt = $cnt + 1;
          if($myclr eq $yelclr){$myclr = $yelclr1;} else{$myclr = $yelclr;}
          print "<tr $myclr><td>Урок №  $tcnt</td><td><input type='text' name='less\_$cnt' value=\'$calendardate{$egsId}\'></td>
          <td><input type='text' name='time\_$cnt' value=\'$egsTimeList[$cnt]\'></td></tr>\n";  
          $cnt++;
       }
       if( $cnt == 18 || $cnt == 30 ){ 
          if($myclr eq $yelclr){$myclr = $yelclr1;} else{$myclr = $yelclr;} $tcnt = $cnt + 1;
          print "<tr $myclr><td>Урок №  $tcnt</td><td><input type='text' name='less\_$cnt' value=\'$ekiaialga\'></td>
          <td><input type='text' name='time\_$cnt' value=\'$egsTimeList[$cnt]\'></td></tr>\n"; $cnt++; 
          if($myclr eq $yelclr){$myclr = $yelclr1;} else{$myclr = $yelclr;} $tcnt = $cnt + 1;
          print "<tr $myclr><td>Урок №  $tcnt</td><td><input type='text' name='less\_$cnt' value=\'$ekiaialga\'></td>
          <td><input type='text' name='time\_$cnt' value=\'$egsTimeList[$cnt]\'></td></tr>\n"; $cnt++; 
          if($myclr eq $yelclr){$myclr = $yelclr1;} else{$myclr = $yelclr;} $tcnt = $cnt + 1;
          print "<tr $myclr><td>Урок №  $tcnt</td><td><input type='text' name='less\_$cnt' value=\'$ekiaialga\'></td>
          <td><input type='text' name='time\_$cnt' value=\'$egsTimeList[$cnt]\'></td></tr>\n"; $cnt++; 
       }
   }
   print "</table><p> <input type = 'hidden' name = 'listmax' value = \'$cnt\'> </p><table> <tr><td $ac>
   <input type = 'reset' value = 'Reset' style='height:50px; width:150px'></td> <td> -[-]-[-]-[-]- </td>
   <td $ac><input type = 'submit' value = 'Record Data' style='height:50px; width:150px'></td></tr></table>\n";
}
#####################################################################################
############################# CREATE GROUP SUB ######################################
#####################################################################################
sub createGroupSub {    &printjavascript();  #@uniqueSchoolNumList # @globalTrainersList $TrainerFullName{$egsUser}
    print "<p> </p><form method='post' action=\'$indexcgi\' name = 'createnewgroup' onsubmit='return checkAllFunction();'>
    <input type = 'hidden' name = 'action' value = 'record'>\n";
    print "<table><tr $yelclr1><td>Выберите школу:</td> <td><select name ='schoolid'><option value='' selected>Select one</option>";
    foreach $cgsSchid (@uniqueSchoolNumList) { 
       if ( length($cgsSchid) > 0 ) { print "<option value=\'$cgsSchid\'>$cgsSchid</option>\n"; } } 
    print "</select></td></tr>\n";#School number
    print "<tr $yelclr><td>Выберите группу:</td> <td><select name ='groupid'><option value='' selected>Select one</option>";  # Group number
    foreach $cgsGrpid (@uniqueGroupNumList){if(length($cgsGrpid)>0){print "<option value = \'$cgsGrpid\'>$cgsGrpid</option>";}}
    print "</select></td></tr>\n<tr $yelclr1><td>Выберите тренера:</td> <td><select name ='traineer'><option value='' selected>Select one</option>";
    foreach $cgsUser (@globalTrainersList) { 
       print "<option value = \'$TrainerFullName{$cgsUser}\'>$TrainerFullName{$cgsUser}</option>\n"; }    print "</select></td></tr>\n"; # Traineer
    print "<tr $yelclr><td>1-ый волонтер:</td> <td><select name ='volunteerone'><option value='' selected>Select one</option>"; # Volunteer 1
    foreach $cgsUser (@globalLeadersIdList){print "<option value=\'$cgsUser\'>$LeaderFullName{$cgsUser}</option>\n";} print "</select></td></tr>\n";
    print "<tr $yelclr1><td>2-ой волонтер:</td> <td><select name ='volunteertwo'><option value='' selected>Select one</option>"; # Volunteer 2
    foreach $cgsUser (@globalLeadersIdList){print "<option value=\'$cgsUser\'>$LeaderFullName{$cgsUser}</option>\n";} print "</select></td></tr>\n"; 
    print "<tr $yelclr><td>Дата начала уроков:</td> <td><input type='text' name='datestart' value=\'$datenow\'> Format: DD.MM.YYYY</td></tr>\n"; #Start Date
    print "<tr $yelclr1><td>Дата завершения уроков:</td> <td><input type='text' name='dateend' value=\'$datenow\'> Format: DD.MM.YYYY</td></tr>\n"; # Finish Date
    print "<tr $yelclr><td>Модуль платный? :</td><td> <select name ='paid'>\n<option value='' selected>Select one</option>
    <option value='Paid'>Платный</option>\n<option value='Free'>Пилотный</option>\n</select> </td></tr><tr $yelclr1><td>Текущий статус группы:</td> 
    <td><select name ='status'>\n<option value='' selected>Select one</option>
    <option value='Active'>Активный</option>\n<option value='Frozen'>Заморожен</option>
    <option value='Finished'>Завершен</option>\n<option value='Cancelled'>Отменен</option>\n</select></td></tr></table><p> </p>\n"; #Paid or Pilot
    print "<table><caption>Выберите дни занятий</caption><tr $yelclr><td>Выберите дни недели</td>
    <td><input type='checkbox' name='monday' value='1'>Monday</td>
    <td><input type='checkbox' name='tuesday' value='1'>Tuesday</td> <td><input type='checkbox' name='wednesday' value='1'>Wednesday</td>  
    <td><input type='checkbox' name='thursday' value='1'>Thursday</td> <td><input type='checkbox' name='friday' value='1'>Friday<br></td> 
    <td><input type='checkbox' name='saturday' value='1'>Saturday<br></td> <td><input type='checkbox' name='sunday' value='1'>Sunday</td></tr>
    <tr $yelclr1><td>Время уроков</td><td><input type='text' name='mondaytime' value=''></td><td><input type='text' name='tuesdaytime' value=''></td>
    <td><input type='text' name='wednesdaytime' value=''></td><td><input type='text' name='thursdaytime' value=''></td>
    <td><input type='text' name='fridaytime' value=''></td><td><input type='text' name='saturdaytime' value=''></td>
    <td><input type='text' name='sundaytime' value=''></td></tr></table>\n"; # The lesson's time
    print "<p> </p><table> <tr><td $ac><input type = 'reset' value = 'Reset' style='height:50px; width:150px'></td><td> -[-]-[-]-[-]- </td>
    <td $ac><input type = 'submit' value = 'Record Data' style='height:50px; width:150px'></td></tr></table>\n";
}

#####################################################################################
############################## WRITE GROUP SUB ######################################
#####################################################################################
sub writeGroupSub {
    $wgsVolOneCode = $whatis{'volunteerone'}; $wgsVolOneName = $LeaderFullName{$wgsVolOneCode};
    $wgsVolTwoCode = $whatis{'volunteertwo'}; $wgsVolTwoName = $LeaderFullName{$wgsVolTwoCode};
    print "<table><tr $yelclr><td>Parameters</td><td>Values</td></tr><tr $yelclr1><td>School</td><td>$whatis{'schoolid'}</td></tr>
    <tr $yelclr><td>Group</td><td>$whatis{'groupid'}</td></tr><tr $yelclr1><td>Traineer of group</td><td>$whatis{'traineer'}</td></tr>
    <tr $yelclr><td>First Volunteer</td><td>$wgsVolOneName</td></tr><tr $yelclr1><td>Second Volunteer</td><td>$wgsVolTwoName</td></tr>
    <tr $yelclr><td>Start Date</td><td>$whatis{'datestart'}</td></tr><tr $yelclr1><td>Finish Date</td><td>$whatis{'dateend'}</td></tr>
    <tr $yelclr><td>Paid module</td><td>$whatis{'paid'}</td></tr><tr $yelclr1><td>Status of the group</td><td>$whatis{'status'}</td></tr></table><p> </p>
    <table><caption>Edited dates and time of each lessons</caption><tr><td>№ урока</td><td>Дата урока</td><td>Время урока</td></tr>\n";
 # $calendarweek{$tclndrnum} = $tcndrweek; $calendardate{$tclndrnum} = $tclndrdate;  $calendarweek{$tclndrdate} = $tcndrweek;  $calendarnumber{$tclndrdate} = $tclndrnum;
    $wgsListMax = $whatis{'listmax'}; $cnt = 0; $tcnt = 0;
    while ($cnt < $wgsListMax){
          $tcnt = $cnt + 1;  $wgsLessId = 'less_' . $cnt;  $wgsTimeId = 'time_' . $cnt; if($myclr eq $yelclr){$myclr = $yelclr1;} else{$myclr = $yelclr;} 
          print "<tr $myclr><td>Урок №  $tcnt</td><td id = \'$wgsLessId\' name = 'LessId'>$whatis{$wgsLessId}</td>
          <td id = \'$calendarnumber{$whatis{$wgsLessId}}\' name = 'calendarnumber'>$whatis{$wgsTimeId}</td></tr>\n";  
          if ( $tcnt == 1 ) { $wgsCalendarList = $calendarnumber{$whatis{$wgsLessId}}; $wgsTimeList = $whatis{$wgsTimeId}; } 
          else { $wgsCalendarList = $wgsCalendarList . ', ' . $calendarnumber{$whatis{$wgsLessId}};  $wgsTimeList = $wgsTimeList . '<tab>' . $whatis{$wgsTimeId};  }  
          $cnt++;
    }
    $group_data_file = $groups_folder . $whatis{'groupid'} . '_data.txt';
    open(WGSDATA,">$group_data_file");
    print WGSDATA "\n<start of new project = $timedatenow>\n";
    print WGSDATA "OEP_Created: $timedatenow\n";
    print WGSDATA "OEP_Editor: $gotusrid\n";
    print WGSDATA "OEP_School: $whatis{'schoolid'}\n";
    print WGSDATA "OEP_Group: $whatis{'groupid'}\n";
    print WGSDATA "OEP_Traineer: $whatis{'traineer'}\n";
    print WGSDATA "OEP_VolunteerOne: $wgsVolOneName\n";
    print WGSDATA "OEP_VolunteerOneCode: $whatis{'volunteerone'}\n";
    print WGSDATA "OEP_VolunteerTwo: $wgsVolTwoName\n";
    print WGSDATA "OEP_VolunteerTwoCode: $whatis{'volunteertwo'}\n";
    print WGSDATA "OEP_StartDate: $whatis{'datestart'}\n";
    print WGSDATA "OEP_FinishDate: $whatis{'dateend'}\n";
    print WGSDATA "OEP_Paid: $whatis{'paid'}\n";
    print WGSDATA "OEP_Status: $whatis{'status'}\n";
    print WGSDATA "OEP_Calendar: $wgsCalendarList\n";
    print WGSDATA "OEP_TimeList: $wgsTimeList\n";
    print WGSDATA "OEP_MondayTime: $whatis{'mondaytime'}\n";
    print WGSDATA "OEP_TuesdayTime: $whatis{'tuesdaytime'}\n";
    print WGSDATA "OEP_WednesdayTime: $whatis{'wednesdaytime'}\n";
    print WGSDATA "OEP_ThursdayTime: $whatis{'thursdaytime'}\n";
    print WGSDATA "OEP_FridayTime: $whatis{'fridaytime'}\n";
    print WGSDATA "OEP_SaturdayTime: $whatis{'saturdaytime'}\n";
    print WGSDATA "OEP_SundayTime: $whatis{'sundaytime'}\n";
    print WGSDATA "OEP_Monday: $whatis{'monday'}\n";
    print WGSDATA "OEP_Tuesday: $whatis{'tuesday'}\n";
    print WGSDATA "OEP_Wednesday: $whatis{'wednesday'}\n";
    print WGSDATA "OEP_Thursday: $whatis{'thursday'}\n";
    print WGSDATA "OEP_Friday: $whatis{'friday'}\n";
    print WGSDATA "OEP_Saturday: $whatis{'saturday'}\n";
    print WGSDATA "OEP_Sunday: $whatis{'sunday'}\n";
    close(WGSDATA);
    
    print "</table><p> Correction Data is recorded! </p><p> </p>\n";
}
#####################################################################################
############################# RECORD GROUP SUB ######################################
#####################################################################################
sub recordGroupSub {
    $rgsVolOneCode = $whatis{'volunteerone'}; $rgsVolOneName = $LeaderFullName{$rgsVolOneCode};
    $rgsVolTwoCode = $whatis{'volunteertwo'}; $rgsVolTwoName = $LeaderFullName{$rgsVolTwoCode};
    print "<table><tr $yelclr><td>Parameters</td><td>Values</td></tr><tr $yelclr1><td>School</td>
    <td><a href=\'$httpreadcgi?list=groups\&schoolid=$whatis{'schoolid'}\'>$whatis{'schoolid'}</a></td></tr>
    <tr $yelclr><td>Group</td><td>$whatis{'groupid'}</td></tr><tr $yelclr1><td>Traineer of group</td><td>$whatis{'traineer'}</td></tr>
    <tr $yelclr><td>First Volunteer</td><td>$rgsVolOneName</td></tr><tr $yelclr1><td>Second Volunteer</td><td>$rgsVolTwoName</td></tr>
    <tr $yelclr><td>Start Date</td><td>$whatis{'datestart'}</td></tr><tr $yelclr1><td>Finish Date</td><td>$whatis{'dateend'}</td></tr>
    <tr $yelclr><td>Paid module</td><td>$whatis{'paid'}</td></tr><tr $yelclr1><td>Status of the group</td><td>$whatis{'status'}</td></tr>
    </table><p> </p><table><caption>Checked week days</caption><tr $yelclr>\n"; if($whatis{'monday'} eq '1'){print "<td>Monday</td>";}
    if($whatis{'tuesday'} eq '1'){print "<td>Tuesday</td>";} if($whatis{'wednesday'} eq '1'){print "<td>Wednesday</td>";} 
    if($whatis{'thursday'} eq '1'){print "<td>Thursday</td>";} if($whatis{'friday'} eq '1'){print "<td>Friday</td>";} 
    if($whatis{'saturday'} eq '1'){print "<td>Saturday</td>";} if($whatis{'sunday'} eq '1'){print "<td>Sunday</td>";}
    print "</tr></table><p> </p>\n";   $rgsLessMax = 21;
    if($whatis{'groupid'} =~/M2/ || $whatis{'groupid'} =~/M3/){$rgsLessMax = 33;} $cnt=1; $rgsDayNum = $calendarnumber{$whatis{'datestart'}}; 
    $rgsLessList = $rgsDayNum;  $rgsCheckLoop = 0;  $rgsTimeList = '';

    while($cnt < $rgsLessMax){
          $rgsDayNum++; $rgsCheckLoop++;
          if ( $calendarweek{$rgsDayNum} =~/Monday/ && $whatis{'monday'} eq '1' ){ $rgsStartTime = $whatis{'mondaytime'};
          $rgsLessList = $rgsLessList . ", $rgsDayNum"; $rgsTimeList = $rgsTimeList . "<tab>$whatis{'mondaytime'}"; $cnt++; }
          elsif ( $calendarweek{$rgsDayNum} =~/Tuesday/ && $whatis{'tuesday'} eq '1' ){ $rgsStartTime = $whatis{'tuesdaytime'};
           $rgsLessList = $rgsLessList . ", $rgsDayNum"; $rgsTimeList = $rgsTimeList . "<tab>$whatis{'tuesdaytime'}"; $cnt++; }
          elsif ( $calendarweek{$rgsDayNum} =~/Wednesday/ && $whatis{'wednesday'} eq '1' ){ $rgsStartTime = $whatis{'wednesdaytime'};
          $rgsLessList = $rgsLessList . ", $rgsDayNum"; $rgsTimeList = $rgsTimeList . "<tab>$whatis{'wednesdaytime'}"; $cnt++; }
          elsif ( $calendarweek{$rgsDayNum} =~/Thursday/ && $whatis{'thursday'} eq '1' ){ $rgsStartTime = $whatis{'thursdaytime'};
          $rgsLessList = $rgsLessList . ", $rgsDayNum"; $rgsTimeList = $rgsTimeList . "<tab>$whatis{'thursdaytime'}"; $cnt++; }
          elsif ( $calendarweek{$rgsDayNum} =~/Friday/ && $whatis{'friday'} eq '1' ){ $rgsStartTime = $whatis{'fridaytime'};
          $rgsLessList = $rgsLessList . ", $rgsDayNum"; $rgsTimeList = $rgsTimeList . "<tab>$whatis{'fridaytime'}"; $cnt++; }
          elsif ( $calendarweek{$rgsDayNum} =~/Saturday/ && $whatis{'saturday'} eq '1' ){ $rgsStartTime = $whatis{'saturdaytime'};
          $rgsLessList = $rgsLessList . ", $rgsDayNum"; $rgsTimeList = $rgsTimeList . "<tab>$whatis{'saturdaytime'}"; $cnt++; }
          elsif ( $calendarweek{$rgsDayNum} =~/Sunday/ && $whatis{'sunday'} eq '1' ){ $rgsStartTime = $whatis{'sundaytime'};
           $rgsLessList = $rgsLessList . ", $rgsDayNum"; $rgsTimeList = $rgsTimeList . "<tab>$whatis{'sundaytime'}"; $cnt++; }
          if($rgsCheckLoop > 300){last;}
    }
    $rgsTimeList = $rgsStartTime . $rgsTimeList;  $group_data_file = $groups_folder . $whatis{'groupid'} . '_data.txt';
    open(RGSDATA,">$group_data_file");
    print RGSDATA "\n<start of new project = $timedatenow>\n";
    print RGSDATA "OEP_Created: $timedatenow\n";
    print RGSDATA "OEP_Editor: $gotusrid\n";
    print RGSDATA "OEP_School: $whatis{'schoolid'}\n";
    print RGSDATA "OEP_Group: $whatis{'groupid'}\n";
    print RGSDATA "OEP_Traineer: $whatis{'traineer'}\n";
    print RGSDATA "OEP_VolunteerOne: $rgsVolOneName\n";
    print RGSDATA "OEP_VolunteerOneCode: $whatis{'volunteerone'}\n";
    print RGSDATA "OEP_VolunteerTwo: $rgsVolTwoName\n";
    print RGSDATA "OEP_VolunteerTwoCode: $whatis{'volunteertwo'}\n";
    print RGSDATA "OEP_StartDate: $whatis{'datestart'}\n";
    print RGSDATA "OEP_FinishDate: $whatis{'dateend'}\n";
    print RGSDATA "OEP_Paid: $whatis{'paid'}\n";
    print RGSDATA "OEP_Status: $whatis{'status'}\n";
    print RGSDATA "OEP_Calendar: $rgsLessList\n";
    print RGSDATA "OEP_TimeList: $rgsTimeList\n";
    print RGSDATA "OEP_MondayTime: $whatis{'mondaytime'}\n";
    print RGSDATA "OEP_TuesdayTime: $whatis{'tuesdaytime'}\n";
    print RGSDATA "OEP_WednesdayTime: $whatis{'wednesdaytime'}\n";
    print RGSDATA "OEP_ThursdayTime: $whatis{'thursdaytime'}\n";
    print RGSDATA "OEP_FridayTime: $whatis{'fridaytime'}\n";
    print RGSDATA "OEP_SaturdayTime: $whatis{'saturdaytime'}\n";
    print RGSDATA "OEP_SundayTime: $whatis{'sundaytime'}\n";
    print RGSDATA "OEP_Monday: $whatis{'monday'}\n";
    print RGSDATA "OEP_Tuesday: $whatis{'tuesday'}\n";
    print RGSDATA "OEP_Wednesday: $whatis{'wednesday'}\n";
    print RGSDATA "OEP_Thursday: $whatis{'thursday'}\n";
    print RGSDATA "OEP_Friday: $whatis{'friday'}\n";
    print RGSDATA "OEP_Saturday: $whatis{'saturday'}\n";
    print RGSDATA "OEP_Sunday: $whatis{'sunday'}\n";
    close(RGSDATA);
    
    print "<p> Data is recorded! </p><p> </p>\n";
}
#####################################################################################
############################ FINISH END BODY #########################################
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
#else{print "<p><a href=\'$httpindexcgi\?browser=desktop\'>DESKTOP</a></p>\n";}

##################################################################################################################
################################# Sub checkcookies ##################################################################
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