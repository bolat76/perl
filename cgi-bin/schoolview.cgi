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
        if($cookiekey =~ /candidatesproject/){$gotcookie = $hotcookie; }
    }
#$gotcookie = $ENV{'HTTP_COOKIE'};
$cookie_file = '../oedata/cn_cookies.txt';
$users_file = '../oedata/cn_usrdata.txt';

###################### end of cookie part #########################
$oe_folder = '../oedata/';
$upload_folder = '../oedata/';
$groups_folder = '../oedata/groups/';
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$indexcgi = 'schoolview.cgi';
$glMonthPayValue = 5500;
$glSchoolFeeValue = 1500;
$students_file = $oe_folder . 'students.txt';
$calendar_file = $oe_folder . 'calendar.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httplimbocgi = 'http://accelerator.kvadra.kz/cgi-bin/limbo.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Оплата учеников';

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
   if($tstudgrp ne '' && $tstudschl ne ''){ $studentFullName{$tstudid} = "$tstudfirstnam $tstudscndnam";
      $studentFirstName{$tstudid} = $tstudfirstnam; $studentSecondName{$tstudid} = $tstudscndnam;
      $studentThirdName{$tstudid} = $tstudthrdnam; $studentPositionNum{$tstudid} = $tstudnum; 
      $studentSchoolNum{$tstudid} = $tstudschl; $studentGroupNum{$tstudid} = $tstudgrp;     
      $existSchool{$tstudschl}++;  $existGroup{$tstudgrp}++; # $totalStudents++; $totalGroups++; $totalSchools
      if ( grep( /^$tstudschl$/, @uniqueSchoolNumList ) ) { $done = 1; } 
      else { if ( $tstudgrp !~ /-P/ ) { push(@uniqueSchoolNumList, $tstudschl); $totalSchools++; } }
      if ( grep( /^$tstudgrp$/, @uniqueGroupNumList ) ){ $done = 1;} 
      else { $GroupsPerSchool{$tstudschl}++; $totalGroups++; push(@uniqueGroupNumList, $tstudgrp); $groupSchoolNum{$tstudgrp} = $tstudschl; }
      push(@studentUniqueNumList, $tstudid); $totalStudents++;
   }
}  # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents ;$totalSchools; $totalGroups

open(INF, $calendar_file); 
@calendar_list = <INF>;
close(INF);
foreach $i(@calendar_list){ chomp($i); #12<tab>12.01.19<tab>Saturday
    ($tclndrnum, $tclndrdate, $tcndrweek, @other) = split (/<tab>/, $i);  
    $calendarweek{$tclndrnum} = $tcndrweek; $calendarweek{$tclndrdate} = $tcndrweek;
    $calendarnumber{$tclndrdate} = $tclndrnum;  $calendardate{$tclndrnum} = $tclndrdate;
}

open(INF, $users_file); 
@userlist = <INF>; 
close(INF); 
foreach $i(@userlist){ 
   #3<tab>Болатхан<tab>Джайдаринов<tab><tab>america<tab>8 777 277 0326<tab>candidate<tab>b.jaidarinov@gmail.com
   #<tab>25.07.2019<tab>12.07.1976<tab>Male<tab>85 room<tab>1233333<tab>12341556688<tab>reserve
   ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, $tusrtype, $tusreml, $tusrcreated,
   $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $i);
   $userCategory{$tusrid} = $tusrctgr; $userFullName{$tusrid} = "$tusrfrstnam $tusrthrdname $tusrscndnam";
   $userFirstName{$tusrid} = $tusrfrstnam; $userSecondName{$tusrid} = $tusrscndnam; $userThirdName{$tusrid} = $tusrthrdname;
   $userpwd{$tusreml} = $tusrpwd; $userpwd{$tusrid} = $tusrpwd; $userPhoneNumber{$tusrid} = $tusrphnnum;
   $userType{$tusrid} = $tusrtype; $userEmail{$tusrid} = $tusreml; $userEmailExist{$tusreml} = 1;  
   $userCreateDate{$tusrid} = $tusrcreated; $userBirthDay{$tusrid} = $tusrbrthday; 
   $userGender{$tusrid} = $tusrgndr; $userWorkPlace{$tusrid} = $tusrwrkplc; $userPersonId{$tusrid} = $tusrprsnid;
   $userIndivideId{$tusrid} = $tusrindvdid; $userStatus{$tusrid} = $tusrstats; $userSchoolId{$tusrid} = $tusrschlid;
   $usernumber{$tusrid} = $tusrid; $usernumber{$tusreml} = $tusrid; $userslist++; push(@loginuserslist, $tusrid);
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
&checkcookies();  print "\n"; &printfile($bas, $title);

if ( $whatis{'action'} ne '' ) { open(GURD,">>$log_file");
print GURD "Time: [$timedatenow] User ID: [$gotusrid] IP address: [$userip] User action: [$whatis{'action'}] Script: [$indexcgi] \n";
close(GURD); }

#####################################################################################
############################ LOGIN CHECK PART #######################################
#####################################################################################
print "<p>";
if($userlogged == 1){
    print "Hello $b1 $userFirstName{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>";
    if ( $userCategory{$gotusrid} eq 'School' && $userType{$gotusrid} eq 'confirmed' && $userSchoolId{$gotusrid} ne '' && $existSchool{$userSchoolId{$gotusrid}} > 0 ) {
       $whatis{'schoolid'} = $userSchoolId{$gotusrid}; if ( $whatis{'groupid'} ne '' ) { ($lcpQuerySchlId, @others) = split ( /-/, $whatis{'groupid'} ); }
       if ( $whatis{'action'} eq 'open' && $whatis{'groupid'} ne '' && $whatis{'schoolid'} eq $lcpQuerySchlId ) { &openGroupPageSub(); }
       elsif ( $whatis{'action'} eq 'show' ) { &showSchoolDataSub(); }
       else { &blankPageSub() ; }
    }
    else { print "<h3>Нет активной школы для показа..</h3><p> </p><p><a href=\'$httplimbocgi\'>[ Вернуться ДОМОЙ ]</a></p>\n"; }
}
else{
    if ( $whatis{'action'} eq 'login' && $userlogged != 1) { print "<p>$rf $errorlogin $f2</p>\n" ; }  
    print "<form method='post' action=\'$indexcgi\'><table><caption>Enter Login Data</caption><tr><td>Email: </td>
    <td><input type = 'text'  name = 'email'></td>  <td>Password: </td><td><input type = 'password'  name = 'userpwd'> </td>
    <td><input type = 'hidden' name = 'action' value = 'login'> <input type = 'submit' value = 'Enter'></td></tr></table></form>\n";
    print "<p> </p>";
}
print "<p> </p><p><a href=\'$httplimbocgi\'>[ Вернуться ДОМОЙ ]</a></p>\n";
#####################################################################################
########################### OPEN GROUP PAGE SUB #####################################
#####################################################################################
sub openGroupPageSub { # $calendarnumber{$tclndrdate} = $tclndrnum;  $calendardate{$tclndrnum} = $tclndrdate; $glPayStatus{$glPayId}
    &getGroupSub();
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
          if ( $ogpGrpId =~ /M2/ || $ogpGrpId =~ /M3/ )  { 
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
          $ogpPerStdtTxt = "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$ogpStdId\'></td>
          <td>$studentFullName{$ogpStdId}</td> $ogpNewLineOne $ogpNewLineTwo $ogpHtmlCodeTri";
          $ogpTodayExpected{$ogpGrpId} = $ogpTodayExpected{$ogpGrpId} + $ogpTodayStdExpected{$ogpStdIndex};
          $ogpStdUnpaidValue{$ogpStdIndex} = $ogpTodayStdExpected{$ogpStdIndex} - $ogpStdPaidValue{$ogpStdIndex};
          if ( $ogpStdUnpaidValue{$ogpStdIndex} < 0 ) { $ogpStdUnpaidValue{$ogpStdIndex} = 0; }
          $ogpPerStdtTxt = $ogpPerStdtTxt . "<td>$ogpTodayStdExpected{$ogpStdIndex}</td><td>$ogpStdPaidValue{$ogpStdIndex}</td>";
          $ogpPerStdtTxt = $ogpPerStdtTxt . "<td>$ogpStdUnpaidValue{$ogpStdIndex}</td><td>$ogpStdtTotalSum{$ogpStdIndex}</td></tr>\n";
          $ogpGroupTotalSum{$ogpGrpId} = $ogpGroupTotalSum{$ogpGrpId} + $ogpStdtTotalSum{$ogpStdIndex};
          $ogpUnpaidValue{$ogpGrpId} = $ogpUnpaidValue{$ogpGrpId} + $ogpStdUnpaidValue{$ogpStdIndex};
          $cnt++; push(@ogpHtmlCodeList, $ogpPerStdtTxt);
       }
    }
    if ( $blankPageSubIndex == 1 ) { return; }
    print "<h2>Таблица по оплатам учеников</h2>\n <p>Список учеников группы № [$whatis{'groupid'}]</p>
    <table><tr $yelclr><td>No</td><td>ФИО</td><td>Оплата<br>№1</td><td>Оплата<br>№2</td>$ogpHtmlCodeOne<td>На сегодня<br>
    ожидаем</td><td>На сегодня<br>получено</td><td>На сегодня<br>не оплачено</td><td>Всего ожидаем<br>за курс</td></tr>
    <tr $yelclr1><td>#</td><td>$b1 Дни оплаты<br>по плану: $b2</td>
    <td>$b1 $calendardate{$ogpGroupPayDayOne} $b2</td><td>$b1 $calendardate{$ogpGroupPayDayTwo} $b2</td>
    $ogpHtmlCodeTwo<td>$b1 $ogpTodayExpected{$ogpGrpId} $b2</td><td>$b1 $glGroupPaidValue{$ogpGrpId} $b2</td>
    <td>$b1 $ogpUnpaidValue{$ogpGrpId} $b2</td><td>$b1 $ogpGroupTotalSum{$ogpGrpId} $b2</td></tr>\n";
    foreach $ogpHtmlCode (@ogpHtmlCodeList) { print "$ogpHtmlCode"; }
    print "</table>\n <p> </p> <a href=\'$httpindexcgi\'>[ Вернуться НАЗАД ]</a>\n"; 
}
#####################################################################################
################################# GET GROUP SUB ######################################
#####################################################################################
sub getGroupSub {
   #foreach $stdid (@studentUniqueNumList){ if($studentGroupNum{$stdid} =~ $whatis{'groupid'}){  push(@glsStudentsList, $stdid); } }
   $ggsgrpfile = $groups_folder . $whatis{'groupid'} . '_data.txt'; $ggsid = $whatis{'groupid'};
   open(UPL, $ggsgrpfile);   @ggsprojectlist = <UPL>;   close(UPL);
   foreach $i (@ggsprojectlist){  chomp($i);  if($i =~ /<start of new project = /){ $donothing = 1; }
      elsif($i =~ /OEP_School: /){$i =~ s/OEP_School: //g; $OEP_School{$ggsid} = $i;}
      elsif($i =~ /OEP_Group: /){$i =~ s/OEP_Group: //g; $OEP_Group{$ggsid} = $i;}
      elsif($i =~ /OEP_StartDate: /){$i =~ s/OEP_StartDate: //g; $OEP_StartDate{$ggsid} = $i;}
      elsif($i =~ /OEP_FinishDate: /){$i =~ s/OEP_FinishDate: //g; $OEP_FinishDate{$ggsid} = $i;}
      elsif($i =~ /OEP_Paid: /){$i =~ s/OEP_Paid: //g; $OEP_Paid{$ggsid} = $i;}
      elsif($i =~ /OEP_Status: /){$i =~ s/OEP_Status: //g; $OEP_Status{$ggsid} = $i;}
      elsif($i =~ /OEP_Calendar: /){$i =~ s/OEP_Calendar: //g; $OEP_Calendar{$ggsid} = $i;}
   }
   @ggsGroupDaysList = split (/, /, $OEP_Calendar{$ggsid}); 
   $ggsGroupPayDayOne = $ggsGroupDaysList[7]; $ggsGroupPayDayTwo = $ggsGroupDaysList[14]; 
   if ( $ggsGroupPayDayOne > $ssdEndDayNum ) { $ggsPeriodNotStarted{$ggsid} = 1; } else { $ggsPeriodNotStarted{$ggsid} = 0; }
   if ( $ggsGroupPayDayTwo < $ssdBasDayNum ) { $ggsPeriodFinished{$ggsid} = 1; } else { $ggsPeriodFinished{$ggsid} = 0; }
   if ( $ggsid =~ /M2/ || $ggsid =~ /M3/ )  { # $ggsPeriodNotStarted{$ggsid}  $ggsPeriodFinished{$ggsid}
      $ggsGroupPayDayTri = $ggsGroupDaysList[21]; $ggsGroupPayDayFor = $ggsGroupDaysList[28]; 
      if ( $ggsGroupPayDayFor < $ssdBasDayNum ) { $ggsPeriodFinished{$ggsid} = 1; } else { $ggsPeriodFinished{$ggsid} = 0; } }
   
   $gpsPayDataFile = $groups_folder . $whatis{'groupid'} . '_payments.txt'; $glGroupPaidValue{$ggsid} = 0;
   open(INF, $gpsPayDataFile);    @paymentslist = <INF>;    close(INF); 
   foreach $i(@paymentslist){ #1<tab>56BC4703<tab>99-10-M2<tab><tab><tab><tab><tab>reserve
      ($tpaynum, $tpaystudid, $tpaystudgrp, $tpayonedate, $tpaytwodate, $tpaytridate, $tpayfordate, 
      $tpaystatusone, $tpaystatustwo, $tpaystatustri, $tpaystatusfor, @other) = split (/<tab>/, $i);
      if ( $tpaystudid =~ /56BC/ && $tpaystudgrp ne '' ) {  $glPayId = $tpaystudid . '<tab>' . $tpaystudgrp;  
         $glPayOneDate{$glPayId} = $tpayonedate;  $glPayTwoDate{$glPayId} = $tpaytwodate;
         $glPayThreeDate{$glPayId} = $tpaytridate;  $glPayFourDate{$glPayId} = $tpayfordate; 
         $glPayStatusOne{$glPayId} = $tpaystatusone; $glPayStatusTwo{$glPayId} = $tpaystatustwo; 
         $glPayStatusTri{$glPayId} = $tpaystatustri; $glPayStatusFor{$glPayId} = $tpaystatusfor;
         if ( $SchoolDataSubIndex == 1 ) { $gssStudsFound{$tpaystudgrp}++;
            $gssDayOneNum = $calendarnumber{$tpayonedate}; $gssDayTwoNum = $calendarnumber{$tpaytwodate};
            $gssDayTriNum = $calendarnumber{$tpaytridate}; $gssDayForNum = $calendarnumber{$tpayfordate};
            if ( $gssDayOneNum >= $ssdBasDayNum && $gssDayOneNum <= $ssdEndDayNum ) { 
               $gssGrpPayTimeOne{$tpaystudgrp} = 1; $gssGrpPaid{$tpaystudgrp} =  $gssGrpPaid{$tpaystudgrp} + $glMonthPayValue; } 
            if ( $gssDayTwoNum >= $ssdBasDayNum && $gssDayTwoNum <= $ssdEndDayNum ) { 
               $gssGrpPayTimeTwo{$tpaystudgrp} = 1; $gssGrpPaid{$tpaystudgrp} =  $gssGrpPaid{$tpaystudgrp} + $glMonthPayValue; } 
            if ( $tpaystatusone eq 'Free' ) { $gssGrpFreed{$tpaystudgrp}++; }
            if ( $tpaystatustwo eq 'Free' ) { $gssGrpFreed{$tpaystudgrp}++; }
            if ( $ggsid =~ /M2/ || $ggsid =~ /M3/ )  {
               if ( $gssDayTriNum >= $ssdBasDayNum && $gssDayTriNum <= $ssdEndDayNum ) { 
                  $gssGrpPayTimeTri{$tpaystudgrp} = 1; $gssGrpPaid{$tpaystudgrp} =  $gssGrpPaid{$tpaystudgrp} + $glMonthPayValue; } 
               if ( $gssDayForNum >= $ssdBasDayNum && $gssDayForNum <= $ssdEndDayNum ) { 
                  $gssGrpPayTimeFor{$tpaystudgrp} = 1; $gssGrpPaid{$tpaystudgrp} =  $gssGrpPaid{$tpaystudgrp} + $glMonthPayValue; } 
               if ( $tpaystatustri eq 'Free' ) { $gssGrpFreed{$tpaystudgrp}++; }
               if ( $tpaystatusfor eq 'Free' ) { $gssGrpFreed{$tpaystudgrp}++; } }
         }
      }
   }
}

#####################################################################################
############################ SHOW SCHOOL DATA SUB ###################################
#####################################################################################
sub showSchoolDataSub { &printjavascript();
   $ssdStyle = "style='height:50px; width:150px'"; $ssdGrpNum = 0; $ssdSchlNum = 0; $SchoolDataSubIndex = 1;
  if ( $whatis{'startdate'} ne '' ) { $ssdBasDateNow = $whatis{'startdate'}; } else { $ssdBasDateNow = $datenow; }
  if ( $whatis{'finishdate'} ne '' ) { $ssdEndDateNow = $whatis{'finishdate'}; } else { $ssdEndDateNow = $datenow; }
  print "<h2>Данные по оплатам</h2><form method='post' action=\'$httpindexcgi\' onsubmit='return checkDateFunction();'>
  <table><tr $yelclr><td>Start Date: <br><input type='text' name='startdate' value=\'$ssdBasDateNow\' ></td>
  <td>Finish Date: <br><input type='text' name='finishdate' value=\'$ssdEndDateNow\'></td></tr>
  <tr $yelclr1><td><input type = 'hidden' name = 'action' value = 'show'><input type='reset' value = 'ОТМЕНИТЬ' $ssdStyle></td>
  <td><input type = 'submit' value = 'ОТКРЫТЬ' $ssdStyle></td></tr></table></form>\n";
  $ssdBasDayNum = $calendarnumber{$whatis{'startdate'}}; $ssdEndDayNum = $calendarnumber{$whatis{'finishdate'}};
  if ( $ssdBasDayNum < 10 || $ssdEndDayNum > 300 || $ssdBasDayNum > $ssdEndDayNum ){
      print "<h3>$rf Даты начала [$whatis{'startdate'}] и завершения [$whatis{'finishdate'}] указаны неверно! $f2</h3> 
      <p> </p> <a href=\'$httpindexcgi\'>[ Вернуться НАЗАД ]</a>\n"; return;  }
  print "<p> </p><table><caption><h3>Общий свод по оплатам в школе [$whatis{'schoolid'}]
  <br>на период с [$whatis{'startdate'}] по [$whatis{'finishdate'}]</h3></caption>
  <tr $yelclr><td>Школа</td><td>Группа</td><td>Статус<br>группы</td><td>Оплачено</td><td>Оплата в школу</td></tr>\n";
  $ssdPaidVal = 0; $ssdUnpaidVal = 0; $ssdTotalVal = 0;  $myclr1 = $yelclr; 
  foreach $ssdGrpId (@uniqueGroupNumList) {  ($ssdSchlId, @others) = split (/-/, $ssdGrpId); 
     if ( $ssdGrpId ne '' && $ssdGrpId !~ /P/ && $ssdSchlId eq $whatis{'schoolid'} ) { 
        $gssGrpPayTimeOne{$ssdGrpId} = 0; $gssGrpPayTimeTwo{$ssdGrpId} = 0; $gssGrpPayTimeTri{$ssdGrpId} = 0; $gssGrpPayTimeFor{$ssdGrpId} = 0;
        $gssGrpPayTimeIndx{$ssdGrpId} = 0; $ssdGrpNum++; $whatis{'groupid'} = $ssdGrpId; &getGroupSub(); 
        $gssGrpPayTimeIndx{$ssdGrpId} = $gssGrpPayTimeOne{$ssdGrpId} + $gssGrpPayTimeTwo{$ssdGrpId};
         $gssGrpPayTimeIndx{$ssdGrpId} =$gssGrpPayTimeIndx{$ssdGrpId} + $gssGrpPayTimeTri{$ssdGrpId} + $gssGrpPayTimeFor{$ssdGrpId};
        if ( $ggsPeriodNotStarted{$ssdGrpId} == 1 ) { $gssGrpPayers{$ssdGrpId} = 0; }
        elsif ( $ggsPeriodFinished{$ssdGrpId} == 1 ) { $gssGrpPayers{$ssdGrpId} = $existGroup{$ssdGrpId} * 2;
           if ( $ssdGrpId =~ /M2/ || $ssdGrpId =~ /M3/ ) { $gssGrpPayers{$ssdGrpId} = $existGroup{$ssdGrpId} * 2; } }
        else { $gssGrpPayers{$ssdGrpId} = $existGroup{$ssdGrpId} * $gssGrpPayTimeIndx{$ssdGrpId}; }
        $gssGrpPayers{$ssdGrpId} = $gssGrpPayers{$ssdGrpId} - $gssGrpFreed{$ssdGrpId};
        $ssdGroupTotalSum{$ssdGrpId} = $gssGrpPayers{$ssdGrpId} * $glMonthPayValue;
        $ssdUnpaidValue{$ssdGrpId} = $ssdGroupTotalSum{$ssdGrpId} - $gssGrpPaid{$ssdGrpId};
        $ssdSchlGrpPaid{$ssdGrpId} = ( $gssGrpPaid{$ssdGrpId} / $glMonthPayValue ) * $glSchoolFeeValue;
        if ( $ssdUnpaidValue{$ssdGrpId} < 0 ) { $ssdUnpaidValue{$ssdGrpId} = 0; }
        if ( $myclr1 eq $yelclr ) { $myclr1 = $yelclr1; } else { $myclr1 = $yelclr; }
        print "<tr $myclr1><td $ac>$ssdSchlId</td>
        <td><a href = \'$indexcgi?action=open\&groupid\=$ssdGrpId\'>$ssdGrpId</a> [$existGroup{$ssdGrpId}]</td>
        <td $ac>$OEP_Status{$ssdGrpId}</td><td $ac>$gssGrpPaid{$ssdGrpId}</td><td $ac>$ssdSchlGrpPaid{$ssdGrpId}</td></tr>\n";
        $ssdSchlExist{$ssdSchlId}++; if ( $ssdSchlExist{$ssdSchlId} == 1 ) { $ssdSchlNum++; } 
        $ssdPaidVal = $ssdPaidVal + $gssGrpPaid{$ssdGrpId}; $ssdTotalPayables = $ssdTotalPayables + $gssGrpPayers{$ssdGrpId};
        $ssdSchoolTotalVal = $ssdSchoolTotalVal + $ssdSchlGrpPaid{$ssdGrpId};
        $ssdUnpaidVal = $ssdUnpaidVal + $ssdUnpaidValue{$ssdGrpId}; $ssdTotalVal = $ssdTotalVal + $ssdGroupTotalSum{$ssdGrpId};
     }
  }
  if ( $myclr1 eq $yelclr ) { $myclr1 = $yelclr1; } else { $myclr1 = $yelclr; }
  print "<tr $myclr1><td $ac>$ssdSchlNum</td><td $ac>$ssdGrpNum</td><td>$b1 ИТОГО: $b2</td><td $ac>$ssdPaidVal</td>
  <td $ac>$ssdSchoolTotalVal</td></tr></table>\n"; 
  #print "<p> </p> <a href=\'$httpindexcgi\'>[ Вернуться НАЗАД ]</a>\n"; 
}
#####################################################################################
################################ BLANK PAGE SUB #####################################
#####################################################################################
sub blankPageSub { &printjavascript();
   $bpsStyle = "style='height:50px; width:150px'";  $blankPageSubIndex = 0; $bpsGrpNum = 0; $bpsSchlNum = 0;
  print "<h2>Данные по оплатам по школе № $whatis{'schoolid'}</h2>\n 
  <form method='post' action=\'$httpindexcgi\' onsubmit='return checkDateFunction();'><table>
  <tr $yelclr><td>Start Date: <br><input type='text' name='startdate' value=\'$datenow\' ></td>
  <td>Finish Date: <br><input type='text' name='finishdate' value=\'$datenow\'></td></tr>
  <tr $yelclr1><td><input type = 'hidden' name = 'action' value = 'show'><input type='reset' value = 'ОТМЕНИТЬ' $bpsStyle></td>
  <td><input type = 'submit' value = 'ОТКРЫТЬ' $bpsStyle></td></tr></table></form>
  <p> </p><table><caption><h3>Общий свод по оплатам по школе № $whatis{'schoolid'} на текущую дату</h3></caption>
  <tr $yelclr><td>Школа</td><td>Группа</td><td>Статус<br>группы</td><td>Оплачено<br>(Всего)</td>
  <td>$b1 Оплачено<br>(Доля школы) $b2</td><td>Не оплачено<br>(Всего)</td>
  <td>$b1 Не оплачено<br>(Доля школы) $b2</td><td>Итого</td><td>$b1 Итого<br>(Доля школы) $b2</td></tr>\n";
  $bpsPaidVal = 0; $bpsUnpaidVal = 0; $bpsTotalVal = 0;  $myclr1 = $yelclr;
  foreach $bpsGrpId (@uniqueGroupNumList) { ($bpsSchlId, @others) = split (/-/, $bpsGrpId); 
     if ( $bpsGrpId ne '' && $bpsGrpId !~ /P/ && $bpsSchlId ne '' && $bpsSchlId eq $whatis{'schoolid'} ) { 
        $bpsMonthPayValue = $glMonthPayValue; $bpsGrpNum++;  #$glMonthPayValue = 5500; $glSchoolFeeValue = 1500;
        $whatis{'groupid'} = $bpsGrpId; &getGroupSub(); $blankPageSubIndex = 1; &openGroupPageSub(); $blankPageSubIndex = 0;
        $glSchoolPaidValue{$bpsGrpId} = ( $glGroupPaidValue{$bpsGrpId} / $glMonthPayValue ) * $glSchoolFeeValue;
        $ogpSchoolUnpaidValue{$bpsGrpId} = ( $ogpUnpaidValue{$bpsGrpId} / $glMonthPayValue ) * $glSchoolFeeValue;
        $ogpSchoolTotalSum{$bpsGrpId} = ( $ogpGroupTotalSum{$bpsGrpId} / $glMonthPayValue ) * $glSchoolFeeValue;
        if ( $myclr1 eq $yelclr ) { $myclr1 = $yelclr1; } else { $myclr1 = $yelclr; }
        print "<tr $myclr1><td $ac>$bpsSchlId</td><td><a href = \'$indexcgi?action=open\&groupid\=$bpsGrpId\'>$bpsGrpId</a> 
        [$existGroup{$bpsGrpId}]</td><td $ac>$OEP_Status{$bpsGrpId}</td><td $ac>$glGroupPaidValue{$bpsGrpId}</td>
        <td $ac>$b1 $glSchoolPaidValue{$bpsGrpId} $b2</td><td $ac>$ogpUnpaidValue{$bpsGrpId}</td>
        <td $ac>$b1 $ogpSchoolUnpaidValue{$bpsGrpId} $b2</td><td $ac>$ogpGroupTotalSum{$bpsGrpId}</td>
        <td $ac>$b1 $ogpSchoolTotalSum{$bpsGrpId} $b2</td></tr>\n";
        $bpsSchlExist{$bpsSchlId}++; if ( $bpsSchlExist{$bpsSchlId} == 1 ) { $bpsSchlNum++; } 
        $bpsPaidVal = $bpsPaidVal + $glGroupPaidValue{$bpsGrpId}; $bpsUnpaidVal = $bpsUnpaidVal + $ogpUnpaidValue{$bpsGrpId}; 
        $bpsTotalVal = $bpsTotalVal + $ogpGroupTotalSum{$bpsGrpId}; $bpsSchoolVal = $bpsSchoolVal + $glSchoolPaidValue{$bpsGrpId}; 
        $bpsSchlUnpaidVal = $bpsSchlUnpaidVal + $ogpSchoolUnpaidValue{$bpsGrpId};
        $bpsSchlTotalVal = $bpsSchlTotalVal + $ogpSchoolTotalSum{$bpsGrpId};
     }
  }
  if ( $myclr1 eq $yelclr ) { $myclr1 = $yelclr1; } else { $myclr1 = $yelclr; }
  print "<tr $myclr1><td $ac>$bpsSchlNum</td><td $ac>$bpsGrpNum</td><td></td><td $ac>$bpsPaidVal</td>
  <td $ac>$b1 $bpsSchoolVal $b2</td><td $ac>$bpsUnpaidVal</td><td $ac>$b1 $bpsSchlUnpaidVal $b2</td>
  <td $ac>$bpsTotalVal</td><td $ac>$b1 $bpsSchlTotalVal $b2</td></tr></table>\n"; 
} 

#####################################################################################
########################### FINISH END BODY #########################################
#####################################################################################

print "</center></body></html>";

##################################################################################################################
################################# Sub checkcookies ###############################################################
##################################################################################################################
sub checkcookies {
    #print "<br>i am in checkcookies\n";
    #7<tab>30569458007812<tab>Tue Sep 11 11:35:10 2012<tab>172.81.88.121<tab>reserve
    # $userid<tab>$randnum<tab>$timedatenow<tab>$userip<tab>future_reserve
    # $gotcookie = $ENV{'HTTP_COOKIE'};    # $oeusercookiernd{$clusrnum} = $clusrrnd;    
    # $oeusercookiedate{$clusrnum} = $clusrdate;    # $oeusercookieip{$clusrnum} = $clusrip;
    ($gccontsupgrp, $gcusrnumrnd) = split(/=/, $gotcookie);
    ($gcusrnum, $gcusrrnd, $gcusrbrowser) = split(/_/, $gcusrnumrnd);
    $logindata = "User got number: [$gcusrnum] User RND: [$gcusrrnd] User's Cookies RND: [$oeusercookiernd{$gcusrnum}] UserIP:[$userip] ";
    if ( $gotcookie =~ /candidatesproject/ && $whatis{'action'} ne 'logout' && $whatis{'action'} ne 'login' ) { $iwashere = 1;
       if ( $oeusercookiernd{$gcusrnum} eq $gcusrrnd && $userip eq $oeusercookieip{$gcusrnum} && $userip ne '' ) {  
          $userlogged = 1;   $gotusrid = $gcusrnum;
          if($whatis{'browser'} eq 'mobile'){ $userbrowser = 'mobile'; }
          elsif($whatis{'browser'} eq 'desktop'){ $userbrowser = 'desktop'; }
          else{ $userbrowser = $gcusrbrowser; }
          $newcookie = "candidatesproject\=$gcusrnum\_$gcusrrnd\_$userbrowser\; expires=$live_time\; path=/\;";
          print "Set-Cookie: " . $newcookie . "\n";
       }
       else { $errorlogin = "$rf $b1 User not identified or no permission to access! $b2 $f2"; }
    } # $usernumber{$tusrid} = $tusrid; $usernumber{$tusreml} = $tusrid;
    elsif ( $whatis{'action'} eq 'login' || $whatis{'action'} eq 'logout' ) {
       if ( $whatis{'action'} eq 'logout' ) {
          $userlogged = 0;   $gotusrid = $gcusrnum;     $oeusercookiernd{$gotusrid} = '1234567890';
          $oeusercookiedate{$gotusrid} = $timedatenow;  $oeusercookieip{$gotusrid} = $userip;
          $newcookie = "candidatesproject=0_1234567890_desktop\; expires=$live_time\; path=/\;";
          print "Set-Cookie: " . $newcookie . "\n";  $iwashere = 2;
       } # $userpwd{$tusreml} = $tusrpwd; $userpwd{$tusrid} = $tusrpwd; 
       elsif ( $whatis{'action'} eq 'login' ) {
          if ( $whatis{'userpwd'} eq $userpwd{$whatis{'email'}} && $whatis{'userpwd'} ne '' ) {
              $ccUserNumber = $usernumber{$whatis{'email'}};
              if ( $ccUserNumber ne '' ) { $gotusrid = $ccUserNumber; }  else { $gotusrid = 0; }
              $randnum = int(rand(10)*1000000000000);       $oeusercookiernd{$gotusrid} = $randnum;
              $oeusercookiedate{$gotusrid} = $timedatenow;  $oeusercookieip{$gotusrid} = $userip;
              $newcookie = "candidatesproject\=$gotusrid\_$randnum\_desktop\; expires=$live_time\; path=/\;";
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
          if($tclusrnum eq $usernumber{$whatis{'email'}} && $tclusrnum ne '' ) { $donothing = 1; }
          else { push(@ccNewCookieList, $i); }
       }
       open(D,">$cookie_file");
       foreach $i (@ccNewCookieList){ if ( $i ne '' ) { print D "$i\n"; } }
       if ( $ccDataLine ne '' ) { print D "$ccDataLine\n"; }
       close(D); 
       $cnt = 0;       
    }
    else{$userlogged = 0; $iwashere = 4;}
    $logindata = $logindata . " Got User ID: [$gotusrid] ";
}

#######################################################################################
########################## JAVASCRIPT PART ###########################################
#######################################################################################
sub printjavascript {
print  <<EOT;
 <script>
 function checkDateFunction (){
   if(document.getElementsByName('startdate')[0].value == ''){alert('Укажите начальную дату периода!'); return false;}
   var usr = document.getElementsByName('startdate')[0].value;
   if (isValidDate(usr)) { document.getElementsByName('startdate')[0].value = usr; }
   else {alert('Неправильная дата: [' + usr + ']!'); return false;}
   if(document.getElementsByName('finishdate')[0].value == ''){alert('Укажите конечную дату периода!'); return false;}
   usr = document.getElementsByName('finishdate')[0].value;
   if (isValidDate(usr)) { document.getElementsByName('finishdate')[0].value = usr; }
   else {alert('Неправильная дата: [' + usr + ']!'); return false;}
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