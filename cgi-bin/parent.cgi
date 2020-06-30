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
$indexcgi = 'parent.cgi';
$students_file = $oe_folder . 'students.txt';
$parents_file = $oe_folder . 'parents.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpreadcgi = 'http://accelerator.kvadra.kz/cgi-bin/read.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Read-Create-Edit Parents';

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

open(INF, $parents_file); 
@parentslist = <INF>; 
close(INF); 
foreach $i(@parentslist){
   #1<tab>55FM4703<tab>56BC4703<tab>Sergei<tab>Sergeev<tab>Sergeevich<tab>99<tab>99-M2-1<tab>
   #$usernum<tab>$userID<tab>$studentID<tab>$user1stname<tab>$user2ndname<tab>$user3rdname<tab>$userschool<tab>$usergroup<tab>$other
   ($tparntnum, $tparntid, $tparntstudid, $tparntfirstnam, $tparntscndnam, $tparntthrdnam, $tparntschl, $tparntgrp,
      $tparntbrtd, $tparntphn, $tparntwrkplc, $tparntemail, @other) = split (/<tab>/, $i);
   if ( $tparntnum ne '' && $tparntid ne '' ) { $glLastParentNumber = $tparntnum; $glLastParentCode = $tparntid; }
   if($tparntid ne ''){  $ParentUniqueId{$tparntstudid} = $tparntid;
      $ParentFirstName{$tparntid} = $tparntfirstnam; $ParentSecondName{$tparntid} = $tparntscndnam;
      $ParentThirdName{$tparntid} = $tparntthrdnam; $ParentPositionNum{$tparntid} = $tparntnum; 
      $ParentSchoolNum{$tparntid} = $tparntschl; $ParentGroupNum{$tparntid} = $tparntgrp;     
      $ParentBirthDay{$tparntid} = $tparntbrtd; $ParentPhoneNum{$tparntid} = $tparntphn; 
      $ParentWorkPlace{$tparntid} = $tparntwrkplc; $ParentEmail{$tparntid} = $tparntemail; 
   }
}  # $existSchool{$tparntschl}; $existGroup{$tparntgrp}; $GroupsPerSchool{$tparntschl}; $totalParents ;$totalSchools; $totalGroups

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
    if ( $whatis{'action'} eq 'open' && $whatis{'groupid'} ne '') { &openGroupPageSub(); }
    elsif ( $whatis{'action'} eq 'edit' && $whatis{'userid'} =~/56BC/) { &editParentSub(); }
    elsif ( $whatis{'action'} eq 'save' && $whatis{'userid'} =~/56BC/) { &saveParentDataSub(); }
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
########################## EDIT PARENT DATA SUB #####################################
#####################################################################################
sub editParentSub {
   &printjavascript(); $epsUsrId = $whatis{'userid'};  $epsParntId = $ParentUniqueId{$epsUsrId};
   print "<h2>Изменение данных родителя учеников</h2>\n"; $epsStyle = "style='height:50px; width:150px'";
   if ($studentFullName{$epsUsrId} ne '  ') {
      print "<form method='post' action=\'$httpindexcgi\' onsubmit='return checkSaveFunction();'>
      <input type = 'hidden' name = 'action' value = 'save'><input type = 'hidden' name = 'userid' value = \'$whatis{'userid'}\'>
      <input type = 'hidden' name = 'schoolid' value = \'$studentSchoolNum{$epsUsrId}\'> 
      <input type = 'hidden' name = 'groupid' value = \'$studentGroupNum{$epsUsrId}\'>\n<table>";
      if ( $epsParntId ne '' ) { print "<caption><h3>Parent ID [$epsParntId]</h3></caption>\n"; }
      print "<tr $yelclr><td>1</td><td>Имя: </td><td><input type = 'text' name = 'firstname' value = \'$ParentFirstName{$epsParntId}\'></td></tr>
      <tr $yelclr1><td>2</td><td>Фамилия: </td><td><input type = 'text' name = 'secondname' value = \'$ParentSecondName{$epsParntId}\'></td></tr>
      <tr $yelclr><td>3</td><td>Отчество: </td><td><input type = 'text' name = 'thirdname' value = \'$ParentThirdName{$epsParntId}\'></td></tr>
      <tr $yelclr1><td>4</td><td>Номер школы: </td><td>$studentSchoolNum{$epsUsrId}</td></tr>
      <tr $yelclr><td>5</td><td>Номер группы:</td><td>$studentGroupNum{$epsUsrId}</td></tr>
      <tr $yelclr1><td>6</td><td>Дата рождения: </td><td><input type = 'text' name = 'birthday' value = \'$ParentBirthDay{$epsParntId}\'></td></tr>
      <tr $yelclr><td>7</td><td>Номер телефона: </td><td><input type = 'text' name = 'phonenumber' value = \'$ParentPhoneNum{$epsParntId}\'></td></tr>
      <tr $yelclr1><td>8</td><td>Место работы: </td><td><input type = 'text' name = 'workplace' value = \'$ParentWorkPlace{$epsParntId}\'></td></tr>
      <tr $yelclr><td>9</td><td>EMAIL: </td><td><input type = 'text' name = 'email' value = \'$ParentEmail{$epsParntId}\'></td></tr></table>
      <input type='reset' value = 'ОТМЕНИТЬ' $epsStyle>-[-]-[-]-[-]-<input type = 'submit' value = 'ЗАПИСАТЬ' $epsStyle></form>
      <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
   }
   else { print "<h3>$rf Неверные данные, запись не найдена! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; }
}
#####################################################################################
########################## SAVE PARENT DATA SUB #####################################
#####################################################################################
sub saveParentDataSub { # $glLastParentNumber = $tparntnum; $glLastParentCode = $tparntid;
print "<h2>Сохранение данных родителя по ученикам</h2>\n";  $spdUserFound = 0; $spdUsrId = $whatis{'userid'};
   if ( $studentFullName{$spdUsrId} eq '  ' ) { 
   print "<h3>$rf Данные ученика не найдены! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; return; }
   foreach $spdLine(@parentslist){ $spdChompLine = $spdLine; chomp($spdChompLine);
      ($tparntnum, $tparntid, $tparntstudid, $tparntfirstnam, $tparntscndnam, $tparntthrdnam, $tparntschl, $tparntgrp,
      $tparntbrtd, $tparntphn, $tparntwrkplc, $tparntemail, @other) = split (/<tab>/, $spdChompLine);
      if ( $tparntstudid eq $whatis{'userid'} && $spdUserFound == 0 ) { $spdUserFound = 1; $spdUserPlaceNum = $tparntnum; }
      elsif ( $spdUserFound == 0 && $spdLine ne '' ) { push(@spdStartParentsList, $spdLine); }
      elsif ( $spdUserFound == 1 && $spdLine ne '' ) { push(@spdEndParentsList, $spdLine); }
      else { $donothing = 1; }
   } # 1<tab>55FM4703<tab>56BC4703<tab>Sergei<tab>Sergeev<tab>Sergeevich<tab>99<tab>99-M2-1<tab>
   if ( $spdUserFound == 1 ) { $spdParentId = $ParentUniqueId{$spdUsrId}; }
   else { 
      ($spdParentOldPlaceNum, $spdParentOldId) = split (/55FM/, $glLastParentCode);
      $spdParentOldId++; $spdParentId = '55FM' . $spdParentOldId; $spdUserPlaceNum = $glLastParentNumber + 1;
   }
   $spdNewLineText = "$spdUserPlaceNum<tab>$spdParentId<tab>$whatis{'userid'}<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}";
   $spdNewLineText = $spdNewLineText . "<tab>$whatis{'thirdname'}<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'birthday'}";
   $spdNewLineText = $spdNewLineText . "<tab>$whatis{'phonenumber'}<tab>$whatis{'workplace'}<tab>$whatis{'email'}<tab>reserve\n";
   open(SSDATA,">$parents_file");
   print SSDATA @spdStartParentsList;
   print SSDATA $spdNewLineText;
   if ( $spdUserFound == 1 ) { print SSDATA @spdEndParentsList; }
   close(SSDATA);
   print "<table $grnclr><tr><td><h2>Данные изменения внесены в систему.</h2></td></tr></table>
   <p> </p><table><caption><h3>Parent ID [$epsParntId]</h3></caption>
   <tr $yelclr1><td>1</td><td>Данные ученика: </td><td>$studentFullName{$spdUsrId}</td></tr>
   <tr $yelclr><td>2</td><td>Имя родителя: </td><td>$whatis{'firstname'}</td></tr>
   <tr $yelclr1><td>3</td><td>Фамилия родителя: </td><td>$whatis{'secondname'}</td></tr>
   <tr $yelclr><td>4</td><td>Отчество родителя: </td><td>$whatis{'thirdname'}</td></tr>
   <tr $yelclr1><td>5</td><td>Номер школы: </td><td>$whatis{'schoolid'}</td></tr>
   <tr $yelclr><td>6</td><td>Номер группы:</td><td>$whatis{'groupid'}</td></tr>
   <tr $yelclr1><td>7</td><td>Дата рождения: </td><td>$whatis{'birthday'}</td></tr>
   <tr $yelclr><td>8</td><td>Номер телефона: </td><td>$whatis{'phonenumber'}</td></tr>
   <tr $yelclr1><td>9</td><td>Место учебы/работы: </td><td>$whatis{'workplace'}</td></tr>
   <tr $yelclr><td>10</td><td>EMAIL: </td><td>$whatis{'email'}</td></tr></table>
   <p> </p><p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 

}

#####################################################################################
########################### OPEN GROUP PAGE SUB #####################################
#####################################################################################
sub openGroupPageSub {
    &printjavascript(); $myclr = $yelclr; $cnt = 1;
    print "<h2>Изменение данных родителя учеников</h2>\n <p>Список учеников школы № [$whatis{'schoolid'}] и группы № [$whatis{'groupid'}]</p>
    <table><tr $myclr><td>No</td><td>ID</td><td>ФИО</td><td>Редактировать данные родителя</td></tr>\n";
    if ( $whatis{'groupid'} eq 'empty') {
        foreach $ogpStdId (@emptyGroupList) {
            if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
            print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$ogpStdId\'></td><td>[$ogpStdId]</td>
            <td>$studentFirstName{$ogpStdId} $studentThirdName{$ogpStdId} $studentSecondName{$ogpStdId}</td>
            <td><button onclick=\"return checkEditFunction\($cnt\)\;\" $bpsStyle>Редактировать / Добавить</button> данные родителя</td></tr>\n"; 
            $cnt++;
        }
    }
    else{
        foreach $ogpStdId (@studentUniqueNumList) {
           if($studentGroupNum{$ogpStdId} =~ $whatis{'groupid'}){
              if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
              print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$ogpStdId\'></td><td>[$ogpStdId]</td>
              <td>$studentFirstName{$ogpStdId} $studentThirdName{$ogpStdId} $studentSecondName{$ogpStdId}</td>
              <td><button onclick=\"return checkEditFunction\($cnt\)\;\" $bpsStyle>Редактировать / Добавить</button> данные родителя</td></tr>\n"; 
              $cnt++;
           } # checkEditFunction
        }
    }
    print "</table>\n <p> </p> <a href=\'$httpindexcgi\'>[ Вернуться НАЗАД ]</a>\n"; 
}
#####################################################################################
################################ BLANK PAGE SUB #####################################
#####################################################################################
sub blankPageSub {
  &printjavascript(); $bpsStyle = "style='height:50px; width:150px'";
  print "<h2>Открыть список учеников OpenEnglish</h2>\n <form method='post' action=\'$httpindexcgi\' onsubmit='return checkGoFunction();'>
  <table><tr $yelclr><td>Выберите школу</td><td>Выберите группу</td></tr>
  <tr $yelclr1><td><select name = 'schoolid' onchange=\"showGroupFunction()\"><option value = ''>Выберите школу</option>";
  foreach $bpsSchlId (@uniqueSchoolNumList) { if ( $bpsSchlId ne '' ) { print "<option value = \'$bpsSchlId\'>Школа № $bpsSchlId</option>"; } }
  print "</select></td><td><p id = 'myGroupList'></p></td></tr><tr $yelclr><td><input type = 'hidden' name = 'action' value = 'open'>
  <input type='reset' value = 'ОТМЕНИТЬ' $bpsStyle></td><td><input type = 'submit' value = 'ОТКРЫТЬ' $bpsStyle></td></tr></table></form>\n";
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
sub printjavascript {  #var cars = ["Saab", "Volvo", "BMW"];
$pjsGroupArray = ''; $cnt = 0;
foreach $pjsGrpId (@uniqueGroupNumList) {
    if ( $pjsGrpId ne '' ) { 
        if ($cnt == 0) { $pjsGroupArray = "\"$pjsGrpId\""; }
        else { $pjsGroupArray = $pjsGroupArray . ", \"$pjsGrpId\""; }
        $cnt++;
    }
}
print  <<EOT;
 <script>
 function checkAllFunction (){
   if(document.getElementsByName('firstname')[0].value == ''){alert('Укажите имя!'); return false;}
   if(document.getElementsByName('secondname')[0].value == ''){alert('Укажите фамилию!'); return false;}
   if(document.getElementsByName('phonenumber')[0].value == ''){alert('Укажите номер телефона!'); return false;}
   if(document.getElementsByName('email')[0].value == ''){alert('Укажите Email!'); return false;}
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
     if ( mySchoolId != '' ) { GroupText = GroupText + '</select>'; }
     else { GroupText = ''; }
     document.getElementById('myGroupList').innerHTML = GroupText;
 }
 function checkEditFunction (cnt) {
     var userlink = \'$httpindexcgi\?action=edit\&userid=' + document.getElementById(cnt).value;
     var usr = confirm('Изменить Запись?');
     if(usr){window.location.href = userlink;}
     else{return false;}
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