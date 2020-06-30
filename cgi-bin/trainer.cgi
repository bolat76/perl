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
$emailPattern = '^([a-zA-Z0-9][\w\_\.]{6,20})\@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,4})$';
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$indexcgi = 'trainer.cgi';
$students_file = $oe_folder . 'students.txt';
$trainers_file = $oe_folder . 'trainers.txt';
$trainersdata_file = $oe_folder . 'trainersdata.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpreadcgi = 'http://accelerator.kvadra.kz/cgi-bin/read.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Read-Create-Edit Trainers';

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

open(INF, $trainers_file); 
@trainerslist = <INF>; 
close(INF); 
foreach $i(@trainerslist){
   # No<tab>Uniques ID<tab>1st name<tab>2nd name<tab>3rd name<tab>PWD<tab>Phone Num<tab>Email<tab>Date<tab>Reserve
   #$trnrnum<tab>$trnrID<tab>$trnr1stname<tab>$trnr2ndname<tab>$trnr3rdname<tab>$trnrpwd<tab>$usergroup<tab>$other
   ($ttrnrnum, $ttrnrid, $ttrnrfirstnam, $ttrnrscndnam, $ttrnrthrdnam, $ttrnrpwd, $ttrnrphn, $ttrnremail, @other) = split (/<tab>/, $i);
   if ( $ttrnrnum ne '' && $ttrnrid ne '' ) { $glLastTrainerNumber = $ttrnrnum; $glLastTrainerCode = $ttrnrid; }
   if($ttrnrid ne ''){  $TrainerFullName{$ttrnrid} = "$ttrnrfirstnam $ttrnrscndnam $ttrnrthrdnam"; $ttrnremail = lc $ttrnremail;
      $TrainerUniqueId{$ttrnrid} = $ttrnrid; $TrainerFirstName{$ttrnrid} = $ttrnrfirstnam; $TrainerSecondName{$ttrnrid} = $ttrnrscndnam;
      $TrainerThirdName{$ttrnrid} = $ttrnrthrdnam; $TrainerPositionNum{$ttrnrid} = $ttrnrnum; $TrainerPhoneNum{$ttrnrid} = $ttrnrphn; 
      $TrainerEmail{$ttrnrid} = $ttrnremail; $TrainerPwd{$ttrnrid} = $ttrnrpwd; push(@globalTrainersList, $ttrnrid); $totalTrainers++;
   }
}  # $existSchool{$ttrnrschl}; $existGroup{$ttrnrgrp}; $GroupsPerSchool{$ttrnrschl}; $totalTrainers ;$totalSchools; $totalGroups

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
############### check COOKIES and LOG actions #########################################
#######################################################################################
if ( $whatis{'email'} ne '' ) { $whatis{'email'} = lc $whatis{'email'};  $whatis{'email'} =~s/ //g; }
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
    if ( $whatis{'action'} eq 'newtrainer' ) { &newTrainerSub(); }
    elsif ( $whatis{'action'} eq 'edit' && $whatis{'userid'} =~/44TR/) { &editTrainerSub(); }
    elsif ( $whatis{'action'} eq 'save') { &saveTrainerDataSub(); }
    else { &openGroupPageSub() ; }
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
############################### NEW TRAINER SUB #####################################
#####################################################################################
sub newTrainerSub { $ntsStyle = "style='height:50px; width:150px'"; &printjavascript();
   print "<form method='post' action=\'$httpindexcgi\' onsubmit='return checkAllFunction();'>
   <input type = 'hidden' name = 'action' value = 'save'>
   <table><tr $yelclr><td>1</td><td>Имя: </td><td><input type = 'text' name = 'firstname' value = ''></td></tr>
   <tr $yelclr1><td>2</td><td>Фамилия: </td><td><input type = 'text' name = 'secondname' value = ''></td></tr>
   <tr $yelclr><td>3</td><td>Отчество: </td><td><input type = 'text' name = 'thirdname' value = ''></td></tr>
   <tr $yelclr1><td>4</td><td>Группа №1: </td><td><select name = 'grouponeid'><option value = ''>Выберите группу</option>\n";
   foreach $i (@uniqueGroupNumList) { if ($i ne '') { print "<option value = \'$i\'>$i</option>\n"; } }
   print "</select></td></tr>
   <tr $yelclr><td>5</td><td>Группа №2: </td><td><select name = 'grouptwoid'><option value = ''>Выберите группу</option>\n";
   foreach $i (@uniqueGroupNumList) { if ($i ne '') { print "<option value = \'$i\'>$i</option>\n"; } }
   print "</select></td></tr>
   <tr $yelclr1><td>6</td><td>Группа №3: </td><td><select name = 'grouptriid'><option value = ''>Выберите группу</option>\n";
   foreach $i (@uniqueGroupNumList) { if ($i ne '') { print "<option value = \'$i\'>$i</option>\n"; } }
   print "</select></td></tr>
   <tr $yelclr><td>7</td><td>Группа №4: </td><td><select name = 'groupfourid'><option value = ''>Выберите группу</option>\n";
   foreach $i (@uniqueGroupNumList) { if ($i ne '') { print "<option value = \'$i\'>$i</option>\n"; } }
   print "</select></td></tr>
   <tr $yelclr1><td>8</td><td>Группа №5: </td><td><select name = 'groupfiveid'><option value = ''>Выберите группу</option>\n";
   foreach $i (@uniqueGroupNumList) { if ($i ne '') { print "<option value = \'$i\'>$i</option>\n"; } }
   print "</select></td></tr>
   <tr $yelclr><td>9</td><td>Группа №6: </td><td><select name = 'groupsixid'><option value = ''>Выберите группу</option>\n";
   foreach $i (@uniqueGroupNumList) { if ($i ne '') { print "<option value = \'$i\'>$i</option>\n"; } }
   print "</select></td></tr>\n"; 
   print "<tr $yelclr1><td>10</td><td>Номер телефона: </td><td><input type = 'text' name = 'phonenumber' value = ''></td></tr>
   <tr $yelclr><td>7</td><td>EMAIL: </td><td><input type = 'text' name = 'email' value = ''></td></tr></table>
   <input type='reset' value = 'ОТМЕНИТЬ' $ntsStyle>-[-]-[-]-[-]-<input type = 'submit' value = 'ЗАПИСАТЬ' $ntsStyle></form>
   <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
}

#####################################################################################
######################### EDIT TRAINER DATA SUB #####################################
#####################################################################################
sub editTrainerSub {
   # No<tab>Uniques ID<tab>1st name<tab>2nd name<tab>3rd name<tab>PWD<tab>School ID<tab>Group ID<tab>Phone Num<tab>Email<tab>Date<tab>Reserve
   $etsGroupName{'1'} = 'grouponeid'; $etsGroupName{'2'} = 'grouptwoid'; $etsGroupName{'3'} = 'grouptriid';
   $etsGroupName{'4'} = 'groupfourid'; $etsGroupName{'5'} = 'groupfiveid'; $etsGroupName{'6'} = 'groupsixid';
   $etsGroupName{'7'} = 'groupsvnid'; $etsGroupName{'8'} = 'groupeitid'; $etsGroupName{'9'} = 'groupnineid';
   $etsGroupName{'10'} = 'grouptenid'; $etsGroupName{'11'} = 'grouplvnid'; $etsGroupName{'12'} = 'grouptwlid';
   &printjavascript(); $etsTrnrId = $whatis{'userid'};  $cnt = 1; $trcnt = 0; $etsStyle = "style='height:50px; width:150px'";
   if( $etsTrnrId =~ /44TR/ ){
       print "<h2>Изменение данных тренеров</h2> <form method='post' action=\'$httpindexcgi\' onsubmit='return checkAllFunction();'>
       <input type = 'hidden' name = 'action' value = 'save'><input type = 'hidden' name = 'userid' value = \'$whatis{'userid'}\'>
       <table><caption><h3>$TrainerFullName{$etsTrnrId} ID:[$etsTrnrId]</h3></caption>
       <tr $yelclr><td>1</td><td>Имя: </td><td><input type = 'text' name = 'firstname' value = \'$TrainerFirstName{$etsTrnrId}\'></td></tr>
       <tr $yelclr1><td>2</td><td>Фамилия: </td><td><input type = 'text' name = 'secondname' value = \'$TrainerSecondName{$etsTrnrId}\'></td></tr>
       <tr $yelclr><td>3</td><td>Отчество: </td><td><input type = 'text' name = 'thirdname' value = \'$TrainerThirdName{$etsTrnrId}\'></td></tr>
       <tr $yelclr1><td>4</td><td>Номер телефона: </td><td><input type = 'text' name = 'phonenumber' value = \'$TrainerPhoneNum{$etsTrnrId}\'></td></tr>\n";
       if ( $TrainerEmail{$etsTrnrId} =~ /$emailPattern/ ) { $etsEmailTxt = "<input type = 'hidden' name = 'oldemail' value = 'true'>\n";
          $etsEmailTxt = $etsEmailTxt . "<input type = 'hidden' name = 'email' value = \'$TrainerEmail{$etsTrnrId}\'> $b1 $TrainerEmail{$etsTrnrId} $b2"; }
       else { $etsEmailTxt = "<input type = 'text' name = 'email' value = ''>\n<input type = 'hidden' name = 'oldemail' value = 'false'>\n"; }
       print "<tr $yelclr><td>5</td><td>EMAIL: </td><td>$etsEmailTxt</td></tr>\n";
       open(INF, $trainersdata_file); @trainersDataList = <INF>; close(INF); $myclr = $yelclr;
       foreach $i(@trainersDataList) { #4<tab>44TR4701<tab>75-1-M1<tab>19.06.19<tab>reserve
          ($ttrnrnum, $ttrnrid, $ttrnrgrp, $ttrnrday, @other) = split (/<tab>/, $i); 
          if ( $ttrnrid eq $etsTrnrId && $cnt < 13) {  $trcnt = $cnt + 5;
             if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
             print "<tr $myclr><td>$trcnt</td><td>Группа \№$cnt: </td><td><select name = \'$etsGroupName{$cnt}\'>";
             if ( $ttrnrgrp ne '' ) { print "<option value = \'$ttrnrgrp\' selected>$ttrnrgrp</option>\n"; }
             foreach $i (@uniqueGroupNumList) { if ($i ne '') { print "<option value = \'$i\'>$i</option>\n"; } }
             print "<option value = ''>Выберите группу</option></select></td></tr>\n"; $cnt++;
          }
       } 
       while ( $cnt < 7 ) { $trcnt = $cnt + 5;
          if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
          print "<tr $myclr><td>$trcnt</td><td>Группа \№$cnt: </td><td><select name = \'$etsGroupName{$cnt}\'>\n";
          print "<option value = ''>Выберите группу</option>\n";
          foreach $i (@uniqueGroupNumList) { if ($i ne '') { print "<option value = \'$i\'>$i</option>\n"; } }
          print "</select></td></tr>\n"; $cnt++; 
       }
       print "</table><input type='reset' value = 'ОТМЕНИТЬ' $etsStyle>-[-]-[-]-[-]-<input type = 'submit' value = 'ЗАПИСАТЬ' $etsStyle></form>
       <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";   
   }
   else { print "<h3>$rf Неверные данные, запись не найдена! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; }
}
#####################################################################################
########################## SAVE TRAINER DATA SUB #####################################
#####################################################################################
sub saveTrainerDataSub { 
   if ( $whatis{'firstname'} eq '' || $whatis{'secondname'} eq '' || $whatis{'phonenumber'} eq '' || $whatis{'email'} eq '' ) { 
      print "<h3>$rf Неверные данные! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; return; 
   }
   print "<h2>Сохранение данных по тренерам</h2>\n";  $stdTrainerFound = 0; $stdTrnrId = $whatis{'userid'};
   foreach $stdLine(@trainerslist){
      ($ttrnrnum, $ttrnrid, @other) = split (/<tab>/, $stdLine);
      if ( $ttrnrid eq $stdTrnrId && $stdTrainerFound == 0 ) { $stdTrainerFound = 1; $stdTrainerPlaceNum = $ttrnrnum; }
      elsif ( $stdTrainerFound == 0 && $stdLine ne '' ) { push(@stdStartTrainersList, $stdLine); }
      elsif ( $stdTrainerFound == 1 && $stdLine ne '' ) { push(@stdEndTrainersList, $stdLine); }
      else { $donothing = 1; }
   } 
   if ( $stdTrainerFound == 1 ) { $stdTrainerId = $TrainerUniqueId{$stdTrnrId}; $stdTrnrPwd = $TrainerPwd{$stdTrnrId}; }
   else { 
      ($stdTrainerOldPlaceNum, $stdTrainerOldId) = split (/44TR/, $glLastTrainerCode); $stdTrnrPwd = '1';
      $stdTrainerOldId++; $stdTrainerId = '44TR' . $stdTrainerOldId; $stdTrainerPlaceNum = $glLastTrainerNumber + 1;
   } #No<tab>Uniques ID<tab>1st name<tab>2nd name<tab>3rd name<tab>PWD<tab>Phone Num<tab>Email<tab>Date<tab>Reserve
   if ( $TrainerPwd{$ttrnrid} ne '' ) {  }
   
   $stdNewLineText = "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}";
   $stdNewLineText = $stdNewLineText . "<tab>$stdTrnrPwd<tab>$whatis{'phonenumber'}<tab>$whatis{'email'}<tab>$datenow<tab>reserve\n";
   open(SSDATA,">$trainers_file");   print SSDATA @stdStartTrainersList;   print SSDATA $stdNewLineText;
   if ( $stdTrainerFound == 1 ) { print SSDATA @stdEndTrainersList; }   close(SSDATA);
   open(INF, $trainersdata_file); @trainersDataList = <INF>; close(INF); $stdTrainerFound = 0;
   foreach $stdLine(@trainersDataList) { #1<tab>44TR4701<tab>99-1-M1<tab>19.06.19<tab>reserve
      ($ttrnrnum, $ttrnrid, @other) = split (/<tab>/, $stdLine);
      if ( $ttrnrid =~ /44TR/ ) { $stdTranerDataLastNum = $ttrnrnum; }
      if ( $ttrnrid eq $stdTrnrId ) { $donothing = 1; }
      else { push(@stdTrainersDataList, $stdLine); }
   }  #1<tab>44TR4701<tab>99-1-M1<tab>19.06.19<tab>reserve
   $stdTrainerPlaceNum = $stdTranerDataLastNum; $stdDataLineText = '';
   if( $whatis{'grouponeid'} ne '' ) { $stdTrainerPlaceNum++;
      $stdDataLineText = $stdDataLineText . "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'grouponeid'}<tab>$datenow<tab>reserve\n"; 
   }
   if( $whatis{'grouptwoid'} ne '' ) { $stdTrainerPlaceNum++;
      $stdDataLineText = $stdDataLineText . "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'grouptwoid'}<tab>$datenow<tab>reserve\n"; 
   }
   if( $whatis{'grouptriid'} ne '' ) { $stdTrainerPlaceNum++;
      $stdDataLineText = $stdDataLineText . "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'grouptriid'}<tab>$datenow<tab>reserve\n"; 
   }
   if( $whatis{'groupfourid'} ne '' ) { $stdTrainerPlaceNum++;
      $stdDataLineText = $stdDataLineText . "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'groupfourid'}<tab>$datenow<tab>reserve\n"; 
   }
   if( $whatis{'groupfiveid'} ne '' ) { $stdTrainerPlaceNum++;
      $stdDataLineText = $stdDataLineText . "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'groupfiveid'}<tab>$datenow<tab>reserve\n"; 
   }
   if( $whatis{'groupsixid'} ne '' ) { $stdTrainerPlaceNum++;
      $stdDataLineText = $stdDataLineText . "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'groupsixid'}<tab>$datenow<tab>reserve\n"; 
   }
   if( $whatis{'groupsvnid'} ne '' ) { $stdTrainerPlaceNum++; $stdTxtSvnLine = "<tr><td>12</td><td>Номер группы 7:</td><td>$whatis{'groupsvnid'}</td></tr>";
      $stdDataLineText = $stdDataLineText . "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'groupsvnid'}<tab>$datenow<tab>reserve\n"; 
   }
   if( $whatis{'groupeitid'} ne '' ) { $stdTrainerPlaceNum++; $stdTxtEitLine = "<tr><td>12</td><td>Номер группы 8:</td><td>$whatis{'groupeitid'}</td></tr>";
      $stdDataLineText = $stdDataLineText . "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'groupeitid'}<tab>$datenow<tab>reserve\n"; 
   }
   if( $whatis{'groupnineid'} ne '' ) { $stdTrainerPlaceNum++; $stdTxtNinLine = "<tr><td>12</td><td>Номер группы 9:</td><td>$whatis{'groupnineid'}</td></tr>";
      $stdDataLineText = $stdDataLineText . "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'groupnineid'}<tab>$datenow<tab>reserve\n"; 
   }
   if( $whatis{'grouptenid'} ne '' ) { $stdTrainerPlaceNum++; $stdTxtTenLine = "<tr><td>12</td><td>Номер группы 10:</td><td>$whatis{'grouptenid'}</td></tr>";
      $stdDataLineText = $stdDataLineText . "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'grouptenid'}<tab>$datenow<tab>reserve\n"; 
   }
   if( $whatis{'grouplvnid'} ne '' ) { $stdTrainerPlaceNum++; $stdTxtLvnLine = "<tr><td>12</td><td>Номер группы 11:</td><td>$whatis{'grouplvnid'}</td></tr>";
      $stdDataLineText = $stdDataLineText . "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'grouplvnid'}<tab>$datenow<tab>reserve\n"; 
   }
   if( $whatis{'grouptwlid'} ne '' ) { $stdTrainerPlaceNum++; $stdTxtTwlLine = "<tr><td>12</td><td>Номер группы 12:</td><td>$whatis{'grouptwlid'}</td></tr>";
      $stdDataLineText = $stdDataLineText . "$stdTrainerPlaceNum<tab>$stdTrainerId<tab>$whatis{'grouptwlid'}<tab>$datenow<tab>reserve\n"; 
   }
   open(SSDATA,">$trainersdata_file");   print SSDATA @stdTrainersDataList;   
   if ( $stdDataLineText ne '' ) { print SSDATA $stdDataLineText; }
   close(SSDATA);
   
   print "<table $grnclr><tr><td><h2>Данные изменения внесены в систему.</h2></td></tr></table>
   <p> </p><table><caption><h3>Trainer ID [$stdTrainerId]</h3></caption>
   <tr $yelclr><td>1</td><td>Имя тренера: </td><td>$whatis{'firstname'}</td></tr>
   <tr $yelclr1><td>2</td><td>Фамилия тренера: </td><td>$whatis{'secondname'}</td></tr>
   <tr $yelclr><td>3</td><td>Отчество тренера: </td><td>$whatis{'thirdname'}</td></tr>
   <tr $yelclr1><td>4</td><td>Номер телефона: </td><td>$whatis{'phonenumber'}</td></tr>
   <tr $yelclr><td>5</td><td>EMAIL: </td><td>$whatis{'email'}</td></tr>
   <tr $yelclr1><td>6</td><td>Номер группы 1: </td><td>$whatis{'grouponeid'}</td></tr>
   <tr $yelclr><td>7</td><td>Номер группы 2:</td><td>$whatis{'grouptwoid'}</td></tr>
   <tr $yelclr1><td>8</td><td>Номер группы 3: </td><td>$whatis{'grouptriid'}</td></tr>
   <tr $yelclr><td>9</td><td>Номер группы 4:</td><td>$whatis{'groupfourid'}</td></tr>
   <tr $yelclr1><td>10</td><td>Номер группы 5: </td><td>$whatis{'groupfiveid'}</td></tr>
   <tr $yelclr><td>11</td><td>Номер группы 6:</td><td>$whatis{'groupsixid'}</td></tr>
   $stdTxtSvnLine $stdTxtEitLine $stdTxtNinLine $stdTxtTenLine $stdTxtLvnLine $stdTxtTwlLine</table>
   <p> </p><p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 

}

#####################################################################################
########################### OPEN GROUP PAGE SUB #####################################
#####################################################################################
sub openGroupPageSub {
   &printjavascript(); $myclr = $yelclr; $cnt = 1; $ogpStyle = "style='height:50px; width:150px'";
   print "<h2>Изменение данных тренеров</h2>\n 
   <table><tr $myclr><td>No</td><td>ID</td><td>ФИО</td><td>Редактировать данные тренеров</td></tr>\n";
   foreach $ogpTrnrId(@globalTrainersList){
      if ( $ogpTrnrId ne '' ) {
         if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
         print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$ogpTrnrId\'></td><td>[$ogpTrnrId]</td>
         <td>$TrainerFullName{$ogpTrnrId}</td> <td><button onclick=\"return checkEditFunction\($cnt\)\;\">
         Редактировать / Добавить</button> данные тренера</td></tr>\n"; 
         $cnt++;
      }
   }
   print "</table><p> </p> 
   <button onclick=\"window.location.href = \'$httpindexcgi\?action=newtrainer\'\;\" $ogpStyle>Добавить Нового Тренера</button>
   <p> </p> <a href=\'$httpindexcgi\'>[ Вернуться НАЗАД ]</a>\n"; 
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
$cnt = 0; $pjsEmailArray = '';
foreach $i(@trainerslist){
   ($ttrnrnum, $ttrnrid, $ttrnrfirstnam, $ttrnrscndnam, $ttrnrthrdnam, $ttrnrpwd, $ttrnrphn, $ttrnremail, @other) = split (/<tab>/, $i);
   if ( $ttrnrid ne '' && $ttrnremail =~ /\@/ ) {  $ttrnremail = lc $ttrnremail;
      if ($cnt == 0) { $pjsEmailArray = "\"$ttrnrfirstnam\", \"$ttrnrscndnam\", \"$ttrnremail\""; }
      else { $pjsEmailArray = $pjsEmailArray . ",\n \"$ttrnrfirstnam\", \"$ttrnrscndnam\", \"$ttrnremail\""; }
      $cnt++;
   }
}
print  <<EOT;
 <script>
 function checkAllFunction (){ var emailList = [$pjsEmailArray]; var emailExist = 0; var emailAddress = ''; var oldEmail = '';
   if(document.getElementsByName('firstname')[0].value == ''){alert('Укажите имя!'); return false;}
   if(document.getElementsByName('secondname')[0].value == ''){alert('Укажите фамилию!'); return false;}
   if(document.getElementsByName('phonenumber')[0].value == ''){alert('Укажите номер телефона!'); return false;}
   if(document.getElementsByName('email')[0].value == ''){alert('Укажите EMAIL!'); return false;}
   else { oldEmail = document.getElementsByName('oldemail')[0].value;
      if ( oldEmail == 'true' ) { emailExist = 0; }
      else { emailAddress = document.getElementsByName('email')[0].value; emailAddress = emailAddress.toLowerCase();
         document.getElementsByName('email')[0].value = emailAddress; emailExist = emailList.indexOf(emailAddress);
         if ( emailExist > 0 ) {
            var userFirstNameId = emailExist - 2; var userSecondNameId = emailExist - 1;
            var userFirstName = emailList[userFirstNameId]; var userSecondName = emailList[userSecondNameId];
            alert('Такой EMAIL:[' + emailAddress + '] уже используется - Имя:[' + userFirstName + '] Фамилия:[' + userSecondName + ']'); return false;
         }
         else{ document.getElementsByName('email')[0].value = emailAddress; }
      }
   }
 }
 function checkSaveFunction (){
     var usr = confirm('Изменить Запись?');
     if(usr){return true;}
     else{return false;}
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