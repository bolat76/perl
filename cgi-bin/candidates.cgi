#!/usr/bin/perl

print "Content-Type: text/html\n";
#######################################################################################
######### defining initial data
#######################################################################################
srand();

$b1 = '<b>'; $b2 = '</b>'; $u1 = '<u>'; $u2 = '<u2>';
$rf = '<font color = red>'; $f2 = '</font>'; $cnt = 0; $ac = "align = 'center'";
$ct1 = '</center>'; $ct2 = '</center>'; $hr = '<hr>'; $br = '<br>';
$grnclr1 = 'bgcolor = #CCFFCC;'; $grnclr2 = 'bgcolor = #99CCFF;';
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
$cands_file = '../oedata/cn_usrdata.txt';
$cands_archivefile = '../oedata/cn_archive_usrdata.txt';
$children_file = '../oedata/cn_childrendata.txt';
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
$indexcgi = 'candidates.cgi';
$students_file = $oe_folder . 'students.txt';
$parents_file = $oe_folder . 'parents.txt';
$log_students_file = $oe_folder . 'log_students.txt';
$leaders_file = $oe_folder . 'leaders.txt';
$legion_file = $oe_folder . 'legion.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpreadcgi = 'http://accelerator.kvadra.kz/cgi-bin/read.cgi';
$httplegioncgi = 'http://accelerator.kvadra.kz/cgi-bin/legion.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Read-Create-Edit Candidates';

open(INF, $cookie_file); @cookielist = <INF>; close(INF); foreach $i(@cookielist){
    chomp($i); #8<tab>8250732421875<tab>Tue Apr 23 14:16:01 2013<tab>172.28.113.66<tab>reserve
    ($clusrnum, $clusrrnd, $clusrdate, $clusrip, @other) = split (/<tab>/, $i);
    $oeusercookiernd{$clusrnum} = $clusrrnd;
    $oeusercookiedate{$clusrnum} = $clusrdate;
    $oeusercookieip{$clusrnum} = $clusrip;
}

open(INF, $legion_file);   @legionlist = <INF>;   close(INF);
open(INF, $cands_file);   @candslist = <INF>;   close(INF);
open(INF, $cands_archivefile);   @candsArchiveList = <INF>;   close(INF);

open(INF, $users_file); @userlist = <INF>; close(INF); foreach $i(@userlist){ 
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
    if ( $whatis{'action'} eq 'edit' && $whatis{'userid'} ne '' ) { &editCandidateSub(); }
    elsif ( $whatis{'action'} eq 'save' && $whatis{'userid'} ne '' ) { &saveCandidateDataSub(); }
    elsif ( $whatis{'action'} eq 'archive' && $whatis{'userid'} ne '' ) { &archiveCandidateDataSub(); }
    elsif ( $whatis{'action'} eq 'restore' && $whatis{'userid'} ne '' ) { &restoreArchiveDataSub(); }
    elsif ( $whatis{'action'} eq 'activate' && $whatis{'userid'} ne '' ) { &activateCandidateSub(); }
    elsif ( $whatis{'action'} eq 'editchild' && $whatis{'userid'} ne '' && $whatis{'childid'} ne '' ) { &editChildrenDataSub(); }
    elsif ( $whatis{'action'} eq 'savechild' && $whatis{'userid'} ne '' && $whatis{'childid'} ne '' ) { &saveChildrenDataSub(); }
    elsif ( $whatis{'action'} eq 'confirm' && $whatis{'userid'} ne '' && $whatis{'childid'} ne '' ) { &activateChildTypeSub(); }
    elsif ( $whatis{'action'} eq 'showarchive' ) { &showArchiveDataSub(); }
    elsif ( $whatis{'action'} eq 'showactive' ) { &showWorkGroupSub(); }
    else { &blankPageSub(); }
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
######################### ACTIVATE CHILD TYPE SUB ###################################
#####################################################################################
sub activateChildTypeSub { 
   print "<h2>Активация данных ученика</h2>\n"; $actUsrId = $whatis{'userid'}; $actChldId = $whatis{'childid'}; 
   
   #########################################################################################   
   ############################# Get id of parent and child ################################  
   open(INF, $students_file);   @studentslist = <INF>;   close(INF);
   foreach $actStudLine (@studentslist) { $actChompStudLine = $actStudLine; chomp($actChompStudLine);
      #($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp, 
      #$tstudbrthd, $tstudphnm, $tstudclss, $tstudemail, @other) = split (/<tab>/, $i);
      ($tstudnm, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp, 
      $tstudbrthd, $tstudphnm, $tstudclss, $tstudemail, @other) = split (/<tab>/, $actChompStudLine);
      if ( $tstudnm ne '' && $tstudid =~ /56BC/ ) { $actNewStudNum = $tstudnm + 1; $tstudemail = lc $tstudemail;
         if ($tstudemail =~ /$emailPattern/) { $actStudentEmailExist{$tstudemail} = 1; }
         ( $other, $actStudId ) = split(/56BC/, $tstudid); $actStudId++; $actNewStudId = '56BC' . $actStudId;      }   }
   open(INF, $parents_file);   @parentslist = <INF>;   close(INF);
   foreach $actPrntLine (@parentslist) { $actChompPrntLine = $actPrntLine; chomp($actChompPrntLine);
      ($tprntnm, $tprntid, @other) = split (/<tab>/, $actChompPrntLine);
      if ( $tprntnm ne '' && $tprntid =~ /55FM/ ) { $actNewPrntNum = $tprntnm + 1;
         ( $other, $actPrntId ) = split(/55FM/, $tprntid); $actPrntId++; $actNewPrntId = '55FM' . $actPrntId;      }   }
   foreach $actCandLine (@candslist) { $actCandChompLine = $actCandLine; chomp($actCandChompLine);
      ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, $tusrtype, $tusreml, $tusrcreated,
      $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $actCandChompLine);
      if ( $tusrid eq $actUsrId && $tusrctgr eq 'Parent' ) { $tusreml = lc $tusreml; $tusreml =~s/ //g;
         $actPnrtFirstName{$tusrid} = $tusrfrstnam; $actPnrtSecondName{$tusrid} = $tusrscndnam; $actPnrtThirdName{$tusrid} = $tusrthrdname;
         $actPnrtSchoolId{$tusrid} = $tusrschlid; $actPnrtBirthDay{$tusrid} = $tusrbrthday; $actPnrtPhoneNum{$tusrid} = $tusrphnnum;
         $actPnrtWorkPlace{$tusrid} = $tusrwrkplc; $actPnrtPersonId{$tusrid} = $tusrprsnid; $actPnrtIndivideId{$tusrid} = $tusrindvdid;
         $actPnrtEmail{$tusrid} = $tusreml; $actPnrtCreated{$tusrid} = $tusrcreated;
      }
   }
   ############################# Get id of parent and child ################################
   #########################################################################################
   
   open(INF, $children_file); @childrenlist = <INF>; close(INF);  $actChildFound = 0;
   foreach $actLine (@childrenlist) { $actChompLine = $actLine; chomp($actChompLine);
      ($tparntid, $tchildid, $tchildfirstnam, $tchildscndnam, $tchildthrdnam, $tusrtype, $tchildschl, $tchildclss, $tchildprd,
      $tchildemail, $tchildphn, $tchildbrthd, $tchildgndr, $tchildcreated, @other) = split (/<tab>/, $actChompLine);
      $tchildemail = lc $tchildemail; $tchildemail =~s/ //g;
      if ( $tparntid eq $actUsrId ) { $actChildFound = 1; $actNewStudentLine = $actChompLine;
         if ( $tchildid eq $whatis{'childid'} && $whatis{'childid'} ne '' && $tusrtype eq 'candidate' ) { 
            $actNewLineText = "$tparntid<tab>$tchildid<tab>$tchildfirstnam<tab>$tchildscndnam<tab>$tchildthrdnam<tab>confirmed<tab>";
            $actNewLineText = $actNewLineText . "$tchildschl<tab>$tchildclss<tab>$tchildprd<tab>$tchildemail<tab>$tchildphn<tab>";
            $actNewLineText = $actNewLineText . "$tchildbrthd<tab>$tchildgndr<tab>$tchildcreated<tab>$actNewStudId<tab>$actNewPrntId<tab>reserved\n";
            $actChildFullName = "$tchildfirstnam $tchildthrdnam $tchildscndnam"; $actChildEmail = $tchildemail;
            $actChildCreated = $tchildcreated; push(@actNewChildrenList, $actNewLineText); }
         else { push(@actNewChildrenList, $actLine); }
      }
      else { if ( $actLine ne '' ) { push(@actNewChildrenList, $actLine); } }
   }   
   if ( $actStudentEmailExist{$actChildEmail} == 1 ) { print "<h2>$rf Email $b1 [$actChildEmail]$b2 уже используется! проверьте еще раз.. $f2</h2>
      <p> </p>\n<p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; return; }
   if ( $actChildFound == 1 ) {
       open(SSDATA,">$children_file");    print SSDATA @actNewChildrenList;    close(SSDATA);
       ($tparntid, $tchildid, $tchildfirstnam, $tchildscndnam, $tchildthrdnam, $tusrtype, $tchildschl, $tchildclss, $tchildprd,
       $tchildemail, $tchildphn, $tchildbrthd, $tchildgndr, $tchildcreated, @other) = split (/<tab>/, $actNewStudentLine);
       $tchildemail = lc $tchildemail; $tchildemail =~s/ //g;
       # $StudentNumber<tab>$StudentCode<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}
       #<tab>$whatis{'schoolid'}<tab>$whatis{'groupid'}<tab>$whatis{'birthday'}<tab>$whatis{'phonenumber'}
       #<tab>$whatis{'workplace'}<tab>$whatis{'email'}<tab>reserve";
       $actNewStudText = "$actNewStudNum<tab>$actNewStudId<tab>$tchildfirstnam<tab>$tchildscndnam<tab>$tchildthrdnam<tab>";
       $actNewStudText = "\n" . $actNewStudText . "$tchildschl<tab><tab>$tchildbrthd<tab>$tchildphn<tab>$tchildclss";
       $actNewStudText = $actNewStudText . "<tab>$tchildemail<tab>$tchildgndr<tab>$tchildcreated<tab>reserve";
       open(NEWDATA,">>$students_file");    print NEWDATA $actNewStudText;    close(NEWDATA);
       open(LOGDATA,">>$log_students_file");    print LOGDATA $actNewStudText;    close(LOGDATA);
       # 1<tab>55FM4703<tab>56BC4703<tab>Sergei<tab>Sergeev<tab>Sergeevich<tab>99<tab>99-M2-1<tab>05.05.2005
       #<tab>8 777 123 4567<tab>5 room<tab>34523452<tab>200505 05300 123 <tab>Sergei.Sergeev@mail.ru <tab> reserve
       #($tparntnum, $tparntid, $tparntstudid, $tparntfirstnam, $tparntscndnam, $tparntthrdnam, $tparntschl, 
       #$tparntgrp, $tparntbrtd, $tparntphn, $tparntwrkplc, $tparntemail, @other) = split (/<tab>/, $i);
                         $actNewPrntText = "$actNewPrntNum<tab>$actNewPrntId<tab>$actNewStudId<tab>"; 
       $actNewPrntText = $actNewPrntText . "$actPnrtFirstName{$actUsrId}<tab>$actPnrtSecondName{$actUsrId}<tab>$actPnrtThirdName{$actUsrId}";
       $actNewPrntText = $actNewPrntText . "<tab>$actPnrtSchoolId{$actUsrId}<tab><tab>$actPnrtBirthDay{$actUsrId}<tab>$actPnrtPhoneNum{$actUsrId}";
       $actNewPrntText = $actNewPrntText . "<tab>$actPnrtWorkPlace{$actUsrId}<tab>$actPnrtEmail{$actUsrId}<tab>$actPnrtCreated{$actUsrId}<tab>reserve\n";
       open(PARDATA,">>$parents_file");    print PARDATA $actNewPrntText;    close(PARDATA);
       print "<table $grnclr><tr><td><h2>Данный ученик утвержден!</h2></td></tr></table>\n<p> </p><table>
       <tr $yelclr><td>1</td><td>Дата регистрации ученика: </td><td>$actChildCreated</td></tr>
       <tr $yelclr1><td>2</td><td>ФИО ученика: </td><td>$actChildFullName</td></tr>
       <tr $yelclr><td>3</td><td>EMAIL: </td><td>$actChildEmail</td></tr></table>
       <p> </p><p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
   }
   else { print "<h2>$rf Неверные данные! проверьте еще раз.. $f2</h2>\n<p> </p><p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";  }
}

#####################################################################################
######################## SAVE CHILDREN DATA SUB #####################################
#####################################################################################
sub saveChildrenDataSub { # $glLastParentNumber = $tparntnum; $glLastParentCode = $tparntid;
   print "<h2>Сохранение данных ученика</h2>\n"; $schdUsrId = $whatis{'userid'}; $schdChldId = $whatis{'childid'}; $schdChildFound = 0;
   $schdNewLineText = "<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}<tab>$whatis{'type'}<tab>$whatis{'schoolid'}";
   $schdNewLineText = $schdNewLineText . "<tab>$whatis{'class'}<tab>$whatis{'period'}<tab>$whatis{'email'}<tab>$whatis{'phone'}";
   $schdNewLineText = $schdNewLineText . "<tab>$whatis{'birthday'}<tab>$whatis{'gender'}<tab>$whatis{'created'}<tab>reserve\n";
   open(INF, $children_file); @childrenlist = <INF>; close(INF);  
   foreach $schdLine (@childrenlist) { $schdChompLine = $schdLine; chomp($schdChompLine);
      ($tparntid, $tchildid, $tchildfirstnam, $tchildscndnam, $tchildthrdnam, $tusrtype, $tchildschl, $tchildclss, $tchildprd,
      $tchildemail, $tchildphn, $tchildbrthd, $tchildgndr, $tchildcreated, @other) = split (/<tab>/, $schdChompLine);
      $tchildemail = lc $tchildemail; $tchildemail =~s/ //g;
      if ( $tparntid eq $schdUsrId ) { $schdChildFound = 1;
         if ( $tchildid eq $whatis{'childid'} && $whatis{'childid'} ne '' && $whatis{'type'} eq 'candidate' ) { 
            $schdNewLineText = "$schdUsrId<tab>$schdChldId" . $schdNewLineText; push(@schdNewChildrenList, $schdNewLineText); }
         else { push(@schdNewChildrenList, $schdLine); }
      }
      else { if ( $schdLine ne '' ) { push(@schdNewChildrenList, $schdLine); } }
   }   
   if ( $schdChildFound == 1 ) {
       open(SSDATA,">$children_file");    print SSDATA @schdNewChildrenList;    close(SSDATA);
       print "<table $grnclr><tr><td><h2>Данные изменения внесены в систему.</h2></td></tr></table>\n<p> </p><table>
       <tr $yelclr><td>1</td><td>Дата регистрации ученика: </td><td>$whatis{'created'}</td></tr>
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
   else { print "<h2>$rf Неверные данные! проверьте еще раз.. $f2</h2>\n<p> </p><p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";  }
}

#####################################################################################
########################## EDIT CHILDREN DATA SUB ###################################
#####################################################################################
sub editChildrenDataSub {
   &printjavascript(); $echdUsrId = $whatis{'userid'}; $echdChildId = $whatis{'childid'}; 
   if ( $echdUsrId eq '' || $echdChildId eq '' ) { print "<p> </p> <h3>$rf Неверные данные, запись не найдена! $f2</h3>
   <p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; return; }
   print "<h2>Изменение данных ученика</h2>\n";  $echdStyle = "style='height:50px; width:150px'";
   open(INF, $children_file); @childrenlist = <INF>; close(INF); $echdChildFound = 0;
   foreach $echdLine (@childrenlist) { $echdChompLine = $echdLine; chomp($echdChompLine);
      ($tparntid, $tchildid, $tchildfirstnam, $tchildscndnam, $tchildthrdnam, $tusrtype, $tchildschl, $tchildclss, $tchildprd,
      $tchildemail, $tchildphn, $tchildbrthd, $tchildgndr, $tchildcreated, @other) = split (/<tab>/, $echdChompLine);
      $tchildemail = lc $tchildemail; $tchildemail =~s/ //g;
      if ( $tparntid eq $echdUsrId && $tchildid eq $echdChildId && $tusrtype eq 'candidate' ) { $echdChildFound = 1;
         print "<form method='post' action=\'$httpindexcgi\' onsubmit='return checkChildFunction();'>
         <input type = 'hidden' name = 'action' value = 'savechild'><input type = 'hidden' name = 'userid' value = \'$echdUsrId\'>
         <input type = 'hidden' name = 'type' value = \'$tusrtype\'><input type = 'hidden' name = 'childid' value = \'$echdChildId\'>
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
         </table> <input type='reset' value = 'ОТМЕНИТЬ' $echdStyle>-[ ]-[ ]-[ ]-<input type = 'submit' value = 'ЗАПИСАТЬ' $echdStyle>
         <input type = 'hidden' name = 'created' value = \'$tchildcreated\'></form><p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
      }
   }
   if ( $echdChildFound == 0 ) { 
      print "<h3>$rf Неверные данные, запись не найдена! $f2</h3><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>"; }
}

#####################################################################################
######################### RESTORE ARCHIVE DATA SUB ##################################
#####################################################################################
sub restoreArchiveDataSub { 
   $myclr = $yelclr; $radUsrId = $whatis{'userid'}; $radStyle = "style='height:50px; width:150px'"; $radUserFound = 0;
   print "<h2>Welcome to restoreArchiveDataSub [$radUsrId]</h2>\n <table>";
   $radGenderRuName{'Male'} = 'Мужской';  $radGenderRuName{'Female'} = 'Женский';
   foreach $radLine (@candsArchiveList) { $radChompLine = $radLine; chomp($radChompLine);
     ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, $tusrtype, $tusreml, $tusrcreated,
     $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $radChompLine);
     $tusreml = lc $tusreml; $tusreml =~s/ //g;
     if ( $tusrid eq $radUsrId ) { $radUserFound = 1; $radFoundUserEmail = $tusreml; 
        $radLookedLine = "$tusrctgr<tab>$tusrfrstnam<tab>$tusrscndnam<tab>$tusrthrdname<tab>$tusrpwd<tab>$tusrphnnum<tab>";
        $radLookedLine = $radLookedLine . "$tusrtype<tab>$tusreml<tab>$tusrcreated<tab>$tusrbrthday<tab>$tusrgndr<tab>";
        $radLookedLine = $radLookedLine . "$tusrwrkplc<tab>$tusrprsnid<tab>$tusrindvdid<tab>$tusrstats<tab>$tusrschlid<tab>reserve";
        $radHtmlLine = "<caption><table $grnclr><tr><td><h3>Данный пользователь восстановлен из архива!<h3></td></tr></table></caption>
        <tr $yelclr><td>Имя кандидата: </td><td>$tusrfrstnam</td></tr>
        <tr $yelclr1><td>Фамилия: </td><td>$tusrscndnam</td></tr>
        <tr $yelclr><td>Отчество: </td><td>$tusrthrdname</td></tr>
        <tr $yelclr1><td>Телефон: </td><td>$tusrphnnum</td></tr>
        <tr $yelclr><td>Категория: </td><td>$tusrctgr</td></tr>
        <tr $yelclr1><td>EMAIL: </td><td>$tusreml</td></tr>
        <tr $yelclr><td>Дата регистрации: </td><td>$tusrcreated</td></tr>
        <tr $yelclr1><td>День рождения: </td><td>$tusrbrthday</td></tr>
        <tr $yelclr><td>Пол: </td><td>$radGenderRuName{$tusrgndr}</td></tr>
        <tr $yelclr1><td>Школа: </td><td>$tusrschlid</td></tr>
        <tr $yelclr1><td>Статус: </td><td>$tusrtype</td></tr>
        <tr $yelclr><td>Род деятельности: </td><td>$tusrstats</td></tr>
        <tr $yelclr1><td>Место работы / учебы: </td><td>$tusrwrkplc</td></tr>
        <tr $yelclr><td>Номер удостоверения: </td><td>$tusrprsnid</td></tr>
        <tr $yelclr1><td>ИИН: </td><td>$tusrindvdid</td></tr></table>\n";
        push(@newCandsArchiveList, "$tusrid<tab><tab><tab><tab><tab><tab><tab><tab>reserve\n");
     }
     else { push(@newCandsArchiveList, $radLine); } #cands_archivefile cands_file
   }

   foreach $radLine (@candslist) { $radChompLine = $radLine; chomp($radChompLine);
     ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, $tusrtype, $tusreml, $tusrcreated,
     $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $radChompLine);
     $tusreml = lc $tusreml; $tusreml =~s/ //g;
     if ( $tusreml eq $radFoundUserEmail ) { $radUserFound = 0; 
        print "<h2>$rf Уже есть пользователь с таким емэйлом [$radFoundUserEmail]!<br>Восстановить невозможно из архива.. $f2</h2>\n"; }
   }

   if ( $radUserFound == 1 ) { 
      foreach $radLine (@candslist) { ($cnt, @other) = split (/<tab>/, $radLine); } $cnt++;
      open(CDATA,">>$cands_file"); print CDATA "$cnt<tab>$radLookedLine\n"; close(CDATA);
      open(ADATA,">$cands_archivefile"); print ADATA @newCandsArchiveList; close(ADATA);
      print "$radHtmlLine";
   }
   else { print "<h2>$rf Ошибка в записи Пользователя! Проверьте еще раз.. $f2</h2>\n"; }
   print "<p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
}

#####################################################################################
####################### ARCHIVE CANDIDATE DATA SUB ##################################
#####################################################################################
sub archiveCandidateDataSub { 
   $myclr = $yelclr; $acdUsrId = $whatis{'userid'}; $acdStyle = "style='height:50px; width:150px'"; $acdUserFound = 0;
   print "<h2>Welcome to archiveCandidateDataSub [$acdUsrId]</h2>\n <table>";
   $acdGenderRuName{'Male'} = 'Мужской';  $acdGenderRuName{'Female'} = 'Женский';
   foreach $acdLine (@candslist) { $acdChompLine = $acdLine; chomp($acdChompLine);
     ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, $tusrtype, $tusreml, $tusrcreated,
     $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $acdChompLine);
     $tusreml = lc $tusreml; $tusreml =~s/ //g;
     if ( $tusrid eq $acdUsrId && $tusreml ne '' ) { $acdUserFound = 1; 
        $acdLookedLine = "$tusrctgr<tab>$tusrfrstnam<tab>$tusrscndnam<tab>$tusrthrdname<tab>$tusrpwd<tab>$tusrphnnum<tab>$tusrtype<tab>";
        $acdLookedLine = $acdLookedLine . "$tusreml<tab>$tusrcreated<tab>$tusrbrthday<tab>$tusrgndr<tab>$tusrwrkplc<tab>$tusrprsnid<tab>";
        $acdLookedLine = $acdLookedLine . "$tusrindvdid<tab>$tusrstats<tab>$tusrschlid<tab>reserve";
        $acdHtmlLine = "<caption><table $grnclr><tr><td><h3>Данный пользователь удален в архив!<h3></td></tr></table></caption>
        <tr $yelclr><td>Имя кандидата: </td><td>$tusrfrstnam</td></tr>
        <tr $yelclr1><td>Фамилия: </td><td>$tusrscndnam</td></tr>
        <tr $yelclr><td>Отчество: </td><td>$tusrthrdname</td></tr>
        <tr $yelclr1><td>Телефон: </td><td>$tusrphnnum</td></tr>
        <tr $yelclr><td>Категория: </td><td>$tusrctgr</td></tr>
        <tr $yelclr1><td>EMAIL: </td><td>$tusreml</td></tr>
        <tr $yelclr><td>Дата регистрации: </td><td>$tusrcreated</td></tr>
        <tr $yelclr1><td>День рождения: </td><td>$tusrbrthday</td></tr>
        <tr $yelclr><td>Пол: </td><td>$acdGenderRuName{$tusrgndr}</td></tr>
        <tr $yelclr1><td>Школа: </td><td>$tusrschlid</td></tr>
        <tr $yelclr1><td>Статус: </td><td>$tusrtype</td></tr>
        <tr $yelclr><td>Род деятельности: </td><td>$tusrstats</td></tr>
        <tr $yelclr1><td>Место работы / учебы: </td><td>$tusrwrkplc</td></tr>
        <tr $yelclr><td>Номер удостоверения: </td><td>$tusrprsnid</td></tr>
        <tr $yelclr1><td>ИИН: </td><td>$tusrindvdid</td></tr></table>\n";
     }
     else { push(@acdNewCandsList, $acdLine); }
   }
   if ( $acdUserFound == 1 ) { $cnt = 0;  foreach $acdLine (@candsArchiveList) { $cnt++; }
      open(ADATA,">>$cands_archivefile"); print ADATA "$cnt<tab>$acdLookedLine\n"; close(ADATA);
      open(CDATA,">$cands_file"); print CDATA @acdNewCandsList; close(CDATA);
      print "$acdHtmlLine";
   }
   else { print "<h2>$rf Пользователь не найден! Проверьте еще раз.. $f2</h2>\n"; }
   print "<p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
}

#####################################################################################
######################## ACTIVATE CANDIDATE SUB #####################################
#####################################################################################
sub activateCandidateSub { 
   $myclr = $yelclr; $acsUsrId = $whatis{'userid'}; $acsStyle = "style='height:50px; width:150px'"; $acsUserFound = 0;
   print "<h2>Welcome to activateCandidateSub [$acsUsrId]</h2>\n "; $acsLegionerFound = 0; $cnt = 0;
   $acsGenderRuName{'Male'} = 'Мужской';  $acsGenderRuName{'Female'} = 'Женский';
   foreach $acsLine (@candslist) { $acsChompLine = $acsLine; chomp($acsChompLine);
     ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, $tusrtype, $tusreml, $tusrcreated,
     $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $acsChompLine);
     $tusreml = lc $tusreml; $tusreml =~s/ //g;
     if ( $tusrid eq $acsUsrId && $tusreml ne '' ) { $acsUserFound = 1; $acsUserCategory = $tusrctgr;
        $acsUserFullName = "$tusrfrstnam $tusrthrdname $tusrscndnam"; $acsUserEmail = $tusreml;
        $acsLookedLine = "$acsUsrId<tab>$tusrctgr<tab>$tusrfrstnam<tab>$tusrscndnam<tab>$tusrthrdname<tab>";
        $acsLookedLine = $acsLookedLine . "$tusrpwd<tab>$tusrphnnum<tab>confirmed<tab>$tusreml<tab>$tusrcreated<tab>";
        $acsLookedLine = $acsLookedLine . "$tusrbrthday<tab>$tusrgndr<tab>$tusrwrkplc<tab>$tusrprsnid<tab>";
        $acsLookedLine = $acsLookedLine . "$tusrindvdid<tab>$tusrstats<tab>$tusrschlid<tab>reserve\n";
        push(@acsNewCandsList, $acsLookedLine);
     }
     else { push(@acsNewCandsList, $acsLine); }
   }
   if ( $acsUserCategory eq 'Volonteer' && $acsUserFound == 1 ) {
      foreach $acsLine (@legionlist) { ($tusrnm, $tusrid, @other) = split (/<tab>/, $acsLine);
         $acsLegUsrNum = $tusrnm + 1;  ( $other, $acsLegUsrId ) = split ( /2LEG/, $tusrid );
         if ( $acsLine =~ /$acsUserEmail/ ) { $acsLegionerFound = 1; } $acsLegUsrId++; $cnt++;
      }
      if ( $acsLegionerFound == 1 ) { 
         print "<h2>$rf Пользователь с таким емэйлом<br>уже существует в базе! Проверьте еще раз.. $f2</h2>\n"; }
      else { $acsLegUsrIndx = $acsLegUsrNum . '<tab>22LEG' . $acsLegUsrId;
         open(LDATA,">>$legion_file"); print LDATA "$acsLegUsrIndx<tab><tab>$acsLookedLine"; close(LDATA);
         open(CDATA,">$cands_file"); print CDATA @acsNewCandsList; close(CDATA);
         print "<table $grnclr><tr><td></td><td><h2>Данный Кандидат утвержден!</h2></td></tr>
         <tr><td>ФИО кандидата: </td><td><h3>$acsUserFullName</h3></td></tr>
         <tr><td>EMAIL кандидата: </td><td><h3>$acsUserEmail</h3></td></tr></table>\n";      }
   }
   elsif ( $acsUserFound == 1 ) { 
      open(CDATA,">$cands_file"); print CDATA @acsNewCandsList; close(CDATA);
      print "<table $grnclr><tr><td></td><td><h2>Данный Кандидат утвержден!</h2></td></tr>
      <tr><td>ФИО кандидата: </td><td><h3>$acsUserFullName</h3></td></tr>
      <tr><td>EMAIL кандидата: </td><td><h3>$acsUserEmail</h3></td></tr></table>\n";
   }
   else { print "<h2>$rf Пользователь не найден! Проверьте еще раз.. $f2</h2>\n"; }
   print "<p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
}

#####################################################################################
####################### SAVE CANDIDATE DATA SUB #####################################
#####################################################################################
sub saveCandidateDataSub { 
   $myclr = $yelclr; $scdUsrId = $whatis{'userid'}; $scdStyle = "style='height:50px; width:150px'"; $scdUserFound = 0;
   print "<h2>Welcome to saveCandidateDataSub [$scdUsrId]</h2>\n ";
   $scdGenderRuName{'Male'} = 'Мужской';  $scdGenderRuName{'Female'} = 'Женский';
   foreach $scdLine (@candslist) { $scdChompLine = $scdLine; chomp($scdChompLine);
     ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, $tusrtype, $tusreml, $tusrcreated,
     $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $scdChompLine);
     $tusreml = lc $tusreml; $tusreml =~s/ //g;
     if ( $tusrid eq $scdUsrId && $tusreml ne '' ) { $scdUserFound = 1; 
        $scdLookedLine = "$scdUsrId<tab>$whatis{'category'}<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}";
        $scdLookedLine = $scdLookedLine . "<tab>$tusrpwd<tab>$whatis{'phone'}<tab>$tusrtype<tab>$tusreml<tab>$tusrcreated<tab>";
        $scdLookedLine = $scdLookedLine . "$whatis{'birthday'}<tab>$whatis{'gender'}<tab>$whatis{'workplace'}<tab>$whatis{'personid'}";
        $scdLookedLine = $scdLookedLine . "<tab>$whatis{'individid'}<tab>$whatis{'status'}<tab>$whatis{'schoolid'}<tab>reserve\n";
        push(@scdNewCandsList, $scdLookedLine);
     }
     else { push(@scdNewCandsList, $scdLine); }
   }
   if ( $scdUserFound == 1 ) { 
      open(CDATA,">$cands_file"); print CDATA @scdNewCandsList; close(CDATA);
      print "<table><caption><table $grnclr><tr><td><h3>Данные сохранены!<h3></td></tr></table></caption>
      <tr $yelclr><td>Имя кандидата: </td><td>$whatis{'firstname'}</td></tr>
      <tr $yelclr1><td>Фамилия: </td><td>$whatis{'secondname'}</td></tr>
      <tr $yelclr><td>Отчество: </td><td>$whatis{'thirdname'}</td></tr>
      <tr $yelclr1><td>Телефон: </td><td>$whatis{'phone'}</td></tr>
      <tr $yelclr><td>Категория: </td><td>$whatis{'category'}</td></tr>
      <tr $yelclr1><td>Статус: </td><td>$whatis{'type'}</td></tr>
      <tr $yelclr><td>Род деятельности: </td><td>$whatis{'status'}</td></tr>
      <tr $yelclr1><td>EMAIL: </td><td>$whatis{'email'}</td></tr>
      <tr $yelclr><td>Дата регистрации: </td><td>$whatis{'created'}</td></tr>
      <tr $yelclr1><td>День рождения: </td><td>$whatis{'birthday'}</td></tr>
      <tr $yelclr><td>Пол: </td><td>$scdGenderRuName{$whatis{'gender'}}</td></tr>
      <tr $yelclr1><td>Место работы / учебы: </td><td>$whatis{'workplace'}</td></tr>
      <tr $yelclr><td>Номер удостоверения: </td><td>$whatis{'personid'}</td></tr>
      <tr $yelclr1><td>ИИН: </td><td>$whatis{'individid'}</td></tr></table>\n";
   }
   else { print "<h2>$rf Пользователь не найден! Проверьте еще раз.. $f2</h2>\n"; }
   print "<p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
}

#####################################################################################
############################ EDIT CANDIDATE SUB #####################################
#####################################################################################
sub editCandidateSub { 
   $myclr = $yelclr; $ecsUsrId = $whatis{'userid'}; $ecsStyle = "style='height:50px; width:150px'"; &printjavascript(); 
   print "<h2>Welcome to editCandidateSub [$ecsUsrId]</h2>\n 
   <form method='post' action=\'$httpindexcgi\' name = 'updatedata' onsubmit='return checkAllFunction();' >
   <input type = 'hidden' name = 'action' value = 'save'><input type = 'hidden' name = 'userid' value = \'$ecsUsrId\'><table>";
   $ecsGenderRuName{'Male'} = 'Мужской';  $ecsGenderRuName{'Female'} = 'Женский';
   foreach $ecsLine (@candslist) { $ecsChompLine = $ecsLine; chomp($ecsChompLine);
     ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, $tusrtype, $tusreml, $tusrcreated,
     $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $ecsChompLine);
     if ( $tusrid eq $ecsUsrId && $tusreml ne '' ) { $tusreml = lc $tusreml; $tusreml =~s/ //g;
        print "<!-- tusrid:[$tusrid] ecsUsrId:[$ecsUsrId] tusreml:[$tusreml] -->\n";
        print "<tr $yelclr><td>Имя кандидата: </td><td><input type= 'text' name = 'firstname' value = \'$tusrfrstnam\'></td></tr>
        <tr $yelclr1><td>Фамилия: </td><td><input type= 'text' name = 'secondname' value = \'$tusrscndnam\'></td></tr>
        <tr $yelclr><td>Отчество: </td><td><input type= 'text' name = 'thirdname' value = \'$tusrthrdname\'></td></tr>
        <tr $yelclr1><td>Телефон: </td><td><input type= 'text' name = 'phone' value = \'$tusrphnnum\'></td></tr>
        <tr $yelclr><td>Категория: </td><td>$b1 $tusrctgr $b2<input type= 'hidden' name = 'category' value = \'$tusrctgr\'>
        <input type= 'hidden' name = 'type' value = \'$tusrtype\'></td></tr>
        <tr $yelclr1><td>EMAIL: </td><td>$b1 $tusreml $b2<input type= 'hidden' name = 'email' value = \'$tusreml\'></td></tr>
        <tr $yelclr><td>Дата регистрации: </td><td>$b1 $tusrcreated $b2<input type= 'hidden' name = 'created' value = \'$tusrcreated\'></td></tr>";
        if ( $tusrctgr eq 'School' || $tusrctgr eq 'Parent' ) { 
           print "<tr $yelclr1><td>Школа: </td><td><input type= 'text' name = 'phone' value = \'$tusrschlid\'></td></tr>\n"; }
        elsif ( $tusrctgr eq 'Volonteer' ) { 
           print "<tr $yelclr1><td>День рождения: </td><td><input type= 'text' name = 'birthday' value = \'$tusrbrthday\'></td></tr>
           <tr $yelclr><td>Пол: </td><td><select name = 'gender'><option value = ''>Выберите пол</option>";
           if ( $tusrgndr ne '' ) { print "<option value = \'$tusrgndr\' selected>$ecsGenderRuName{$tusrgndr}</option>\n"; }
           print "<option value = 'Male'>Мужской</option> <option value = 'Female'>Женский</option></select></td></tr>
           <tr $yelclr><td>Род деятельности: </td><td><select name = 'status'><option value = ''>Выберите род деятельности</option>";
           if ( $tusrstats ne '' ) { print "<option value = \'$tusrstats\' selected>$tusrstats</option>\n"; }
           print "<option value = 'Школьник'>Школьник</option> <option value = 'Студент'>Студент</option>
           <option value = 'Работаю'>Работаю</option></select></td></tr>
           <tr $yelclr1><td>Место работы / учебы: </td><td><input type= 'text' name = 'workplace' value = \'$tusrwrkplc\'></td></tr>
           <tr $yelclr><td>Номер удостоверения: </td><td><input type= 'text' name = 'personid' value = \'$tusrprsnid\'></td></tr>
           <tr $yelclr1><td>ИИН: </td><td><input type= 'text' name = 'individid' value = \'$tusrindvdid\'></td></tr>\n";
        }
        print "<tr $yelclr><td><input type='reset' value = 'RESET' $ecsStyle></td>
        <td><input type = 'submit' value = 'ENTER' $ecsStyle></td></tr>\n";
     }
   }
   print "</form></table><p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n"; 
}

#####################################################################################
########################### SHOW WORK GROUP SUB #####################################
#####################################################################################
sub showWorkGroupSub {
  $cnt = 1; $myclr = $yelclr; &printjavascript(); 
  open(INF, $children_file); @childrenlist = <INF>; close(INF);  $myclr = $yelclr;
  foreach $swgChildLine (@childrenlist) { $swgChildChompLine = $swgChildLine; chomp($swgChildChompLine);
      ($tparntid, $tchildid, $tchildfirstnam, $tchildscndnam, $tchildthrdnam, $tusrtype, $tchildschl, $tchildclss, $tchildprd,
      $tchildemail, $tchildphn, $tchildbrthd, $tchildgndr, $tchildcreated, @other) = split (/<tab>/, $swgChildChompLine);
      $tchildemail = lc $tchildemail; $tchildemail =~s/ //g;
      $swgChildIndex = "$tparntid<tab>$tchildid"; $swgChildExist{$tparntid}++; $swgChildId{$swgChildIndex} = $tchildid; 
      $swgChildFullName{$swgChildIndex} = "$tchildfirstnam $tchildthrdnam $tchildscndnam";
      $swgChildType{$swgChildIndex} = $tusrtype; $swgChildSchoolId{$swgChildIndex} = $tchildschl; 
      $swgChildEmail{$swgChildIndex} = $tchildemail; 
      $swgChildPhone{$swgChildIndex} = $tchildphn; $swgChildCreated{$swgChildIndex} = $tchildcreated;
      $swgChildBirthDay{$swgChildIndex} = $tchildbrthd; $swgChildGender{$swgChildIndex} = $tchildgndr;
  }
  print "<h2>утвержденные списки кандидатов в волонтеры OpenEnglish</h2>\n 
  <table><tr $myclr><td>No</td><td>ФИО кандидата</td><td>Включить в группу</td><td>Телефон</td><td>Категория</td>
  <td>Емэйл</td><td>Дата<br> регистрации</td><td>Школа</td><td>Дата<br>рождения</td><td>Пол</td>
  <td>Место работы<br>/ учебы</td><td>Номер<br>удостоверения</td><td>ИИН</td></tr>\n";
  foreach $swgLine (@candslist) { $swgChompLine = $swgLine; chomp($swgChompLine);
     ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdnam, $tusrpwd, $tusrphnnum, 
     $tusrtype, $tusreml, $tusrcreated, $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, 
     $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $swgChompLine);
     $tusreml = lc $tusreml; $tusreml =~s/ //g;
     if ($tusrfrstnam ne '' && $tusrscndnam ne '' && $tusrtype eq 'confirmed' ) { 
         if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
         if ( $tusrctgr eq 'Volonteer' ) {
            $swgButtonTxt = "<button onclick=\"return checkAssignFunction\($cnt\)\;\">Перейти в группу обучения</button>"; }
         else { $swgButtonTxt = ''; }
         print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$tusrid\'></td><td>$tusrfrstnam $tusrthrdnam 
         $tusrscndnam</td><td>$swgButtonTxt</td><td>$tusrphnnum</td><td>$tusrctgr</td><td>$tusreml</td><td>$tusrcreated</td>
         <td>$tusrschlid</td><td>$tusrbrthday</td><td>$tusrgndr</td><td>$tusrwrkplc</td><td>$tusrprsnid</td><td>$tusrindvdid</td></tr>\n";
         if ( $swgChildExist{$tusrid} ne '' && $swgChildExist{$tusrid} > 0 ) { $swgChldCnt = 0;
            while ( $swgChildExist{$tusrid} > $swgChldCnt ) { 
               $swgChldCnt++; $swgChildIndex = "$tusrid<tab>$swgChldCnt";
               if ( $swgChildType{$swgChildIndex} eq 'confirmed' ) { 
                  if ( $myclr1 eq $grnclr2 ) { $myclr1 = $grnclr1; } else { $myclr1 = $grnclr2; }
                  print "<tr $myclr1><td>$cnt - $swgChldCnt</td><td>$swgChildFullName{$swgChildIndex}</td>
                  <td>Child of: $tusrfrstnam $tusrthrdname $tusrscndnam</td><td>$swgChildPhone{$swgChildIndex}</td>
                  <td>Child</td><td>$swgChildEmail{$swgChildIndex}</td><td>$swgChildCreated{$swgChildIndex}</td>
                  <td>$swgChildSchoolId{$swgChildIndex}</td><td>$swgChildBirthDay{$swgChildIndex}</td>
                  <td>$swgChildGender{$swgChildIndex}</td><td></td><td></td><td></td></tr>\n";
               }
            }
         }
         $cnt++; 
     }
  }
  print "</table> <p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";
} 

#####################################################################################
######################### SHOW ARCHIVE DATA SUB #####################################
#####################################################################################
sub showArchiveDataSub {
  $cnt = 1; $myclr = $yelclr; &printjavascript(); 
  print "<h2>Архивные списки кандидатов в волонтеры OpenEnglish</h2>\n 
  <table><tr $myclr><td>No</td><td>ФИО кандидата</td><td>Восстановить</td><td>Телефон</td><td>Категория</td>
  <td>Емэйл</td><td>Дата<br> регистрации</td><td>Дата<br>рождения</td><td>Пол</td>
  <td>Место работы<br>/ учебы</td><td>Номер<br>удостоверения</td><td>ИИН</td></tr>\n";
  foreach $sadLine (@candsArchiveList) { $sadChompLine = $sadLine; chomp($sadChompLine);
     ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, $tusrtype, $tusreml, $tusrcreated,
     $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $sadChompLine);
     $tusreml = lc $tusreml; $tusreml =~s/ //g;
     if ($tusrfrstnam ne '' && $tusrscndnam ne '' ) { if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
     print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$tusrid\'></td><td>$tusrfrstnam $tusrthrdname $tusrscndnam</td>
     <td><button onclick=\"return checkRestoreFunction\($cnt\)\;\">Восстановить из Архива</button></td><td>$tusrphnnum</td><td>$tusrctgr</td>
     <td>$tusreml</td><td>$tusrcreated</td><td>$tusrbrthday</td><td>$tusrgndr</td><td>$tusrwrkplc</td><td>$tusrprsnid</td><td>$tusrindvdid</td></tr>\n";
     $cnt++; }
  }
  print "</table> <p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";
} 

#####################################################################################
################################ BLANK PAGE SUB #####################################
#####################################################################################
sub blankPageSub {
  $cnt = 1;  &printjavascript(); $bpsStyle = "style='height:50px; width:130px'";
  open(INF, $children_file); @childrenlist = <INF>; close(INF);  $myclr = $yelclr;
  foreach $bpsChildLine (@childrenlist) { $bpsChildChompLine = $bpsChildLine; chomp($bpsChildChompLine);
      ($tparntid, $tchildid, $tchildfirstnam, $tchildscndnam, $tchildthrdnam, $tusrtype, $tchildschl, $tchildclss, $tchildprd,
      $tchildemail, $tchildphn, $tchildbrthd, $tchildgndr, $tchildcreated, @other) = split (/<tab>/, $bpsChildChompLine);
      $tchildemail = lc $tchildemail; $tchildemail =~s/ //g;
      $bpsChildIndex = "$tparntid<tab>$tchildid"; $bpsChildExist{$tparntid}++; $bpsChildId{$bpsChildIndex} = $tchildid; 
      $bpsChildFullName{$bpsChildIndex} = "$tchildfirstnam $tchildthrdnam $tchildscndnam";
      $bpsChildType{$bpsChildIndex} = $tusrtype; $bpsChildSchoolId{$bpsChildIndex} = $tchildschl; 
      $bpsChildEmail{$bpsChildIndex} = $tchildemail; 
      $bpsChildPhone{$bpsChildIndex} = $tchildphn; $bpsChildCreated{$bpsChildIndex} = $tchildcreated;
      $bpsChildBirthDay{$bpsChildIndex} = $tchildbrthd; $bpsChildGender{$bpsChildIndex} = $tchildgndr;
  }
  print "<h2>Списки кандидатов в волонтеры OpenEnglish</h2>\n <table>
  <tr $myclr><td>No</td><td>ФИО кандидата</td><td>Редактировать</td><td>Телефон</td><td>Категория</td>
  <td>Архив</td><td>Емэйл</td><td>Дата<br>регистрации</td><td>Утвердить</td><td>Школа</td><td>Дата<br>рождения</td>
  <td>Пол</td><td>Место работы<br>/ учебы</td><td>Номер<br>удостоверения</td><td>ИИН</td></tr>\n";
  foreach $bpsLine (@candslist) { $bpsChompLine = $bpsLine; chomp($bpsChompLine);
     ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, $tusrtype, $tusreml, $tusrcreated,
     $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $bpsChompLine);
     $tusreml = lc $tusreml; $tusreml =~s/ //g;
     if ( $tusrtype eq 'candidate' ) { if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
         print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$tusrid\'></td><td>$tusrfrstnam $tusrthrdname $tusrscndnam</td>
         <td><button onclick=\"return checkEditFunction\($cnt\)\;\" $bpsStyle>Редактировать</button></td><td>$tusrphnnum</td><td>$tusrctgr</td>
         <td><button onclick=\"return checkArchiveFunction\($cnt\)\;\" $bpsStyle>Убрать в архив</button></td><td>$tusreml</td><td>$tusrcreated</td>
         <td><button onclick=\"return checkActivateFunction\($cnt\)\;\" $bpsStyle>Утвердить</button></td><td>$tusrschlid</td><td>$tusrbrthday</td>
         <td>$tusrgndr</td><td>$tusrwrkplc</td><td>$tusrprsnid</td><td>$tusrindvdid</td></tr>\n";
     $cnt++; }
     if ( $bpsChildExist{$tusrid} ne '' && $bpsChildExist{$tusrid} > 0 ) { $bpsChldCnt = 0;
        while ( $bpsChildExist{$tusrid} > $bpsChldCnt ) { $bpsChldCnt++; $bpsChildIndex = "$tusrid<tab>$bpsChldCnt";
           if ( $bpsChildType{$bpsChildIndex} eq 'candidate' ) { if ( $myclr eq $grnclr2 ) { $myclr = $grnclr1; } else { $myclr = $grnclr2; }
               print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$tusrid\_$bpsChldCnt\'></td>
               <td>$bpsChildFullName{$bpsChildIndex}</td>
               <td><button onclick=\"return checkEditChildFunction\($cnt\)\;\" $bpsStyle>Редактировать</button></td><td>$bpsChildPhone{$bpsChildIndex}</td>
               <td>Child of</td><td>$tusrfrstnam $tusrthrdname $tusrscndnam</td><td>$bpsChildEmail{$bpsChildIndex}</td>
               <td>$bpsChildCreated{$bpsChildIndex}</td><td><button onclick=\"return checkConfirmFunction\($cnt\)\;\" $bpsStyle>Утвердить</button></td>
               <td>$bpsChildSchoolId{$bpsChildIndex}</td><td>$bpsChildBirthDay{$bpsChildIndex}</td>
               <td>$bpsChildGender{$bpsChildIndex}</td><td></td><td></td><td></td></tr>\n";
           }
        }
     }
  }
  print "</table> <p> </p> <table><tr><td><a href=\'$httpindexcgi?action=showactive\'>Утвержденный ПЕРЕЧЕНЬ</a></td>
  <td>-[]-[]-[]-</td><td><a href=\'$httpindexcgi?action=showarchive\'>Посмотреть АРХИВ</a></td></tr></table>\n";
} 
#####################################################################################
########################### FINISH END BODY #########################################
#####################################################################################

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
########################### JAVASCRIPT PART ###########################################
#######################################################################################
sub printjavascript {
print  <<EOT;
 <script>
 function checkEditFunction (cnt) {
     var userlink = \'$httpindexcgi\?action=edit\&userid=' + document.getElementById(cnt).value;
     var usr = confirm('Изменить Запись?');
     if(usr){window.location.href = userlink;}     else{return false;}
 }
 function checkRestoreFunction (cnt) {
     var userlink = \'$httpindexcgi\?action=restore\&userid=' + document.getElementById(cnt).value;
     var usr = confirm('Восстановить?');
     if(usr){window.location.href = userlink;}     else{return false;}
 }
 function checkAssignFunction (cnt) {
     var userlink = \'$httplegioncgi\';     var usr = confirm('Открыть группу обучения?');
     if(usr){window.location.href = userlink;}     else{return false;}
 }
 function checkEditChildFunction (cnt) {
     var cntval = document.getElementById(cnt).value;  var index = cntval.split('_');
     var userid = index[0]; var childid = index[1];
     var userlink = \'$httpindexcgi\?action=editchild\&userid=' + userid + '\&childid=' + childid;
     var usr = confirm('Изменить Запись?');
     if(usr){window.location.href = userlink;}     else{return false;}
 }
 function checkConfirmFunction (cnt) {
     var cntval = document.getElementById(cnt).value;  var index = cntval.split('_');
     var userid = index[0]; var childid = index[1];
     var userlink = \'$httpindexcgi\?action=confirm\&userid=' + userid + '\&childid=' + childid;
     var usr = confirm('Утвердить?');
     if(usr){window.location.href = userlink;}     else{return false;}
 }
 function checkActivateFunction (cnt) {
     var userlink = \'$httpindexcgi\?action=activate\&userid=' + document.getElementById(cnt).value;
     var usr = confirm('Утвердить?');
     if(usr){window.location.href = userlink;}     else{return false;}
 }
 function checkArchiveFunction (cnt) {
     var userlink = \'$httpindexcgi\?action=archive\&userid=' + document.getElementById(cnt).value;
     var usr = confirm('Убрать в архив?');
     if(usr){window.location.href = userlink;}     else{return false;}
 }
 function checkParFunction (){
   if(document.getElementsByName('firstname')[0].value == ''){alert('Ваше имя?'); return false;}
   if(document.getElementsByName('secondname')[0].value == ''){alert('Фамилия?'); return false;}
   if(document.getElementsByName('phone')[0].value == ''){alert('Номер телефона?'); return false;}
 }
 function checkChildFunction (){
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
 function checkAllFunction (){
   if(document.getElementsByName('firstname')[0].value == ''){alert('Ваше имя?'); return false;}
   if(document.getElementsByName('secondname')[0].value == ''){alert('Фамилия?'); return false;}
   if(document.getElementsByName('phone')[0].value == ''){alert('Номер телефона?'); return false;}
   if(document.getElementsByName('birthday')[0].value == ''){alert('Дата рождения?'); return false;}
   var usr = document.getElementsByName('birthday')[0].value;
   if (isValidDate(usr)) { document.getElementsByName('birthday')[0].value = usr; }
   else {alert('Неправильная дата: [' + usr + ']!'); return false;}
   if(document.getElementsByName('gender')[0].value == ''){alert('Выберите пол!'); return false;}
   if(document.getElementsByName('status')[0].value == ''){alert('Род деятельности?'); return false;}
   if(document.getElementsByName('workplace')[0].value == ''){alert('Место учебы / работы?'); return false;}
   if(document.getElementsByName('personid')[0].value == ''){alert('Номер удостоверения?'); return false;}
   if(document.getElementsByName('individid')[0].value == ''){alert('ИИН?'); return false;}
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