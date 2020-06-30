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
$indexcgi = 'leader.cgi';
$students_file = $oe_folder . 'students.txt';
$leaders_file = $oe_folder . 'leaders.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpreadcgi = 'http://accelerator.kvadra.kz/cgi-bin/read.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Read-Create-Edit Leaders';

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

open(INF, $leaders_file); 
@leaderslist = <INF>; 
close(INF); 
foreach $i(@leaderslist){
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

open(INF, $students_file); 
@studentslist = <INF>; 
close(INF); 
@uniqueSchoolNumList = "";  @uniqueGroupNumList = "";  @studentUniqueNumList = "";
foreach $i(@studentslist){ 
   #1<tab>56BC4567<tab>Томирис<tab>Толенді<tab><tab>71<tab>71-1-M1<tab>reserve
   #$usernum<tab>$userID<tab>$user1stname<tab>$user2ndname<tab>$user3rdname<tab>$userschool<tab>$usergroup<tab>$other
   ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp, @other) = split (/<tab>/, $i);
   if ( $tstudnum ne '' && $tstudid ne '' ) { 
      if ( $tstudgrp eq '' ) { 
          $studentFirstName{$tstudid} = $tstudfirstnam; $studentSecondName{$tstudid} = $tstudscndnam;
          $studentThirdName{$tstudid} = $tstudthrdnam; push(@emptyGroupList, $tstudid); 
      }
      $glLastStudentNumber = $tstudnum; $glLastStudentCode = $tstudid; 
   }
   if($tstudgrp ne '' && $tstudschl ne ''){
      $studentFirstName{$tstudid} = $tstudfirstnam; $studentSecondName{$tstudid} = $tstudscndnam;
      $studentThirdName{$tstudid} = $tstudthrdnam; $studentPositionNum{$tstudid} = $tstudnum; 
      $studentFullName{$tstudid} = "$tstudfirstnam $tstudthrdnam $tstudscndnam";
      $studentSchoolNum{$tstudid} = $tstudschl; $studentGroupNum{$tstudid} = $tstudgrp;     
      $existSchool{$tstudschl}++;  $existGroup{$tstudgrp}++; 
      if ( grep( /^$tstudschl$/, @uniqueSchoolNumList ) ) { $done = 1; } else { push(@uniqueSchoolNumList, $tstudschl); $totalSchools++; }
      if ( grep( /^$tstudgrp$/, @uniqueGroupNumList ) ){ $done = 1;} 
      else { $GroupsPerSchool{$tstudschl}++; $totalGroups++; push(@uniqueGroupNumList, $tstudgrp); $groupSchoolNum{$tstudgrp} = $tstudschl; }
      push(@studentUniqueNumList, $tstudid); $totalStudents++;
   }
}  # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents ;$totalSchools; $totalGroups

open(INF, $users_file); 
@userlist = <INF>; 
close(INF); 
foreach $i(@userlist){ 
   #1<tab>user1<tab>6<tab>777<tab>13.03.2013<tab>rest
   #$usernum<tab>$username<tab>$userlevel<tab>$userpwd<tab>$other
   ($tusrnum, $tusrnam, $tusrlvl, $tusrpwd, @other) = split (/<tab>/, $i);
   $username{$tusrnum} = $tusrnam; $userpwd{$tusrnum} = $tusrpwd;
   ($userfirstname{$tusrnum}, $userlastname{$tusrnum}) = split(/ /, $tusrnam);
   $userlevel{$tusrnum} = $tusrlvl; $usernumber{$tusrnum} = $tusrnum;
   $usernumber{$tusrnam} = $tusrnum; $userslist++; push(@loginuserslist, $tusrnam);
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
&checkcookies();  print "\n"; &printfile($bas, $title);

if ( $whatis{'action'} ne '' ) { open(GURD,">>$log_file");
print GURD "Time: [$timedatenow] User ID: [$gotusrid] IP address: [$userip] User action: [$whatis{'action'}] Script: [$indexcgi] \n";
close(GURD); }

#####################################################################################
############################ LOGIN CHECK PART #######################################
#####################################################################################
print "<p>";
if($userlogged == 1){
    print "Hello $b1 $userfirstname{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>";
    if ( $whatis{'action'} eq 'newleader' ) { &newLeaderPageSub(); }
    elsif ( $whatis{'action'} eq 'open' && $whatis{'groupid'} ne '' ) { &openGroupPageSub(); }
    elsif ( $whatis{'action'} eq 'edit' && $whatis{'userid'} =~/54LD/ ) { &editLeaderSub(); }
    elsif ( $whatis{'action'} eq 'save' && $whatis{'userid'} =~/54LD/ ) { &saveLeaderDataSub(); }
    else { &blankPageSub() ; }
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
########################### NEW LEADER DATA SUB #####################################
#####################################################################################
sub newLeaderPageSub {
   # No<tab>Uniques ID<tab>1st name<tab>2nd name<tab>3rd name<tab>PWD<tab>School ID<tab>Group ID<tab>Phone Num<tab>Email<tab>Date<tab>Reserve
   &printjavascript(); #$elsLdrId = $whatis{'userid'};  
   print "<h2>Создать запись нового волонтера</h2>\n"; $elsStyle = "style='height:50px; width:150px'";
   $elsGroupHtmlCode = "<select name = 'groupid'><option value = ''>Выберите группу</option>\n";
   if ( $LeaderGroupNum{$elsLdrId} ne '' ) { 
   $elsGroupHtmlCode = $elsGroupHtmlCode . "<option value = \'$LeaderGroupNum{$elsLdrId}\' selected>$LeaderGroupNum{$elsLdrId}</option>\n"; }
   foreach $i (@uniqueGroupNumList) { if ($i ne '') { $elsGroupHtmlCode = $elsGroupHtmlCode . "<option value = \'$i\'>$i</option>\n"; } }
   $elsGroupHtmlCode = $elsGroupHtmlCode . "</select>\n";   
   $elsSchoolHtmlCode = "<select name = 'schoolid'><option value = ''>Выберите школу</option>\n";
   if ( $LeaderSchoolNum{$elsLdrId} ne '' ) { 
   $elsSchoolHtmlCode = $elsSchoolHtmlCode . "<option value = \'$LeaderSchoolNum{$elsLdrId}\' selected>$LeaderSchoolNum{$elsLdrId}</option>\n"; }
   foreach $i (@uniqueSchoolNumList) { if ($i ne '') { $elsSchoolHtmlCode = $elsSchoolHtmlCode . "<option value = \'$i\'>$i</option>\n"; } }
   $elsSchoolHtmlCode = $elsSchoolHtmlCode . "</select>\n";
   if ($LeaderFullName{$elsLdrId} ne '  ') {#$LeaderSchoolNum{$tldrid}    $LeaderGroupNum{$tldrid}
      print "<form method='post' action=\'$httpindexcgi\' onsubmit='return checkNewFunction();'>
      <input type = 'hidden' name = 'action' value = 'save'> <input type = 'hidden' name = 'userid' value = '54LD-new'>
      <table><tr $yelclr><td>1</td><td>Имя: </td><td><input type = 'text' name = 'firstname' value = ''></td></tr>
      <tr $yelclr1><td>2</td><td>Фамилия: </td><td><input type = 'text' name = 'secondname' value = ''></td></tr>
      <tr $yelclr><td>3</td><td>Отчество: </td><td><input type = 'text' name = 'thirdname' value = ''></td></tr>
      <tr $yelclr1><td>4</td><td>Номер школы: </td><td>$elsSchoolHtmlCode</td></tr>
      <tr $yelclr><td>5</td><td>Номер группы:</td><td>$elsGroupHtmlCode</td></tr>
      <tr $yelclr1><td>6</td><td>Дата рождения: </td><td><input type = 'text'  name = 'birthday' value = ''> FORMAT: DD.MM.YYYY</td></tr>
      <tr $yelclr><td>7</td><td>Пол: </td><td><select name = 'gender'><option value = ''>Выберите пол</option>
      <option value = 'Male'>Male</option>      <option value = 'Female'>Female</option></select></td></tr>
      <tr $yelclr1><td>8</td><td>Место учебы/ работы: </td><td><input type = 'text'  name = 'workplace' value = ''></td></tr>
      <tr $yelclr><td>9</td><td>Номер удостоверения: </td><td><input type = 'text'  name = 'personid' value = ''></td></tr>
      <tr $yelclr1><td>10</td><td>ИИН: </td><td><input type = 'text'  name = 'individ' value = ''></td></tr>
      <tr $yelclr><td>11</td><td>Номер телефона: </td><td><input type = 'text' name = 'phonenumber' value = ''></td></tr>
      <tr $yelclr1><td>12</td><td>EMAIL: </td><td><input type = 'text' name = 'email' value = ''></td></tr></table>
      <input type='reset' value = 'ОТМЕНИТЬ' $elsStyle>-[-]-[-]-[-]-<input type = 'submit' value = 'ЗАПИСАТЬ' $elsStyle></form>
      <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
   }
   else { print "<h3>$rf Неверные данные, запись не найдена! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; }
}

#####################################################################################
########################## EDIT LEADER DATA SUB #####################################
#####################################################################################
sub editLeaderSub {
   # No<tab>Uniques ID<tab>1st name<tab>2nd name<tab>3rd name<tab>PWD<tab>School ID<tab>Group ID<tab>Phone Num<tab>Email<tab>Date<tab>Reserve
   &printjavascript(); $elsLdrId = $whatis{'userid'};  
   print "<h2>Изменение данных волонтеров</h2>\n"; $elsStyle = "style='height:50px; width:150px'";
   $elsGroupHtmlCode = "<select name = 'groupid'><option value = ''>Выберите группу</option>\n";
   if ( $LeaderGroupNum{$elsLdrId} ne '' ) { 
   $elsGroupHtmlCode = $elsGroupHtmlCode . "<option value = \'$LeaderGroupNum{$elsLdrId}\' selected>$LeaderGroupNum{$elsLdrId}</option>\n"; }
   foreach $i (@uniqueGroupNumList) { if ($i ne '') { $elsGroupHtmlCode = $elsGroupHtmlCode . "<option value = \'$i\'>$i</option>\n"; } }
   $elsGroupHtmlCode = $elsGroupHtmlCode . "<option value = ''>Удалите группу</option></select>\n";   
   $elsSchoolHtmlCode = "<select name = 'schoolid'><option value = ''>Выберите школу</option>\n";
   if ( $LeaderSchoolNum{$elsLdrId} ne '' ) { 
   $elsSchoolHtmlCode = $elsSchoolHtmlCode . "<option value = \'$LeaderSchoolNum{$elsLdrId}\' selected>$LeaderSchoolNum{$elsLdrId}</option>\n"; }
   foreach $i (@uniqueSchoolNumList) { if ($i ne '') { $elsSchoolHtmlCode = $elsSchoolHtmlCode . "<option value = \'$i\'>$i</option>\n"; } }
   $elsSchoolHtmlCode = $elsSchoolHtmlCode . "<option value = ''>Удалите школу</option></select>\n";
   if ($LeaderFullName{$elsLdrId} ne '  ') {#$LeaderSchoolNum{$tldrid}    $LeaderGroupNum{$tldrid}
      print "<form method='post' action=\'$httpindexcgi\' onsubmit='return checkNewFunction();'>
      <input type = 'hidden' name = 'action' value = 'save'><input type = 'hidden' name = 'userid' value = \'$whatis{'userid'}\'>
      <table><caption><h3>User ID [$whatis{'userid'}]</h3></caption>
      <tr $yelclr><td>1</td><td>Имя: </td><td><input type = 'text' name = 'firstname' value = \'$LeaderFirstName{$elsLdrId}\'></td></tr>
      <tr $yelclr1><td>2</td><td>Фамилия: </td><td><input type = 'text' name = 'secondname' value = \'$LeaderSecondName{$elsLdrId}\'></td></tr>
      <tr $yelclr><td>3</td><td>Отчество: </td><td><input type = 'text' name = 'thirdname' value = \'$LeaderThirdName{$elsLdrId}\'></td></tr>
      <tr $yelclr1><td>4</td><td>Номер школы: </td><td>$elsSchoolHtmlCode</td></tr>
      <tr $yelclr><td>5</td><td>Номер группы:</td><td>$elsGroupHtmlCode</td></tr>
      <tr $yelclr1><td>6</td><td>Дата рождения: </td>
      <td><input type = 'text'  name = 'birthday' value = \'$LeaderBirthDay{$edsUsrId}\'> FORMAT: DD.MM.YYYY</td></tr>
      <tr $yelclr><td>7</td><td>Пол: </td><td><select name = 'gender'><option value = ''>Выберите пол</option><option value = 'Male'>Male</option>\n";
      if ( $LeaderGender{$elsLdrId} ne '' ) { print "<option value = \'$LeaderGender{$elsLdrId}\' selected>$LeaderGender{$elsLdrId}</option>"; }
      $LeaderEmail{$elsLdrId} = lc $LeaderEmail{$elsLdrId};
      print "<option value = 'Female'>Female</option></select></td></tr>
      <tr $yelclr1><td>8</td><td>Место учебы/ работы: </td><td><input type = 'text'  name = 'workplace' value = \'$LeaderWorkPlace{$elsLdrId}\'></td></tr>
      <tr $yelclr><td>9</td><td>Номер удостоверения: </td><td><input type = 'text'  name = 'personid' value = \'$LeaderPersonId{$elsLdrId}\'></td></tr>
      <tr $yelclr1><td>10</td><td>ИИН: </td><td><input type = 'text'  name = 'individ' value = \'$LeaderIndividId{$elsLdrId}\'></td></tr>
      <tr $yelclr><td>11</td><td>Номер телефона: </td><td><input type = 'text' name = 'phonenumber' value = \'$LeaderPhoneNum{$elsLdrId}\'></td></tr>
      <tr $yelclr1><td>12</td><td>EMAIL: </td><td><input type = 'text' name = 'email' value = \'$LeaderEmail{$elsLdrId}\'></td></tr></table>
      <input type='reset' value = 'ОТМЕНИТЬ' $elsStyle>-[-]-[-]-[-]-<input type = 'submit' value = 'ЗАПИСАТЬ' $elsStyle></form>
      <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
   }
   else { print "<h3>$rf Неверные данные, запись не найдена! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; }
}
#####################################################################################
########################## SAVE LEADER DATA SUB #####################################
#####################################################################################
sub saveLeaderDataSub { 
   #   $glLastLeaderNumber = $tldrnum; $glLastLeaderCode = $tldrid;
   #   $LeaderFullName{$tldrid} = "$tldrfirstnam $tldrscndnam $tldrthrdnam"; $LeaderPassWord{$tldrid} = $tldrpwd;
   #   $LeaderUniqueId{$tldrid} = $tldrid; $LeaderFirstName{$tldrid} = $tldrfirstnam; $LeaderSecondName{$tldrid} = $tldrscndnam;
   #   $LeaderThirdName{$tldrid} = $tldrthrdnam; $LeaderPositionNum{$tldrid} = $tldrnum;   $LeaderSchoolNum{$tldrid} = $tldrschl;
   #   $LeaderGroupNum{$tldrid} = $tldrgrp; $LeaderPhoneNum{$tldrid} = $tldrphn; $LeaderEmail{$tldrid} = $tldremail; 
   print "<h2>Сохранение данных по волонтерам</h2>\n";  
   $sldLeaderFound = 0; $sldLdrId = $whatis{'userid'}; $whatis{'email'} = lc $whatis{'email'};
   # if ( $LeaderFullName{$sldLdrId} eq '  ' ) { 
   # print "<h3>$rf Данные волонтера не найдены! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; return; }
   foreach $sldLine(@leaderslist){
      ($tldrnum, $tldrid, @other) = split (/<tab>/, $sldLine);
      if ( $tldrid eq $whatis{'userid'} && $sldLeaderFound == 0 ) { $sldLeaderFound = 1; $sldLeaderPlaceNum = $tldrnum; }
      elsif ( $sldLeaderFound == 0 && $sldLine ne '' ) { push(@sldStartLeadersList, $sldLine); }
      elsif ( $sldLeaderFound == 1 && $sldLine ne '' ) { push(@sldEndLeadersList, $sldLine); }
      else { $donothing = 1; }
   } # $ldrnum<tab>$ldrID<tab>$ldr1stname<tab>$ldr2ndname<tab>$ldr3rdname<tab>$ldrpwd<tab>$userschool<tab>$usergroup<tab>$other
   if ( $sldLeaderFound == 1 ) { $sldLeaderId = $LeaderUniqueId{$sldLdrId}; $sldLeaderPassword = $LeaderPassWord{$sldLdrId}; }
   else { 
      ($sldLeaderOldPlaceNum, $sldLeaderOldId) = split (/54LD/, $glLastLeaderCode); $sldLeaderPassword = 'america';
      $sldLeaderOldId++; $sldLeaderId = '54LD' . $sldLeaderOldId; $sldLeaderPlaceNum = $glLastLeaderNumber + 1;
   }
   $sldNewLineText = "$sldLeaderPlaceNum<tab>$sldLeaderId<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}";
   $sldNewLineText = $sldNewLineText . "<tab>$sldLeaderPassword<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'phonenumber'}";
   $sldNewLineText = $sldNewLineText . "<tab>$whatis{'email'}<tab>$datenow<tab>$whatis{'birthday'}<tab>$whatis{'gender'}";
   $sldNewLineText = $sldNewLineText . "<tab>$whatis{'workplace'}<tab>$whatis{'personid'}<tab>$whatis{'individ'}<tab>reserve\n";
   open(SSDATA,">$leaders_file");
   print SSDATA @sldStartLeadersList;
   print SSDATA $sldNewLineText;
   if ( $sldLeaderFound == 1 ) { print SSDATA @sldEndLeadersList; }
   close(SSDATA);
   print "<table $grnclr><tr><td><h2>Данные изменения внесены в систему [$datenow].</h2></td></tr></table>
   <p> </p><table><caption><h3>User ID [$whatis{'userid'}]</h3></caption>
   <tr $yelclr><td>1</td><td>Имя волонтера: </td><td>$whatis{'firstname'}</td></tr>
   <tr $yelclr1><td>2</td><td>Фамилия волонтера: </td><td>$whatis{'secondname'}</td></tr>
   <tr $yelclr><td>3</td><td>Отчество волонтера: </td><td>$whatis{'thirdname'}</td></tr>
   <tr $yelclr1><td>4</td><td>Номер школы: </td><td>$whatis{'schoolid'}</td></tr>
   <tr $yelclr><td>5</td><td>Номер группы:</td><td>$whatis{'groupid'}</td></tr>
   <tr $yelclr1><td>6</td><td>Номер телефона: </td><td>$whatis{'phonenumber'}</td></tr>
   <tr $yelclr><td>7</td><td>EMAIL: </td><td>$whatis{'email'}</td></tr>
   <tr $yelclr1><td>8</td><td>Дата рождения: </td><td>$whatis{'birthday'}</td></tr>
   <tr $yelclr><td>9</td><td>Пол волонтера: </td><td>$whatis{'gender'}</td></tr>
   <tr $yelclr1><td>10</td><td>Место работы / учебы: </td><td>$whatis{'workplace'}</td></tr>
   <tr $yelclr><td>11</td><td>Номер удостоверения: </td><td>$whatis{'personid'}</td></tr>
   <tr $yelclr1><td>12</td><td>ИИН: </td><td>$whatis{'individ'}</td></tr></table>
   <p> </p><p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 

}

#####################################################################################
########################### OPEN GROUP PAGE SUB #####################################
#####################################################################################
sub openGroupPageSub {
   &printjavascript(); $myclr = $yelclr; $cnt = 1;
   print "<h2>Изменение данных волонтеров</h2>\n <p>Список волонтеров школы № [$whatis{'schoolid'}] и группы № [$whatis{'groupid'}]</p>
   <table><tr $myclr><td>No</td><td $ac>ID</td><td>ФИО</td><td>Редактировать данные волонтеров</td></tr>\n";
   if ( $whatis{'groupid'} eq 'empty' || $whatis{'groupid'} eq '' ) {
      foreach $ogpLine(@leaderslist){ $ogpChompLine = $ogpLine; chomp($ogpChompLine);
         ($tldrnum, $tldrid, $tldrfirstnam, $tldrscndnam, $tldrthrdnam, $tldrpwd, $tldrschl, $tldrgrp, @other) = split (/<tab>/, $ogpChompLine);
         if ( $tldrgrp eq '' ) {
             if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
             print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$tldrid\'></td><td>[$tldrid]</td>
             <td>$tldrfirstnam $tldrscndnam $tldrthrdnam</td> <td><button onclick=\"return checkEditFunction\($cnt\)\;\" $bpsStyle>
             Редактировать / Добавить</button> данные волонтера</td></tr>\n"; 
             $cnt++;
         }
      }
   }
   else{
      foreach $ogpLine(@leaderslist){ $ogpChompLine = $ogpLine; chomp($ogpChompLine);
         ($tldrnum, $tldrid, $tldrfirstnam, $tldrscndnam, $tldrthrdnam, $tldrpwd, $tldrschl, $tldrgrp, @other) = split (/<tab>/, $ogpChompLine);
         if ( $tldrgrp eq $whatis{'groupid'} ) {
             if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
             print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$tldrid\'></td><td>[$tldrid]</td>
             <td>$tldrfirstnam $tldrscndnam $tldrthrdnam</td> <td><button onclick=\"return checkEditFunction\($cnt\)\;\" $bpsStyle>
             Редактировать / Добавить</button> данные волонтера</td></tr>\n"; 
             $cnt++;
         }
      }
      &getGroupSub(); $ogpid = $whatis{'groupid'}; 
      $ogpLeaderOneId = $OEP_VolunteerOneCode{$ogpid}; $ogpLeaderTwoId = $OEP_VolunteerTwoCode{$ogpid};
      if ( $ogpLeaderOneId =~ /54LD/ ) {
          if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
          print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$ogpLeaderOneId\'></td><td>[$tldrid]</td>
          <td>$LeaderFullName{$ogpLeaderOneId} [1-ый волонтер]</td> <td><button onclick=\"return checkEditFunction\($cnt\)\;\" $bpsStyle>
          Редактировать / Добавить</button> данные волонтера</td></tr>\n"; $cnt++;
      }
      if ( $ogpLeaderTwoId =~ /54LD/ ) {
          if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
          print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$ogpLeaderTwoId\'></td><td>[$tldrid]</td>
          <td>$LeaderFullName{$ogpLeaderTwoId} [2-ой волонтер]</td> <td><button onclick=\"return checkEditFunction\($cnt\)\;\" $bpsStyle>
          Редактировать / Добавить</button> данные волонтера</td></tr>\n"; $cnt++;
      }
   }
   print "</table>\n <p> </p> <a href=\'$httpindexcgi\'>[ Вернуться НАЗАД ]</a>\n"; 
}
#####################################################################################
################################ BLANK PAGE SUB #####################################
#####################################################################################
sub blankPageSub {
  &printjavascript(); $bpsStyle = "style='height:50px; width:150px'";
  print "<h2>Списки волонтеров OpenEnglish</h2>\n <form method='post' action=\'$httpindexcgi\' onsubmit='return checkGoFunction();'>
  <table><tr $yelclr><td>Выберите школу</td><td>Выберите группу</td></tr>
  <tr $yelclr1><td><select name = 'schoolid' onchange=\"showGroupFunction()\"><option value = ''>Выберите школу</option>";
  foreach $bpsSchlId (@uniqueSchoolNumList) { if ( $bpsSchlId ne '' ) { print "<option value = \'$bpsSchlId\'>Школа № $bpsSchlId</option>"; } }
  print "<option value = 'empty'>волонтеры без группы</option></select></td><td><p id = 'myGroupList'></p></td></tr>
  <tr $yelclr><td><input type = 'hidden' name = 'action' value = 'open'>
  <input type='reset' value = 'ОТМЕНИТЬ' $bpsStyle></td><td><input type = 'submit' value = 'ОТКРЫТЬ' $bpsStyle></td></tr></table></form>
  <button onclick=\"window.location.href = \'$httpindexcgi\?action=newleader\'\;\" $bpsStyle>Добавить Нового Волонтера</button>\n";
} 
#####################################################################################
################################ GET GROUP SUB ######################################
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
########################### FINISH END BODY #########################################
#####################################################################################

#if($userbrowser eq 'desktop'){print "<p><a href=\'$httpindexcgi\?browser=mobile\'>MOBILE</p>\n";}
#else{print "<p><a href=\'$httpindexcgi\?browser=desktop\'>DESKTOP</p>\n";}

&printfile($end, $title);

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

#######################################################################################
########################## JAVASCRIPT PART ###########################################
#######################################################################################
sub printjavascript {
$pjsGroupArray = ''; $cnt = 0;
foreach $pjsGrpId (@uniqueGroupNumList) {
    if ( $pjsGrpId ne '' ) { 
        if ($cnt == 0) { $pjsGroupArray = "\"$pjsGrpId\""; }
        else { $pjsGroupArray = $pjsGroupArray . ", \"$pjsGrpId\""; }
        $cnt++;
    }
}
$cnt = 0; $pjsEmailArray = '';
foreach $i(@leaderslist){
   ($tldrnum, $tldrid, $tldrfirstnam, $tldrscndnam, $tldrthrdnam, $tldrpwd, $tldrschl, $tldrgrp, $tldrphn, $tldremail, @other) = split (/<tab>/, $i);
   if ( $tldrid ne '' && $tldremail =~ /\@/ ) {  $tldremail = lc $tldremail;
      if ($cnt == 0) { $pjsEmailArray = "\"$tldrfirstnam\", \"$tldrscndnam\", \"$tldremail\""; }
      else { $pjsEmailArray = $pjsEmailArray . ",\n \"$tldrfirstnam\", \"$tldrscndnam\", \"$tldremail\""; }
      $cnt++;
   }
}

print  <<EOT;
 <script>
 function checkNewFunction (){
   var emailList = [$pjsEmailArray]; var emailExist = 0; var emailAddress = '';
   if(document.getElementsByName('firstname')[0].value == ''){alert('Укажите имя!'); return false;}
   if(document.getElementsByName('secondname')[0].value == ''){alert('Укажите фамилию!'); return false;}
   if(document.getElementsByName('birthday')[0].value != ''){
      var usr = document.getElementsByName('birthday')[0].value;
      if (isValidDate(usr)) { document.getElementsByName('birthday')[0].value = usr; }
      else {alert('Неправильная дата: [' + usr + ']!'); return false;}
   }
   if(document.getElementsByName('phonenumber')[0].value == ''){alert('Укажите номер телефона!'); return false;}
   if(document.getElementsByName('email')[0].value == ''){alert('Укажите EMAIL!'); return false;}
   else {
      emailAddress = document.getElementsByName('email')[0].value; emailAddress = emailAddress.toLowerCase();
      document.getElementsByName('email')[0].value = emailAddress; emailExist = emailList.indexOf(emailAddress);
      if(emailExist > 0 ){
         var userFirstNameId = emailExist - 2; var userSecondNameId = emailExist - 1;
         var userFirstName = emailList[userFirstNameId]; var userSecondName = emailList[userSecondNameId];
         alert('Такой EMAIL:[' + emailAddress + '] уже используется - Имя:[' + userFirstName + '] Фамилия:[' + userSecondName + ']'); return false;
      }
      else{ document.getElementsByName('email')[0].value = emailAddress; }
   }
 }
 function checkSaveFunction (){
     var usr = confirm('Изменить Запись?');
     if(usr){return true;}
     else{return false;}
 }
 function checkGoFunction (){
        if(document.getElementsByName('schoolid')[0].value == ''){alert('Выберите номер школы!'); return false;}
        if(document.getElementsByName('groupid')[0].value == ''){alert('Выберите номер группы!'); return false;}
 }
 function showGroupFunction (){
     var groupList = [$pjsGroupArray];     var mySchoolId = document.getElementsByName('schoolid')[0].value;
     var GroupText = '<select name = "groupid"><option value = "">Выберите группу</option>'; var foundResult = 0;
     groupList.forEach(function(GroupId, i, groupList) {
        foundResult = GroupId.indexOf(mySchoolId);
        if(foundResult == 0) { GroupText = GroupText + '<option value = "' + GroupId + '">' + GroupId + '</option>' ; }
     }); 
     if ( mySchoolId == 'empty' ) { GroupText = '<select name = "groupid"><option value = "empty">волонтеры без группы</option></select>'; }
     else if ( mySchoolId != '' ) { GroupText = GroupText + '</select>'; }
     else { GroupText = ''; }
     document.getElementById('myGroupList').innerHTML = GroupText;
 }
 function checkEditFunction (cnt) {
     var userlink = \'$httpindexcgi\?action=edit\&userid=' + document.getElementById(cnt).value;
     var usr = confirm('Изменить Запись?');
     if(usr){window.location.href = userlink;}
     else{return false;}
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