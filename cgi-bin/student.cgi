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
$emailPattern = '^([a-zA-Z0-9][\w\_\.]{6,20})\@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,4})$';
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$indexcgi = 'student.cgi';
$students_file = $oe_folder . 'students.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpreadcgi = 'http://accelerator.kvadra.kz/cgi-bin/read.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Read-Create-Edit Students';
$glbGenderRusTxt{'Male'} = 'Мужской пол'; $glbGenderRusTxt{'Female'} = 'Женский пол';

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

open(INF, $students_file); 
@studentslist = <INF>; 
close(INF); 
@uniqueSchoolNumList = "";  @uniqueGroupNumList = "";  @studentUniqueNumList = "";
foreach $i(@studentslist){ 
   #"$actNewStudNum<tab>$actNewStudId<tab>$tchildfirstnam<tab>$tchildscndnam<tab>$tchildthrdnam<tab>";
   #"$tchildschl<tab>GroupId-Null<tab>$tchildbrthd<tab>$tchildphn<tab>$tchildclss<tab>$tchildemail<tab>$tchildgndr<tab>$tchildcreated<tab>reserve";
   #1<tab>56BC4567<tab>Томирис<tab>Толенді<tab><tab>71<tab>71-1-M1<tab>reserve
   #$usernum<tab>$userID<tab>$user1stname<tab>$user2ndname<tab>$user3rdname<tab>$userschool<tab>$usergroup<tab>$other
   ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp, 
   $tstudbrthd, $tstudphnm, $tstudclss, $tstudemail, @other) = split (/<tab>/, $i);
   if ( $tstudnum ne '' && $tstudid ne '' ) { 
      if ( $tstudemail =~ /$emailPattern/ ){ $tstudemail = lc $tstudemail; $tstudemail =~s/ //g;
         $studentEmailExist{$tstudemail} = 1; $studentFullName{$tstudemail} = "$tstudfirstnam $tstudthrdnam $tstudscndnam"; }
      if ( $tstudgrp eq '' ) { 
         $studentFirstName{$tstudid} = $tstudfirstnam; $studentSecondName{$tstudid} = $tstudscndnam;
         $studentThirdName{$tstudid} = $tstudthrdnam; push(@emptyGroupList, $tstudid);       }
      $glLastStudentNumber = $tstudnum; $glLastStudentCode = $tstudid; 
   }
   if ( $tstudgrp ne '' && $tstudschl ne '' ) {
      $studentFirstName{$tstudid} = $tstudfirstnam; $studentSecondName{$tstudid} = $tstudscndnam;
      $studentThirdName{$tstudid} = $tstudthrdnam; $studentPositionNum{$tstudid} = $tstudnum; 
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
############### check COOKIES and LOG actions #########################################
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
    if ( $whatis{'action'} eq 'newstudent') { &newStudentPageSub(); }
    elsif ( $whatis{'action'} eq 'open' && $whatis{'groupid'} ne '') { &openGroupPageSub(); }
    elsif ( $whatis{'action'} eq 'add' && $whatis{'groupid'} ne '') { &addNewStudentSub(); }
    elsif ( $whatis{'action'} eq 'delete' && $whatis{'userid'} =~/56BC/) { &deleteStudentSub(); }
    elsif ( $whatis{'action'} eq 'edit' && $whatis{'userid'} =~/56BC/) { &editStudentSub(); }
    elsif ( $whatis{'action'} eq 'save' && $whatis{'userid'} =~/56BC/) { &saveStudentDataSub(); }
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
######################### EDIT STUDENT DATA SUB #####################################
#####################################################################################
sub editStudentSub {     &printjavascript(); 
    print "<h2>Изменение данных учеников</h2>\n"; $essUserFound = 0; $essStyle = "style='height:50px; width:150px'";
    foreach $essLine(@studentslist){ $essChompLine = $essLine; chomp($essChompLine);
       #"$actNewStudNum<tab>$actNewStudId<tab>$tchildfirstnam<tab>$tchildscndnam<tab>$tchildthrdnam<tab>";
       #"$tchildschl<tab>GroupId-Null<tab>$tchildbrthd<tab>$tchildphn<tab>$tchildclss<tab>$tchildemail<tab>$tchildgndr<tab>$tchildcreated<tab>reserve";
       #1<tab>56BC4567<tab>Томирис<tab>Толенді<tab><tab>71<tab>71-1-M1<tab>reserve
       # $glLastStudentNumber<tab>$ansStudentNewCode<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}
       #<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'birthday'}<tab>$whatis{'phonenumber'}
       #<tab>$whatis{'workplace'}<tab>$whatis{'email'}<tab>$whatis{'gender'}<tab>$whatis{'created'}<tab>reserve";
       ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp,
        $tstudbrtd, $tstudphn, $tstudwrkplc, $tstudemail, $tstudgndr, $tstudcrtd, @other) = split (/<tab>/, $essChompLine);
        if ( $tstudid ne '' && $tstudid eq $whatis{'userid'} ) { $tstudemail = lc $tstudemail; $essUserFound = 1;
           $essUserFirstName = $tstudfirstnam; $essUserSecondName = $tstudscndnam; $essUserThirdName = $tstudthrdnam;
           $essUserPlaceNum = $tstudnum; $essUserSchoolId = $tstudschl; $essUserGroupId = $tstudgrp;
           $essUserBirthDay = $tstudbrtd; $essUserPhoneNum = $tstudphn; $essUserWorkPlace = $tstudwrkplc;
           $essUserEmail = $tstudemail; $essUserGender = $tstudgndr; $essUserCreated = $tstudcrtd;
        }
    }
    if ($essUserFound == 1) {
        $essGroupHtmlCode = "<select name = 'groupid'><option value = ''>Выберите группу</option>\n";
        if ( $essUserGroupId ne '' ) { 
        $essGroupHtmlCode = $essGroupHtmlCode . "<option value = \'$essUserGroupId\' selected>$essUserGroupId</option>\n"; }
        foreach $i (@uniqueGroupNumList) { if ($i ne '') { $essGroupHtmlCode = $essGroupHtmlCode . "<option value = \'$i\'>$i</option>\n"; } }
        $essGroupHtmlCode = $essGroupHtmlCode . "</select>\n";   
        $essSchoolHtmlCode = "<select name = 'schoolid'><option value = ''>Выберите школу</option>\n";
        if ( $essUserSchoolId ne '' ) { 
        $essSchoolHtmlCode = $essSchoolHtmlCode . "<option value = \'$essUserSchoolId\' selected>$essUserSchoolId</option>\n"; }
        foreach $i (@uniqueSchoolNumList) { if ($i ne '') { $essSchoolHtmlCode = $essSchoolHtmlCode . "<option value = \'$i\'>$i</option>\n"; } }
        $essSchoolHtmlCode = $essSchoolHtmlCode . "</select>\n";
        print "<form method='post' action=\'$httpindexcgi\' onsubmit='return checkSaveFunction();'>
        <input type = 'hidden' name = 'action' value = 'save'><input type = 'hidden' name = 'userid' value = \'$whatis{'userid'}\'>
        <table><caption><h3>User ID [$whatis{'userid'}]</h3></caption>
        <tr $yelclr><td id=\'$essUserPlaceNum\'>1</td><td>Имя: </td><td><input type = 'text' name = 'firstname' value = \'$essUserFirstName\'></td></tr>
        <tr $yelclr1><td>2</td><td>Фамилия: </td><td><input type = 'text' name = 'secondname' value = \'$essUserSecondName\'></td></tr>
        <tr $yelclr><td>3</td><td>Отчество: </td><td><input type = 'text' name = 'thirdname' value = \'$essUserThirdName\'></td></tr>
        <tr $yelclr1><td>4</td><td>Номер школы: </td><td>$essSchoolHtmlCode</td></tr>
        <tr $yelclr><td>5</td><td>Номер группы:</td><td>$essGroupHtmlCode</td></tr>
        <tr $yelclr1><td>6</td><td>Дата рождения: </td><td><input type = 'text' name = 'birthday' value = \'$essUserBirthDay\'></td></tr>
        <tr $yelclr><td>7</td><td>Номер телефона: </td><td><input type = 'text' name = 'phonenumber' value = \'$essUserPhoneNum\'></td></tr>
        <tr $yelclr1><td>8</td><td>Место учебы/работы: </td><td><input type = 'text' name = 'workplace' value = \'$essUserWorkPlace\'></td></tr>\n";
        if ( $essUserEmail =~ /$emailPattern/ ) { print "<tr $yelclr><td>9</td>
           <td>EMAIL:<input type = 'hidden' name = 'email' value = \'$essUserEmail\'></td>
           <td>$b1 $essUserEmail $rf Email нельзя редактировать! $f2 $b2</td></tr>"; } #$glbGenderRusTxt{'Male'}
        else { print "<tr $yelclr><td>9</td><td>EMAIL:</td><td><input type = 'text' name = 'email' value = ''></td></tr>"; }
        print "<tr $yelclr1><td>10</td><td>Пол ученика: </td><td><select name = 'gender'><option value=''>Выберите пол</option>\n";
        if ( $essUserGender ne '' ) { print "<option value = \'$essUserGender\' selected>$glbGenderRusTxt{$essUserGender}</option>\n"; }
        if ( $essUserCreated eq '' ) { $essUserCreated = $timedatenow; }
        print "<option value='Male'>Мужской пол</option><option value='Female'>Женский пол</option></select></td></tr>
        <tr $yelclr><td>11</td><td>Дата создания: </td><td>$b1 $essUserCreated $b2</td></tr></table> 
        <input type = 'hidden' name = 'created' value = \'$essUserCreated\'>       
        <input type='reset' value = 'ОТМЕНИТЬ' $essStyle>-[-]-[-]-[-]-<input type = 'submit' value = 'ЗАПИСАТЬ' $essStyle></form>
        <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
    }
    else { print "<h3>$rf Неверные данные, запись не найдена! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; }
}
#####################################################################################
######################### SAVE STUDENT DATA SUB #####################################
#####################################################################################
sub saveStudentDataSub { $ssdUserFound = 0; $ssdStyle = "style='height:50px; width:150px'";
   print "<h2>Сохранение данных по ученикам</h2>\n";     
   foreach $ssdLine(@studentslist){ $ssdChompLine = $ssdLine; chomp($ssdChompLine);
      ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp,
      $tstudbrtd, $tstudphn, $tstudwrkplc, $tstudemail, @other) = split (/<tab>/, $ssdChompLine);
      if ( $tstudid ne '' && $tstudid eq $whatis{'userid'} && $ssdUserFound == 0 ) { 
         $ssdUserFound = 1; $ssdUserPlaceNum = $tstudnum; $ssdUserEmail = $tstudemail; }
      elsif ( $ssdUserFound == 0 && $ssdLine ne '' ) { push(@ssdStartStudentsList, $ssdLine); }
      elsif ( $ssdUserFound == 1 && $ssdLine ne '' ) { push(@ssdEndStudentsList, $ssdLine); }
      else { $donothing = 1; }
   }
   if ( $ssdUserFound == 1 ) {  @ssdNewStudentsList = @ssdStartStudentsList; 
      # $glLastStudentNumber<tab>$ansStudentNewCode<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}
      #<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'birthday'}<tab>$whatis{'phonenumber'}
      #<tab>$whatis{'workplace'}<tab>$whatis{'email'}<tab>$whatis{'gender'}<tab>$whatis{'created'}<tab>reserve";
      if ( $ssdUserEmail =~ /$emailPattern/ ) { $whatis{'email'} = $ssdUserEmail; }
      else { if ( $studentEmailExist{$whatis{'email'}} == 1 ) {
            print "<h3>$rf Email: $b1 [$whatis{'email'}]$b2 уже используется учеником $b1 [$studentFullName{$tstudemail}]$b2! $f2</h3>
            <p> </p>\n<p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; return; }       }
      $ssdNewLineText = "$ssdUserPlaceNum<tab>$whatis{'userid'}<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}";
      $ssdNewLineText = $ssdNewLineText . "<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'birthday'}<tab>$whatis{'phonenumber'}";
      $ssdNewLineText = $ssdNewLineText . "<tab>$whatis{'workplace'}<tab>$whatis{'email'}<tab>$whatis{'gender'}<tab>$whatis{'created'}<tab>reserve\n";
      push(@ssdNewStudentsList, $ssdNewLineText); push(@ssdNewStudentsList, @ssdEndStudentsList);
      open(SSDATA,">$students_file");
      foreach $i (@ssdNewStudentsList) {       if ( $i ne '' ) { print SSDATA $i; }       }
      close(SSDATA);
      print "<table $grnclr><tr><td><h2>Данные изменения внесены в систему.</h2></td></tr></table>
      <p> </p><table><caption><h3>User ID [$whatis{'userid'}]</h3></caption>
      <tr $yelclr><td>1</td><td id = \'$whatis{'userid'}\'>Имя: </td><td>$whatis{'firstname'}</td></tr>
      <tr $yelclr1><td>2</td><td>Фамилия: </td><td>$whatis{'secondname'}</td></tr>
      <tr $yelclr><td>3</td><td>Отчество: </td><td>$whatis{'thirdname'}</td></tr>
      <tr $yelclr1><td>4</td><td>Номер школы: </td><td>$whatis{'schoolid'}</td></tr>
      <tr $yelclr><td>5</td><td>Номер группы:</td><td>$whatis{'groupid'}</td></tr>
      <tr $yelclr1><td>6</td><td>Дата рождения: </td><td>$whatis{'birthday'}</td></tr>
      <tr $yelclr><td>7</td><td>Номер телефона: </td><td>$whatis{'phonenumber'}</td></tr>
      <tr $yelclr1><td>8</td><td>Место учебы/работы: </td><td>$whatis{'workplace'}</td></tr>
      <tr $yelclr><td>9</td><td>EMAIL: </td><td>$whatis{'email'}</td></tr> 
      <tr $yelclr1><td>10</td><td>Пол ученика: </td><td>$glbGenderRusTxt{$whatis{'gender'}}</td></tr>
      <tr $yelclr><td>11</td><td>Дата создания: </td><td>$whatis{'created'}</td></tr></table>
      <p> </p><p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
   } #$glbGenderRusTxt{'Male'}
   else { print "<h3>$rf Неверные данные, запись не найдена! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; } 
}
#####################################################################################
####################### DELETE STUDENT DATA SUB #####################################
#####################################################################################
sub deleteStudentSub {
   print "<h2>Удаление данных ученика</h2>\n";  $dssUserFound = 0; $dssStyle = "style='height:50px; width:150px'";
   foreach $dssLine(@studentslist){ $dssChompLine = $dssLine; chomp($dssChompLine);
      ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp,
      $tstudbrtd, $tstudphn, $tstudwrkplc, $tstudemail, $tstudgndr, $tstudcrtd, @other) = split (/<tab>/, $dssChompLine);
      if ( $tstudid ne '' && $tstudid eq $whatis{'userid'} && $dssUserFound == 0 ) { $dssUserFound = 1;
         $dssUserFirstName = $tstudfirstnam; $dssUserSecondName = $tstudscndnam; $dssUserThirdName = $tstudthrdnam;
         $dssUserPlaceNum = $tstudnum; $dssUserSchoolId = $tstudschl; $dssUserGroupId = $tstudgrp;
         $dssUserBirthDay = $tstudbrtd; $dssUserPhoneNum = $tstudphn; $dssUserWorkPlace = $tstudwrkplc;
         $dssUserEmail = $tstudemail; $dssUserGender = $tstudgndr; $dssUserCreated = $tstudcrtd;
         # $glLastStudentNumber<tab>$ansStudentNewCode<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}
         #<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'birthday'}<tab>$whatis{'phonenumber'}
         #<tab>$whatis{'workplace'}<tab>$whatis{'email'}<tab>$whatis{'gender'}<tab>$whatis{'created'}<tab>reserve";
         $dssNewLineText = "$dssUserPlaceNum<tab>$whatis{'userid'}<tab>$dssUserFirstName<tab>$dssUserSecondName<tab>$dssUserThirdName";
         $dssNewLineText = $dssNewLineText . "<tab><tab><tab>$dssUserBirthDay<tab>$dssUserPhoneNum<tab>$dssUserWorkPlace";
         $dssNewLineText = $dssNewLineText . "<tab>$dssUserEmail<tab>$dssUserGender<tab>$dssUserCreated<tab>reserve\n";
      }
      elsif ( $dssUserFound == 0 && $dssLine ne '' ) { push(@dssStartStudentsList, $dssLine); }
      elsif ( $dssUserFound == 1 && $dssLine ne '' ) { push(@dssEndStudentsList, $dssLine); }
      else { $donothing = 1; }
   }
   if ( $dssUserFound == 1 ) {        @dssNewStudentsList = @dssStartStudentsList; 
       push(@dssNewStudentsList, $dssNewLineText); push(@dssNewStudentsList, @dssEndStudentsList);
       open(DSSDATA,">$students_file");
       foreach $i (@dssNewStudentsList) {          if ( $i ne '' ) { print DSSDATA $i; }       }
       close(DSSDATA);
       print "<table $grnclr><tr><td><h2>Удалены записи ученика со следующими данными</h2></td></tr></table>
        <p> </p><table><caption><h3>User ID [$whatis{'userid'}]</h3></caption>
        <tr $yelclr><td>1</td><td id = \'$whatis{'userid'}\'>Имя: </td><td>$dssUserFirstName</td></tr>
        <tr $yelclr1><td>2</td><td>Фамилия: </td><td>$dssUserSecondName</td></tr>
        <tr $yelclr><td>3</td><td>Отчество: </td><td>$dssUserThirdName</td></tr>
        <tr $yelclr1><td>4</td><td>Дата рождения: </td><td>$dssUserBirthDay</td></tr>
        <tr $yelclr><td>5</td><td>Номер телефона: </td><td>$dssUserPhoneNum</td></tr>
        <tr $yelclr1><td>6</td><td>Место учебы/работы: </td><td>$dssUserWorkPlace</td></tr>
        <tr $yelclr><td>7</td><td>EMAIL: </td><td>$dssUserEmail</td></tr>
        <tr $yelclr1><td>8</td><td>Пол ученика: </td><td>$glbGenderRusTxt{$dssUserGender}</td></tr>
        <tr $yelclr><td>9</td><td>Дата создания: </td><td>$dssUserCreated</td></tr></table>
        <p> </p><p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
   } #$glbGenderRusTxt{'Male'}
   else { print "<h3>$rf Неверные данные, запись не найдена! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; } 

}
#####################################################################################
########################### OPEN GROUP PAGE SUB #####################################
#####################################################################################
sub openGroupPageSub {
    &printjavascript(); $myclr = $yelclr; $cnt = 1;
    print "<h2>Изменение данных учеников</h2>\n <p>Список учеников школы № [$whatis{'schoolid'}] и группы № [$whatis{'groupid'}]</p>
    <table><tr $myclr><td>No</td><td>ID</td><td>ФИО</td><td>Редактировать данные</td><td>Удалить</td></tr>\n";
    if ( $whatis{'groupid'} eq 'empty') {
        foreach $ogpStdId (@emptyGroupList) {
            if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; }
            print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$ogpStdId\'></td><td>[$ogpStdId]</td>
            <td>$studentFirstName{$ogpStdId} $studentThirdName{$ogpStdId} $studentSecondName{$ogpStdId}</td>
            <td><button onclick=\"return checkEditFunction\($cnt\)\;\" $bpsStyle>Редактировать</button> запись ученика</td>
            <td><button onclick=\"return checkDeleteFunction\($cnt\)\;\" $bpsStyle>Удалить запись ученика</button></td></tr>\n"; 
            $cnt++;
        }
    }
    else{
        foreach $ogpStdId (@studentUniqueNumList) {
           if ( $studentGroupNum{$ogpStdId} =~ $whatis{'groupid'} ) {
              if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; }
              print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$ogpStdId\'></td><td>[$ogpStdId]</td>
              <td>$studentFirstName{$ogpStdId} $studentThirdName{$ogpStdId} $studentSecondName{$ogpStdId}</td>
              <td><button onclick=\"return checkEditFunction\($cnt\)\;\" $bpsStyle>Редактировать</button> запись ученика</td>
              <td><button onclick=\"return checkDeleteFunction\($cnt\)\;\" $bpsStyle>Удалить запись ученика</button></td></tr>\n"; 
              $cnt++;
           } # checkEditFunction
        }
    }
    print "</table>\n <p> </p> <a href=\'$httpindexcgi\'>[ Вернуться НАЗАД ]</a>\n"; 
}
#####################################################################################
########################### ADD NEW STUDENT SUB #####################################
#####################################################################################
sub addNewStudentSub {
    if ( $whatis{'firstname'} eq '' ) { push(@ansErrorsList, 'Имя не указано. '); $ansErrorsExist = 1; }
    if ( $whatis{'secondname'} eq '' ) { push(@ansErrorsList, 'Фамилия не указана. '); $ansErrorsExist = 1; }
    if ( $whatis{'schoolid'} eq '' ) { push(@ansErrorsList, 'Номер школы не указан. '); $ansErrorsExist = 1; }
    if ( $whatis{'groupid'} eq '' ) { push(@ansErrorsList, 'Номер группы не указан. '); $ansErrorsExist = 1; }
    if ( $whatis{'birthday'} eq '' ) { push(@ansErrorsList, 'Дата рождения не указано. '); $ansErrorsExist = 1; }
    if ( $whatis{'phonenumber'} eq '' ) { push(@ansErrorsList, 'Номер телефона не указан. '); $ansErrorsExist = 1; }
    if ( $whatis{'workplace'} eq '' ) { push(@ansErrorsList, 'Место учебы/работы не указано. '); $ansErrorsExist = 1; }
    if ( $whatis{'email'} !~ /$emailPattern/ || $whatis{'email'} eq '' ) { push(@ansErrorsList, 'Email неверный. '); $ansErrorsExist = 1; }
    if ( $studentEmailExist{$whatis{'email'}} == 1 ) { push(@ansErrorsList, 'Email уже использется. '); $ansErrorsExist = 1; }
    if ( $whatis{'gender'} eq '' ) { push(@ansErrorsList, 'Пол ученика не указан. '); $ansErrorsExist = 1; }
    if ( $ansErrorsExist == 1 ) {
        print "<h3>$rf Неверные данные, запись не возможна! $f2</h3><table><caption>Перечень обнаруженных ошибок</caption>";
        foreach $ansErr (@ansErrorsList) { 
            if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; }
            print "<tr $myclr><td>$ansErr</td></tr>\n"; 
        }
        print "</table>\n <p><a href=\'$httpindexcgi\?action=newstudent\'>Вернуться НАЗАД</a></p>\n"; 
    }
    else { #  1<tab>56BC4567<tab>Томирис<tab>Толенді<tab><tab>71<tab>71-1-M1<tab>reserve     $glLastStudentNumber = $tstudnum; $glLastStudentCode = $tstudid;
        ($ansStudentFirstCode, $ansStudentLastCode) = split (/BC/, $glLastStudentCode); $glLastStudentNumber++;
        $ansStudentLastCode++; $ansStudentNewCode = $ansStudentFirstCode . 'BC' . $ansStudentLastCode;
        # $glLastStudentNumber<tab>$ansStudentNewCode<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}
        #<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'birthday'}<tab>$whatis{'phonenumber'}
        #<tab>$whatis{'workplace'}<tab>$whatis{'email'}<tab>$whatis{'gender'}<tab>$whatis{'created'}<tab>reserve";
        $ansNewLineText = "$glLastStudentNumber<tab>$ansStudentNewCode<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}";
        $ansNewLineText = $ansNewLineText . "<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'birthday'}<tab>$whatis{'phonenumber'}";
        $ansNewLineText = $ansNewLineText . "<tab>$whatis{'workplace'}<tab>$whatis{'email'}<tab>$whatis{'gender'}<tab>$timedatenow<tab>reserve";
        open(ANSDATA,">>$students_file");
        print ANSDATA "\n";
        print ANSDATA $ansNewLineText;
        close(ANSDATA);
        print "<table $grnclr><tr><td><h2>Добавлен ученик со следующими данными</h2></td></tr></table>
        <p> </p><table><caption><h3>User ID [$whatis{'userid'}]</h3></caption>
        <tr $yelclr><td>1</td><td>Имя: </td><td>$whatis{'firstname'}</td></tr>
        <tr $yelclr1><td>2</td><td>Фамилия: </td><td>$whatis{'secondname'}</td></tr>
        <tr $yelclr><td>3</td><td>Отчество: </td><td>$whatis{'thirdname'}</td></tr>
        <tr $yelclr1><td>4</td><td>Номер школы: </td><td>$whatis{'schoolid'}</td></tr>
        <tr $yelclr><td>5</td><td>Номер группы:</td><td>$whatis{'groupid'}</td></tr>
        <tr $yelclr1><td>6</td><td>Дата рождения: </td><td>$whatis{'birthday'}</td></tr>
        <tr $yelclr><td>7</td><td>Номер телефона: </td><td>$whatis{'phonenumber'}</td></tr>
        <tr $yelclr1><td>8</td><td>Место учебы/работы: </td><td>$whatis{'workplace'}</td></tr>
        <tr $yelclr><td>9</td><td>EMAIL: </td><td>$whatis{'email'}</td></tr>
        <tr $yelclr1><td>10</td><td>Пол ученика: </td><td>$glbGenderRusTxt{$whatis{'gender'}}</td></tr>
        <tr $yelclr><td>11</td><td>Дата создания: </td><td>$timedatenow</td></tr></table>
        <p> </p><p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
    } 
}
#####################################################################################
########################## NEW STUDENT PAGE SUB #####################################
#####################################################################################
sub newStudentPageSub { &printjavascript();   $nspsStyle = "style='height:50px; width:150px'";
print "<h2>Добавление нового ученика</h2>\n <p>Заполните поля для записи нового ученика. $rf * Required $f2 </p>
<form method='post' action=\'$httpindexcgi\' onsubmit='return checkAllFunction();'><input type = 'hidden' name = 'action' value = 'add'>
<table><tr $yelclr><td>Имя $rf * $f2</td><td><input type='text' name='firstname' value=''></td></tr>
<tr $yelclr1><td>Фамилия $rf * $f2</td><td><input type='text' name='secondname' value=''></td></tr>
<tr $yelclr><td>Отчество</td><td><input type='text' name='thirdname' value=''></td></tr>
<tr $yelclr1><td>Номер школы $rf * $f2</td><td><input type='text' name='schoolid' value=''> </td></tr>
<tr $yelclr><td>Номер группы $rf * $f2</td><td><table><tr><td>Выберите номер группы: <select name='groupnumber'><option value='1'>1</option>
<option value='2'>2</option><option value='3'>3</option><option value='4'>4</option><option value='5'>5</option><option value='6'>6</option>
<option value='7'>7</option><option value='8'>8</option><option value='9'>9</option><option value='10'>10</option><option value='11'>11</option>
<option value='12'>12</option><option value='13'>13</option><option value='14'>14</option><option value='15'>15</option></select></td></tr><tr>
<td>Выберите номер модуля: <select name='modulenumber'><option value='M0'>M0</option><option value='M1'>M1</option><option value='M2'>M2</option>
<option value='M3'>M3</option></select></td></tr><tr><td>Модуль платный или нет? : <select name='modulepaid'><option value='paid'>Платный</option>
<option value='pilot'>Пилот</option></select><input type='hidden' name='groupid' value=''></td></tr></table></td></tr>
<tr $yelclr1><td>Дата рождения $rf * $f2</td><td><input type='text' name='birthday' value=''> DD.MM.YYYY</td></tr>
<tr $yelclr><td>Номер телефона $rf * $f2</td><td><input type='text' name='phonenumber' value=''> 8 7XX ABC XXXX</td></tr>
<tr $yelclr1><td>Место учебы/работы $rf * $f2</td><td><input type='text' name='workplace' value=''> </td></tr>
<tr $yelclr><td>EMAIL $rf * $f2</td><td><input type='text' name='email' value=''></td></tr>
<tr $yelclr1><td>Пол ученика $rf * $f2</td><td><select name = 'gender'><option value=''>Выберите пол</option>
<option value='Male'>Мужской пол</option><option value='Female'>Женский пол</option></select></td></tr>
<tr $yelclr><td><input type='reset' value = 'ОБНУЛИТЬ' $nspsStyle></td>
<td><input type = 'submit' value = 'СОЗДАТЬ' $nspsStyle></td></tr>
</table></form> <p> </p>\n<p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";
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
  print "<option value = 'empty'>Ученики без группы</option></select></td><td><p id = 'myGroupList'></p></td></tr>
  <tr $yelclr><td><input type = 'hidden' name = 'action' value = 'open'>
  <input type='reset' value = 'ОТМЕНИТЬ' $bpsStyle></td><td><input type = 'submit' value = 'ОТКРЫТЬ' $bpsStyle></td></tr></table></form>
  <button onclick=\"window.location.href = \'$httpindexcgi\?action=newstudent\'\;\" $bpsStyle>Добавить Нового Ученика</button>\n";
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
print  <<EOT;
 <script>
 function checkAllFunction (){
   if(document.getElementsByName('firstname')[0].value == ''){alert('Укажите имя!'); return false;}
   if(document.getElementsByName('secondname')[0].value == ''){alert('Укажите фамилию!'); return false;}
   if(document.getElementsByName('schoolid')[0].value == ''){alert('Укажите номер школы!'); return false;}
   if(document.getElementsByName('birthday')[0].value == ''){alert('Укажите дату рождения!'); return false;}
   if(document.getElementsByName('phonenumber')[0].value == ''){alert('Укажите номер телефона!'); return false;}
   if(document.getElementsByName('workplace')[0].value == ''){alert('Укажите место учебы или работы!'); return false;}
   if(document.getElementsByName('email')[0].value == ''){alert('Укажите EMAIL!'); return false;}
   if(document.getElementsByName('gender')[0].value == ''){alert('Выберите пол!'); return false;}
   var myGrpPaid = document.getElementsByName('modulepaid')[0].value; if(myGrpPaid == 'paid'){myGrpPaid = '';} else{myGrpPaid = '-P';}
   var myGroupNum = document.getElementsByName('schoolid')[0].value + '-' 
   + document.getElementsByName('groupnumber')[0].value + '-' + document.getElementsByName('modulenumber')[0].value + myGrpPaid;
   document.getElementsByName('groupid')[0].value = myGroupNum;
 }
 function checkDeleteFunction (cnt) {
     var userlink = \'$httpindexcgi\?action=delete\&userid=' + document.getElementById(cnt).value;
     var usr = confirm('УДАЛИТЬ ЗАПИСЬ?');
     if(usr){window.location.href = userlink;}
     else{return false;}
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
     if ( mySchoolId == 'empty' ) { GroupText = '<select name = "groupid"><option value = "empty">Ученики без группы</option></select>'; }
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