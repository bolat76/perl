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
$activeGroups_file = '../oedata/oe_active_groups.txt';
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$indexcgi = 'read.cgi';
$students_file = $oe_folder . 'students.txt';
$calendar_file = $oe_folder . 'calendar.txt';
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
$cnt = 0;

open(INF, $calendar_file); @calendar_list = <INF>; close(INF); foreach $i(@calendar_list){ chomp($i); 
    ($tclndrnum, $tclndrdate, $tcndrweek, @other) = split (/<tab>/, $i);  #12<tab>12.01.19<tab>Saturday
    $calendarweek{$tclndrnum} = $tcndrweek; $calendardate{$tclndrnum} = $tclndrdate;
    $calendarweek{$tclndrdate} = $tcndrweek;  $calendarnumber{$tclndrdate} = $tclndrnum;
    ($clndrDay, $clndrMonth, $clndrYear) = split(/\./, $tclndrdate);  
} 

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
########################## LOGIN CHECK PART #######################################
#####################################################################################
print "<p>";
if($userlogged == 1){
    print "Hello $b1 $userfirstname{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>";
    
    &startmainbody();
    
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
######################### START MAIN BODY #########################################
#####################################################################################
sub startmainbody {
if($whatis{'list'} eq 'schools'){                     ############### LIST of SCHOOLS ####################
    print "</p>"; $myclr = $yelclr; $cnt = 0;
    print "<table><caption>Список всех школ</caption>\n";
    print "<tr $myclr><td align = 'center'>N</td><td align = 'center'>№ Школы</td><td align = 'center'>кол-во группы</td><td align = 'center'>Кол-во учеников</td></tr>\n";
    foreach $sclid (@uniqueSchoolNumList){
          if($existSchool{$sclid} ne ''){
                if($myclr eq $yelclr){$myclr = $yelclr1;} else{$myclr = $yelclr;}
                $cnt++; # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents ;$totalSchools; $totalGroups
                print "<tr $myclr><td align = 'center'>$cnt</td><td align = 'center'><a href=\'$httpindexcgi?list=groups\&schoolid=$sclid\'>$sclid</a></td> 
                <td align = 'center'>$GroupsPerSchool{$sclid}</td> <td align = 'center'>$existSchool{$sclid}</td> </tr>\n";
          }
    }
    if($myclr eq $yelclr){$myclr = $yelclr1;} else{$myclr = $yelclr;}
    print "<tr $myclr><td>Всего: </td><td align = 'center'>$totalSchools</td><td align = 'center'>$totalGroups</td><td align = 'center'>$totalStudents</td></tr></table>\n"; 
    #print "<p><a href=\'$httpindexcgi?list=all\'>Общий список в основной таблице</a></p>\n";
}####################################################################################
elsif($whatis{'list'} eq 'groups' && $whatis{'schoolid'} ne ''){########## LIST of GROUPS #############
    print "</p>"; $myclr = $yelclr; $cnt = 0;
    print "<p> </p><table><caption>Школа № $whatis{'schoolid'}</caption>\n";
    print "<tr $myclr><td>№</td><td>Группа №</td><td>Кол-во учеников</td><td>История уроков</td><td>Новый Урок</td></tr>\n";
    foreach $grpid (@uniqueGroupNumList){
        if($groupSchoolNum{$grpid} eq $whatis{'schoolid'}){
              if($myclr eq $yelclr){$myclr = $yelclr1;}
              else{$myclr = $yelclr;}
              $cnt++; # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents ;$totalSchools; $totalGroups
              print "<tr $myclr><td>$cnt</td><td><a href=\'$httpindexcgi?list=group\&groupid=$grpid\&schoolid=$whatis{'schoolid'}\'>$grpid</a></td>
              <td align='center'>$existGroup{$grpid}</td>
              <td><a href=\'$httpgroupcgi?action=read\&groupid=$grpid\&schoolid=$whatis{'schoolid'}\'>Посмотреть историю уроков</a></td>
              <td><a href=\'$httpgroupcgi?action=create\&groupid=$grpid\&schoolid=$whatis{'schoolid'}\'>Записать Урок</a></td></tr>\n";
        }
    }
    print "</table>\n"; 
    print "<p><a href=\'$httpindexcgi?list=schools\'>Список всех школ</a> -[]-[]-[]-
    <a href=\'$httpindexcgi?list=active\'>[Список активных школ]</a> -[]-[]-[]-
    <a href=\'$httpindexcgi?list=delays\'>[График заполнения уроков]</a></p>\n";
 #   print "<p><a href=\'$httpindexcgi?list=all\'>Общий список в основной таблице</a></p>\n";
    
}###################################################################################
elsif ( $whatis{'list'} eq 'soclift' ) { ######## LIST of Balls assigned to STUDENTS and LEADERS ###########
   $myclr = $yelclr; $slCnt = 1;
   print "</p><table><caption><h3>Список баллов начисленных за участие в проекте OPEN ENGLISH</h3></caption>
   <tr $myclr><td>N</td><td>Проект</td><td>Статус</td><td>ID Инициатора</td><td>Школа</td><td>Группа</td><td>№ Урока</td>
   <td>ID ученика</td><td>ФИО ученика</td><td>EMail ученика</td><td>Баллы</td><td>Дата</td><td>Категория</td></tr>\n";
   foreach $i (@OpEnSocLiftBallsList) { if ( $i =~ /<tab>/ ) { chomp($i);  # $studentFullName{$tstudid}
      ($slPrjct, $slReqst, $slUsrId, $slSchlId, $slGrpId, $slLssnId, $slStudId, $slUsrEmail, $slBalls, $slDate, $slCtgr, @other) = split (/<tab>/, $i);
      if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
      print "<tr $myclr><td>$slCnt</td><td $ac>$slPrjct</td><td $ac>$slReqst</td><td $ac>$slUsrId</td><td $ac>$slSchlId</td>
      <td $ac>$slGrpId</td><td $ac>$slLssnId</td><td $ac>$slStudId</td><td $ac>$studentFullName{$slStudId}</td>
      <td $ac>$slUsrEmail</td><td $ac>$slBalls</td><td $ac>$slDate</td><td $ac>$slCtgr</td></tr>\n";
      $slCnt++;
   } }
   print "</table>\n";
   if ( $slCnt == 1 ) { print "<h3>$rf Еще никому баллы не начислили. Ждем-с.. $f2</h3>\n"; }
}###################################################################################
elsif($whatis{'list'} eq 'group' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){######## LIST of STUDENTS ###########
    print "</p>"; $myclr = $yelclr; $cnt = 0;
    print "<table><caption><a href=\'$httpindexcgi?list=groups\&schoolid=$whatis{'schoolid'}\'>$whatis{'schoolid'}</a> School</caption>\n";
    print "<tr $myclr><td>N</td><td>$whatis{'groupid'} Group</td></tr>\n";
    foreach $stdid (@studentUniqueNumList){
        if($studentGroupNum{$stdid} =~ $whatis{'groupid'}){
              if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
              $cnt++; # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents ;$totalSchools; $totalGroups
              print "<tr $myclr><td>$cnt</td><td>";
              print "$studentFirstName{$stdid} $studentThirdName{$stdid} $studentSecondName{$stdid}";
              print "</td></tr>\n";
        }
    }
    print "</table>\n"; 
    print "<p><a href=\'$httpindexcgi?list=schools\'>Список всех школ</a> -[]-[]-[]-
    <a href=\'$httpindexcgi?list=active\'>[Список активных школ]</a> -[]-[]-[]-
    <a href=\'$httpindexcgi?list=delays\'>[График заполнения уроков]</a></p>\n";
 #   print "<p><a href=\'$httpindexcgi?list=all\'>Общий список в основной таблице</a></p>\n";
}##################################################################################
elsif($whatis{'list'} eq 'all'){
      print "</p>"; $myclr = $yelclr; $cnt = 0;
      print "<table><caption>Список всех школ</caption>\n";
      print "<tr $myclr><td>№</td><td>Школа №</td><td>Кол-во учеников</td><td>Группа-1</td><td>Группа-2</td>
      <td>Группа-3</td><td>Группа-4</td><td>Группа-5</td><td>Группа-6</td></tr>\n";
      foreach $sclid (@uniqueSchoolNumList){
           if($existSchool{$sclid} ne ''){
                if($myclr eq $yelclr){$myclr = $yelclr1;} else{$myclr = $yelclr;}
                $cnt++; # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents; $totalSchools; $totalGroups
                print "<tr $myclr><td>$cnt</td><td  align='center'><a href=\'$httpindexcgi?list=groups\&schoolid=$sclid\'>$sclid</a></td>
                <td  align='center'>$existSchool{$sclid}</td>";
                foreach $grpid (@uniqueGroupNumList){
                    #chomp($grpid); 
                    if($groupSchoolNum{$grpid} eq $sclid){
                        print "<td><a href=\'$httpindexcgi?list=group\&groupid=$grpid\&schoolid=$sclid\'>$grpid</a> [$existGroup{$grpid}]</td>";
                    }
                }
                print "</tr>\n";
           }
      }
      if($myclr eq $yelclr){$myclr = $yelclr1;} else{$myclr = $yelclr;}
      print "<tr $myclr><td>Sum:</td><td  align='center'>$totalSchools</td><td  align='center'>$totalStudents</td></tr></table>\n"; 
      print "<p><a href=\'$httpindexcgi?list=schools\'>Список всех школ</a> -[]-[]-[]-
      <a href=\'$httpindexcgi?list=active\'>[Список активных школ]</a> -[]-[]-[]-
      <a href=\'$httpindexcgi?list=delays\'>[График заполнения уроков]</a></p>\n";
}##################################################################################
elsif ( $whatis{'list'} eq 'active' ) {
   print "</p>"; $myclr = $yelclr; $cnt = 0; $smbTotalActive = 0;
   print "<table><caption>Список всех школ</caption>\n";
   print "<tr $myclr><td>№</td><td>Школа №</td><td>Кол-во учеников</td>
   <td>Группа-1</td><td>Группа-2</td><td>Группа-3</td><td>Группа-4</td><td>Группа-5</td><td>Группа-6</td></tr>\n";
   foreach $sclid (@uniqueSchoolNumList){ # $totalStudents; $totalSchools; $totalGroups
      if ( $existSchool{$sclid} ne '' ) { # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; 
          if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
          $smbStudPerSchl{$sclid} = 0; $cnt++; $smbTxtLine = '';
          print "<tr $myclr><td>$cnt</td><td  align='center'><a href=\'$httpindexcgi?list=groups\&schoolid=$sclid\'>$sclid</a></td>";
          foreach $grpid (@uniqueGroupNumList) { # $existGroup{$tstudgrp}
             $whatis{'groupid'} = $grpid; &getGroupSub(); 
             #print "<!-- grpid:[$grpid] smbActiveSchlId:[$smbActiveSchlId] existGroup{$grpid}:[$existGroup{$grpid}] -->\n";
             if ( $groupSchoolNum{$grpid} eq $sclid && $OEP_Status{$grpid} eq 'Active' ) {
                $smbStudPerSchl{$sclid} = $smbStudPerSchl{$sclid} + $existGroup{$grpid};
                $smbTxtLine = $smbTxtLine . "<td><a href=\'$httpindexcgi?list=group\&groupid=$grpid\&schoolid=$sclid\'>";
                $smbTxtLine = $smbTxtLine . "$grpid</a> [$existGroup{$grpid}] <br>$rf $OEP_FinishDate{$grpid} $f2</td>";
                $smbActiveGroupLine = "$grpid\n"; push(@smbActiveGroupList, $smbActiveGroupLine);
             }
          }
          $smbTotalActive = $smbTotalActive + $smbStudPerSchl{$sclid};
          print "<td  align='center'> $smbStudPerSchl{$sclid} </td> $smbTxtLine </tr>\n";
      }
   }
   if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
   print "<tr $myclr><td>Sum:</td><td  align='center'>$totalSchools</td><td  align='center'>$smbTotalActive</td></tr></table>\n"; 
   print "<p><a href=\'$httpindexcgi?list=schools\'>Список всех школ</a> -[]-[]-[]-
    <a href=\'$httpindexcgi?list=active\'>[Список активных школ]</a> -[]-[]-[]-
    <a href=\'$httpindexcgi?list=delays\'>[График заполнения уроков]</a></p>\n";
   open(AGRP,">$activeGroups_file");   print AGRP @smbActiveGroupList;   close(AGRP);
}##################################################################################
elsif ( $whatis{'list'} eq 'delays' ) {
   if ( $whatis{'groupid'} eq '' ) { open(ACTGRP, $activeGroups_file); @dlyActiveGroupList = <ACTGRP>; close(ACTGRP); 
      foreach $i (@dlyActiveGroupList){ chomp($i); $whatis{'groupid'} = $i; &printGroupDelaysSub(); } }
   else { &printGroupDelaysSub(); }
   print "<p><a href=\'$httpindexcgi?list=schools\'>Список всех школ</a> -[]-[]-[]-
    <a href=\'$httpindexcgi?list=active\'>[Список активных школ]</a> -[]-[]-[]-
    <a href=\'$httpindexcgi?list=delays\'>[График заполнения уроков]</a></p>\n";
}##################################################################################
else{ 
    print "<p><a href=\'$httpindexcgi?list=schools\'>Список всех школ</a> -[]-[]-[]-
    <a href=\'$httpindexcgi?list=active\'>[Список активных школ]</a> -[]-[]-[]-
    <a href=\'$httpindexcgi?list=delays\'>[График заполнения уроков]</a></p>\n";
   #   print "<p><a href=\'$httpindexcgi?list=all\'>Общий список в основной таблице</a></p>\n";
}
}

#####################################################################################
############################# PRINT GROUP DELAYS SUB ################################
#####################################################################################
sub printGroupDelaysSub { &getGroupSub(); $pgdGrpId = $whatis{'groupid'}; $cnt = 0; $pgdFaultAllNum = 0;
   &getLessonSub(); foreach $pgdIndx (@glsLessonNumList) { ($pgdWrtnLessNum, $pgdIndx2) = split(/<tab>/, $pgdIndx);
      ($pgdWrtnUserId, $pgdWrtnPrjctNum) = split(/-/, $pgdIndx2); $pgdPrjctNum{$pgdWrtnLessNum} = $pgdWrtnPrjctNum; }
   (@pgdCalendarList) = split(/\, /, $OEP_Calendar{$pgdGrpId});  (@pgdTimeList) = split(/<tab>/, $OEP_TimeList{$pgdGrpId});
   print "<p> </p><table><caption><h2>Данные по группе № $pgdGrpId</h2></caption>\n";
   $pgdLessNumbLine = "<tr $yelclr><td>Номер урока</td>";
   $pgdPlanTimeLine = "<tr $yelclr1><td>Время урока <br>по графику</td>";
   $pgdPlanLessLine = "<tr $yelclr><td>Дата урока <br>по графику</td>";
   $pgdFactLessLine = "<tr $yelclr1><td>Дата урока <br>по факту</td>";
   $pgdFactRcrdLine = "<tr $yelclr><td>Дата заполнения <br>урока по факту</td>";
   $pgdFaultNumLine = "<tr $yelclr1><td>Кол-во<br>просроченных дней</td>";
   foreach $pgdId (@pgdCalendarList) { $pgdLessNum = $cnt + 1; $pgdLessDate = $calendardate{$pgdId};
      $pgdLessArg = $pgdGrpId . '<tab>' . $pgdLessNum; 
      $pgdLessNumbLine = $pgdLessNumbLine . "<td $ac>$pgdLessNum</td>";
      $pgdPlanTimeLine = $pgdPlanTimeLine . "<td>$pgdTimeList[$cnt]</td>";
      $pgdPlanLessLine = $pgdPlanLessLine . "<td>$pgdLessDate</td>";
      $pgdFactLessLine = $pgdFactLessLine . "<td name = \"$pgdGrpId\" id = \"$pgdLessNum\">$glsGroupLessonDate{$pgdLessArg}</td>";
      #print "<!-- pgdLessNum:[$pgdLessNum] pgdPrjctNum{$pgdLessNum}:[$pgdPrjctNum{$pgdLessNum}] pgdGrpId:[$pgdGrpId] -->\n";
      if ( length($pgdPrjctNum{$pgdLessNum}) > 8 && $glsGroupLessonDate{$pgdLessArg} ne '' ) { 
         $pgdLsnFactTxt = substr($pgdPrjctNum{$pgdLessNum}, 0, 8); $pgdLsnFactDayNum = substr($pgdLsnFactTxt, 4, 2); 
         $pgdLsnFactMnthNum = substr($pgdLsnFactTxt, 6, 2); $pgdLsnFactYearNum = substr($pgdLsnFactTxt, 0, 4);
         $pgdLsnFactDate = "$pgdLsnFactDayNum.$pgdLsnFactMnthNum.$pgdLsnFactYearNum"; $pgdLsnFactNum = $calendarnumber{$pgdLsnFactDate};
      }
      else { $pgdLsnFactNum = $calendarnumber{$datenow}; $pgdLsnFactDate = ""; }
      $pgdFactRcrdLine = $pgdFactRcrdLine . "<td>$pgdLsnFactDate</td>";
      if ( $glsGroupLessonDate{$pgdLessArg} ne '' ) { $pgdFaultNum = $pgdLsnFactNum - $calendarnumber{$glsGroupLessonDate{$pgdLessArg}}; 
         $pgdFaultAllNum = $pgdFaultAllNum + $pgdFaultNum; }
      else { $pgdFaultNum = ""; }
      $pgdFaultNumLine = $pgdFaultNumLine . "<td $ac>$pgdFaultNum</td>";
      $cnt++; 
   }
   print "$pgdLessNumbLine</tr>\n $pgdPlanTimeLine</tr>\n $pgdPlanLessLine</tr>\n $pgdFactLessLine</tr>
   $pgdFactRcrdLine</tr>\n $pgdFaultNumLine</tr>\n </table>\n<h3>Всего в группе 
   [ <a href = \"$httpindexcgi?list=delays\&groupid\=$pgdGrpId\">$pgdGrpId</a> ] просрочено [$pgdFaultAllNum] дней</h3>\n<p> </p>\n";
}
    #$calendarweek{$tclndrnum} = $tcndrweek; $calendardate{$tclndrnum} = $tclndrdate; substr($yearnow, 2, 2);
    #$calendarweek{$tclndrdate} = $tcndrweek;  $calendarnumber{$tclndrdate} = $tclndrnum;
    #$glsGroupLessonDateArgument = $whatis{'groupid'} . '<tab>' . $GLS_Lesson{$glsprnum};  
    #$glsGroupLessonDate{$glsGroupLessonDateArgument} = $GLS_Date{$glsprnum};

#####################################################################################
################################# GET GROUP SUB #####################################
#####################################################################################
sub getGroupSub {    $ggsgrpfile = $groups_folder . $whatis{'groupid'} . '_data.txt'; $ggsid = $whatis{'groupid'};
    open(UPL, $ggsgrpfile);    @ggsprojectlist = <UPL>;    close(UPL);    foreach $i (@ggsprojectlist){  chomp($i);  
          if ( $i =~ /OEP_School: / )     { $i =~ s/OEP_School: //g;     $OEP_School{$ggsid} = $i; }
       elsif ( $i =~ /OEP_Group: / )      { $i =~ s/OEP_Group: //g;      $OEP_Group{$ggsid} = $i; }
       elsif ( $i =~ /OEP_StartDate: / )  { $i =~ s/OEP_StartDate: //g;  $OEP_StartDate{$ggsid} = $i; }
       elsif ( $i =~ /OEP_FinishDate: / ) { $i =~ s/OEP_FinishDate: //g; $OEP_FinishDate{$ggsid} = $i; }
       elsif ( $i =~ /OEP_Paid: / )       { $i =~ s/OEP_Paid: //g;       $OEP_Paid{$ggsid} = $i; }
       elsif ( $i =~ /OEP_Status: / )     { $i =~ s/OEP_Status: //g;     $OEP_Status{$ggsid} = $i; }
       elsif ( $i =~ /OEP_Calendar: / )   { $i =~ s/OEP_Calendar: //g;   $OEP_Calendar{$ggsid} = $i; }
       elsif ( $i =~ /OEP_TimeList: / )   { $i =~ s/OEP_TimeList: //g;   $OEP_TimeList{$ggsid} = $i; }
    }
}

#####################################################################################
############################### GET LESSONS SUB #####################################
#####################################################################################
sub getLessonSub {
      # foreach $stdid (@studentUniqueNumList){ if($studentGroupNum{$stdid} =~/$whatis{'groupid'}/){  push(@glsStudentsList, $stdid); } }
      $glsgrpfile = $groups_folder . $whatis{'groupid'} . '.txt'; 
      open(UPL, $glsgrpfile);       @glsprojectlist = <UPL>;       close(UPL);      @glsProjectNumList = '';
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
          #elsif($i =~ /OEP_Lesson: /){$i =~ s/OEP_Lesson: //g; $GLS_Lesson{$glsprnum} = $i;}
          elsif($i =~ /OEP_Lesson: /){ $i =~ s/OEP_Lesson: //g; $GLS_Lesson{$glsprnum} = $i;
             if ( $i ne '' ) { push(@glsLessonNumList, "$i<tab>$glsprnum"); } }
          elsif($i =~ /OEP_Date: /){
            $i =~ s/OEP_Date: //g; $GLS_Date{$glsprnum} = $i; #$calendarnumber{$tclndrdate}
            $glsGroupLessonDateArgument = $whatis{'groupid'} . '<tab>' . $GLS_Lesson{$glsprnum};  
            $glsGroupLessonDate{$glsGroupLessonDateArgument} = $GLS_Date{$glsprnum};
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
########################### FINISH END BODY #########################################
#####################################################################################

if($userbrowser eq 'desktop'){print "<p><a href=\'$httpindexcgi\?browser=mobile\'>MOBILE</a></p>\n";}
else{print "<p><a href=\'$httpindexcgi\?browser=desktop\'>DESKTOP</a></p>\n";}

if($userlogged == 1){
   if ( $gotusrid eq '6' || $gotusrid eq '8' || $gotusrid eq '3' || $gotusrid eq '9' ){
      open(INF, $adminText_file); @adminTextList = <INF>; close(INF); print @adminTextList; 
      &printfile($end, $title);
   }
}
else {print "</body></html>";}

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