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
        if($cookiekey =~ /volonteersproject/){$gotcookie = $hotcookie; }
    }
#$gotcookie = $ENV{'HTTP_COOKIE'};
$cookie_file = '../oedata/vl_cookies.txt';
$accesslevel = 8;
$cookiemaxamount = 50;
###################### end of cookie part #########################
$users_file = '../oedata/leaders.txt';
$oe_folder = '../oedata/';
$groups_folder = '../oedata/groups/';
$oe_sl_balls_file = '../oedata/oe_sl_balls_data.txt';
$oeLiftStudPoints = 1200;
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$indexcgi = 'active.cgi';
$students_file = $oe_folder . 'students.txt';
$upd_user_file = $oe_folder . 'ld_upd_usr.txt';
$adminText_file = $oe_folder . 'admin.txt';
$activeText_file = $oe_folder . 'activehtml.txt';
$lessons_file = $oe_folder . 'lessons.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpgroupcgi = 'http://accelerator.kvadra.kz/cgi-bin/group.cgi';
$httpcalendarcgi = 'http://accelerator.kvadra.kz/cgi-bin/ldrcalendar.cgi';
$httppersoncgi = 'http://accelerator.kvadra.kz/cgi-bin/person.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Read lists';

open(INF, $cookie_file); @cookielist = <INF>; close(INF); foreach $i(@cookielist){
    chomp($i); #8<tab>8250732421875<tab>Tue Apr 23 14:16:01 2013<tab>172.28.113.66<tab>reserve
    ($clusrnum, $clusrrnd, $clusrdate, $clusrip, @other) = split (/<tab>/, $i);
    $oeusercookiernd{$clusrnum} = $clusrrnd;
    $oeusercookiedate{$clusrnum} = $clusrdate;
    $oeusercookieip{$clusrnum} = $clusrip;
}

open(INF, $lessons_file); @lessonslist = <INF>; close(INF); foreach $i(@lessonslist){  chomp($i); 
    ($lesspwd, $lessnum, $lessgrp, $lesschl, $lessdate, $lesstime, @other) = split (/<tab>/, $i);
    $lessIndx = $lessgrp . '_' . $lesschl . '_' . $lessdate; $lessPassword{$lessIndx} = $lesspwd;
    $lessonNumber{$lesspwd} = $lessnum; $lessonGroup{$lesspwd} = $lessgrp; 
    if ( $lessgrp ne '' ) { $lessonExist{$lessIndx} = 1; }
    $lessonSchool{$lesspwd} = $lesschl; $lessonDate{$lesspwd} = $lessdate;
    if ( $lessdate eq $datenow ) { $lessonExist{$lesspwd} = 1; } $lessonTime{$lesspwd} = $lesstime;
}

@uniqueSchoolNumList = "";  @uniqueGroupNumList = "";  @studentUniqueNumList = "";
open(INF, $students_file); @studentslist = <INF>; close(INF); foreach $i(@studentslist){ 
   #1<tab>56BC4567<tab>Томирис<tab>Толенді<tab><tab>71<tab>71-1-M1
   #$usernum<tab>$userID<tab>$user1stname<tab>$user2ndname<tab>$user3rdname<tab>$userschool<tab>$usergroup<tab>$other
   ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp,
   $tstudbrthd, $tstudphnnm, $tstudwrkplc, $tstudemail, @other) = split (/<tab>/, $i);
   $tstudemail = lc $tstudemail; $tstudemail =~s/ //g; if ( $tstudemail =~ /\@/ ) { $studentEmail{$tstudid} = $tstudemail; }
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
   #3<tab>54LD4705<tab>Болатхан<tab>Джайдаринов<tab><tab>1<tab>85<tab>85-1-M2<tab>8 777 277 0326<tab>b.jaidarinov@gmail.com<tab>25.07.2019<tab>reserve
   ($tusrnum, $tusrid, $tusrfrstnam, $tusrscndnam, $tusrthrdnam, $tusrpwd, $tusrsclid, $tusrgrpid, $tusrphnnum, $tusremail, @other) = split (/<tab>/, $i);
   $tusremail = lc $tusremail; $tusremail =~s/ //g;
   $userFullName{$tusrid} = "$tusrfrstnam $tusrscndnam"; $userpwd{$tusrid} = $tusrpwd; $userpwd{$tusremail} = $tusrpwd;
   $userFirstName{$tusrid} = $tusrfrstnam; $userCode{$tusrid} = $tusrid; $userCode{$tusremail} = $tusrid;
   $userSchoolId{$tusrid} = $tusrsclid; $userGroupId{$tusrid} = $tusrgrpid; 
   push(@loginuserslist, $tusrid);
}
$cnt = 0;
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
if ( $whatis{'email'} ne '' ) { $whatis{'email'} = lc $whatis{'email'}; $whatis{'email'} =~s/ //g; }
&checkcookies();
print "\n";
if($userbrowser eq 'desktop'){ &printfile($bas, $title);}
else {&printfile($basm, $title);}

if ( $whatis{'action'} ne '' ) { open(GURD,">>$log_file");
print GURD "Time: [$timedatenow] User ID: [$gotusrid] IP address: [$userip] User action: [$whatis{'action'}] Script: [$indexcgi] \n";
close(GURD); }
#####################################################################################
########################## LOGIN CHECK PART #########################################
#####################################################################################
print "<p>";
if ( $userlogged == 1 && $gotusrid =~ /54LD/ ) {
   print "Привет волонтёр $b1 $userFirstName{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>\n";
   print "<p> </p>\n<table $grnclr><tr><td $ac> $b1 $rf Напоминаем про Итоговое Тестирование! $f2
   <br>Запишите его как урок обязательно! $b2 </td></tr></table><p> </p>\n";
########################## START ADMIN PART #########################################
   if ( $gotusrid eq '54LD4705' ) {
      open(CTRD, $upd_user_file);    $updatedLeaderId = <CTRD>;    close(CTRD); 
      print "<form method='post' action=\'$indexcgi\'><select name='changeuser'>"; 
      if ( $whatis{'changeuser'} ne '' ) { print "<option value = \'$whatis{'changeuser'}\' selected>$userFullName{$whatis{'changeuser'}}</option>\n"; }
      foreach $i (@loginuserslist) { 
         if ( $updatedLeaderId eq $i && $whatis{'changeuser'} eq '' ) { print "<option value = \'$i\' selected>$userFullName{$i}</option>\n"; }
         else { print "<option value = \'$i\'>$userFullName{$i}</option>\n"; } }
      print "</select><input type = 'submit' value = 'Change User'></form>\n"; 
      if ( $whatis{'changeuser'} ne '' ) { open(CTRD,">$upd_user_file"); print CTRD $whatis{'changeuser'}; close(CTRD);
         $gotusrid = $whatis{'changeuser'}; print "<h3>User updated: [$gotusrid]</h3>\n";    }
      elsif ( $updatedLeaderId =~ /54LD/ ) { $gotusrid = $updatedLeaderId; print "<h3>User updated: [$gotusrid]</h3>\n"; }
   }   
######################### FINISH ADMIN PART #########################################
   $lcpGroupId = $whatis{'groupid'};
   foreach $tmpGrpId (@uniqueGroupNumList) {
      $whatis{'groupid'} = $tmpGrpId; &getGroupSub();
      if ( $OEP_VolunteerOneCode{$tmpGrpId} eq $gotusrid || $OEP_VolunteerTwoCode{$tmpGrpId} eq $gotusrid ) { $glbGroupActive{$tmpGrpId} = 1; }
   }
   $whatis{'groupid'} = $lcpGroupId;
   if ( $whatis{'groupid'} eq '' ) { $whatis{'groupid'} = $userGroupId{$gotusrid}; }
   elsif ( $glbGroupActive{$whatis{'groupid'}} != 1 ) { $whatis{'groupid'} = $userGroupId{$gotusrid}; }
   ($whatis{'schoolid'}, @others) = split ( /-/, $whatis{'groupid'} ); 
   
   if ( $whatis{'action'} eq 'create' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' ) { &createLessonSub(); }
   elsif ( $whatis{'action'} eq 'record' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){&recordLessonSub();}
   elsif ( $whatis{'action'} eq 'door' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){&openDoorsSub();}
   elsif ( $whatis{'action'} eq 'savedoor' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){&saveDoorsSub();}
   elsif ( $whatis{'action'} eq 'read' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){&getLessonSub(); &printListLessons();}
   elsif ( $whatis{'action'} eq 'open' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' && $whatis{'lessonid'} ne ''){&openLessonSub();}
   elsif ( $whatis{'action'} eq 'delete' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' && $whatis{'lessonid'} ne ''){&deleteLessonSub();}
   else { &openBlankPage(); }
}
else{
    if ( $whatis{'action'} eq 'login' && $userlogged != 1) { print "<p>$rf $errorlogin $f2</p>\n" ; }  
    print "<form method='post' action=\'$httpindexcgi\'><table><caption>Enter Login Data</caption><tr><td>Email: </td>
    <td><input type = 'text'  name = 'email'></td>  <td>Password: </td><td><input type = 'password'  name = 'userpwd'> </td>
    <td><input type = 'hidden' name = 'action' value = 'login'> <input type = 'submit' value = 'Enter'></td></tr></table></form>\n";
    print "<p><a href=\'$httppersoncgi?action=reset\'>Изменить Пароль?</a></p>";
    &printfile($activeText_file, $title);
}
#####################################################################################
########################### START MAIN BODY #########################################
#####################################################################################
sub openBlankPage {
   $myclr = $yelclr; $cnt = 0; $obpGrpId = $whatis{'groupid'}; $obpTxtLine = '';
   foreach $obpTmpGrpId (@uniqueGroupNumList) {
      $whatis{'groupid'} = $obpTmpGrpId; &getGroupSub();
      if ( $OEP_VolunteerOneCode{$obpTmpGrpId} eq $gotusrid ) {
         if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
         $obpTxtLine = $obpTxtLine . "<tr $myclr><td><a href=\'$httpindexcgi?action=list\&groupid\=$obpTmpGrpId\'>$obpTmpGrpId</a>
          [1-ый волонтер]</td> <td align='center'>$existGroup{$obpTmpGrpId}</td>
         <td><a href=\'$httpindexcgi?action=read\&groupid\=$obpTmpGrpId\'>Посмотреть историю уроков</a></td>
         <td><a href=\'$httpindexcgi?action=create\&groupid\=$obpTmpGrpId\'>Записать Урок</a></td></tr>\n";
      }
      elsif ( $OEP_VolunteerTwoCode{$obpTmpGrpId} eq $gotusrid ) {
         if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
         $obpTxtLine = $obpTxtLine . "<tr $myclr><td><a href=\'$httpindexcgi?action=list\&groupid\=$obpTmpGrpId\'>$obpTmpGrpId</a>
         [2-ой волонтер]</td> <td align='center'>$existGroup{$obpTmpGrpId}</td>
         <td><a href=\'$httpindexcgi?action=read\&groupid\=$obpTmpGrpId\'>Посмотреть историю уроков</a></td>
         <td><a href=\'$httpindexcgi?action=create\&groupid\=$obpTmpGrpId\'>Записать Урок</a></td></tr>\n";
      }
   }
   $whatis{'groupid'} = $obpGrpId ;
   
   if ( $obpGrpId ne '' ) { 
       print "<p> </p><table><tr $myclr><td>Группа №</td><td>Кол-во<br>учеников</td><td>История уроков</td><td>Новый Урок</td></tr>\n";
       if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
       print "<tr $myclr><td><a href=\'$httpindexcgi?action=list\&groupid\=$userGroupId{$gotusrid}\'>$userGroupId{$gotusrid}</a></td>
       <td align='center'>$existGroup{$userGroupId{$gotusrid}}</td>
       <td><a href=\'$httpindexcgi?action=read\&groupid\=$userGroupId{$gotusrid}\'>Посмотреть историю уроков</a></td>
       <td><a href=\'$httpindexcgi?action=create\&groupid\=$userGroupId{$gotusrid}\'>Записать Урок</a></td></tr>$obpTxtLine</table>\n";
   }
   else { print "<h3>У Вас нет активной группы для показа. <br>Пожалуйста обратитесь к координатору, чтобы Вам назначили группу.</h3>\n"; }
   if ( $whatis{'action'} eq 'list' && $whatis{'groupid'} ne '' ) { ######## LIST of STUDENTS ###########
       $obpLessIndx = $whatis{'groupid'} . '_' . $whatis{'schoolid'} . '_' . $datenow; 
       $obpLessPass = $lessPassword{$obpLessIndx}; $obpLessCodeTxt = '';
       if ( $lessonExist{$obpLessPass} == 1 ) { $obpLessCodeTxt = "<table><tr $grnclr><td><h3>$rf По данной группе урок открыт сегодня. 
       <br>Кодовое слово урока: [$obpLessPass] $f2</h3></td></tr></table>"; }
       print "<p> </p>\n"; $myclr = $yelclr; $cnt = 0;
       print "<table><tr $myclr><td>N</td><td>$whatis{'groupid'} Group</td></tr>\n";
       foreach $stdid (@studentUniqueNumList){
          if ( $studentGroupNum{$stdid} =~ $whatis{'groupid'} ) { $cnt++;
             if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
             # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents ;$totalSchools; $totalGroups
             print "<tr $myclr><td>$cnt</td><td>$studentFirstName{$stdid} $studentThirdName{$stdid} $studentSecondName{$stdid}</td></tr>\n";
          }
       } # $userSchoolId{$tusrid} = $tusrsclid; $userGroupId{$tusrid} = $tusrgrpid; 
       print "</table><p> </p><button onclick=\"window.location.href = \'$httpindexcgi?action=door\&groupid\=$whatis{'groupid'}';\" 
  style='height:50px; width:150px'>Открыть Урок</button>  <p> </p> $obpLessCodeTxt <p> </p>\n";
   }
   print "<p> </p><table cellpadding='7' border='2'><tr bgcolor = 'gainsboro'><td>
   <a href=\'$httppersoncgi?action=show\'><h3>Персональные Данные</h3></a></td>
   <td>-[]-[]-[]-</td><td><a href=\'$httpcalendarcgi\'><h3>Календарь Занятий</h3></a></td></tr>
   </table><p> </p><p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n";
}

#####################################################################################
################################ SAVE DOORS SUB #####################################
#####################################################################################
sub saveDoorsSub { $sdsCodeExist = 0;
   open(INF, $lessons_file);   @sdsLessonsList = <INF>;   close(INF);
   foreach $sdsLine ( @sdsLessonsList ) { if ( $sdsLine ne '' ) { chomp($sdsLine);
      ($tsdsCode, @other) = split (/<tab>/, $sdsLine);
      if ( $whatis{'code'} eq $tsdsCode ) { $sdsCodeExist = 1; }
      if ( $sdsLine =~ /$datenow/ ) { push(@sdsNewLessonsList, $sdsLine); }
   } }
   if ( $sdsCodeExist == 1 ) { print "<h2>$rf Такой код уже использован! Укажите другой код.. $f2</h2>\n"; &openDoorsSub(); }
   else {
      print "<table $grnclr><tr><td><h2>Данные записаны!</h2></td></tr></table>
      <h3>Урок будет открыт два часа</h3><table>
      <tr $yelclr><td>Урок: </td><td $ac>$b1 $whatis{'lessid'} $b2</td></tr>
      <tr $yelclr1><td>Школа: </td><td $ac>$b1 $whatis{'schoolid'} $b2</td></tr>
      <tr $yelclr><td>Группа: </td><td $ac>$b1 $whatis{'groupid'} $b2</td></tr>
      <tr $yelclr1><td>Время: </td><td $ac>$b1 $whatis{'hour'}\:$whatis{'mins'}\:00 $b2</td></tr>
      <tr $yelclr><td>Кодовое слово: </td><td $ac>$b1 $whatis{'code'} $b2</td></tr> </table>
      <p> </p><p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n"; 
      $sdsNewCodeLineTxt = "$whatis{'code'}<tab>$whatis{'lessid'}<tab>$whatis{'groupid'}<tab>$whatis{'schoolid'}<tab>";
      $sdsNewCodeLineTxt = $sdsNewCodeLineTxt . "$datenow<tab>$whatis{'hour'}\:$whatis{'mins'}\:00<tab>$gotusrid<tab>rest\n";
      open(SDSDATA,">$lessons_file");
      foreach $i (@sdsNewLessonsList) { print SDSDATA "$i\n"; }
      print SDSDATA $sdsNewCodeLineTxt;
      close(SDSDATA);
      
   }
}

#####################################################################################
################################ OPEN DOORS SUB #####################################
#####################################################################################
sub openDoorsSub {  
   $odsLessIndx = $whatis{'groupid'} . '_' . $whatis{'schoolid'} . '_' . $datenow; 
   $odsLessPass = $lessPassword{$odsLessIndx}; $odsLessCodeTxt = '';
   if ( $lessonExist{$odsLessPass} == 1 ) { $whatis{'lessid'} = $lessonNumber{$odsLessPass};
      $whatis{'code'} = $odsLessPass; ($whatis{'hour'}, $whatis{'mins'}, $rest) = split(/\:/, $lessonTime{$odsLessPass}); }
   $odsCnt = 0; &printjavascript(); print "<h2>Открыть урок для учеников</h2>
   <form method='post' action=\'$httpindexcgi\' onsubmit='return checkDoorFunction();'>
   <input name = 'action' type = 'hidden' value = 'savedoor'><input name = 'date' type = 'hidden' value = \'$datenow\'>
   <input name = 'groupid' type = 'hidden' value = \'$whatis{'groupid'}\'>
   <table><caption><h3>Группа [$whatis{'groupid'}] Школа [$whatis{'schoolid'}] </h3></caption>
   <tr $yelclr><td>Выберите номер урока: </td><td $ac><select name = 'lessid'><option value = ''>Укажите № урока</option>\n";
   if ( $whatis{'lessid'} ne '' ) { print "<option value = \'$whatis{'lessid'}\' selected>Урок № $whatis{'lessid'}</option>\n"; }
   if ( $whatis{'groupid'} =~ /M2/ || $whatis{'groupid'} =~ /M3/ ) { $odsMaxLess = 33; } else { $odsMaxLess = 21; }
   while ( $odsCnt < $odsMaxLess ) { $odsCnt++; print "<option value = \'$odsCnt\'>Урок № $odsCnt</option>\n"; }
   print "</select></td></tr>\n<tr $yelclr1><td>Дата урока: </td><td $ac><b>Сегодня - $datenow</b></td></tr>
   <tr $yelclr><td>Выберите время урока: </td><td>Часы: <select name = 'hour'>\n   <option value = '08'>08:00</option>\n";
   if ( $whatis{'hour'} ne '' ) { print "<option value = \'$whatis{'hour'}\' selected>$whatis{'hour'}\:00</option>\n"; }
   print "   <option value = '09'>09:00</option>\n   <option value = '10'>10:00</option>\n   <option value = '11'>11:00</option>
   <option value = '12'>12:00</option>\n   <option value = '13'>13:00</option>\n   <option value = '14'>14:00</option>
   <option value = '15'>15:00</option>\n   <option value = '16'>16:00</option>\n   <option value = '17'>17:00</option>
   <option value = '18'>18:00</option>\n</select> Минуты: <select name = 'mins'>\n   <option value = '00'>00</option>\n";
   if ( $whatis{'mins'} ne '' ) { print "<option value = \'$whatis{'mins'}\' selected>$whatis{'mins'}</option>\n"; }
   print "   <option value = '15'>15</option>\n   <option value = '30'>30</option>\n   <option value = '45'>45</option>
   </select></td></tr>\n<tr $yelclr1><td>Выберите кодовое слово: </td>
   <td $ac><input type = 'text' name = 'code' value = \'$whatis{'code'}\'></td></tr>
   <tr $yelclr><td $ac><input type = 'reset' value = 'RESET' style='height:50px; width:150px'></td>
   <td $ac><input type = 'submit' value = 'ENTER' style='height:50px; width:150px'></td></tr>
   </table></form><p> </p>";
   if ( $lessonExist{$odsLessIndx} == 1 ) { print "<table><caption><h3>Список открытых уроков</h3></caption>
      <tr $yelclr><td>Номер урока: </td><td $ac>$b1 $lessonNumber{$odsLessPass} $b2</td></tr>
      <tr $yelclr1><td>Дата урока: </td><td $ac>$b1 Сегодня - $datenow $b2</td></tr>
      <tr $yelclr><td>Время урока: </td><td $ac>$b1 $lessonTime{$odsLessPass} $b2</td></tr>
      <tr $yelclr1><td>Кодовое слово: </td><td $ac>$b1 $odsLessPass $b2</td></tr></table><p> </p>"; }
   print "<p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n";
}

#####################################################################################
############################# DELETE LESSON SUB #####################################
#####################################################################################
sub deleteLessonSub {
      $dlsGroupFile = $groups_folder . $whatis{'groupid'} . '.txt'; $dlsDelStat = 0;
      open(UPL, $dlsGroupFile);
      @dlsProjectList = <UPL>;
      close(UPL);
      foreach $i (@dlsProjectList){
          chomp($i);
          if ( $i =~ /<start of new project = / ) {
              if( $i =~ /$whatis{'lessonid'}/ ){ $dlsDelStat = 1; }
              else { $dlsDelStat = 0; push(@dlsNewProjectList, $i); }
          }
          else { if ( $dlsDelStat == 0 ) { push(@dlsNewProjectList, $i); } }
      }
      open(DLSDATA,">$dlsGroupFile");  foreach $i (@dlsNewProjectList){ chomp($i);  print DLSDATA "$i\n"; } close(DLSDATA);
      print "<p> </p><p><a href=\'$httpindexcgi?action=list\'>$whatis{'schoolid'}-ая</a>
       Школа [группа № $whatis{'groupid'}]</p><h3> $rf Урок удален! $f2</h3>
       <p> </p><p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n";
}
#####################################################################################
############################### OPEN LESSON SUB #####################################
#####################################################################################
sub openLessonSub {
   &getLessonSub();  $olsid = $whatis{'lessonid'};
   print "<p> </p><table>
   <caption><a href=\'$httpindexcgi?action=list\'>$whatis{'schoolid'}-ая</a> Школа</caption>
   <tr $yelclr><td>Группа №</td>  <td $ac>$whatis{'groupid'}</td></tr>
   <tr $yelclr1><td>Тема урока</td><td>$OEP_Topic{$olsid}</td></tr>
   <tr $yelclr><td>Номер урока</td><td $ac>$OEP_Lesson{$olsid}</td></tr>
   <tr $yelclr1><td>Дата урока</td><td $ac>$OEP_Date{$olsid}</td></tr></table><p>.</p><table>
   <tr $yelclr><td>№</td><td>Имя Фамилия</td><td>Посещение</td><td>Опоздание</td><td>Штраф за опоздание</td><td>Тестирование</td>
   <td>Баллы за тест</td><td>Всего</td><td>Оценка за тему</td><td>Комментарий по ученику</td><td>Оценка за домашнее задание</td></tr>\n";    
   foreach $i (@glsStudentsList){ $cnt = 1;  $olsUserID_PRNum = $i . '_' . $olsid;
      if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; }
      print "<tr $myclr><td>$cnt</td><td>$studentFirstName{$i} $studentSecondName{$i}</td><td $ac>$OEP_Participation{$olsUserID_PRNum}</td>
      <td $ac>$OEP_Late{$olsUserID_PRNum}</td><td $ac>$OEP_LiftMinus{$olsUserID_PRNum}</td><td $ac>$OEP_Test{$olsUserID_PRNum}</td>
      <td $ac>$OEP_LiftPlus{$olsUserID_PRNum}</td><td $ac>$OEP_TotalPoints{$olsUserID_PRNum}</td><td $ac>$OEP_Eval{$olsUserID_PRNum}</td>
      <td $ac>$OEP_UserComment{$olsUserID_PRNum}</td><td $ac>$OEP_HomeWork{$olsUserID_PRNum}</td></tr>\n"; 
      $cnt++;
   }
   if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; }
   print "</table><table><tr $myclr><td>Комментарии</td><td>$OEP_Comments{$olsid}</td></tr></table>
   <p> </p><p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n";
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
          #$newline = $newline . "OEP_UserComment\_$stdid: $whatis{$rlscomm}\n";    $newline = $newline . "OEP_HomeWork\_$stdid: $whatis{$rlshome}\n";
      }
      
}
#####################################################################################
########################## PRINT LIST OF LESSONS SUB ##################################
#####################################################################################
sub printListLessons {    
    print "<p> </p><table><caption>Группа № $whatis{'groupid'}</caption><tr $yelclr><td>Уроки</td>\n";  
    foreach $i (@glsStudentsList){ 
       print "<td>$studentFirstName{$i}";  
       if ( $studentFirstName{$i} ne '' ) { print "<br>"; }
       print "$studentSecondName{$i}</td>"; 
    }
    print "<td>Всего</td><td>Delete</td></tr>\n";   $myclr = $yelclr;
    @glsLessonNumList = sort(@glsLessonNumList);
    #@glsProjectNumList = sort(@glsProjectNumList);
    foreach $pllId ( @glsLessonNumList ) {
        if($pllId ne ''){ ($pllLessId, $i) = split (/<tab>/, $pllId);
            if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; }
            $pllIndexCgiTitle = "title = \'$OEP_Topic{$i}\'";
            $pllIndexCgiText = "<a href=\'$indexcgi?action=open\&groupid\=$whatis{'groupid'}\&lessonid=$i\' $pllIndexCgiTitle>";
            print "<tr $myclr><td>$pllIndexCgiText Урок $OEP_Lesson{$i} [ $OEP_Date{$i} ] </a></td>"; $glsVisitsPerLesson = 0;
            foreach $x (@glsStudentsList){
               $glsUserID_PRNum = $x . '_' . $i;  
               if ( $OEP_Participation{$glsUserID_PRNum} ne '' ) { $tdclr = $grnclr; $glsVisitsPerLesson++; } else { $tdclr = ''; }
               print "<td $tdclr $ac>$OEP_Participation{$glsUserID_PRNum}</td>";
            }
            print "<td $ac>$glsVisitsPerLesson</td>
            <td><a href=\'$indexcgi?action=delete\&groupid\=$whatis{'groupid'}\&lessonid=$i\'>УДАЛИТЬ УРОК</a></td></tr>\n";
        }
    }
    print "</table>\n<p> </p><p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n"; #list=groups&schoolid=71
}
#####################################################################################
############################ CREATE LESSON SUB ######################################
#####################################################################################
sub createLessonSub {
    &printjavascript();  $myclr = $yelclr; $cnt = 0;
    print "</p><form method='post' action=\'$indexcgi\' name = 'createnewlesson' onsubmit='return checkAllFunction();'>";
    print "<table><tr $yelclr>
    <td><a href='#' onclick='return checkFunction(1, 5);'>Укажите тему урока:</a> <input type='hidden' name='topic' value=''></td>
    <td><p id='topic'></p></td></tr>\n"; # Theme topic name
    print "<tr><td><input type='hidden' name = 'schoolid' value= \'$whatis{'schoolid'}\'></td>
    <td><input type='hidden' name='date' value=\'$datenow\'></td></tr>\n";
    print "<tr $yelclr1><td>Укажите номер урока: </td><td><select name = 'lesson'><option value = ''>Укажите № урока</option>\n"; # The lesson's number
    if ( $whatis{'groupid'} =~ /M2/ || $whatis{'groupid'} =~ /M3/ ) { $clsMaxLess = 33; } else { $clsMaxLess = 21; }
    $clsCnt = 0; while ( $clsCnt < $clsMaxLess ) { $clsCnt++; print "<option value = \'$clsCnt\'>Урок № $clsCnt</option>\n"; }
    print "</select></td></tr>\n<tr><td><input type='hidden' name = 'groupid' value= \'$whatis{'groupid'}\'></td>
    <td><input type='hidden' name = 'action' value= 'record'></td></tr>\n";
    print "<tr $yelclr><td><a href='#' onclick='return checkFunction(1, 7);'>Изменить дату урока</a> [DD.MM.YYYY]: </td>
    <td><p id='date'>$daynow\.$ai{$monthnow}\.$yearnow</p></td></tr></table>\n"; # The lesson's date
    print "<p> </p><table>
    <caption><a href=\'$indexcgi?action=list\'>$whatis{'schoolid'}-ая</a> Школа [группа № $whatis{'groupid'}]</caption>\n";
    print "<tr $myclr><td>N</td><td>Students Name</td><td>Participation</td><td>Late</td><td>LIFT [-]</td>";
    print "<td>Test %</td><td>LIFT [+]</td><td>Total</td><td>Evaluation</td><td>Comments</td><td>Homework Quality</td></tr>\n";
    foreach $stdid (@studentUniqueNumList) {
       if ( $studentGroupNum{$stdid} =~ $whatis{'groupid'} ) {
          if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; }
          $cnt++;
          print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' name = 'userid' value= \'$stdid\'></td>";
          print "<td id='name'><a href='#' onclick='return checkFunction($cnt, 1);'>$studentFirstName{$stdid} "; #Students name
          print "$studentThirdName{$stdid} $studentSecondName{$stdid}</a></td>\n<td id='part'><p id='part_$stdid\'>Пришел на урок?</p>
          <input type='hidden' name='part_$stdid\' value='0'></td>\n"; # Participation
          print "<td id='late'><a href='#' onclick='return checkFunction($cnt, 2);'>Опоздал?</a><p id='late_$stdid\'></p>
          <input type='hidden' name='late_$stdid\' value='0'></td>\n"; # Late
          print "<td id='liftminus'><p id='liftMinus_$stdid\'></p><input type='hidden' name='liftMinus_$stdid\' value='0'></td>\n"; # LIFT minus
          print "<td id='test'><a href='#' onclick='return checkFunction($cnt, 3);'>Тестирование?</a>
          <p id='test_$stdid\'></p><input type='hidden' name='test_$stdid\' value='0'></td>\n"; # Test %
          print "<td id='liftplus'><p id='liftPlus_$stdid\'></p><input type='hidden' name='liftPlus_$stdid\' value='0'></td>\n"; # LIFT plus
          print "<td id='total'><p id='totalPoints_$stdid\'></p><input type='hidden' name='totalPoints_$stdid\' value='0'></td>\n"; # TOTAL POINTS
          print "<td id='eval'><a href='#' onclick='return checkFunction($cnt, 4);'>Оценить?</a><p id='eval_$stdid\'></p>
          <input type='hidden' name='eval_$stdid\' value='0'></td>
          <td><input type='text' name='comm_$stdid\' value=''></td><td><select name='home_$stdid\'><option value='' selected>Choose one</option>
          <option value='1'>1</option><option value='2'>2</option><option value='3'>3</option><option value='4'>4</option><option value='5'>5</option>
          <option value='6'>6</option><option value='7'>7</option><option value='8'>8</option><option value='9'>9</option><option value='10'>10</option>
          </select></td></tr>\n"; 
       }
    } #<h4 id="text1" style="display:none">This is some toggleable text</h4>
    print "</table>\n<input type='hidden' id = 'totalusers' name = 'totalusers' value= \'$cnt\'>
    <a href='#' onclick='return showFunction();'>Комментарии?</a>\n
    <table id='comments' style='display:none'> <tr $yelclr> <td>.</td> <td>Вопросы по проведенному занятию:</br>
    Были ли проблемы в целом, какие - опишите!</br>
    Какие из упражнений понравились ученикам, какие - опишите!</br>
    Сталкивались вы с техническими проблемами, какие - опишите!</br>
    Что именно не получилось сделать в ходе проведенного занятия - опишите!</td>
    <td><textarea rows='10' cols='50' name ='comments'></textarea></td></tr></table>
    <table><tr><td $ac><input type = 'reset' value = 'Reset' style='height:50px; width:150px'></td>
    <td> -[-]-[-]-[-]- </td><td $ac><input type = 'submit' value = 'Record Data' style='height:50px; width:150px'></td></tr></table>
    <p> </p><p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n";
}
#####################################################################################
########################## RECORD LESSON SUB ######################################
#####################################################################################
sub recordLessonSub {
   print "<table><tr $yelclr><td>Parameters</td><td>Values</td></tr><tr $yelclr1><td>School</td>
   <td><a href=\'$indexcgi?action=list\'>$whatis{'schoolid'}</a></td></tr>
   <tr $yelclr><td>Group</td><td>$whatis{'groupid'}</td></tr><tr $yelclr1><td>Lesson Number</td><td>$whatis{'lesson'}</td></tr>
   <tr $yelclr><td>Date</td><td>$whatis{'date'}</td></tr><tr $yelclr1><td>Topic</td><td>$whatis{'topic'}</td></tr></table>\n
   <table><tr $yelclr><td>N</td><td>Students name</td><td>Participation</td><td>Late</td><td>LIFT [-]</td>
   <td>Test %</td><td>LIFT [+]</td><td>Total</td><td>Evaluation</td></tr>\n"; $cnt = 1; $myclr = $yelclr;
   foreach $stdid (@studentUniqueNumList){ $myclr = $yelclr;
      if ( $studentGroupNum{$stdid} =~ $whatis{'groupid'} ) {
          $rlspart = 'part_' . $stdid; $rlslate = 'late_' . $stdid; $rlstest = 'test_' . $stdid;  
          $rlseval = 'eval_' . $stdid; $rlscomm = 'comm_' . $stdid; $rlshome = 'home_' . $stdid; 
          if ( $whatis{$rlspart} eq '1' ) {
             $rlsLiftMinus{$stdid} = $whatis{$rlslate} * 10; if($whatis{$rlstest} > 50){$rlsLiftPlus{$stdid} = ($whatis{$rlstest} - 50) * 10;}
             $rlsTotalPoints{$stdid} = 1200 - $rlsLiftMinus{$stdid} + $rlsLiftPlus{$stdid};  
             $cnt1 = $cnt / 2; $cnt2 = int( $cnt / 2 ); if($cnt1 == $cnt2){$myclr = $yelclr;} else{$myclr = $yelclr1;}
             print "<tr $myclr><td>$cnt</td><td>$studentFirstName{$stdid} $studentThirdName{$stdid} $studentSecondName{$stdid}</td> 
             <td>$whatis{$rlspart}</td> <td>$whatis{$rlslate}</td> <td>$rlsLiftMinus{$stdid}</td> <td>$whatis{$rlstest}</td>
             <td>$rlsLiftPlus{$stdid}</td> <td>$rlsTotalPoints{$stdid}</td> <td>$whatis{$rlseval}</td></tr>\n";
             $newline = $newline . "OEP_Participation\_$stdid: $whatis{$rlspart}\n";
             $newline = $newline . "OEP_LateMinutes\_$stdid: $whatis{$rlslate}\n";
             $newline = $newline . "OEP_LiftMinus\_$stdid: $rlsLiftMinus{$stdid}\n";
             $newline = $newline . "OEP_Tests\_$stdid: $whatis{$rlstest}\n";
             $newline = $newline . "OEP_LiftPlus\_$stdid: $rlsLiftPlus{$stdid}\n";
             $newline = $newline . "OEP_TotalPoints\_$stdid: $rlsTotalPoints{$stdid}\n";
             $newline = $newline . "OEP_Eval\_$stdid: $whatis{$rlseval}\n";
             $newline = $newline . "OEP_UserComment\_$stdid: $whatis{$rlscomm}\n";
             $newline = $newline . "OEP_HomeWork\_$stdid: $whatis{$rlshome}\n"; # $studentEmail{$tstudid}
             $oe_sl_balls_line = $oe_sl_balls_line . "OPENENGLISH<tab>requested<tab>$gotusrid<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'lesson'}";
             $oe_sl_balls_line = $oe_sl_balls_line . "<tab>$stdid<tab>$studentEmail{$stdid}<tab>$oeLiftStudPoints<tab>$timedatenow<tab>STUDENT<tab>reserve\n";
          }
          else {
             $cnt1 = $cnt / 2; $cnt2 = int( $cnt / 2 ); if ( $cnt1 == $cnt2 ) { $myclr = $yelclr; } else { $myclr = $yelclr1; }
             print "<tr $myclr><td>$cnt</td><td>$studentFirstName{$stdid} $studentThirdName{$stdid} $studentSecondName{$stdid}</td> 
             <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td></tr>\n"; }
          $cnt++; 
      }
   }
   $whatis{'comments'} =~s/\n/<br>/g; $whatis{'comments'} =~s/\n//g; $whatis{'comments'} =~s/\n//g;
   print "</table>\n<br><table><tr $myclr><td>Comments and remarks: </td><td>$whatis{'comments'}</td></tr></table>\n";
   open(SLPDATA,">>$oe_sl_balls_file"); print SLPDATA $oe_sl_balls_line; close(SLPDATA);  # Points assigned to each student for Social LIFT project
   $group_file = $groups_folder . $whatis{'groupid'} . '.txt';
   $generateRandomNumber =  $gotusrid . '-' .  $yearnow . $daynow . $ai{$monthnow} .  $hournow . $minutenow . $secondnow;
   open(OEPDATA,">>$group_file");
   #binmode(OEPDATA, ":utf8");
   print OEPDATA "\n<start of new project = $generateRandomNumber>\n";
   print OEPDATA "OEP_School: $whatis{'schoolid'}\n";
   print OEPDATA "OEP_Group: $whatis{'groupid'}\n";
   print OEPDATA "OEP_Lesson: $whatis{'lesson'}\n";
   print OEPDATA "OEP_Date: $whatis{'date'}\n";
   print OEPDATA "OEP_Topic: $whatis{'topic'}\n";
   print OEPDATA $newline;
   print OEPDATA "OEP_Comments: $whatis{'comments'}\n";
   close(OEPDATA);
   print "<p> </p><p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>";
   # print "<br>\n <p>.</p><p><a href=\'$httpreadcgi?list=all\'>Общий список в основной таблице</a></p>\n";
}

#####################################################################################
################################# GET GROUP SUB ######################################
#####################################################################################
sub getGroupSub {
    $ggsgrpfile = $groups_folder . $whatis{'groupid'} . '_data.txt'; $ggsid = $whatis{'groupid'};
    open(UPL, $ggsgrpfile);
    @ggsprojectlist = <UPL>;
    close(UPL);
    foreach $i (@ggsprojectlist){  chomp($i);  
          if($i =~ /OEP_School: /){$i =~ s/OEP_School: //g; $OEP_School{$ggsid} = $i;}
       elsif($i =~ /OEP_Group: /){$i =~ s/OEP_Group: //g; $OEP_Group{$ggsid} = $i;}
       elsif($i =~ /OEP_StartDate: /){$i =~ s/OEP_StartDate: //g; $OEP_StartDate{$ggsid} = $i;}
       elsif($i =~ /OEP_FinishDate: /){$i =~ s/OEP_FinishDate: //g; $OEP_FinishDate{$ggsid} = $i;}
       elsif($i =~ /OEP_Paid: /){$i =~ s/OEP_Paid: //g; $OEP_Paid{$ggsid} = $i;}
       elsif($i =~ /OEP_Status: /){$i =~ s/OEP_Status: //g; $OEP_Status{$ggsid} = $i;}
       elsif($i =~ /OEP_Calendar: /){$i =~ s/OEP_Calendar: //g; $OEP_Calendar{$ggsid} = $i;}
       elsif($i =~ /OEP_TimeList: /){$i =~ s/OEP_TimeList: //g; $OEP_TimeList{$ggsid} = $i;}
       elsif($i =~ /OEP_VolunteerOne: /){$i =~ s/OEP_VolunteerOne: //g; $OEP_VolunteerOne{$ggsid} = $i;}
       elsif($i =~ /OEP_VolunteerOneCode: /){$i =~ s/OEP_VolunteerOneCode: //g; $OEP_VolunteerOneCode{$ggsid} = $i;}
       elsif($i =~ /OEP_VolunteerTwo: /){$i =~ s/OEP_VolunteerTwo: //g; $OEP_VolunteerTwo{$ggsid} = $i;}
       elsif($i =~ /OEP_VolunteerTwoCode: /){$i =~ s/OEP_VolunteerTwoCode: //g; $OEP_VolunteerTwoCode{$ggsid} = $i;}
    }
}
#######################################################################################
########################### JAVASCRIPT PART ###########################################
#######################################################################################
sub printjavascript {
print  <<EOT;
 <script>
 function checkDoorFunction (){ 
    if(document.getElementsByName('lessid')[0].value == ''){alert('Выберите номер урока!'); return false;}
    if(document.getElementsByName('code')[0].value == ''){alert('Укажите кодовое слово!'); return false;}
 }
 function checkAllFunction (){
        if(document.getElementsByName('lesson')[0].value == ''){alert('Укажите номер урока!'); return false;}
        if(document.getElementsByName('topic')[0].value == ''){alert('Укажите тему урока!'); return false;}
 }
 function showFunction(){ var x = document.getElementById('comments');
  if (x.style.display === 'none') {x.style.display = 'block'; } else { x.style.display = 'none'; }
 }
 function checkFunction (id, act){
    var dat = 'date' ;  var top = 'topic';  var les = 'lesson' ;      var dateval = document.getElementsByName(dat)[0].value;
    var part = 'part_' + document.getElementById(id).value;           var late = 'late_' + document.getElementById(id).value;  
    var lim = 'liftMinus_' + document.getElementById(id).value;       var test = 'test_' + document.getElementById(id).value;     
    var lip = 'liftPlus_' + document.getElementById(id).value;        var tot = 'totalPoints_' + document.getElementById(id).value; 
    var eval = 'eval_' + document.getElementById(id).value;           var totval = Number(document.getElementsByName(tot)[0].value); 
    var limval = Number(document.getElementsByName(lim)[0].value);    var lipval = Number(document.getElementsByName(lip)[0].value); 
    var lateval = Number(document.getElementsByName(late)[0].value);  var usr; var testval = Number(document.getElementsByName(test)[0].value);

    if(act == '1'){
          usr = confirm('Ученик пришел на урок?');
          if(usr){
              document.getElementsByName(part)[0].value = '1'; document.getElementById(part).innerHTML = 'Да!';
              document.getElementsByName(tot)[0].value = 1200; document.getElementById(tot).innerHTML = 1200;
          }
          else{
              document.getElementsByName(part)[0].value = '0'; document.getElementById(part).innerHTML = 'Нет!';
              document.getElementsByName(tot)[0].value = '0'; document.getElementById(tot).innerHTML = '0';
          }
    }
    else if(act == '2'){
          usr = Number(prompt('На сколько минут опоздал?', '0')); limval = usr * 10;
           if(usr > 0 && usr < 120 && document.getElementsByName(part)[0].value == '1'){
              document.getElementsByName(late)[0].value = usr; document.getElementById(late).innerHTML = usr;
              document.getElementsByName(tot)[0].value = 1200 - limval; document.getElementById(tot).innerHTML = 1200 - limval;
              document.getElementsByName(lim)[0].value = limval; document.getElementById(lim).innerHTML = limval;
           }
    }
    else if(act == '3'){
          usr = Number(prompt('Введите только цифры', '0')); lipval = (usr -50) * 10;
           if(usr > 50 && usr < 101 && document.getElementsByName(part)[0].value == '1'){
              document.getElementsByName(test)[0].value = usr; document.getElementById(test).innerHTML = usr;
              document.getElementsByName(tot)[0].value = 1200 - limval + lipval; document.getElementById(tot).innerHTML = 1200 - limval + lipval;
              document.getElementsByName(lip)[0].value = lipval; document.getElementById(lip).innerHTML = lipval;
           }
    }
    else if(act == '4'){
         usr = Number(prompt('Укажите оценку от 1 до 10', '0'));
         if(usr > 0 && usr < 11 && document.getElementsByName(part)[0].value == '1'){
            document.getElementsByName(eval)[0].value = usr; document.getElementById(eval).innerHTML = usr;
         }
    }
    else if(act == '5'){
         usr = prompt('Укажите тему урока');
         document.getElementsByName(top)[0].value = usr; document.getElementById(top).innerHTML = usr;
    }
    else if(act == '6'){usr = Number(prompt('Укажите номер урока'));
         if(usr > 0 && usr < 31){document.getElementsByName(les)[0].value = usr; document.getElementById(les).innerHTML = usr;}
    }
    else if(act == '7'){
         usr = prompt('Измените дату урока', dateval);
         if (isValidDate(usr)) { document.getElementsByName(dat)[0].value = usr; document.getElementById(dat).innerHTML = usr; }
         else {alert('Неправильная дата: [' + usr + ']!');}
    }
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
    if ( $gotcookie =~ /volonteersproject/ && $whatis{'action'} ne 'logout' && $whatis{'action'} ne 'login' ) { $iwashere = 1;
       if ( $oeusercookiernd{$gcusrnum} eq $gcusrrnd && $userip eq $oeusercookieip{$gcusrnum} && $userip ne '' ) {  
          $userlogged = 1;   $gotusrid = $gcusrnum;
          if($whatis{'browser'} eq 'mobile'){ $userbrowser = 'mobile'; }
          elsif($whatis{'browser'} eq 'desktop'){ $userbrowser = 'desktop'; }
          else{ $userbrowser = $gcusrbrowser; }
          $newcookie = "volonteersproject\=$gcusrnum\_$gcusrrnd\_$userbrowser\; expires=$live_time\; path=/\;";
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
          $newcookie = "volonteersproject=0_1234567890_desktop\; expires=$live_time\; path=/\;";
          print "Set-Cookie: " . $newcookie . "\n";  $iwashere = 2;
       }
       elsif ( $whatis{'action'} eq 'login' ) {
          if ( $whatis{'userpwd'} eq $userpwd{$whatis{'email'}} && $whatis{'userpwd'} ne '' ) {
              $ccUserNumber = $userCode{$whatis{'email'}};
              if ( $ccUserNumber =~ /54LD/ ) { $gotusrid = $ccUserNumber; }  else { $gotusrid = 0; }
              $randnum = int(rand(10)*1000000000000);       $oeusercookiernd{$gotusrid} = $randnum;
              $oeusercookiedate{$gotusrid} = $timedatenow;  $oeusercookieip{$gotusrid} = $userip;
              $newcookie = "volonteersproject\=$gotusrid\_$randnum\_desktop\; expires=$live_time\; path=/\;";
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