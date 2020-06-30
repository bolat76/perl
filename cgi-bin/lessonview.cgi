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
$groups_folder = '../oedata/groups/';
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$glMonthPayValue = 5500;
$indexcgi = 'lessonview.cgi';
$students_file = $oe_folder . 'students.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httplimbocgi = 'http://accelerator.kvadra.kz/cgi-bin/limbo.cgi';
$httpschlviewcgi = 'http://accelerator.kvadra.kz/cgi-bin/schoolview.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Уроки';

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
   #1<tab>56BC4567<tab>Томирис<tab>Толенді<tab><tab>71<tab>71-1-M1
   #$usernum<tab>$userID<tab>$user1stname<tab>$user2ndname<tab>$user3rdname<tab>$userschool<tab>$usergroup<tab>$other
   ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp, @other) = split (/<tab>/, $i);
   if ( $tstudgrp ne '' && $tstudschl ne '' ) { $studentFullName{$tstudid} = "$tstudfirstnam $tstudscndnam";
      $studentFirstName{$tstudid} = $tstudfirstnam; $studentSecondName{$tstudid} = $tstudscndnam;
      $studentThirdName{$tstudid} = $tstudthrdnam; $studentPositionNum{$tstudid} = $tstudnum; 
      $studentSchoolNum{$tstudid} = $tstudschl; $studentGroupNum{$tstudid} = $tstudgrp; $existSchool{$tstudschl}++;  $existGroup{$tstudgrp}++; 
      if ( grep( /^$tstudschl$/, @uniqueSchoolNumList ) ) { $done = 1; } else { push(@uniqueSchoolNumList, $tstudschl); $totalSchools++; }
      if ( grep( /^$tstudgrp$/, @uniqueGroupNumList ) ) { $done = 1;} 
      else { $GroupsPerSchool{$tstudschl}++; $totalGroups++; push(@uniqueGroupNumList, $tstudgrp); $groupSchoolNum{$tstudgrp} = $tstudschl; }
      push(@studentUniqueNumList, $tstudid); $totalStudents++;
   }
}  # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents ;$totalSchools; $totalGroups

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
if ( $userlogged == 1 ) { $whatis{'schoolid'} = $userSchoolId{$gotusrid}; 
   print "Hello $b1 $userFirstName{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>";
   if ( $userCategory{$gotusrid} eq 'School' && $userType{$gotusrid} eq 'confirmed') {
      if ( $userSchoolId{$gotusrid} ne '' && $existSchool{$userSchoolId{$gotusrid}} > 0 ) { 
         if ( $whatis{'groupid'} ne '' ) { ($lcpQuerySchlId, @others) = split ( /-/, $whatis{'groupid'} ); }
         if ( $whatis{'groupid'} ne '' && $whatis{'schoolid'} eq $lcpQuerySchlId ) { 
            if ( $whatis{'action'} eq 'open' && $whatis{'lessonid'} ne '' ) { &openLessonSub(); }
            elsif ( $whatis{'action'} eq 'read' ) { &getLessonSub(); &printListLessons(); } 
            else { &openBlankPage(); } 
         }  
         else { &openBlankPage() ; }
      }
      else { print "<h3>Нет активной школы для показа..</h3><p> </p><p><a href=\'$httplimbocgi\'>[ Вернуться ДОМОЙ ]</a></p>\n"; } 
   }
   else { print "<h3>Нет активной школы для показа..</h3><p> </p><p><a href=\'$httplimbocgi\'>[ Вернуться ДОМОЙ ]</a></p>\n"; }
}
else{
    if ( $whatis{'action'} eq 'login' && $userlogged != 1) { print "<p>$rf $errorlogin $f2</p>\n" ; }  
    print "<form method='post' action=\'$httpindexcgi\'><table><caption>Enter Login Data</caption><tr><td>Email: </td>
    <td><input type = 'text'  name = 'email'></td>  <td>Password: </td><td><input type = 'password'  name = 'userpwd'> </td>
    <td><input type = 'hidden' name = 'action' value = 'login'> <input type = 'submit' value = 'Enter'></td></tr></table></form>\n";
    print "<p> </p> <p><a href=\'$httpregistercgi\'>РЕГИСТРАЦИЯ</a></p>";
}

#####################################################################################
########################### START MAIN BODY #########################################
#####################################################################################
sub openBlankPage {
   $myclr = $yelclr; $cnt = 0; $obpTxtLine = '';
   foreach $obpGrpId (@uniqueGroupNumList) { $cnt++;
      if ( $obpGrpId ne '' ) { ($obpSchlId, @others) = split ( /-/, $obpGrpId ); }
      if ( $obpSchlId eq $whatis{'schoolid'} ) {
         if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
         $obpTxtLine = $obpTxtLine . "<tr $myclr><td><a href=\'$httpindexcgi?action=list\&groupid\=$obpGrpId\'>$obpGrpId</a></td> 
         <td><a href=\'$httpschlviewcgi\'>Посмотреть оплату</a></td><td align='center'>$existGroup{$obpGrpId}</td>
         <td><a href=\'$httpindexcgi?action=read\&groupid\=$obpGrpId\'>Посмотреть историю уроков</a></td></tr>\n";
      }
   }
   if ( $obpTxtLine ne '' ) { 
       print "<p> </p><table><tr $myclr><td>Группа №</td><td>Платежи</td><td>Кол-во<br>учеников</td>\n";
       print "<td>История уроков</td></tr>$obpTxtLine</table>\n";
   }
   else { print "<h3>По Вашей школе $whatis{'schoolid'} нет активных групп для показа. <br>Пожалуйста уточните у координатора..</h3>\n"; }
   if ( $whatis{'action'} eq 'list' && $whatis{'groupid'} ne '' ) { ######## LIST of STUDENTS ###########
       print "<p> </p>\n"; $myclr = $yelclr; $cnt = 0;
       print "<table><tr $myclr><td>N</td><td>$whatis{'groupid'} Group</td></tr>\n";
       foreach $stdid (@studentUniqueNumList){
          ($obpSchlId, @others) = split ( /-/, $studentGroupNum{$stdid} );
          if ( $obpSchlId ne '' && $obpSchlId eq $whatis{'schoolid'} && $studentGroupNum{$stdid} eq $whatis{'groupid'} ) { $cnt++;
             if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
             # $existSchool{$tstudschl}; $existGroup{$tstudgrp}; $GroupsPerSchool{$tstudschl}; $totalStudents ;$totalSchools; $totalGroups
             print "<tr $myclr><td>$cnt</td><td>$studentFirstName{$stdid} $studentThirdName{$stdid} $studentSecondName{$stdid}</td></tr>\n";
          }
       } # $userSchoolId{$tusrid} = $tusrsclid; $userGroupId{$tusrid} = $tusrgrpid; 
       print "</table>\n";
   }
   print "<p> </p><p align = 'center'><a href=\'$httplimbocgi\'>[ Вернуться ДОМОЙ ]</a></p>\n";
}

#####################################################################################
############################### OPEN LESSON SUB #####################################
#####################################################################################
sub openLessonSub {
   ($olsSchlId, @others) = split ( /-/, $whatis{'groupid'} ); if ( $olsSchlId ne $whatis{'schoolid'} ) { return; }
   &getLessonSub();  $olsid = $whatis{'lessonid'};
   print "<p> </p><table><caption><a href=\'$httpindexcgi\'>$whatis{'schoolid'}-ая</a> Школа</caption>
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
   <p> </p><p align = 'center'><a href=\'$httpindexcgi\'>[ Вернуться НАЗАД ]</a></p>\n";
}
#####################################################################################
############################### GET LESSONS SUB #####################################
#####################################################################################
sub getLessonSub {
      ($glsSchlId, @others) = split ( /-/, $whatis{'groupid'} ); if ( $glsSchlId ne $whatis{'schoolid'} ) { return; }
      foreach $stdid (@studentUniqueNumList){ if($studentGroupNum{$stdid} =~/$whatis{'groupid'}/){  push(@glsStudentsList, $stdid); } }
      $glsgrpfile = $groups_folder . $whatis{'groupid'} . '.txt';
      open(UPL, $glsgrpfile);      @glsprojectlist = <UPL>;      close(UPL);      @glsProjectNumList = '';
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
########################## PRINT LIST OF LESSONS SUB ##################################
#####################################################################################
sub printListLessons {    
    ($pllSchlId, @others) = split ( /-/, $whatis{'groupid'} ); if ( $pllSchlId ne $whatis{'schoolid'} ) { return; }
    print "<p> </p><table><caption>Группа № $whatis{'groupid'}</caption><tr $yelclr><td>Уроки</td>\n";  
    foreach $i (@glsStudentsList){ 
       print "<td>$studentFirstName{$i}";  
       if ( $studentFirstName{$i} ne '' ) { print "<br>"; }
       print "$studentSecondName{$i}</td>"; 
    }
    print "<td>Всего</td></tr>\n";   $myclr = $yelclr;
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
            print "<td $ac>$glsVisitsPerLesson</td></tr>\n";
        }
    }
    print "</table>\n<p> </p><p align = 'center'><a href=\'$httpindexcgi\'>[ Вернуться НАЗАД ]</a></p>\n"; #list=groups&schoolid=71
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