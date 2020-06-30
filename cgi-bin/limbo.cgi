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
$students_file = $oe_folder . 'students.txt';
$legion_file = $oe_folder . 'legion.txt';
$legiongroups_file = $oe_folder . 'legiongroups.txt';
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$emailPattern = '^([a-zA-Z0-9][\w\_\.]{6,20})\@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,4})$';
$bas = $oe_folder  . 'bas.txt';
$end = $oe_folder . 'end.txt';
$indexcgi = 'limbo.cgi';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpregistercgi = 'http://accelerator.kvadra.kz/cgi-bin/register.cgi';
$httpparentviewcgi = 'http://accelerator.kvadra.kz/cgi-bin/parentview.cgi';
$httpschoolviewcgi = 'http://accelerator.kvadra.kz/cgi-bin/schoolview.cgi';
$httplessonviewcgi = 'http://accelerator.kvadra.kz/cgi-bin/lessonview.cgi';
$title = 'Candidates Home page';

open(INF, $cookie_file); @cookielist = <INF>; close(INF); foreach $i(@cookielist){
    chomp($i); #8<tab>8250732421875<tab>Tue Apr 23 14:16:01 2013<tab>172.28.113.66<tab>reserve
    ($clusrnum, $clusrrnd, $clusrdate, $clusrip, @other) = split (/<tab>/, $i);
    $oeusercookiernd{$clusrnum} = $clusrrnd;
    $oeusercookiedate{$clusrnum} = $clusrdate;
    $oeusercookieip{$clusrnum} = $clusrip;
}

open(INF, $legion_file);   @legionlist = <INF>;   close(INF);
open(INF, $legiongroups_file);   @legiongroupslist = <INF>;   close(INF);

open(INF, $students_file); @studentslist = <INF>; close(INF); foreach $i(@studentslist){ 
   ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp, 
   $tstudbrthd, $tstudphnm, $tstudclss, $tstudemail, @other) = split (/<tab>/, $i);
   if ( $tstudnum ne '' && $tstudid =~ /56BC/ && $tstudemail =~ /$emailPattern/ ){ 
      $tstudemail = lc $tstudemail; $tstudemail =~s/ //g; $studentEmailExist{$tstudemail} = 1; 
      $studentFullName{$tstudemail} = "$tstudfirstnam $tstudthrdnam $tstudscndnam"; }
}

open(INF, $users_file); @userlist = <INF>; close(INF); foreach $i(@userlist){ 
   #3<tab>Болатхан<tab>Джайдаринов<tab><tab>america<tab>8 777 277 0326<tab>candidate<tab>b.jaidarinov@gmail.com
   #<tab>25.07.2019<tab>12.07.1976<tab>Male<tab>85 room<tab>1233333<tab>12341556688<tab>reserve
   ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, $tusrtype, $tusreml, $tusrcreated,
   $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $i);
   $tusreml = lc $tusreml; $tusreml =~s/ //g;
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
   if ( $userCategory{$gotusrid} eq 'Parent' && $whatis{'action'} eq 'show' ) { &printChildrenDataSub(); }
   elsif ( $userCategory{$gotusrid} eq 'Parent' && $whatis{'action'} eq 'new' ) { &newChildDataSub(); }
   elsif ( $userCategory{$gotusrid} eq 'Parent' && $whatis{'action'} eq 'edit' ) { &editChildrenDataSub(); }
   elsif ( $userCategory{$gotusrid} eq 'Parent' && $whatis{'action'} eq 'save' ) { &saveChildrenDataSub(); }
   elsif ( $userCategory{$gotusrid} eq 'School' && $userType{$gotusrid} eq 'confirmed' && $whatis{'action'} eq 'show' ) { &showSchoolDataSub(); }
   elsif ( $userCategory{$gotusrid} eq 'Volonteer' && $userType{$gotusrid} eq 'confirmed' && $whatis{'action'} eq 'show' ) { &showVolonteerDataSub(); }
   else { &openBlankPage(); }
}
else{
    if ( $whatis{'action'} eq 'login' && $userlogged != 1) { print "<p>$rf $errorlogin $f2</p>\n" ; }  
    print "<form method='post' action=\'$httpindexcgi\'><table><caption>Enter Login Data</caption><tr><td>Email: </td>
    <td><input type = 'text'  name = 'email'></td>  <td>Password: </td><td><input type = 'password'  name = 'userpwd'> </td>
    <td><input type = 'hidden' name = 'action' value = 'login'> <input type = 'submit' value = 'Enter'></td></tr></table></form>\n";
    print "<p><a href=\'$httpregistercgi?action=email\'>Обновить Персональные Данные</a></p>";
}
#####################################################################################
########################### START MAIN BODY #########################################
#####################################################################################
sub openBlankPage {
   # ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, $tusrtype, $tusreml, $tusrcreated,
   # $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, $tusrindvdid, $tusrstats, $tusrschoolid, @other) = split (/<tab>/, $i);
   # $userCategory{$tusrid} = $tusrgndr; $userFullName{$tusrid} = "$tusrfrstnam $tusrthrdname $tusrscndnam";
   # $userFirstName{$tusrid} = $tusrfrstnam; $userSecondName{$tusrid} = $tusrscndnam; $userThirdName{$tusrid} = $tusrthrdname;
   # $userpwd{$tusreml} = $tusrpwd; $userpwd{$tusrid} = $tusrpwd; $userPhoneNumber{$tusrid} = $tusrphnnum;
   # $userType{$tusrid} = $tusrtype; $userEmail{$tusrid} = $tusreml; $userEmailExist{$tusreml} = 1;  
   # $userCreateDate{$tusrid} = $tusrcreated; $userBirthDay{$tusrid} = $tusrbrthday; 
   # $userGender{$tusrid} = $tusrgndr; $userWorkPlace{$tusrid} = $tusrwrkplc; $userPersonId{$tusrid} = $tusrprsnid;
   # $userIndivideId{$tusrid} = $tusrindvdid; $userStatus{$tusrid} = $tusrstats; $userSchoolId{$tusrid} = $tusrschlid;
   
   if ( $userType{$gotusrid} eq 'confirmed' ) { print "<p> </p><table><tr $grnclr>
      <td><h3>Поздравляю, Ваши данные утверждены!</h3></td></tr></table>\n"; }
   else { print "<h2>Ваши данные переданы координатору.</h2><table><tr $yelclr>
      <td><h3>Пожалуйста, подождите пока координатор активирует ваш статус.
      <br>Все изменения будут отражены на текущей странице.</h3></td></tr></table>\n";  }
   print "<p> </p>\n<table><caption><h3>Ваши персональные данные</h3></caption>
   <tr $yelclr><td>Дата регистрации в системе: </td><td>$b1 $userCreateDate{$gotusrid} $b2</td></tr>
   <tr $yelclr1><td>Ваше имя: </td><td>$userFirstName{$gotusrid}</td></tr>
   <tr $yelclr><td>Фамилия: </td><td>$userSecondName{$gotusrid}</td></tr>
   <tr $yelclr1><td>Отчество: </td><td>$userThirdName{$gotusrid}</td></tr>
   <tr $yelclr><td>Номер телефона: </td><td>$userPhoneNumber{$gotusrid}</td></tr>
   <tr $yelclr1><td>EMAIL: </td><td>$userEmail{$gotusrid}</td></tr>\n";
   if ( $userCategory{$gotusrid} eq 'School' || $userCategory{$gotusrid} eq 'Parent' ) { 
      print "<tr $yelclr><td>Школа: </td><td>$userSchoolId{$gotusrid}</td></tr>\n"; }
   elsif ( $userCategory{$gotusrid} eq 'Volonteer' ) {
       print "<tr $yelclr><td>Дата рождения: </td><td>$userBirthDay{$gotusrid}</td></tr>
       <tr $yelclr1><td>Пол: </td><td>$userGender{$gotusrid}</td></tr>
       <tr $yelclr><td>Место учебы / работы: </td><td>$userWorkPlace{$gotusrid}</td></tr>
       <tr $yelclr1><td>Номер удостоверения: </td><td>$userPersonId{$gotusrid}</td></tr>
       <tr $yelclr><td>ИИН: </td><td>$userIndivideId{$gotusrid}</td></tr>
       <tr $yelclr1><td>Занятость: </td><td>$userStatus{$gotusrid}</td></tr>\n";
   }
   print "</table>\n <p> </p>\n";
   if ( $userCategory{$gotusrid} eq 'Parent' ) { 
      print "<p> </p> <table><tr $yelclr><td $ac><a href=\'$httpindexcgi?action=show\'><h3>Информация по ученикам</h3></a></td></tr>
      <tr $yelclr1><td $ac><a href=\'$httpparentviewcgi\'><h3>Посмотреть уроки и Оплату</h3></a></td></tr></table>\n"; }
   elsif ( $userType{$gotusrid} eq 'confirmed' && $userCategory{$gotusrid} eq 'School' ) { 
      print "<p> </p> <a href=\'$httpschoolviewcgi\'><h3>Полезная Информация по Оплатам</h3></a>
      <p> </p> <a href=\'$httplessonviewcgi\'><h3>Полезная Информация по Урокам</h3></a>\n"; }
   elsif ( $userType{$gotusrid} eq 'confirmed' ) { 
      print "<p> </p> <a href=\'$httpindexcgi?action=show\'><h3>Полезная Информация</h3></a>\n"; }
   print "<p> </p> <a href=\'$httpregistercgi?action=show\'><h3>Обновить Персональные Данные</h3></a>\n";
}

#######################################################################################
########################## PRINT CHILDREN DATA SUB ####################################
#######################################################################################
sub printChildrenDataSub { &printjavascript();
  print "<h3>Список учеников</h3><p> </p>\n"; $pcdChildFound = 0; $myclr = $yelclr;
  open(INF, $children_file); @childrenlist = <INF>; close(INF);  
  foreach $scdLine (@childrenlist) { $scdChompLine = $scdLine; chomp($scdChompLine);
      ($tparntid, $tchildid, $tchildfirstnam, $tchildscndnam, $tchildthrdnam, $tusrtype, $tchildschl, $tchildclss, $tchildprd,
      $tchildemail, $tchildphn, $tchildbrthd, $tchildgndr, $tchildcreated, @other) = split (/<tab>/, $scdChompLine);
      if ( $gotusrid eq $tparntid ) { $pcdChildFound = 1;
         if ( $tusrtype eq 'confirmed' ) { $pcdEditConfirmed = 'Ученик утвержден!'; }
         else { $pcdEditConfirmed = "<button onclick=\"return checkEditFunction\($tchildid\)\;\">Редактировать</button>"; }
         $pcdHtmlLine = "<td>$tchildfirstnam $tchildthrdnam $tchildscndnam</td><td>$tchildschl</td><td>$tchildclss</td>
         <td>$pcdEditConfirmed</td><td>$tchildprd</td>
         <td>$tchildemail</td><td>$tchildphn</td><td>$tchildbrthd</td><td>$tchildgndr</td><td>$tchildcreated</td>";
         push(@pcdChildrenList, $pcdHtmlLine);
      }
  }
  if ( $pcdChildFound == 1 ) { 
     print "<table><tr $myclr><td>No</td><td>ФИО ученика</td><td>Школа</td><td>Класс</td><td>Редактировать</td>
     <td>Смена</td><td>Email</td><td>Телефон</td><td>Дата рождения</td><td>Пол</td><td>Дата регистрации</td></tr>";
     foreach $i (@pcdChildrenList) { $cnt++;
        if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
        print "<tr $myclr><td>$cnt</td> $i </tr>\n";
     }
     print "</table><button onclick=\"window.location.href = \'$httpindexcgi?action=new';\" 
     style='height:50px; width:150px'>Добавить Нового Ученика</button>
     <p> </p> <p align = 'center'><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";
  }
  else { print "<button onclick=\"window.location.href = \'$httpindexcgi?action=new';\" 
     style='height:50px; width:150px'>Добавить Нового Ученика</button><p> </p>
     <p>Нет данных для показа..</p><p align = 'center'><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; }
}

#######################################################################################
############################ SHOW SCHOOL DATA SUB #####################################
#######################################################################################
sub showSchoolDataSub {
  print "<h3>Список доступных групп</h3><p> </p>\n";
  if ( $userSchoolId{$gotusrid} ne '' && $userType{$gotusrid} eq 'confirmed' ) { 
     print "<h3>Школа № $userSchoolId{$gotusrid}</h3><p> </p> <p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n";
  }
  else { print "<p> </p><p>Нет активной школы для показа..</p><p align = 'center'><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; }
}

#######################################################################################
######################### SHOW VOLONTEER DATA SUB #####################################
#######################################################################################
sub showVolonteerDataSub { $svdUserGroupFound = 0;
   print "<h3>Страница волонтёра</h3><p> </p>\n";
   if ( $userType{$gotusrid} eq 'confirmed' ) { 
      foreach $svdLegLine (@legionlist) { chomp($svdLegLine);
         ($tlgnrnum, $tlgnrid, $tlgnrgrp, $tlgnrcndtnum, $tlgnrctgr, $tlgnrfirstname, $tlgnrsecondname, 
         $tlgnrthirdname, $tlgnrpwd, $tlgnrphone, $tlgnrstat, $tlgnremail, @other) = split (/<tab>/, $svdLegLine);
         #print "<!-- tlgnremail:[$tlgnremail] userEmail{$gotusrid}:[$userEmail{$gotusrid}] -->\n";
         if ( $tlgnrstat eq 'confirmed' && $tlgnrid =~ /22LEG/ && $tlgnremail eq $userEmail{$gotusrid} ){ 
            $svdGrpId = $tlgnrgrp; $svdUserGroupFound = 1; }
      }
      if ( $svdUserGroupFound == 1 ) { $whatis{'groupid'} = $svdGrpId; &getGroupSub();
         print "<p> </p><table>   
         <tr $yelclr><td>Уникальное описание группы: </td><td $ac>$LEG_Description{$svdGrpId}</td>
         <td>Статус группы: </td><td $ac>$LEG_Status{$svdGrpId}</td></tr>
         <tr $yelclr1><td>Название Тренинга: </td><td $ac>$LEG_Course{$svdGrpId}</td>
         <td>Кто Ведет Тренинг: </td><td $ac>$LEG_Traineer{$svdGrpId}</td></tr>
         <tr $yelclr><td>Дата начала обучения: </td><td $ac>$LEG_StartDate{$svdGrpId}</td>
         <td>Когда создали группу: </td><td $ac>$LEG_Created{$svdGrpId}</td></tr>
         <tr $yelclr1><td>Дата 1-го Занятия: </td><td $ac>$LEG_DayOne{$svdGrpId}</td>
         <td>Время 1-го Занятия: </td><td $ac>$LEG_TimeOne{$svdGrpId}</td></tr>
         <tr $yelclr><td>Дата 2-го Занятия: </td><td $ac>$LEG_DayTwo{$svdGrpId}</td>
         <td>Время 2-го Занятия: </td><td $ac>$LEG_TimeTwo{$svdGrpId}</td></tr>
         <tr $yelclr1><td>Дата 3-го Занятия: </td><td $ac>$LEG_DayThree{$svdGrpId}</td>
         <td>Время 3-го Занятия: </td><td $ac>$LEG_TimeThree{$svdGrpId}</td></tr>
         <tr $yelclr><td>Дата 4-го Занятия: </td><td $ac>$LEG_DayFour{$svdGrpId}</td>
         <td>Время 4-го Занятия: </td><td $ac>$LEG_TimeFour{$svdGrpId}</td></tr>
         <tr $yelclr1><td>Дата 5-го Занятия: </td><td $ac>$LEG_DayFive{$svdGrpId}</td>
         <td>Время 5-го Занятия: </td><td $ac>$LEG_TimeFive{$svdGrpId}</td></tr>
         <tr $yelclr><td>Дата 6-го Занятия: </td><td $ac>$LEG_DaySix{$svdGrpId}</td>
         <td>Время 6-го Занятия: </td><td $ac>$LEG_TimeSix{$svdGrpId}</td></tr>
         <tr $yelclr1><td>Дата Коучинг Занятия: </td><td $ac>$LEG_CouchDay{$svdGrpId}</td>
         <td>Время Коучинг Занятия: </td><td $ac>$LEG_CouchTime{$svdGrpId}</td></tr>
         <tr $yelclr><td>Дата Пробного Занятия: </td><td $ac>$LEG_TestDay{$svdGrpId}</td>
         <td>Время Пробного Занятия: </td><td $ac>$LEG_TestTime{$svdGrpId}</td></tr>
         </table><p> </p>\n";
      }
      else { print "<p> </p><h3>Нет активной группы для показа..</h3><p> </p>\n"; }
     
     print "<p> </p> <p align = 'center'><a href=\'$httpindexcgi\'>HOME</a></p>\n";
  }
  else { print "<p> </p><p>Нет данных для показа..</p><p align = 'center'><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; }
}

#####################################################################################
############################## NEW CHILD DATA SUB ###################################
#####################################################################################
sub newChildDataSub {
   &printjavascript(); $ncdParntId = $ParentUniqueId{$ncdUsrId};
   print "<h2>Записать данные нового ученика</h2>\n"; $ncdStyle = "style='height:50px; width:150px'";
   print "<form method='post' action=\'$httpindexcgi\' onsubmit='return checkSaveFunction();'>
   <input type = 'hidden' name = 'action' value = 'save'><input type = 'hidden' name = 'child' value = 'new'>
   <table><tr $yelclr><td>1</td><td>Имя: $rf * $f2</td><td><input type = 'text' name = 'firstname' value = ''></td></tr>
   <tr $yelclr1><td>2</td><td>Фамилия: $rf * $f2</td><td><input type = 'text' name = 'secondname' value = ''></td></tr>
   <tr $yelclr><td>3</td><td>Отчество: </td><td><input type = 'text' name = 'thirdname' value = ''></td></tr>
   <tr $yelclr1><td>4</td><td>Школа: $rf * $f2</td><td><input type = 'text' name = 'schoolid' value = ''></td></tr>
   <tr $yelclr><td>5</td><td>Класс (с литерой): $rf * $f2</td><td><input type = 'text' name = 'class' value = ''></td></tr>
   <tr $yelclr1><td>6</td><td>Смена: $rf * $f2</td><td><input type = 'text' name = 'period' value = ''></td></tr>
   <tr $yelclr><td>7</td><td>EMAIL: $rf * $f2</td><td><input type = 'text' name = 'email' value = ''></td></tr>
   <tr $yelclr1><td>8</td><td>Номер телефона: $rf * $f2</td><td><input type = 'text' name = 'phone' value = ''></td></tr>
   <tr $yelclr><td>9</td><td>Дата рождения: $rf * $f2</td><td><input type = 'text' name = 'birthday' value = ''></td></tr>
   <tr $yelclr1><td>10</td><td>Пол ученика: $rf * $f2</td><td><select name = 'gender'><option value = ''>Выберите пол</option>
   <option value = 'Мужской'>Мужской</option><option value = 'Женский'>Женский</option></select></td></tr>
   </table> <input type='reset' value = 'ОТМЕНИТЬ' $ncdStyle>-[ ]-[ ]-[ ]-<input type = 'submit' value = 'ЗАПИСАТЬ' $ncdStyle></form>
   <p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
}

#####################################################################################
########################## EDIT CHILDREN DATA SUB ###################################
#####################################################################################
sub editChildrenDataSub {
   &printjavascript(); $ecdUsrId = $whatis{'userid'};  $ecdStyle = "style='height:50px; width:150px'";
   print "<h2>Изменение данных ученика</h2>\n"; $ecdChildFound = 0;
   open(INF, $children_file); @childrenlist = <INF>; close(INF); 
   foreach $ecdLine (@childrenlist) { $ecdChompLine = $ecdLine; chomp($ecdChompLine);
      ($tparntid, $tchildid, $tchildfirstnam, $tchildscndnam, $tchildthrdnam, $tusrtype, $tchildschl, $tchildclss, $tchildprd,
      $tchildemail, $tchildphn, $tchildbrthd, $tchildgndr, $tchildcreated, @other) = split (/<tab>/, $ecdChompLine);
      if ( $tchildid eq $ecdUsrId && $tusrtype eq 'candidate' ) { $ecdChildFound = 1; 
         if ( $tchildemail ne '' ) { $tchildemail = lc $tchildemail; $tchildemail =~s/ //g; }
         print "<form method='post' action=\'$httpindexcgi\' onsubmit='return checkSaveFunction();'>
         <input type = 'hidden' name = 'action' value = 'save'><input type = 'hidden' name = 'userid' value = \'$ecdUsrId\'>
         <input type = 'hidden' name = 'type' value = \'$tusrtype\'><input type = 'hidden' name = 'child' value = 'old'>
         <table><tr $yelclr><td>1</td><td>Имя: </td><td><input type = 'text' name = 'firstname' value = \'$tchildfirstnam\'></td></tr>
         <tr $yelclr1><td>2</td><td>Фамилия: </td><td><input type = 'text' name = 'secondname' value = \'$tchildscndnam\'></td></tr>
         <tr $yelclr><td>3</td><td>Отчество: </td><td><input type = 'text' name = 'thirdname' value = \'$tchildthrdnam\'></td></tr>
         <tr $yelclr1><td>4</td><td>Школа: </td><td><input type = 'text' name = 'schoolid' value = \'$tchildschl\'></td></tr>
         <tr $yelclr><td>5</td><td>Класс (с литерой): </td><td><input type = 'text' name = 'class' value = \'$tchildclss\'></td></tr>
         <tr $yelclr1><td>6</td><td>Смена: </td><td><input type = 'text' name = 'period' value = \'$tchildprd\'></td></tr>
         <tr $yelclr><td>7</td><td>EMAIL: </td><td><input type = 'text' name = 'email' value = \'$tchildemail\'></td></tr>
         <tr $yelclr1><td>8</td><td>Номер телефона: </td><td><input type = 'text' name = 'phone' value = \'$tchildphn\'></td></tr>
         <tr $yelclr><td>9</td><td>Дата рождения: </td><td><input type = 'text' name = 'birthday' value = \'$tchildbrthd\'></td></tr>
         <tr $yelclr1><td>10</td><td>Пол ученика: </td><td><select name = 'gender'><option value = ''>Выберите пол</option>";
         if ( $tchildgndr ne '' ) { print "<option value = \'$tchildgndr\' selected>$tchildgndr</option>"; }
         print "<option value = 'Мужской'>Мужской</option><option value = 'Женский'>Женский</option></select></td></tr>
         </table> <input type='reset' value = 'ОТМЕНИТЬ' $ecdStyle>-[ ]-[ ]-[ ]-<input type = 'submit' value = 'ЗАПИСАТЬ' $ecdStyle>
         <input type = 'hidden' name = 'created' value = \'$tchildcreated\'></form><p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
      }
   }
   if ( $ecdChildFound == 0 ) { 
      print "<h3>$rf Неверные данные, запись не найдена! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; }
}
#####################################################################################
######################## SAVE CHILDREN DATA SUB #####################################
#####################################################################################
sub saveChildrenDataSub { # $glLastParentNumber = $tparntnum; $glLastParentCode = $tparntid;
   print "<h2>Сохранение данных ученика</h2>\n"; $scdUsrId = $whatis{'userid'}; $scdChildPlaceNum = 0;
   if ( $whatis{'child'} eq 'new' ) { $whatis{'created'} = $timedatenow; $whatis{'type'} = 'candidate'; }
   $scdNewLineText = "<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}<tab>$whatis{'type'}<tab>$whatis{'schoolid'}";
   $scdNewLineText = $scdNewLineText . "<tab>$whatis{'class'}<tab>$whatis{'period'}<tab>$whatis{'email'}<tab>$whatis{'phone'}";
   $scdNewLineText = $scdNewLineText . "<tab>$whatis{'birthday'}<tab>$whatis{'gender'}<tab>$whatis{'created'}<tab>reserve\n";
   
   # $studentEmailExist{$tstudemail} = 1;       $studentFullName{$tstudemail} = "$tstudfirstnam $tstudthrdnam $tstudscndnam";
   if ( $studentEmailExist{$whatis{'email'}} == 1 && $whatis{'email'} ne '' ) { print "<h3>$rf Email $b1 [$whatis{'email'}]
       $b2 уже используется! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; return; }
   open(INF, $children_file); @childrenlist = <INF>; close(INF);  
   foreach $scdLine (@childrenlist) { $scdChompLine = $scdLine; chomp($scdChompLine);
      ($tparntid, $tchildid, $tchildfirstnam, $tchildscndnam, $tchildthrdnam, $tusrtype, $tchildschl, $tchildclss, $tchildprd,
      $tchildemail, $tchildphn, $tchildbrthd, $tchildgndr, $tchildcreated, @other) = split (/<tab>/, $scdChompLine);
      if ( $tparntid eq $gotusrid ) { $scdChildPlaceNum = $tchildid;
         if ( $tchildid eq $whatis{'userid'} && $whatis{'userid'} ne '' ) { 
            $scdNewLineText = "$gotusrid<tab>$tchildid" . $scdNewLineText; push(@scdNewChildrenList, $scdNewLineText); }
         else { push(@scdNewChildrenList, $scdLine); }
      }
      else { if ( $scdLine ne '' ) { push(@scdNewChildrenList, $scdLine); } }
   }   
   if ( $whatis{'child'} eq 'new' ) {      $scdChildPlaceNum++; 
      $scdNewLineText = "$gotusrid<tab>$scdChildPlaceNum" . $scdNewLineText; push(@scdNewChildrenList, $scdNewLineText);
   }
   open(SSDATA,">$children_file");    print SSDATA @scdNewChildrenList;    close(SSDATA);
   print "<table $grnclr><tr><td><h2>Данные изменения внесены в систему.</h2></td></tr></table>\n
   <p> </p><table><tr $yelclr><td>1</td><td>Дата регистрации ученика: </td><td>$whatis{'created'}</td></tr>
   <tr $yelclr1><td>2</td><td>Имя ученика: </td><td>$whatis{'firstname'}</td></tr>
   <tr $yelclr><td>3</td><td>Фамилия ученика: </td><td>$whatis{'secondname'}</td></tr>
   <tr $yelclr1><td>4</td><td>Отчество ученика: </td><td>$whatis{'thirdname'}</td></tr>
   <tr $yelclr><td>5</td><td>Номер школы: </td><td>$whatis{'schoolid'}</td></tr>
   <tr $yelclr1><td>6</td><td>Класс (с литерой): </td><td>$whatis{'class'}</td></tr>
   <tr $yelclr><td>7</td><td>Смена: </td><td>$whatis{'period'}</td></tr>
   <tr $yelclr1><td>8</td><td>EMAIL: </td><td>$whatis{'email'}</td></tr>
   <tr $yelclr><td>9</td><td>Номер телефона: </td><td>$whatis{'phone'}</td></tr>
   <tr $yelclr1><td>10</td><td>Дата рождения: </td><td>$whatis{'birthday'}</td></tr>
   <tr $yelclr><td>11</td><td>Пол ученика: </td><td>$whatis{'gender'}</td></tr></table>
   <p> </p><p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
}

#####################################################################################
################################# GET GROUP SUB ##################################### 
#####################################################################################
sub getGroupSub {
      $ggsgrpfile = $groups_folder . $whatis{'groupid'} . '_data.txt'; $ggsid = $whatis{'groupid'};
      open(UPL, $ggsgrpfile);       @ggsprojectlist = <UPL>;      close(UPL);
      foreach $i (@ggsprojectlist){  chomp($i);  if($i =~ /<start of new project = /){ $donothing = 1; }
          elsif($i =~ /LEG_Created: /){$i =~ s/LEG_Created: //g; $LEG_Created{$ggsid} = $i;}
          elsif($i =~ /LEG_Creator: /){$i =~ s/LEG_Creator: //g; $LEG_Creator{$ggsid} = $i;}
          elsif($i =~ /LEG_LastEdited: /){$i =~ s/LEG_LastEdited: //g; $LEG_LastEdited{$ggsid} = $i;}
          elsif($i =~ /LEG_Editor: /){$i =~ s/LEG_Editor: //g; $LEG_Editor{$ggsid} = $i;}
          elsif($i =~ /LEG_Description: /){$i =~ s/LEG_Description: //g; $LEG_Description{$ggsid} = $i;}
          elsif($i =~ /LEG_Status: /){$i =~ s/LEG_Status: //g; $LEG_Status{$ggsid} = $i;}
          elsif($i =~ /LEG_Course: /){$i =~ s/LEG_Course: //g; $LEG_Course{$ggsid} = $i;}
          elsif($i =~ /LEG_Traineer: /){$i =~ s/LEG_Traineer: //g; $LEG_Traineer{$ggsid} = $i;}
          elsif($i =~ /LEG_Group: /){$i =~ s/LEG_Group: //g; $LEG_Group{$ggsid} = $i;}
          elsif($i =~ /LEG_StartDate: /){$i =~ s/LEG_StartDate: //g; $LEG_StartDate{$ggsid} = $i;}
          elsif($i =~ /LEG_DayOne: /){$i =~ s/LEG_DayOne: //g; $LEG_DayOne{$ggsid} = $i;}
          elsif($i =~ /LEG_DayTwo: /){$i =~ s/LEG_DayTwo: //g; $LEG_DayTwo{$ggsid} = $i;}
          elsif($i =~ /LEG_DayThree: /){$i =~ s/LEG_DayThree: //g; $LEG_DayThree{$ggsid} = $i;}
          elsif($i =~ /LEG_DayFour: /){$i =~ s/LEG_DayFour: //g; $LEG_DayFour{$ggsid} = $i;}
          elsif($i =~ /LEG_DayFive: /){$i =~ s/LEG_DayFive: //g; $LEG_DayFive{$ggsid} = $i;}
          elsif($i =~ /LEG_DaySix: /){$i =~ s/LEG_DaySix: //g; $LEG_DaySix{$ggsid} = $i;}
          elsif($i =~ /LEG_CouchDay: /){$i =~ s/LEG_CouchDay: //g; $LEG_CouchDay{$ggsid} = $i;}
          elsif($i =~ /LEG_TestDay: /){$i =~ s/LEG_TestDay: //g; $LEG_TestDay{$ggsid} = $i;}
          elsif($i =~ /LEG_TimeOne: /){$i =~ s/LEG_TimeOne: //g; $LEG_TimeOne{$ggsid} = $i;}
          elsif($i =~ /LEG_TimeTwo: /){$i =~ s/LEG_TimeTwo: //g; $LEG_TimeTwo{$ggsid} = $i;}
          elsif($i =~ /LEG_TimeThree: /){$i =~ s/LEG_TimeThree: //g; $LEG_TimeThree{$ggsid} = $i;}
          elsif($i =~ /LEG_TimeFour: /){$i =~ s/LEG_TimeFour: //g; $LEG_TimeFour{$ggsid} = $i;}
          elsif($i =~ /LEG_TimeFive: /){$i =~ s/LEG_TimeFive: //g; $LEG_TimeFive{$ggsid} = $i;}
          elsif($i =~ /LEG_TimeSix: /){$i =~ s/LEG_TimeSix: //g; $LEG_TimeSix{$ggsid} = $i;}
          elsif($i =~ /LEG_CouchTime: /){$i =~ s/LEG_CouchTime: //g; $LEG_CouchTime{$ggsid} = $i;}
          elsif($i =~ /LEG_TestTime: /){$i =~ s/LEG_TestTime: //g; $LEG_TestTime{$ggsid} = $i;}
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

#######################################################################################
########################## JAVASCRIPT PART ###########################################
#######################################################################################
sub printjavascript {
print  <<EOT;
 <script>
 function checkSaveFunction (){
   if(document.getElementsByName('firstname')[0].value == ''){alert('Укажите имя!'); return false;}
   if(document.getElementsByName('secondname')[0].value == ''){alert('Укажите фамилию!'); return false;}
   if(document.getElementsByName('schoolid')[0].value == ''){alert('Укажите школу!'); return false;}
   if(document.getElementsByName('class')[0].value == ''){alert('Укажите класс!'); return false;}
   if(document.getElementsByName('period')[0].value == ''){alert('Укажите смену!'); return false;}
   if(document.getElementsByName('email')[0].value == ''){alert('Укажите Email ученика!'); return false;}
   if(document.getElementsByName('phone')[0].value == ''){alert('Укажите номер телефона!'); return false;}
   if(document.getElementsByName('birthday')[0].value == ''){alert('Укажите Дату рождения!'); return false;}
   var usr = document.getElementsByName('birthday')[0].value;
   if (isValidDate(usr)) { document.getElementsByName('birthday')[0].value = usr; }
   else {alert('Неправильная дата: [' + usr + ']!'); return false;}
   if(document.getElementsByName('gender')[0].value == ''){alert('Выберите пол ученика!'); return false;}
 }
 function checkEditFunction (cnt) {
     var userlink = \'$httpindexcgi\?action=edit\&userid=' + cnt;
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