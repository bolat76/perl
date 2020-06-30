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
$glbStyle = "style = 'height:50px; width:150px'";
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
        if($cookiekey =~ /trainersproject/){$gotcookie = $hotcookie; }
    }
#$gotcookie = $ENV{'HTTP_COOKIE'};
$cookie_file = '../oedata/tr_cookies.txt';
###################### end of cookie part #########################
$users_file = '../oedata/trainers.txt';
$leaders_file = '../oedata/leaders.txt';
$usersdata_file = '../oedata/trainersdata.txt';
$oe_sl_balls_file = '../oedata/oe_sl_balls_data.txt';
$oe_folder = '../oedata/';
$groups_folder = '../oedata/groups/';
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$glMonthPayValue = 5500;
$oeLiftStudPoints = 1200;
$oeLiftLeaderPoints = 3200;
$indexcgi = 'control.cgi';
$students_file = $oe_folder . 'students.txt';
$upd_user_file = $oe_folder . 'tr_upd_usr.txt';
$lessons_file = $oe_folder . 'lessons.txt';
$calendar_file = $oe_folder . 'calendar.txt';
$parents_file = $oe_folder . 'parents.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpmanagecgi = 'http://accelerator.kvadra.kz/cgi-bin/manage.cgi';
$httpcalendarcgi = 'http://accelerator.kvadra.kz/cgi-bin/trcalendar.cgi';
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
   if ( $tldrid ne '' ) {  $LeaderFullName{$tldrid} = "$tldrfirstnam $tldrscndnam $tldrthrdnam"; $tldremail = lc $tldremail;
      $LeaderUniqueId{$tldrid} = $tldrid; $LeaderFirstName{$tldrid} = $tldrfirstnam; $LeaderSecondName{$tldrid} = $tldrscndnam;
      $LeaderThirdName{$tldrid} = $tldrthrdnam; $LeaderPositionNum{$tldrid} = $tldrnum;   $LeaderSchoolNum{$tldrid} = $tldrschl;
      $LeaderGroupNum{$tldrid} = $tldrgrp; $LeaderPhoneNum{$tldrid} = $tldrphn; $LeaderEmail{$tldrid} = $tldremail; 
      $LeaderBirthDay{$tldrid} = $tldrbrthday; $LeaderGender{$tldrid} = $tldrgender; $LeaderWorkPlace{$tldrid} = $tldrwrkplc;
      $LeaderPersonId{$tldrid} = $tldrprsnid; $LeaderIndividId{$tldrid} = $tldrindvdid; $LeaderPassWord{$tldrid} = $tldrpwd;
      if ( $tldrfirstnam ne '' ) { push(@glLeadersNumList, $tldrid); }
   }
}  # $existSchool{$tldrschl}; $existGroup{$tldrgrp}; $GroupsPerSchool{$tldrschl}; $totalLeaders ;$totalSchools; $totalGroups

@uniqueSchoolNumList = "";  @uniqueGroupNumList = "";  @studentUniqueNumList = "";
open(INF, $students_file); @studentslist = <INF>; close(INF); foreach $i(@studentslist){ 
   #1<tab>56BC4567<tab>Томирис<tab>Толенді<tab><tab>71<tab>71-1-M1
   #$usernum<tab>$userID<tab>$user1stname<tab>$user2ndname<tab>$user3rdname<tab>$userschool<tab>$usergroup<tab>$other
   #($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp, 
   #$tstudbrthd, $tstudphnm, $tstudclss, $tstudemail, @other) = split (/<tab>/, $i);
   ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp, $tstudbrthd, $tstudphnm, @other) = split (/<tab>/, $i);
   if ( $tstudgrp ne '' && $tstudschl ne '' ) { $studentFullName{$tstudid} = "$tstudfirstnam $tstudscndnam";
      $studentFirstName{$tstudid} = $tstudfirstnam; $studentSecondName{$tstudid} = $tstudscndnam;
      $studentThirdName{$tstudid} = $tstudthrdnam; $studentPositionNum{$tstudid} = $tstudnum; 
      $studentSchoolNum{$tstudid} = $tstudschl; $studentGroupNum{$tstudid} = $tstudgrp; 
      $studentBirthDay{$tstudid} = $tstudbrthd; $studentPhoneNum{$tstudid} = $tstudphnm; $existSchool{$tstudschl}++;  $existGroup{$tstudgrp}++; 
      if ( grep( /^$tstudschl$/, @uniqueSchoolNumList ) ) { $done = 1; } else { push(@uniqueSchoolNumList, $tstudschl); $totalSchools++; }
      if ( grep( /^$tstudgrp$/, @uniqueGroupNumList ) ) { $done = 1;} 
      else { $GroupsPerSchool{$tstudschl}++; $totalGroups++; push(@uniqueGroupNumList, $tstudgrp); $groupSchoolNum{$tstudgrp} = $tstudschl; }
      push(@studentUniqueNumList, $tstudid); $totalStudents++;
   }
}  # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents ;$totalSchools; $totalGroups

open(INF, $lessons_file); @lessonslist = <INF>; close(INF); foreach $i(@lessonslist){  chomp($i); 
    ($lesspwd, $lessnum, $lessgrp, $lesschl, $lessdate, $lesstime, @other) = split (/<tab>/, $i);
    $lessIndx = $lessgrp . '_' . $lesschl . '_' . $lessdate; $lessPassword{$lessIndx} = $lesspwd;
    $lessonNumber{$lesspwd} = $lessnum; $lessonGroup{$lesspwd} = $lessgrp; 
    if ( $lessgrp ne '' ) { $lessonExist{$lessIndx} = 1; }
    $lessonSchool{$lesspwd} = $lesschl; $lessonDate{$lesspwd} = $lessdate;
    if ( $lessdate eq $datenow ) { $lessonExist{$lesspwd} = 1; } $lessonTime{$lesspwd} = $lesstime;
}

open(INF, $parents_file); @parentslist = <INF>; close(INF); foreach $i(@parentslist){
   ($tparntnum, $tparntid, $tparntstudid, $tparntfirstnam, $tparntscndnam, $tparntthrdnam, $tparntschl, $tparntgrp,
   $tparntbrtd, $tparntphn, $tparntwrkplc, $tparntemail, @other) = split (/<tab>/, $i);
   if($tparntid ne ''){  $ParentUniqueId{$tparntstudid} = $tparntid;
      $ParentFullName{$tparntid} = "$tparntfirstnam $tparntthrdnam $tparntscndnam";
      $ParentFirstName{$tparntid} = $tparntfirstnam; $ParentSecondName{$tparntid} = $tparntscndnam;
      $ParentThirdName{$tparntid} = $tparntthrdnam; $ParentPositionNum{$tparntid} = $tparntnum; 
      $ParentSchoolNum{$tparntid} = $tparntschl; $ParentGroupNum{$tparntid} = $tparntgrp;     
      $ParentBirthDay{$tparntid} = $tparntbrtd; $ParentPhoneNum{$tparntid} = $tparntphn; 
      $ParentWorkPlace{$tparntid} = $tparntwrkplc; $ParentEmail{$tparntid} = $tparntemail; 
   }
}

open(INF, $calendar_file); @calendar_list = <INF>;close(INF); foreach $i(@calendar_list){ chomp($i); #12<tab>12.01.19<tab>Saturday
    ($tclndrnum, $tclndrdate, $tcndrweek, @other) = split (/<tab>/, $i);  
    $calendarweek{$tclndrnum} = $tcndrweek; $calendarweek{$tclndrdate} = $tcndrweek;
    $calendarnumber{$tclndrdate} = $tclndrnum;  $calendardate{$tclndrnum} = $tclndrdate;
}

open(INF, $users_file); @userlist = <INF>; close(INF); foreach $i(@userlist){ 
   #6<tab>44TR4706<tab>Болатхан<tab>Джайдаринов<tab><tab>1<tab>8 777 277 0326<tab>b.jaidarinov@gmail.com<tab>14.07.2019<tab>reserve
   ($tusrnum, $tusrid, $tusrfrstnam, $tusrscndnam, $tusrthrdnam, $tusrpwd, $tusrphnnum, $tusremail, $tusrdate, @other) = split (/<tab>/, $i);
   if ( $tusrid ne '' ) { $tusremail = lc $tusremail; $tusremail =~s/ //g;
       $userFullName{$tusrid} = "$tusrfrstnam $tusrscndnam $tusrthrdnam"; $userpwd{$tusrid} = $tusrpwd; 
       $userFirstName{$tusrid} = $tusrfrstnam; $userSecondName{$tusrid} = $tusrscndnam; $userEmail{$tusrid} = $tusremail;
       $userThirdName{$tusrid} = $tusrthrdnam; $userCode{$tusrid} = $tusrid; $userCode{$tusremail} = $tusrid;
       push(@loginuserslist, $tusrid); $userPhoneNumber{$tusrid} = $tusrphnnum; 
       if ( $tusremail ne '' ) { $userEmailExist{$tusremail} = 1; $userpwd{$tusremail} = $tusrpwd; }
   }
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
########################## LOGIN CHECK PART #######################################
#####################################################################################
print "<p>";
if ( $userlogged == 1 && $gotusrid =~ /44TR/ ) {
   print "привет тренер $b1 $userFirstName{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>";
   if ( $gotusrid eq '44TR4706' ) {
      open(CTRD, $upd_user_file);    $updatedTrainerId = <CTRD>;    close(CTRD); 
      print "<form method='post' action=\'$indexcgi\'><select name='changeuser'>"; 
      if ( $whatis{'changeuser'} ne '' ) { print "<option value = \'$whatis{'changeuser'}\' selected>$userFullName{$whatis{'changeuser'}}</option>\n"; }
      foreach $i (@loginuserslist) { 
         if ( $updatedTrainerId eq $i && $whatis{'changeuser'} eq '' ) { print "<option value = \'$i\' selected>$userFullName{$i}</option>\n"; }
         else { print "<option value = \'$i\'>$userFullName{$i}</option>\n"; } }
      print "</select><input type = 'submit' value = 'Change User'></form>\n"; 
      if ( $whatis{'changeuser'} ne '' ) { open(CTRD,">$upd_user_file"); print CTRD $whatis{'changeuser'}; close(CTRD);
         $gotusrid = $whatis{'changeuser'}; print "<h3>User updated: [$gotusrid]</h3>\n";    }
      elsif ( $updatedTrainerId =~ /44TR/ ) { $gotusrid = $updatedTrainerId; print "<h3>User updated: [$gotusrid]</h3>\n"; }
   }   
   
   open(INF, $usersdata_file);    @usersDataList = <INF>;    close(INF); 
   foreach $tmpDataLine (@usersDataList) {
      #1<tab>44TR4701<tab>99-1-M1<tab>19.06.19<tab>reserve
      ($tmpUsrNum, $tmpUsrId, $tmpUsrGrpId, $tmpUsrDate, @other) = split (/<tab>/, $tmpDataLine);
      if ( $gotusrid eq $tmpUsrId ) { $glbUserActive{$gotusrid} = 1; $glbGroupActive{$tmpUsrGrpId} = 1; push(@userGroupNumList, $tmpUsrGrpId); }
   }
   if ( $whatis{'groupid'} eq '' && $whatis{'userid'} =~ /56BC/ ) { $lcpUsrId = $whatis{'userid'};
      $lpcUsrGrpId = $studentGroupNum{$lcpUsrId}; $lpcGrpActv = $glbGroupActive{$lpcUsrGrpId};
      if ( $lpcGrpActv == 1 ) { $whatis{'groupid'} = $lpcUsrGrpId; ($whatis{'schoolid'}, @others) = split ( /-/, $whatis{'groupid'} ); }   }
   else { if ( $glbGroupActive{$whatis{'groupid'}} != 1 ) { $whatis{'groupid'} = ''; $whatis{'schoolid'} = ''; }
      ($whatis{'schoolid'}, @others) = split ( /-/, $whatis{'groupid'} );    }
   
   if ( $whatis{'action'} eq 'create' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' ) { &createLessonSub(); }
   elsif ( $whatis{'action'} eq 'showpay' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' ) { &openGroupPageSub(); }
   elsif ( $whatis{'action'} eq 'saveremark' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' ) { &saveGroupCommentsSub(); &openGroupPageSub(); }
   elsif ( $whatis{'action'} eq 'record' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' ) { &recordLessonSub(); }
   elsif ( $whatis{'action'} eq 'edit' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' ) { &editGroupSub(); }
   elsif ( $whatis{'action'} eq 'write' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' ) { &writeGroupSub(); }
   elsif ( $whatis{'action'} eq 'door' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){&openDoorsSub();}
   elsif ( $whatis{'action'} eq 'savedoor' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){&saveDoorsSub();}
   elsif ( $whatis{'action'} eq 'read' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' ) { &getLessonSub(); &printListLessons(); }
   elsif ( $whatis{'action'} eq 'open' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' && $whatis{'lessonid'} ne '' ) { &openLessonSub(); }
   elsif ( $whatis{'action'} eq 'update' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' && $whatis{'lessonid'} ne '' ) { &updateLessonSub(); }
   elsif ( $whatis{'action'} eq 'delete' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' && $whatis{'lessonid'} ne '' ) { &deleteLessonSub(); }
   else { &openBlankPage(); }
}
else{
    if ( $whatis{'action'} eq 'login' && $userlogged != 1) { print "<p>$rf $errorlogin $f2</p>\n" ; }  
    print "<form method='post' action=\'$httpindexcgi\'><table><caption>Enter Login Data</caption><tr><td>Email: </td>
    <td><input type = 'text'  name = 'email'></td>  <td>Password: </td><td><input type = 'password'  name = 'userpwd'> </td>
    <td><input type = 'hidden' name = 'action' value = 'login'> <input type = 'submit' value = 'Enter'></td></tr></table></form>\n";
    print "<p><a href=\'$httpmanagecgi?action=email\'><h3>Обновить Персональные Данные</h3></a></p>";
}
#####################################################################################
########################### START MAIN BODY #########################################
#####################################################################################
sub openBlankPage {
   $myclr = $yelclr; $cnt = 0; $obpTxtLine = '';
   foreach $obpGrpId (@userGroupNumList) {
      if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
      $obpTxtLine = $obpTxtLine . "<tr $myclr><td><a href=\'$httpindexcgi?action=list\&groupid\=$obpGrpId\'>$obpGrpId</a></td> 
      <td><a href=\'$httpindexcgi?action=showpay\&groupid\=$obpGrpId\'>Открыть оплату</a></td><td align='center'>$existGroup{$obpGrpId}</td>
      <td><a href=\'$httpindexcgi?action=read\&groupid\=$obpGrpId\'>Посмотреть историю уроков</a></td>
      <td><a href=\'$httpindexcgi?action=create\&groupid\=$obpGrpId\'>Записать Урок</a></td></tr>\n";
   }
   if ( $glbUserActive{$gotusrid} == 1 ) { 
       print "<p> </p><table><tr $myclr><td>Группа №</td><td>Платежи</td><td>Кол-во<br>учеников</td>\n";
       print "<td>История уроков</td><td>Новый Урок</td></tr>$obpTxtLine</table>\n";
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
          if ( $studentGroupNum{$stdid} eq $whatis{'groupid'} ) { $cnt++; $obpPrntId = $ParentUniqueId{$stdid};
             if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
             # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents ;$totalSchools; $totalGroups
             print "<tr $myclr><td>$cnt</td><td>$studentFirstName{$stdid} $studentThirdName{$stdid} $studentSecondName{$stdid}</td></tr>\n";
          }
       } # $userSchoolId{$tusrid} = $tusrsclid; $userGroupId{$tusrid} = $tusrgrpid; 
       ($whatis{'schoolid'}, @others) = split ( /-/, $whatis{'groupid'} ); 
       print "</table><p> </p><button onclick=\"window.location.href = \'$httpindexcgi?action=door\&groupid\=$whatis{'groupid'}';\" 
       $glbStyle>Открыть Урок</button>  <p> </p> $obpLessCodeTxt <p> </p>
       <p><a href = \'$httpindexcgi?action=edit\&schoolid\=$whatis{'schoolid'}\&groupid\=$whatis{'groupid'}\'>Редактировать данные группы [$whatis{'groupid'}]</a></p>\n";
   } 
   print "<p> </p><table cellpadding='7' border='2'><tr bgcolor = 'gainsboro'><td>
   <a href=\'$httpmanagecgi?action=show\'><h3>Персональные Данные</h3></a></td>
   <td>-[]-[]-[]-</td><td><a href=\'$httpcalendarcgi\'><h3>Календарь Занятий</h3></a></td></tr></table>
   <p> </p><p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n";
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
   <tr $yelclr><td $ac><input type = 'reset' value = 'RESET' $glbStyle></td>
   <td $ac><input type = 'submit' value = 'ENTER' $glbStyle></td></tr>
   </table></form><p> </p>";
   if ( $lessonExist{$odsLessIndx} == 1 ) { print "<table><caption><h3>Список открытых уроков</h3></caption>
      <tr $yelclr><td>Номер урока: </td><td $ac>$b1 $lessonNumber{$odsLessPass} $b2</td></tr>
      <tr $yelclr1><td>Дата урока: </td><td $ac>$b1 Сегодня - $datenow $b2</td></tr>
      <tr $yelclr><td>Время урока: </td><td $ac>$b1 $lessonTime{$odsLessPass} $b2</td></tr>
      <tr $yelclr1><td>Кодовое слово: </td><td $ac>$b1 $odsLessPass $b2</td></tr></table><p> </p>"; }
   print "<p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n";
}

#####################################################################################
############################## WRITE GROUP SUB ######################################
#####################################################################################
sub writeGroupSub {
    if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
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
    print "</table><p> Correction Data is recorded! </p><p> </p>
    <p> </p><p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n";
}

#####################################################################################
################################ EDIT GROUP SUB #####################################
#####################################################################################
sub editGroupSub {  #$LeaderFirstName{$tldrid} = $tldrfirstnam; $LeaderSecondName{$tldrid} = $tldrscndnam;
    &printjavascript();  &getGroupSub();  $egsid =  $whatis{'groupid'};  #@uniqueSchoolNumList
    if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
    print "<p> </p><form method='post' action=\'$indexcgi\' name = 'editgroup' onsubmit='return checkEditFunction();'> 
    <input type = 'hidden' name = 'action' value = 'write'>\n";
    print "<table><tr $yelclr1><td>№ школы:</td> <td>$whatis{'schoolid'} 
    <input type = 'hidden' name = 'schoolid' value = \'$whatis{'schoolid'}\'></td></tr>\n"; # School number
    print "<tr $yelclr><td>№ группы:</td> <td>$whatis{'groupid'} 
    <input type = 'hidden' name = 'groupid' value = \'$whatis{'groupid'}\'></td></tr>\n";  # Group number
    print "<tr $yelclr1><td>Тренер группы:</td><td>$OEP_Traineer{$egsid}</td></tr>
    <tr $yelclr><td>1-ый волонтер:</td> <td><select name ='volunteerone'>";
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
    print "<tr $yelclr><td>Модуль платный/Бесплатный :</td><td>$OEP_Paid{$egsid}</td></tr>
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
   <input type = 'reset' value = 'Reset' $glbStyle></td> <td> -[-]-[-]-[-]- </td>
   <td $ac><input type = 'submit' value = 'Record Data' $glbStyle></td></tr></table>
   <p> </p><p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n";
}

#####################################################################################
############################# DELETE LESSON SUB #####################################
#####################################################################################
sub deleteLessonSub {
      if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
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
############################# UPDATE LESSON SUB #####################################
#####################################################################################
sub updateLessonSub { 
   if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
   &getGroupSub(); $ulsid = $whatis{'lessonid'}; $ulsGrpId = $whatis{'groupid'};
   $ulsVolOneNewLine = "OEP_VolunteerOneWas: "; $ulsVolTwoNewLine = "OEP_VolunteerTwoWas: ";
    ###################### BAS ASSIGN POINTS FOR LEADER IN SOCIAL LIFT PROJECT ###################################
   if ( $whatis{'volone'} eq 'true' ) { $ulsOpEnLiftOneCode = $OEP_VolunteerOneCode{$ulsGrpId};
      $ulsVolOneNewLine = "OEP_VolunteerOneWas: $OEP_VolunteerOneCode{$ulsGrpId}"; }
   elsif ( $whatis{'volone'} eq 'false' && $whatis{'zamone'} =~ /54LD/ ) { $ulsOpEnLiftOneCode = $whatis{'zamone'};
      $ulsVolOneNewLine = "OEP_VolunteerOneWas: $whatis{'zamone'}"; }
   else { $ulsOpEnLiftOneCode = ''; }
   if ( $whatis{'voltwo'} eq 'true' ) { $ulsOpEnLiftTwoCode = $OEP_VolunteerTwoCode{$ulsGrpId};
      $ulsVolTwoNewLine = "OEP_VolunteerTwoWas: $OEP_VolunteerTwoCode{$ulsGrpId}"; }
   elsif ( $whatis{'voltwo'} eq 'false' && $whatis{'zamtwo'} =~ /54LD/ ) { $ulsOpEnLiftTwoCode = $whatis{'zamtwo'};
      $ulsVolTwoNewLine = "OEP_VolunteerTwoWas: $whatis{'zamtwo'}"; }
   else { $ulsOpEnLiftTwoCode = ''; }
   if ( $ulsOpEnLiftOneCode ne '' ) { 
      $uls_OESLBLine = $uls_OESLBLine . "OPENENGLISH<tab>requested<tab>$gotusrid<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'lesson'}<tab>";
      $uls_OESLBLine = $uls_OESLBLine . "$ulsOpEnLiftOneCode<tab>$LeaderEmail{$ulsOpEnLiftOneCode}<tab>$oeLiftLeaderPoints<tab>$timedatenow<tab>LEADER<tab>reserve\n";
   }
   if ( $ulsOpEnLiftTwoCode ne '' ) { 
      $uls_OESLBLine = $uls_OESLBLine . "OPENENGLISH<tab>requested<tab>$gotusrid<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'lesson'}<tab>";
      $uls_OESLBLine = $uls_OESLBLine . "$ulsOpEnLiftTwoCode<tab>$LeaderEmail{$ulsOpEnLiftTwoCode}<tab>$oeLiftLeaderPoints<tab>$timedatenow<tab>LEADER<tab>reserve\n";
   }
   open(SLPDATA,">>$oe_sl_balls_file"); print SLPDATA $uls_OESLBLine; close(SLPDATA);  # Points assigned to each student for Social LIFT project
   ###################### END ASSIGN POINTS FOR LEADER IN SOCIAL LIFT PROJECT ###################################
   $ulsGrpLssnFile = $groups_folder . $ulsGrpId . '.txt'; $ulsPrjctFound = 0;
   open(ULS, $ulsGrpLssnFile);  @ulsProjectList = <ULS>;   close(ULS);
   foreach $i (@ulsProjectList){  chomp($i);
      if ( $i =~ /<start of new project = /){ $ulsprnum = $i; 
          $ulsprnum =~ s/<start of new project = //g; $ulsprnum =~ s/>//g; $ulsprnum =~ s/ //g;
         if ( $ulsprnum eq $ulsid ) { $ulsPrjctFound = 1; }
         else { $ulsPrjctFound = 0; } }
      elsif ( $i =~ /OEP_Group: / && $i =~ /$ulsGrpId/ && $ulsPrjctFound == 1 ) { 
         push(@ulsNewProjectList, $ulsVolOneNewLine); push(@ulsNewProjectList, $ulsVolTwoNewLine); }
      elsif ($i =~ /OEP_VolunteerOneWas: / && $ulsPrjctFound == 1 ) { $i = ''; }
      elsif ($i =~ /OEP_VolunteerTwoWas: / && $ulsPrjctFound == 1 ) { $i = ''; }
      push(@ulsNewProjectList, $i);
   }
   open(ULSDATA,">$ulsGrpLssnFile");
   foreach $i (@ulsNewProjectList) { if ( $i ne '' ) {
      if ( $i =~ /<start of new project = / ) { print ULSDATA "\n$i\n"; }
      else { print ULSDATA "$i\n"; } } }
   close(ULSDATA);
   &openLessonSub();
}

#####################################################################################
############################### OPEN LESSON SUB #####################################
#####################################################################################
sub openLessonSub { 
   if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
   $olsStyle = $glbStyle; &printjavascript();
   &getLessonSub(); &getGroupSub();  $olsid = $whatis{'lessonid'}; $olsGrpId = $whatis{'groupid'};
   if ( $OEP_VolunteerOneWas{$olsid} =~ /54LD/ ) { $olsVolOne = 'selected'; } else { $olsVolOne = ''; }
   if ( $OEP_VolunteerTwoWas{$olsid} =~ /54LD/ ) { $olsVolTwo = 'selected'; } else { $olsVolTwo = ''; }
   $olsVolOneId = $OEP_VolunteerOneCode{$olsGrpId}; $olsVolTwoId = $OEP_VolunteerTwoCode{$olsGrpId};
   print "<p> </p>\n<form method='post' action=\'$indexcgi\' onsubmit='return checkZamFunction()\;\'><table>
   <caption><a href=\'$httpindexcgi?action=list\'>$whatis{'schoolid'}-ая</a> Школа</caption>
   <tr $yelclr><td>Группа №</td>  <td $ac>$whatis{'groupid'}</td><td $ac></td></tr>
   <tr $yelclr1><td>Тема урока</td><td $ac>$OEP_Topic{$olsid}</td><td $ac></td></tr>
   <tr $yelclr><td>Волонтёр: $b1 $LeaderFullName{$olsVolOneId} $b2</td><td $ac><select name = 'volone'>
   <option value = 'false'>Не пришел</option><option value = 'true' $olsVolOne>Пришел</option></select></td><td $ac>
   <select name = 'zamone'><option value = ''>Выберите замену</option>\n";
   foreach $olsLdrId ( @glLeadersNumList ) { print "<option value = \'$olsLdrId\'>$LeaderFullName{$olsLdrId}</option>\n"; }
   print "</select></td></tr><tr $yelclr1><td>Волонтёр: $b1 $LeaderFullName{$olsVolTwoId} $b2</td><td $ac><select name = 'voltwo'>
   <option value = 'false'>Не пришел</option><option value = 'true' $olsVolTwo>Пришел</option></select></td><td $ac>
   <select name = 'zamtwo'><option value = ''>Выберите замену</option>\n";
   foreach $olsLdrId ( @glLeadersNumList ) { print "<option value = \'$olsLdrId\'>$LeaderFullName{$olsLdrId}</option>\n"; }
   print "</select></td></tr><tr $yelclr><td>Номер урока</td><td $ac>$OEP_Lesson{$olsid}</td><td $ac></td></tr>
   <tr $yelclr1><td>Дата урока</td><td $ac>$OEP_Date{$olsid}</td><td $ac></td></tr>
   <tr $yelclr><td $ac><input type = 'reset' value = 'ОТМЕНА' $olsStyle></td><td $ac></td>
   <td $ac><input type = 'submit' value = 'СОХРАНИТЬ' $olsStyle></td></tr></table>
   <input type='hidden' name = 'groupid' value= \'$olsGrpId\'><input type='hidden' name = 'lessonid' value= \'$olsid\'>
   <input type='hidden' name = 'schoolid' value= \'$whatis{'schoolid'}\'><input type='hidden' name = 'action' value= 'update'>
   </form><p> </p>\n<table>
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
      if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
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
          elsif($i =~ /OEP_VolunteerOneWas: /){$i =~ s/OEP_VolunteerOneWas: //g; $OEP_VolunteerOneWas{$glsprnum} = $i;}
          elsif($i =~ /OEP_VolunteerTwoWas: /){$i =~ s/OEP_VolunteerTwoWas: //g; $OEP_VolunteerTwoWas{$glsprnum} = $i;}
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
    if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
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
    if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
    &printjavascript();  $myclr = $yelclr; $cnt = 0;
    print "</p><form method='post' action=\'$indexcgi\' name = 'createnewlesson' onsubmit='return checkAllFunction();'>";
    print "<table><tr $yelclr>
    <td><a href='#' onclick='return checkFunction(1, 5);'>Укажите тему урока:</a> <input type='hidden' name='topic' value=''></td>
    <td><p id='topic'></p></td></tr>\n"; # Theme topic name
    print "<tr><td><input type='hidden' name = 'schoolid' value= \'$whatis{'schoolid'}\'></td>
    <td><input type='hidden' name='date' value=\'$datenow\'></td></tr>\n";
    print "<tr $yelclr1><td>Укажите номер урока: </td><td><select name = 'lesson'><option value = ''>Укажите № урока</option>\n"; # The lesson's number
    $clsCnt = 0; while ( $clsCnt < 33 ) { $clsCnt++; print "<option value = \'$clsCnt\'>Урок № $clsCnt</option>\n"; }
    print "</select></td></tr>\n<tr><td><input type='hidden' name = 'groupid' value= \'$whatis{'groupid'}\'></td>
    <td><input type='hidden' name = 'action' value= 'record'></td></tr>\n";
    print "<tr $yelclr><td><a href='#' onclick='return checkFunction(1, 7);'>Изменить дату урока</a> [DD.MM.YYYY]: </td>
    <td><p id='date'>$daynow\.$ai{$monthnow}\.$yearnow</p></td></tr></table>\n"; # The lesson's date
    print "<p> </p><table>
    <caption><a href=\'$indexcgi?action=list\'>$whatis{'schoolid'}-ая</a> Школа [группа № $whatis{'groupid'}]</caption>\n";
    print "<tr $myclr><td>N</td><td>ФИО Ученика</td><td>Телефон ученика</td><td>Participation</td><td>Late</td><td>LIFT [-]</td>";
    print "<td>Test %</td><td>LIFT [+]</td><td>Total</td><td>Evaluation</td><td>Comments</td><td>Homework Quality</td></tr>\n";
    foreach $stdid (@studentUniqueNumList) {
       if ( $studentGroupNum{$stdid} eq $whatis{'groupid'} ) {
          if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; }
          $cnt++; $clsPrntId = $ParentUniqueId{$stdid};
          print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' name = 'userid' value= \'$stdid\'></td>";
          print "<td id='name'><a href='#' onclick='return checkFunction($cnt, 1);'>$studentFirstName{$stdid} "; #Students name
          print "$studentThirdName{$stdid} $studentSecondName{$stdid}</a></td><td>$studentPhoneNum{$stdid}</td>
          <td id='part'><p id='part_$stdid\'>Пришел на урок?</p>
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
    <table><tr><td $ac><input type = 'reset' value = 'Reset' $glbStyle></td>
    <td> -[-]-[-]-[-]- </td><td $ac><input type = 'submit' value = 'Record Data' $glbStyle></td></tr></table>
    <p> </p><p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n";
}
#####################################################################################
########################## RECORD LESSON SUB ######################################
#####################################################################################
sub recordLessonSub {
   if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
   print "<table><tr $yelclr><td>Parameters</td><td>Values</td></tr><tr $yelclr1><td>School</td>
   <td><a href=\'$indexcgi?action=list\'>$whatis{'schoolid'}</a></td></tr>
   <tr $yelclr><td>Group</td><td>$whatis{'groupid'}</td></tr><tr $yelclr1><td>Lesson Number</td><td>$whatis{'lesson'}</td></tr>
   <tr $yelclr><td>Date</td><td>$whatis{'date'}</td></tr><tr $yelclr1><td>Topic</td><td>$whatis{'topic'}</td></tr></table>\n
   <table><tr $yelclr><td>N</td><td>Students name</td><td>Participation</td><td>Late</td><td>LIFT [-]</td>
   <td>Test %</td><td>LIFT [+]</td><td>Total</td><td>Evaluation</td></tr>\n"; $cnt = 1; $myclr = $yelclr;
   foreach $stdid (@studentUniqueNumList){ $myclr = $yelclr;
      if($studentGroupNum{$stdid} eq $whatis{'groupid'}){
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
         $newline = $newline . "OEP_HomeWork\_$stdid: $whatis{$rlshome}\n";  
         $oe_sl_balls_line = $oe_sl_balls_line . "OPENENGLISH<tab>requested<tab>$gotusrid<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'lesson'}";
         $oe_sl_balls_line = $oe_sl_balls_line . "<tab>$stdid<tab>$userEmail{$stdid}<tab>$oeLiftStudPoints<tab>$timedatenow<tab>STUDENT<tab>reserve\n";
      } #$oeLiftStudPoints = 1200; $oeLiftLeaderPoints = 3200;
      else{
         $cnt1 = $cnt / 2; $cnt2 = int( $cnt / 2 ); if($cnt1 == $cnt2){$myclr = $yelclr;} else{$myclr = $yelclr1;}
         print "<tr $myclr><td>$cnt</td><td>$studentFirstName{$stdid} $studentThirdName{$stdid} $studentSecondName{$stdid}</td> 
         <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td></tr>\n";}
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
########################### OPEN GROUP PAGE SUB #####################################
#####################################################################################
sub openGroupPageSub { # $calendarnumber{$tclndrdate} = $tclndrnum;  $calendardate{$tclndrnum} = $tclndrdate; $glPayStatus{$glPayId}
    if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
    &printjavascript(); &getGroupSub(); &getGroupCommentsSub();
    $myclr = $yelclr1; $cnt = 1; $ogpHtmlCodeOne = ''; $ogpHtmlCodeTwo = ''; $ogpGrpId = $whatis{'groupid'};
    $ogpDayOnePayable = 0; $ogpDayTwoPayable = 0; $ogpDayTriPayable = 0; $ogpDayForPayable = 0;
    @ogpGroupDaysList = split (/, /, $OEP_Calendar{$ogpGrpId}); $ogpTodayNum = $calendarnumber{$datenow};
    $ogpGroupPayDayOne = $ogpGroupDaysList[7]; $ogpGroupPayDayTwo = $ogpGroupDaysList[14];
    if ( $ogpTodayNum < $ogpGroupPayDayOne ) { $ogpMultiply = 0; }
    elsif ( $ogpTodayNum < $ogpGroupPayDayTwo ) { $ogpMultiply = 1; }
    elsif ( $ogpTodayNum > $ogpGroupPayDayTwo ) { $ogpMultiply = 2; }
    if ( $ogpGrpId =~ /M2/ || $ogpGrpId =~ /M3/ ) { 
        $ogpGroupPayDayTri = $ogpGroupDaysList[21]; $ogpGroupPayDayFour = $ogpGroupDaysList[28]; 
        if ( $ogpTodayNum > $ogpGroupPayDayTri ) { $ogpMultiply = 3; }
        elsif ( $ogpTodayNum > $ogpGroupPayDayFour ) { $ogpMultiply = 4; }
        $ogpHtmlCodeOne = "<td>Оплата<br>№3</td><td>Оплата<br>№4</td>"; 
        $ogpHtmlCodeTwo = "<td>$b1 $calendardate{$ogpGroupPayDayTri} $b2</td><td>$b1 $calendardate{$ogpGroupPayDayFour} $b2</td>";
    }
    foreach $ogpStdId (@studentUniqueNumList) {
       if ( $studentGroupNum{$ogpStdId} eq $whatis{'groupid'} ) {   $ogpStdIndex = $ogpStdId . '<tab>' . $ogpGrpId; 
          if ( $glPayStatusOne{$ogpStdIndex} eq 'Free' ) { $ogpNewLineOne = "<td>Free</td>"; $ogpDayOnePayable = 0; } 
          else { $ogpStdtTotalSum{$ogpStdIndex} = $ogpStdtTotalSum{$ogpStdIndex} + $glMonthPayValue; $ogpDayOnePayable = 1;    
              if ( $glPayOneDate{$ogpStdIndex} =~ /\.20/ ) { 
                  $ogpNewLineOne = "<td>$glPayOneDate{$ogpStdIndex}</td>";  
                  $ogpStdPaidValue{$ogpStdIndex} = $ogpStdPaidValue{$ogpStdIndex} + $glMonthPayValue;  
                  $glGroupPaidValue{$ogpGrpId} = $glGroupPaidValue{$ogpGrpId} + $glMonthPayValue; 
              }  else { $ogpNewLineOne = "<td></td>"; }
          }
          if ( $glPayStatusTwo{$ogpStdIndex} eq 'Free' ) { $ogpNewLineTwo = "<td>Free</td>"; $ogpDayTwoPayable = 0; }
          else { $ogpStdtTotalSum{$ogpStdIndex} = $ogpStdtTotalSum{$ogpStdIndex} + $glMonthPayValue; $ogpDayTwoPayable = 1;    
              if ( $glPayTwoDate{$ogpStdIndex} =~ /\.20/ ) { 
                  $ogpNewLineTwo = "<td>$glPayTwoDate{$ogpStdIndex}</td>";   
                  $ogpStdPaidValue{$ogpStdIndex} = $ogpStdPaidValue{$ogpStdIndex} + $glMonthPayValue; 
                  $glGroupPaidValue{$ogpGrpId} = $glGroupPaidValue{$ogpGrpId} + $glMonthPayValue; 
              }  else { $ogpNewLineTwo = "<td></td>"; }
          } 
          if ( ( $ogpGrpId =~ /M2/ || $ogpGrpId =~ /M3/ ) ) { 
              if ( $glPayStatusTri{$ogpStdIndex} eq 'Free' ) { $ogpNewLineTri = "<td>Free</td>"; $ogpDayTriPayable = 0; }
              else { $ogpStdtTotalSum{$ogpStdIndex} = $ogpStdtTotalSum{$ogpStdIndex} + $glMonthPayValue; $ogpDayTriPayable = 1;  
                  if ( $glPayThreeDate{$ogpStdIndex} =~ /\.20/ ) { 
                      $ogpNewLineTri = "<td>$glPayThreeDate{$ogpStdIndex}</td>"; 
                      $ogpStdPaidValue{$ogpStdIndex} = $ogpStdPaidValue{$ogpStdIndex} + $glMonthPayValue;  
                      $glGroupPaidValue{$ogpGrpId} = $glGroupPaidValue{$ogpGrpId} + $glMonthPayValue; 
                  }  else { $ogpNewLineTri = "<td></td>"; }
              }
              if ( $glPayStatusFor{$ogpStdIndex} eq 'Free' ) { $ogpNewLineFor = "<td>Free</td>"; $ogpDayForPayable = 0; }
              else { $ogpStdtTotalSum{$ogpStdIndex} = $ogpStdtTotalSum{$ogpStdIndex} + $glMonthPayValue; $ogpDayForPayable = 1;
                  if ( $glPayFourDate{$ogpStdIndex} =~ /\.20/ ) { 
                      $ogpNewLineFor = "<td>$glPayFourDate{$ogpStdIndex}</td>";  
                      $ogpStdPaidValue{$ogpStdIndex} = $ogpStdPaidValue{$ogpStdIndex} + $glMonthPayValue;  
                      $glGroupPaidValue{$ogpGrpId} = $glGroupPaidValue{$ogpGrpId} + $glMonthPayValue; 
                  }  else { $ogpNewLineFor = "<td></td>"; }
              }
              # $glPayOneDate{$glPayId}; $glPayTwoDate{$glPayId}; $glPayThreeDate{$glPayId}; $glPayFourDate{$glPayId}; 
              #$glPayStatusOne{$glPayId} $glPayStatusTwo{$glPayId}; $glPayStatusTri{$glPayId}; $glPayStatusFor{$glPayId};
              $ogpHtmlCodeTri = "$ogpNewLineTri $ogpNewLineFor";
          }
          if ( $ogpMultiply == 0 ) { $ogpTodayStdExpected{$ogpStdIndex} = 0; }
          elsif ( $ogpMultiply == 1 ) { $ogpTodayStdExpected{$ogpStdIndex} = $glMonthPayValue * $ogpDayOnePayable; }
          elsif ( $ogpMultiply == 2 ) { $ogpTodayStdExpected{$ogpStdIndex} = $glMonthPayValue * $ogpDayOnePayable + $glMonthPayValue * $ogpDayTwoPayable; }
          elsif ( $ogpMultiply == 3 ) { $ogpTodayStdExpected{$ogpStdIndex} = $glMonthPayValue * $ogpDayOnePayable + $glMonthPayValue * $ogpDayTwoPayable + $glMonthPayValue * $ogpDayTriPayable; }
          elsif ( $ogpMultiply == 4 ) { $ogpTodayStdExpected{$ogpStdIndex} = $glMonthPayValue * $ogpDayOnePayable + $glMonthPayValue * $ogpDayTwoPayable + $glMonthPayValue * $ogpDayTriPayable + $glMonthPayValue * $ogpDayForPayable; }
          if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
          # $ParentUniqueId{$tparntstudid} = $tparntid;   $ParentFullName{$tparntid} = "$tparntfirstnam $tparntthrdnam $tparntscndnam";
          $ogpPrntId = $ParentUniqueId{$ogpStdId};
          $ogpPerStdtTxt = "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$ogpStdId\'></td>
          <td>$studentFullName{$ogpStdId}</td><td>$ParentFullName{$ogpPrntId}</br>
          $ParentPhoneNum{$ogpPrntId}</td>$ogpNewLineOne $ogpNewLineTwo $ogpHtmlCodeTri";
          $ogpTodayExpected{$ogpGrpId} = $ogpTodayExpected{$ogpGrpId} + $ogpTodayStdExpected{$ogpStdIndex};
          $ogpStdUnpaidValue{$ogpStdIndex} = $ogpTodayStdExpected{$ogpStdIndex} - $ogpStdPaidValue{$ogpStdIndex};
          if ( $ogpStdUnpaidValue{$ogpStdIndex} < 0 ) { $ogpStdUnpaidValue{$ogpStdIndex} = 0; }
          $ogpPerStdtTxt = $ogpPerStdtTxt . "<td>$ogpTodayStdExpected{$ogpStdIndex}</td><td>$ogpStdPaidValue{$ogpStdIndex}</td>";
          $ogpPerStdtTxt = $ogpPerStdtTxt . "<td>$ogpStdUnpaidValue{$ogpStdIndex}</td><td>$ogpStdtTotalSum{$ogpStdIndex}</td>
          <td><input type = 'text' name = \'remark\_$ogpStdId\' value = \'$glbPayComment{$ogpStdId}\'></td></tr>\n";
          $ogpGroupTotalSum{$ogpGrpId} = $ogpGroupTotalSum{$ogpGrpId} + $ogpStdtTotalSum{$ogpStdIndex};
          $ogpUnpaidValue{$ogpGrpId} = $ogpUnpaidValue{$ogpGrpId} + $ogpStdUnpaidValue{$ogpStdIndex};
          $cnt++; push(@ogpHtmlCodeList, $ogpPerStdtTxt);
       }
    }
    print "<h2>Таблица по оплатам учеников</h2>\n <p>Список учеников группы № [$whatis{'groupid'}]</p>
    <form method='post' action=\'$httpindexcgi\'><input type = 'hidden' name = 'action' value = 'saveremark'>
    <input type = 'hidden' name = 'groupid' value = \'$ogpGrpId\'><input type = 'hidden' name = 'schoolid' value = \'$whatis{'schoolid'}\'>
    <table><tr $yelclr><td>No</td><td>ФИО ученика</td><td>ФИО родителей</td><td>Оплата<br>№1</td><td>Оплата<br>№2</td>$ogpHtmlCodeOne
    <td>На сегодня<br>ожидаем</td><td>На сегодня<br>получено</td><td>На сегодня<br>не оплачено</td><td>Всего<br>за курс<br>ожидаем</td><td>Комментарии</td></tr>
    <tr $yelclr1><td>#</td><td $ac>$b1 День оплаты $b2</td><td $ac>$b1 по плану: $b2</td><td>$b1 $calendardate{$ogpGroupPayDayOne} $b2</td>
    <td>$b1 $calendardate{$ogpGroupPayDayTwo} $b2</td>$ogpHtmlCodeTwo<td>$b1 $ogpTodayExpected{$ogpGrpId} $b2</td>
    <td>$b1 $glGroupPaidValue{$ogpGrpId} $b2</td><td>$b1 $ogpUnpaidValue{$ogpGrpId} $b2</td><td>$b1 $ogpGroupTotalSum{$ogpGrpId} $b2</td><td></td></tr>\n";
    foreach $ogpHtmlCode (@ogpHtmlCodeList) { print "$ogpHtmlCode"; }
    print "</table>\n <input type = 'submit' value = 'СОХРАНИТЬ' $glbStyle> </form>
     <p> </p> <a href=\'$httpindexcgi\'>[ Вернуться НАЗАД ]</a>\n"; 
}

#####################################################################################
################################# GET GROUP SUB #####################################
#####################################################################################
sub getGroupSub {
    if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
    $ggsgrpfile = $groups_folder . $whatis{'groupid'} . '_data.txt'; $ggsid = $whatis{'groupid'};
    open(UPL, $ggsgrpfile);
    @ggsprojectlist = <UPL>;
    close(UPL);
    foreach $i (@ggsprojectlist){  chomp($i);  
          if($i =~ /OEP_School: /){$i =~ s/OEP_School: //g; $OEP_School{$ggsid} = $i;}
       elsif($i =~ /OEP_Group: /){$i =~ s/OEP_Group: //g; $OEP_Group{$ggsid} = $i;}
       elsif($i =~ /OEP_Traineer: /){$i =~ s/OEP_Traineer: //g; $OEP_Traineer{$ggsid} = $i;}
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
############################## GET GROUP COMMENTS SUB ###############################
#####################################################################################
sub getGroupCommentsSub {
    if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
    $ggcgrpfile = $groups_folder . $whatis{'groupid'} . '_comments.txt'; $ggcid = $whatis{'groupid'};
    open(UPL, $ggcgrpfile);    @ggcprojectlist = <UPL>;    close(UPL);
    foreach $i (@ggcprojectlist){  chomp($i);  #<>
       ($tggctrid, $tggcstudid, $tggccomm, $tggcdate, @other) = split (/<tab>/, $i);
       if ( $gotusrid eq $tggctrid && $gotusrid =~ /44TR/ ) { $glbPayComment{$tggcstudid} = $tggccomm; }
    }
}

#####################################################################################
############################## SAVE GROUP COMMENTS SUB ###############################
#####################################################################################
sub saveGroupCommentsSub {
    if ( $whatis{'groupid'} eq '' ) { print "<h3>$rf Номер группы не корректный! $f2</h3>\n"; return(); }
    $sgcgrpfile = $groups_folder . $whatis{'groupid'} . '_comments.txt'; $sgcid = $whatis{'groupid'};
    foreach $sgcStdId (@studentUniqueNumList){ if ( $studentGroupNum{$sgcStdId} eq $whatis{'groupid'} ) {
       $sgcIndx = 'remark_' . $sgcStdId; $whatis{$sgcIndx} =~ s/<//g; $whatis{$sgcIndx} =~ s/>//g; $whatis{$sgcIndx} =~ s/\n/ /g;
       $sgcLine = "$gotusrid<tab>$sgcStdId<tab>$whatis{$sgcIndx}<tab>$timedatenow<tab>rest\n";
       push(@sgcNewRemarksList, $sgcLine);
    }}
    open(SGCD,">>$sgcgrpfile"); print SGCD @sgcNewRemarksList; close(SGCD); 
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
 function checkEditFunction (){ var x = 0;
        if(document.getElementsByName('volunteerone')[0].value == ''){alert('Укажите 1-го волонтера!'); return false;}
        if(document.getElementsByName('volunteertwo')[0].value == ''){alert('Укажите 2-го волонтера!'); return false;}
        if(isValidDate(document.getElementsByName('datestart')[0].value)){} else {
        alert('Неверный формат даты: [' + document.getElementsByName('datestart')[0].value + ']!'); return false;}
        if(isValidDate(document.getElementsByName('dateend')[0].value)){} else {
        alert('Неверный формат даты: [' + document.getElementsByName('dateend')[0].value + ']!'); return false;}
        if(document.getElementsByName('status')[0].value == ''){alert('Выберите статус группы!'); return false;}
        
 }
 function checkZamFunction (){
    if ( document.getElementsByName('volone')[0].value == 'true' && document.getElementsByName('zamone')[0].value != '' ) { alert('Уберите замену!'); return false;}
    if ( document.getElementsByName('voltwo')[0].value == 'true' && document.getElementsByName('zamtwo')[0].value != '' ) { alert('Уберите замену!'); return false;}
 }
 function checkAllFunction (){
        if(document.getElementsByName('lesson')[0].value == ''){alert('Укажите номер урока!'); return false;}
        if(document.getElementsByName('topic')[0].value == ''){alert('Укажите тему урока!'); return false;}
 }
 function showFunction(){ var x = document.getElementById('comments');
  if (x.style.display === 'none') {x.style.display = 'block'; } else { x.style.display = 'none'; }
 }
 function checkSaveFunction (){
     var dayone = document.getElementsByName('dayonepay')[0].value;
     if(dayone != ''){
       if(isValidDate(dayone)){} else {
       alert('Неверный формат даты: [' + document.getElementsByName('dayonepay')[0].value + ']!'); return false;}
     }
     var daytwo = document.getElementsByName('daytwopay')[0].value;
     if(daytwo != ''){
       if(isValidDate(daytwo)){} else {
       alert('Неверный формат даты: [' + document.getElementsByName('daytwopay')[0].value + ']!'); return false;}
     }
     var daytri = document.getElementsByName('daytripay')[0].value;
     if(daytri != ''){
       if(isValidDate(daytri)){} else {
       alert('Неверный формат даты: [' + document.getElementsByName('daytripay')[0].value + ']!'); return false;}
     }
     var dayfor = document.getElementsByName('dayforpay')[0].value;
     if(dayfor != ''){
       if(isValidDate(dayfor)){} else {
       alert('Неверный формат даты: [' + document.getElementsByName('dayforpay')[0].value + ']!'); return false;}
     }
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