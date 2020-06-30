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
$children_file = '../oedata/cn_childrendata.txt';
###################### end of cookie part #########################
$oe_folder = '../oedata/';
$upload_folder = '../oedata/';
$groups_folder = '../oedata/groups/';
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$bas = $oe_folder  . 'bas.txt';
$end = $oe_folder . 'end.txt';
$indexcgi = 'parentview.cgi';
$glMonthPayValue = 5500;
$students_file = $oe_folder . 'students.txt';
$calendar_file = $oe_folder . 'calendar.txt';
$parents_file = $oe_folder . 'parents.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httplimbocgi = 'http://accelerator.kvadra.kz/cgi-bin/limbo.cgi';
$httpregistercgi = 'http://accelerator.kvadra.kz/cgi-bin/register.cgi';
$title = 'Parent Home Page';

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

open(INF, $parents_file); @parentslist = <INF>; close(INF); foreach $i(@parentslist){
   #1<tab>55FM4703<tab>56BC4703<tab>Sergei<tab>Sergeev<tab>Sergeevich<tab>99<tab>99-M2-1<tab>
   #$usernum<tab>$userID<tab>$studentID<tab>$user1stname<tab>$user2ndname<tab>$user3rdname<tab>$userschool<tab>$usergroup<tab>$other
   ($tparntnum, $tparntid, $tparntstudid, $tparntfirstnam, $tparntscndnam, $tparntthrdnam, $tparntschl, 
   $tparntgrp, $tparntbrtd, $tparntphn, $tparntwrkplc, $tparntemail, @other) = split (/<tab>/, $i);
   if($tparntid ne ''){  $ParentStudentId{$tparntid} = $tparntstudid; $tparntemail = lc $tparntemail;
      $ParentFirstName{$tparntid} = $tparntfirstnam; $ParentSecondName{$tparntid} = $tparntscndnam;
      $ParentThirdName{$tparntid} = $tparntthrdnam; $ParentPositionNum{$tparntid} = $tparntnum; 
      $ParentSchoolNum{$tparntid} = $tparntschl; $ParentGroupNum{$tparntid} = $tparntgrp;     
      $ParentBirthDay{$tparntid} = $tparntbrtd; $ParentPhoneNum{$tparntid} = $tparntphn; 
      $ParentWorkPlace{$tparntid} = $tparntwrkplc; $ParentEmail{$tparntid} = $tparntemail; 
      $ParentUniqueId{$tparntemail} = $tparntid; $ParentChildCnt{$tparntemail}++; 
      $ParentIndex = $ParentChildCnt{$tparntemail} . '_' . $tparntemail; 
      $ParentIndexInfo{$ParentIndex} = $tparntid . '_' . $tparntstudid; 
      $ParentStudentExist{$ParentIndexInfo{$ParentIndex}} = 1;
   }
}  # $existSchool{$tparntschl}; $existGroup{$tparntgrp}; $GroupsPerSchool{$tparntschl}; $totalParents ;$totalSchools; $totalGroups

open(INF, $students_file); @studentslist = <INF>; close(INF); foreach $i(@studentslist){ 
   #1<tab>56BC4567<tab>Томирис<tab>Толенді<tab><tab>71<tab>71-1-M1<tab>reserve
   #$usernum<tab>$userID<tab>$user1stname<tab>$user2ndname<tab>$user3rdname<tab>$userschool<tab>$usergroup<tab>$other
   ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp, @other) = split (/<tab>/, $i);
   if( $tstudid ne '' ) { $studentFullName{$tstudid} = "$tstudfirstnam $tstudthrdnam $tstudscndnam";
      $studentFirstName{$tstudid} = $tstudfirstnam; $studentSecondName{$tstudid} = $tstudscndnam;
      $studentThirdName{$tstudid} = $tstudthrdnam; $studentPositionNum{$tstudid} = $tstudnum; 
      $studentSchoolNum{$tstudid} = $tstudschl; $studentGroupNum{$tstudid} = $tstudgrp;
      push(@glsStudentsList, $tstudid);   
   }
}  # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents ;$totalSchools; $totalGroups

open(INF, $calendar_file); @calendar_list = <INF>; close(INF); foreach $i(@calendar_list){ chomp($i); #12<tab>12.01.19<tab>Saturday
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
   $tusreml = lc $tusreml;
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
############### check COOKIES and LOG actions ###########################################
#######################################################################################
if ( $whatis{'email'} ne '' ) { $whatis{'email'} = lc $whatis{'email'}; $whatis{'email'} =~s/ //g; }
&checkcookies(); print "\n"; &printfile($bas, $title);

if ( $whatis{'action'} ne '' ) { open(GURD,">>$log_file");
print GURD "Time: [$timedatenow] User ID: [$gotusrid] IP address: [$userip] User action: [$whatis{'action'}] Script: [$indexcgi] \n";
close(GURD); }

#####################################################################################
########################## LOGIN CHECK PART #######################################
#####################################################################################
print "<p>";
if ( $userlogged == 1 ) {
   print "Hello $b1 $userFirstName{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>";
   if ( $userCategory{$gotusrid} eq 'Parent' && $userType{$gotusrid} eq 'confirmed' ) { 
      if ( $whatis{'action'} eq 'open' && $whatis{'groupid'} ne '' && $whatis{'lessonid'} ne '' && $whatis{'parid'} =~ /55FM/ && $whatis{'studid'} =~ /56BC/ ) { &openLessonSub($whatis{'groupid'}); }
      elsif ( $whatis{'action'} eq 'paid' && $whatis{'parid'} =~ /55FM/ && $whatis{'studid'} =~ /56BC/ && $whatis{'child'} ne '' ) { &showPaidData(); }
      elsif ( $whatis{'action'} eq 'show' && $whatis{'parid'} =~ /55FM/ && $whatis{'studid'} =~ /56BC/ ) { &showGroupData(); }
      else { &openBlankPage(); }
   }
   else { &openBlankPage(); }
}
else{
    if ( $whatis{'action'} eq 'login' && $userlogged != 1 ) { print "<p>$rf $errorlogin $f2</p>\n" ; }  
    print "<form method='post' action=\'$httpindexcgi\'><table><caption>Enter Login Data</caption><tr><td>Email: </td>
    <td><input type = 'text'  name = 'email'></td>  <td>Password: </td><td><input type = 'password'  name = 'userpwd'> </td>
    <td><input type = 'hidden' name = 'action' value = 'login'> <input type = 'submit' value = 'Enter'></td></tr></table></form>\n";
    print "<p><a href=\'$httpregistercgi?action=email\'>Обновить Персональные Данные</a></p>";
}
print "<p><a href=\'$httplimbocgi\'>Вернуться ДОМОЙ</a></p>";

#####################################################################################
########################### START MAIN BODY #########################################
#####################################################################################
sub showGroupData { $sgdEmail = $userEmail{$gotusrid};   $sgdPrntId = $whatis{'parid'};
   $sgdStudId = $ParentStudentId{$sgdPrntId}; $sgdStudGrpId = $studentGroupNum{$sgdStudId};
   if ( $userType{$gotusrid} eq 'confirmed' && $sgdStudGrpId ne '' ) {
       print "<p> </p>\n<h3> Ученик [$studentFullName{$sgdStudId}] записан в группу [$sgdStudGrpId] </h3>\n";
       &getLessonSub($sgdStudGrpId); &printListLessons($sgdStudGrpId, $sgdPrntId, $sgdStudId);
   }
   else { print "<p> </p>\n<h3>$rf Нет группы для показа! $f2</h3>\n"; }
}

#####################################################################################
################################ OPEN BLANK SUB #####################################
#####################################################################################
sub openBlankPage { $obpEmail = $userEmail{$gotusrid}; 
   if ( $ParentChildCnt{$obpEmail} > 1 ) { $obpCnt = 0; $myclr = $yelclr;
      # $ParentIndex = $ParentChildCnt{$tparntemail} . '_' . $tparntemail; $ParentIndexInfo{$ParentIndex} = $tparntid . '_' . $tparntstudid;
      print "\n<table><tr $myclr><td>No</td><td>ФИО</td><td>Группа</td><td>Данные по Оплатам</td></tr>\n";
      while ( $obpCnt < $ParentChildCnt{$obpEmail} ) { $obpCnt++; $obpParIndx = $obpCnt . '_' . $obpEmail;
         ($obpPrntId, $obpStudId) = split(/_/, $ParentIndexInfo{$obpParIndx}); $obpStudGrpId = $studentGroupNum{$obpStudId};
         if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; }
         print "<tr $myclr><td>$obpCnt</td><td>$studentFullName{$obpStudId}</td>
         <td><a href = \'$httpindexcgi?action=show\&parid\=$obpPrntId\&studid\=$obpStudId\'>$obpStudGrpId</a></td>
         <td><a href = \'$httpindexcgi?action=paid\&parid\=$obpPrntId\&studid\=$obpStudId\&child\=$obpCnt\'>Информация По Оплатам Ученика</a></td></tr>\n";
      } #<p> </p><a href = \'$httpindexcgi?action=paid\&parid\=$pllPrntId\&studid\=$pllStudId\'><h3>Информация По Оплатам Ученика</h3></a>
      print "</table>\n";
   }
   else { $obpPrntId = $ParentUniqueId{$obpEmail};
      $obpStudId = $ParentStudentId{$obpPrntId}; $obpStudGrpId = $studentGroupNum{$obpStudId};
      if ( $userType{$gotusrid} eq 'confirmed' && $obpStudGrpId ne '' ) {
         print "<p> </p>\n<h3> Ученик [$studentFullName{$obpStudId}] записан в группу [$obpStudGrpId] </h3>
         <p> </p><a href = \'$httpindexcgi?action=paid\&parid\=$obpPrntId\&studid\=$obpStudId\&child=1\'><h3>Информация По Оплатам Ученика</h3></a>\n";
         &getLessonSub($obpStudGrpId); &printListLessons($obpStudGrpId, $obpPrntId, $obpStudId);
      }
      else { print "<p> </p>\n<h3>$rf Нет группы для показа! $f2</h3>\n"; }
   } # $ParentUniqueId{$tparntstudid} = $tparntid;
   
}

#####################################################################################
############################### OPEN LESSON SUB #####################################
#####################################################################################
sub openLessonSub { my ($olsGrpId, @rest) = @_; &getLessonSub($olsGrpId);  $olsid = $whatis{'lessonid'};
   $olsPrntId = $whatis{'parid'}; $olsStudId = $whatis{'studid'}; $olsEmail = $userEmail{$gotusrid}; 
   $olsIndex = $olsPrntId . '_' . $olsStudId;
   if ( $userType{$gotusrid} eq 'confirmed' && $ParentStudentExist{$olsIndex} == 1 && $studentGroupNum{$olsStudId} eq $olsGrpId ) {
      print "<p> </p><table> <tr $yelclr1><td>Группа №</td>
      <td $ac><a href = \'$httpindexcgi\'>$olsGrpId</a></td></tr>
      <tr $yelclr><td>Тема урока</td><td $ac>$OEP_Topic{$olsid}</td></tr>
      <tr $yelclr1><td>Номер урока</td><td $ac>$OEP_Lesson{$olsid}</td></tr>
      <tr $yelclr><td>Дата урока</td><td $ac>$OEP_Date{$olsid}</td></tr></table><p> </p><table>
      <tr $yelclr1><td>№</td><td>Имя Фамилия</td><td>Посещение</td><td>Опоздание</td><td>Штраф за опоздание</td><td>Тестирование</td>
      <td>Баллы за тест</td><td>Всего</td><td>Оценка за тему</td><td>Комментарий по ученику</td><td>Оценка за домашнее задание</td></tr>\n";    
      foreach $i (@glsStudentsList){ if ( $studentGroupNum{$i} eq $olsGrpId ) {
            $cnt = 1;  $olsUserID_PRNum = $i . '_' . $olsid; if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
            print "<tr $myclr><td>$cnt</td><td>$studentFirstName{$i} $studentSecondName{$i}</td><td $ac>$OEP_Participation{$olsUserID_PRNum}</td>
            <td $ac>$OEP_Late{$olsUserID_PRNum}</td><td $ac>$OEP_LiftMinus{$olsUserID_PRNum}</td><td $ac>$OEP_Test{$olsUserID_PRNum}</td>
            <td $ac>$OEP_LiftPlus{$olsUserID_PRNum}</td><td $ac>$OEP_TotalPoints{$olsUserID_PRNum}</td><td $ac>$OEP_Eval{$olsUserID_PRNum}</td>
            <td $ac>$OEP_UserComment{$olsUserID_PRNum}</td><td $ac>$OEP_HomeWork{$olsUserID_PRNum}</td></tr>\n"; $cnt++;
      } }
      if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; }
      print "</table><table><tr $myclr><td>Комментарии</td><td>$OEP_Comments{$olsid}</td></tr></table>\n";
   }
}

#####################################################################################
########################## PRINT LIST OF LESSONS SUB ################################
#####################################################################################
sub printListLessons {    my ($pllGrpId, $pllPrntId, $pllStudId, @rest) = @_;
    print "<p> </p><table><caption>Группа № <a href = \'$indexcgi\'>$pllGrpId</a></caption><tr $yelclr><td>Уроки</td>\n";  
    foreach $i (@glsStudentsList){ if ( $studentGroupNum{$i} eq $pllGrpId ) {
       print "<td>$studentFirstName{$i}";  if($studentFirstName{$i} ne ''){print "<br>";} 
       print "$studentSecondName{$i}"; print "</td>"; 
    } }
    print "<td>Всего</td></tr>\n";   $myclr = $yelclr;
    @glsLessonNumList = sort(@glsLessonNumList);
    foreach $pllId (@glsLessonNumList){ 
        if($pllId ne ''){ ($pllLessId, $i) = split (/<tab>/, $pllId);
            if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
            $pllIndexCgiTitle = "title = \'$OEP_Topic{$i}\'";
            $pllIndexCgiText = "<a href=\'$indexcgi?action=open\&groupid=$pllGrpId\&lessonid=$i\&parid\=$pllPrntId\&studid\=$pllStudId\' $pllIndexCgiTitle>";
            print "<tr $myclr><td>$pllIndexCgiText Урок $OEP_Lesson{$i} [ $OEP_Date{$i} ] </a></td>"; $glsVisitsPerLesson = 0;
            foreach $x (@glsStudentsList){ if ( $studentGroupNum{$x} eq $pllGrpId ) {
               $glsUserID_PRNum = $x . '_' . $i;  if($OEP_Participation{$glsUserID_PRNum} ne ''){$tdclr = $grnclr; $glsVisitsPerLesson++;} else {$tdclr = '';}
               print "<td $tdclr $ac>$OEP_Participation{$glsUserID_PRNum}</td>";
            } }
            print "<td $ac>$glsVisitsPerLesson</td></tr>\n";
        }
    }
    print "</table>\n";
}
#####################################################################################
############################### GET LESSONS SUB #####################################
#####################################################################################
sub getLessonSub {
      my ($glsGrpId, @rest) = @_;
      $glsgrpfile = $groups_folder . $glsGrpId . '.txt';
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
      }
}

#####################################################################################
############################## SHOW PAID DATA SUB ###################################
#####################################################################################
sub showPaidData { $spdEmail = $userEmail{$gotusrid}; $spdPrntId = $ParentUniqueId{$spdEmail}; # $ParentIndex = $ParentChildCnt{$tparntemail} . '_' . $tparntemail; 
   $spdChldId = $whatis{'child'}; $spdPrntIndx = $spdChldId . '_' . $spdEmail;                 # $ParentIndexInfo{$ParentIndex} = $tparntid . '_' . $tparntstudid; 
   $spdIndxInfo = $ParentIndexInfo{$spdPrntIndx};                                              # $ParentStudentExist{$ParentIndexInfo{$ParentIndex}} = 1;
   if ( $ParentStudentExist{$spdIndxInfo} == 1 ) { 
      ( $spdTmpPrntId, $spdStudId ) = split ( /_/, $spdIndxInfo );  $spdStudGrpId = $studentGroupNum{$spdStudId}; 
      &getGroupSub($spdStudGrpId, $spdStudId);   $spdPayId = $spdStudId . '<tab>' . $spdStudGrpId;
      #print "\n<!-- TmpPrntId:[$spdTmpPrntId] spdPrntId:[$spdPrntId] spdStudId:[$spdStudId] 
      #spdStudGrpId:[$spdStudGrpId] glGrpFound{$spdPayId}:[$glGrpFound{$spdPayId}] -->\n";
      if ( $spdTmpPrntId eq $spdPrntId && $spdStudId =~ /56BC/ && $spdStudGrpId ne '' && $glGrpFound{$spdPayId} == 1 ) { 
         print "<p> </p><table><caption><h3>Таблица Оплат Ученика</h3></caption>
         <tr $yelclr><td>ФИО</td><td>Оплата<br>№1</td><td>Оплата<br>№2</td>";
         if ( $spdStudGrpId =~ /M2/ || $spdStudGrpId =~ /M3/ ) { print "<td>Оплата<br>№3</td><td>Оплата<br>№4</td>"; }
         print "<td>На сегодня<br>ожидаем</td><td>На сегодня<br>получено</td>
         <td>На сегодня<br>не оплачено</td><td>Всего<br>за курс<br>ожидаем</td></tr>
         <tr $yelclr1><td>$b1 $studentFullName{$spdStudId} $b2</td>"; 
         @spdGroupDaysList = split (/, /, $OEP_Calendar{$spdStudGrpId}); $spdTodayNum = $calendarnumber{$datenow};
         $spdGroupPayDayOne = $spdGroupDaysList[7]; $spdGroupPayDayTwo = $spdGroupDaysList[14];
         if ( $spdTodayNum < $spdGroupPayDayOne ) { $spdMultiply = 0; }
         elsif ( $spdTodayNum < $spdGroupPayDayTwo ) { $spdMultiply = 1; }
         elsif ( $spdTodayNum > $spdGroupPayDayTwo ) { $spdMultiply = 2; }
         if ( $spdStudGrpId =~ /M2/ || $spdStudGrpId =~ /M3/ ) { 
            $spdGroupPayDayTri = $spdGroupDaysList[21]; $spdGroupPayDayFour = $spdGroupDaysList[28]; 
            if ( $spdTodayNum > $spdGroupPayDayTri ) { $spdMultiply = 3; }
            elsif ( $spdTodayNum > $spdGroupPayDayFour ) { $spdMultiply = 4; }
         }
         if ( $glPayStatusOne{$spdPayId} eq 'Free' ) { print "<td $ac>Бесплатно</td>"; $spdDayOnePayable = 0; } 
         else { $spdStdtTotalSum{$spdPayId} = $spdStdtTotalSum{$spdPayId} + $glMonthPayValue; $spdDayOnePayable = 1;    
            if ( $glPayOneDate{$spdPayId} =~ /\.20/ ) { print "<td>$glPayOneDate{$spdPayId}</td>";  
               $spdStdPaidValue{$spdPayId} = $spdStdPaidValue{$spdPayId} + $glMonthPayValue;  
            }  else { print "<td $ac>Нет</td>"; }
         }
         if ( $glPayStatusTwo{$spdPayId} eq 'Free' ) { print "<td $ac>Бесплатно</td>"; $spdDayTwoPayable = 0; }
         else { $spdStdtTotalSum{$spdPayId} = $spdStdtTotalSum{$spdPayId} + $glMonthPayValue; $spdDayTwoPayable = 1;    
             if ( $glPayTwoDate{$spdPayId} =~ /\.20/ ) { print "<td>$glPayTwoDate{$spdPayId}</td>";   
                 $spdStdPaidValue{$spdPayId} = $spdStdPaidValue{$spdPayId} + $glMonthPayValue; 
             }  else { print "<td $ac>Нет</td>"; }
         } 
         if ( $spdStudGrpId =~ /M2/ || $spdStudGrpId =~ /M3/ ) { 
             if ( $glPayStatusTri{$spdPayId} eq 'Free' ) { print "<td $ac>Бесплатно</td>"; $spdDayTriPayable = 0; }
             else { $spdStdtTotalSum{$spdPayId} = $spdStdtTotalSum{$spdPayId} + $glMonthPayValue; $spdDayTriPayable = 1;  
                 if ( $glPayThreeDate{$spdPayId} =~ /\.20/ ) { print "<td>$glPayThreeDate{$spdPayId}</td>"; 
                    $spdStdPaidValue{$spdPayId} = $spdStdPaidValue{$spdPayId} + $glMonthPayValue;  
                 }  else { print "<td $ac>Нет</td>"; }
             }
             if ( $glPayStatusFor{$spdPayId} eq 'Free' ) { print "<td $ac>Бесплатно</td>"; $spdDayForPayable = 0; }
             else { $spdStdtTotalSum{$spdPayId} = $spdStdtTotalSum{$spdPayId} + $glMonthPayValue; $spdDayForPayable = 1;
                 if ( $glPayFourDate{$spdPayId} =~ /\.20/ ) { print "<td>$glPayFourDate{$spdPayId}</td>";  
                    $spdStdPaidValue{$spdPayId} = $spdStdPaidValue{$spdPayId} + $glMonthPayValue;  
                 }  else { print "<td $ac>Нет</td>"; }
             }
         }
         if ( $spdMultiply == 0 ) { $spdTodayStdExpected{$spdPayId} = 0; }
         elsif ( $spdMultiply == 1 ) { $spdTodayStdExpected{$spdPayId} = $glMonthPayValue * $spdDayOnePayable; }
         elsif ( $spdMultiply == 2 ) { $spdTodayStdExpected{$spdPayId} = $glMonthPayValue * $spdDayOnePayable + $glMonthPayValue * $spdDayTwoPayable; }
         elsif ( $spdMultiply == 3 ) { $spdTodayStdExpected{$spdPayId} = $glMonthPayValue * $spdDayOnePayable + $glMonthPayValue * $spdDayTwoPayable + $glMonthPayValue * $spdDayTriPayable; }
         elsif ( $spdMultiply == 4 ) { $spdTodayStdExpected{$spdPayId} = $glMonthPayValue * $spdDayOnePayable + $glMonthPayValue * $spdDayTwoPayable + $glMonthPayValue * $spdDayTriPayable + $glMonthPayValue * $spdDayForPayable; }
         $spdStdUnpaidValue{$spdPayId} = $spdTodayStdExpected{$spdPayId} - $spdStdPaidValue{$spdPayId};
         if ( $spdStdUnpaidValue{$spdPayId} < 0 ) { $spdStdUnpaidValue{$spdPayId} = 0; }
         if ( $spdStdtTotalSum{$spdPayId} eq '' ) { $spdStdtTotalSum{$spdPayId} = 0; }
         if ( $spdStdPaidValue{$spdPayId} eq '' ) { $spdStdPaidValue{$spdPayId} = 0; }
         print "<td>$spdTodayStdExpected{$spdPayId}</td><td>$spdStdPaidValue{$spdPayId}</td>
         <td>$spdStdUnpaidValue{$spdPayId}</td><td>$spdStdtTotalSum{$spdPayId}</td></tr>\n";
         print "<tr $yelclr><td>День оплаты по плану: </td><td>$calendardate{$spdGroupPayDayOne}</td><td>$calendardate{$spdGroupPayDayTwo}</td>";
         if ( $spdStudGrpId =~ /M2/ || $spdStudGrpId =~ /M3/ ) { 
            print "<td>$calendardate{$spdGroupPayDayTri}</td><td>$calendardate{$spdGroupPayDayFour}</td>"; }
         print "<td></td><td></td><td></td><td></td></tr></table>";
      }
      else { print "<p> </p>\n<h3>$rf Данных по оплатам нет! $f2</h3>\n"; }
   }
   else { print "<p> </p>\n<h3>$rf Нет студента с номером [$spdChldId]! $f2</h3>\n"; }
}

#####################################################################################
################################ GET GROUP SUB ######################################
#####################################################################################
sub getGroupSub { my ($gpsGrpId, $gpsStdId) = @_;  $glPayId = $gpsStdId . '<tab>' . $gpsGrpId;  

   $ggsgrpfile = $groups_folder . $gpsGrpId . '_data.txt'; $ggsid = $gpsGrpId;
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
   
   $gpsPayDataFile = $groups_folder . $gpsGrpId . '_payments.txt'; $glGrpFound{$glPayId} = 0;
   #print "<!-- ggsgrpfile:[$ggsgrpfile] gpsPayDataFile:[$gpsPayDataFile] -->\n";
   open(INF, $gpsPayDataFile);    @paymentslist = <INF>;    close(INF); 
   foreach $i(@paymentslist){ #1<tab>56BC4703<tab>99-10-M2<tab><tab><tab><tab><tab>reserve
      ($tpaynum, $tpaystudid, $tpaystudgrp, $tpayonedate, $tpaytwodate, $tpaytridate, $tpayfordate, 
      $tpaystatusone, $tpaystatustwo, $tpaystatustri, $tpaystatusfor, @other) = split (/<tab>/, $i);
      #print "<!-- tpaystudid:[$tpaystudid] gpsStdId:[$gpsStdId] tpaystudgrp:[$tpaystudgrp] gpsGrpId:[$gpsGrpId] -->\n";
      if ( $tpaystudid eq $gpsStdId && $tpaystudgrp eq $gpsGrpId ) {  $glGrpFound{$glPayId} = 1;
         $glPayOneDate{$glPayId} = $tpayonedate;  $glPayTwoDate{$glPayId} = $tpaytwodate;
         $glPayThreeDate{$glPayId} = $tpaytridate;  $glPayFourDate{$glPayId} = $tpayfordate; 
         $glPayStatusOne{$glPayId} = $tpaystatusone; $glPayStatusTwo{$glPayId} = $tpaystatustwo; 
         $glPayStatusTri{$glPayId} = $tpaystatustri; $glPayStatusFor{$glPayId} = $tpaystatusfor;
      }
   }
}


#####################################################################################
########################### FINISH END BODY #########################################
#####################################################################################

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