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
$indexcgi = 'group.cgi';
$students_file = $oe_folder . 'students.txt';
$adminText_file = $oe_folder . 'admin.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpreadcgi = 'http://accelerator.kvadra.kz/cgi-bin/read.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Read-Create-Edit Group';

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
      if($tstudgrp ne '' && $tstudschl ne ''){
             $studentFirstName{$tstudid} = $tstudfirstnam; $studentSecondName{$tstudid} = $tstudscndnam;
             $studentThirdName{$tstudid} = $tstudthrdnam; $studentPositionNum{$tstudid} = $tstudnum; 
             $studentSchoolNum{$tstudid} = $tstudschl; $studentGroupNum{$tstudid} = $tstudgrp;     $existSchool{$tstudschl}++;  $existGroup{$tstudgrp}++; 
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
          $usernumber{$tusrnam} = $tusrnum;
          $userslist++;
          push(@loginuserslist, $tusrnam);
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
&checkcookies();
print "\n";
if($userbrowser eq 'desktop'){ &printfile($bas, $title);}
else {&printfile($basm, $title);}

if ( $whatis{'action'} ne '' ) { open(GURD,">>$log_file");
print GURD "Time: [$timedatenow] User ID: [$gotusrid] IP address: [$userip] User action: [$whatis{'action'}] Script: [$indexcgi] \n";
close(GURD); }

#######################################################################################
########################## JAVASCRIPT PART ###########################################
#######################################################################################
sub printjavascript {
print  <<EOT;
 <script>
 function checkAllFunction (){
        if(document.getElementsByName('lesson')[0].value == ''){alert('Укажите номер урока!'); return false;}
        if(document.getElementsByName('topic')[0].value == ''){alert('Укажите тему урока!'); return false;}
 }
 function showFunction(){ var x = document.getElementById('comments');
  if (x.style.display === 'none') {x.style.display = 'block'; } else { x.style.display = 'none'; }
 }
 function checkFunction (id, act){
    var dat = 'date' ;  var top = 'topic';  var les = 'lesson' ;      var dateval = document.getElementsByName(dat)[0].value;
    var part = 'part_' + document.getElementById(id).value;           var late = 'late_' + document.getElementById(id).value;  
    var lim = 'liftMinus_' + document.getElementById(id).value;       var test = 'test_' + document.getElementById(id).value;     
    var lip = 'liftPlus_' + document.getElementById(id).value;        var tot = 'totalPoints_' + document.getElementById(id).value; 
    var eval = 'eval_' + document.getElementById(id).value;           var totval = Number(document.getElementsByName(tot)[0].value); 
    var limval = Number(document.getElementsByName(lim)[0].value);    var lipval = Number(document.getElementsByName(lip)[0].value); 
    var lateval = Number(document.getElementsByName(late)[0].value);  var usr; var testval = Number(document.getElementsByName(test)[0].value);

    if(act == '1'){
          usr = confirm('Ученик пришел на урок?');
          if(usr){
              document.getElementsByName(part)[0].value = '1'; document.getElementById(part).innerHTML = 'Да!';
              document.getElementsByName(tot)[0].value = 1200; document.getElementById(tot).innerHTML = 1200;
          }
          else{
              document.getElementsByName(part)[0].value = '0'; document.getElementById(part).innerHTML = 'Нет!';
              document.getElementsByName(tot)[0].value = '0'; document.getElementById(tot).innerHTML = '0';
          }
    }
    else if(act == '2'){
          usr = Number(prompt('На сколько минут опоздал?', '0')); limval = usr * 10;
           if(usr > 0 && usr < 120 && document.getElementsByName(part)[0].value == '1'){
              document.getElementsByName(late)[0].value = usr; document.getElementById(late).innerHTML = usr;
              document.getElementsByName(tot)[0].value = 1200 - limval; document.getElementById(tot).innerHTML = 1200 - limval;
              document.getElementsByName(lim)[0].value = limval; document.getElementById(lim).innerHTML = limval;
           }
    }
    else if(act == '3'){
          usr = Number(prompt('Введите только цифры', '0')); lipval = (usr -50) * 10;
           if(usr > 50 && usr < 101 && document.getElementsByName(part)[0].value == '1'){
              document.getElementsByName(test)[0].value = usr; document.getElementById(test).innerHTML = usr;
              document.getElementsByName(tot)[0].value = 1200 - limval + lipval; document.getElementById(tot).innerHTML = 1200 - limval + lipval;
              document.getElementsByName(lip)[0].value = lipval; document.getElementById(lip).innerHTML = lipval;
           }
    }
    else if(act == '4'){
         usr = Number(prompt('Укажите оценку от 1 до 10', '0'));
         if(usr > 0 && usr < 11 && document.getElementsByName(part)[0].value == '1'){
            document.getElementsByName(eval)[0].value = usr; document.getElementById(eval).innerHTML = usr;
         }
    }
    else if(act == '5'){
         usr = prompt('Укажите тему урока');
         document.getElementsByName(top)[0].value = usr; document.getElementById(top).innerHTML = usr;
    }
    else if(act == '6'){usr = Number(prompt('Укажите номер урока'));
         if(usr > 0 && usr < 31){document.getElementsByName(les)[0].value = usr; document.getElementById(les).innerHTML = usr;}
    }
    else if(act == '7'){
         usr = prompt('Измените дату урока', dateval);
         if (isValidDate(usr)) { document.getElementsByName(dat)[0].value = usr; document.getElementById(dat).innerHTML = usr; }
         else {alert('Неправильная дата: [' + usr + ']!');}
    }
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
#####################################################################################
########################## LOGIN CHECK PART #######################################
#####################################################################################
print "<p>";
if($userlogged == 1){
    print "Hello $b1 $userfirstname{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>";
    if($whatis{'action'} eq 'create' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){&createLessonSub();}
    elsif($whatis{'action'} eq 'record' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){&recordLessonSub();}
    elsif($whatis{'action'} eq 'read' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne ''){&getLessonSub(); &printListLessons();}
    elsif($whatis{'action'} eq 'open' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' && $whatis{'lessonid'} ne ''){&openLessonSub();}
    elsif($whatis{'action'} eq 'delete' && $whatis{'schoolid'} ne '' && $whatis{'groupid'} ne '' && $whatis{'lessonid'} ne ''){&deleteLessonSub();}
    else{print "$rf No group ID indicated. Please check! $f2 \n";}
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
############################# DELETE LESSON SUB #####################################
#####################################################################################
sub deleteLessonSub {
      $dlsGroupFile = $groups_folder . $whatis{'groupid'} . '.txt'; $dlsDelStat = 0;
      open(UPL, $dlsGroupFile);
      @dlsProjectList = <UPL>;
      close(UPL);
      foreach $i (@dlsProjectList){
          chomp($i);
          if ( $i =~ /<start of new project = / ) {
              if( $i =~ /$whatis{'lessonid'}/ ){ $dlsDelStat = 1; }
              else { $dlsDelStat = 0; push(@dlsNewProjectList, $i); }
          }
          else { if ( $dlsDelStat == 0 ) { push(@dlsNewProjectList, $i); } }
          
      }
      open(DLSDATA,">$dlsGroupFile");  foreach $i (@dlsNewProjectList){ chomp($i);  print DLSDATA "$i\n"; } close(DLSDATA);
      print "<p> </p><p><a href=\'$httpreadcgi?list=groups\&schoolid=$whatis{'schoolid'}\'>$whatis{'schoolid'}-ая</a> 
      Школа [группа № $whatis{'groupid'}]</p><h3> $rf Урок удален! $f2</h3>\n";

}
#####################################################################################
############################### OPEN LESSON SUB #####################################
#####################################################################################
sub openLessonSub {  &getLessonSub(); &getGroupSub();  $olsid = $whatis{'lessonid'}; $cnt = 1; $olsGrpId = $whatis{'groupid'};
      if ( $OEP_VolunteerOneWas{$olsid} =~ /54LD/ ) { $olsVolOne{$olsid} = 'Был на уроке'; } else { $olsVolOne{$olsid} = 'Отсутствовал'; }
      if ( $OEP_VolunteerTwoWas{$olsid} =~ /54LD/ ) { $olsVolTwo{$olsid} = 'Был на уроке'; } else { $olsVolTwo{$olsid} = 'Отсутствовал'; }
      print "<p>.</p><table>
      <caption><a href=\'$httpreadcgi?list=groups\&schoolid=$whatis{'schoolid'}\'>$whatis{'schoolid'}-ая</a> Школа [группа № $whatis{'groupid'}]</caption>
      <tr $yelclr><td>Группа №</td>
      <td $ac><a href=\'$indexcgi?action=read\&schoolid=$whatis{'schoolid'}\&groupid=$whatis{'groupid'}\'>$whatis{'groupid'}</a></td></tr>
      <tr $yelclr><td>Тема урока</td><td>$OEP_Topic{$olsid}</td></tr>
      <tr $yelclr1><td>Номер урока</td><td $ac>$OEP_Lesson{$olsid}</td></tr>
      <tr $yelclr><td>Дата урока</td><td $ac>$OEP_Date{$olsid}</td></tr>
      <tr $yelclr1><td>Волонтёр: $b1 $OEP_VolunteerOne{$olsGrpId} $b2</td><td $ac>$olsVolOne{$olsid}</td></tr>
      <tr $yelclr><td>Волонтёр: $b1 $OEP_VolunteerTwo{$olsGrpId} $b2</td><td $ac>$olsVolTwo{$olsid}</td></tr></table><p>.</p><table>
      <tr $yelclr1><td>№</td><td>Имя Фамилия</td><td>Посещение</td><td>Опоздание</td><td>Штраф за опоздание</td><td>Тестирование</td>
      <td>Баллы за тест</td><td>Всего</td><td>Оценка за тему</td><td>Комментарий по ученику</td><td>Оценка за домашнее задание</td></tr>\n";    
      foreach $i (@glsStudentsList){   $olsUserID_PRNum = $i . '_' . $olsid;
            if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
            print "<tr $myclr><td>$cnt</td><td>$studentFirstName{$i} $studentSecondName{$i}</td><td $ac>$OEP_Participation{$olsUserID_PRNum}</td>
            <td $ac>$OEP_Late{$olsUserID_PRNum}</td><td $ac>$OEP_LiftMinus{$olsUserID_PRNum}</td><td $ac>$OEP_Test{$olsUserID_PRNum}</td>
            <td $ac>$OEP_LiftPlus{$olsUserID_PRNum}</td><td $ac>$OEP_TotalPoints{$olsUserID_PRNum}</td><td $ac>$OEP_Eval{$olsUserID_PRNum}</td>
            <td $ac>$OEP_UserComment{$olsUserID_PRNum}</td><td $ac>$OEP_HomeWork{$olsUserID_PRNum}</td></tr>\n"; 
            $cnt++;
      }
      if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
      print "</table><table><tr $myclr><td>Комментарии</td><td>$OEP_Comments{$olsid}</td></tr></table>\n";
  #    print "<p>.</p><p><a href=\'$httpreadcgi?list=schools\'>Список всех школ</a></p>\n";
      print "<p>.</p><p><a href=\'$httpreadcgi?list=groups\&schoolid=$whatis{'schoolid'}\'>Список групп школы № $whatis{'schoolid'}</a></p>\n";
  #   print "<p>.</p><p><a href=\'$httpreadcgi?list=all\'>Общий список в основной таблице</a></p>\n";
}
#####################################################################################
############################### GET LESSONS SUB #####################################
#####################################################################################
sub getLessonSub {
      foreach $stdid (@studentUniqueNumList){ if($studentGroupNum{$stdid} =~/$whatis{'groupid'}/){  push(@glsStudentsList, $stdid); } }
      $glsgrpfile = $groups_folder . $whatis{'groupid'} . '.txt';
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
          elsif($i =~ /OEP_VolunteerOneWas: /){$i =~ s/OEP_VolunteerOneWas: //g; $OEP_VolunteerOneWas{$glsprnum} = $i;}
          elsif($i =~ /OEP_VolunteerTwoWas: /){$i =~ s/OEP_VolunteerTwoWas: //g; $OEP_VolunteerTwoWas{$glsprnum} = $i;}
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
################################# GET GROUP SUB ######################################
#####################################################################################
sub getGroupSub {
    $ggsgrpfile = $groups_folder . $whatis{'groupid'} . '_data.txt'; $ggsid = $whatis{'groupid'};
    open(UPL, $ggsgrpfile);     @ggsprojectlist = <UPL>;     close(UPL);
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
########################## PRINT LIST OF LESSONS SUB ################################
#####################################################################################
sub printListLessons {    
    print "<p> </p><table><caption>Группа № $whatis{'groupid'}</caption><tr $yelclr><td>Уроки</td>\n";  
    foreach $i (@glsStudentsList){ print "<td>$studentFirstName{$i}";  if($studentFirstName{$i} ne ''){print "<br>";} print "$studentSecondName{$i}"; print "</td>"; }
    print "<td>Всего</td><td>Delete</td></tr>\n";   $myclr = $yelclr;
    @glsLessonNumList = sort(@glsLessonNumList);
    #@glsProjectNumList = sort(@glsProjectNumList);
    foreach $pllId (@glsLessonNumList){ 
        if($pllId ne ''){ ($pllLessId, $i) = split (/<tab>/, $pllId);
            if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
            $pllIndexCgiTitle = "title = \'$OEP_Topic{$i}\'";
            $pllIndexCgiText = "<a href=\'$indexcgi?action=open\&schoolid=$whatis{'schoolid'}\&groupid=$whatis{'groupid'}\&lessonid=$i\' $pllIndexCgiTitle>";
            print "<tr $myclr><td>$pllIndexCgiText Урок $OEP_Lesson{$i} [ $OEP_Date{$i} ] </a></td>"; $glsVisitsPerLesson = 0; 
            foreach $x (@glsStudentsList){
               $glsUserID_PRNum = $x . '_' . $i;  if($OEP_Participation{$glsUserID_PRNum} ne ''){$tdclr = $grnclr; $glsVisitsPerLesson++;} else {$tdclr = '';}
               print "<td $tdclr $ac>$OEP_Participation{$glsUserID_PRNum}</td>";
            }
            print "<td $ac>$glsVisitsPerLesson</td>
            <td><a href=\'$indexcgi?action=delete\&schoolid=$whatis{'schoolid'}\&groupid=$whatis{'groupid'}\&lessonid=$i\'>УДАЛИТЬ УРОК</a></td></tr>\n";
        }
    }
    print "</table>\n"; #list=groups&schoolid=71
    #print "<p>.</p><p><a href=\'$httpreadcgi?list=schools\'>Список всех школ</a></p>\n";
    print "<p>.</p><p><a href=\'$httpreadcgi?list=groups\&schoolid=$whatis{'schoolid'}\'>Список групп школы № $whatis{'schoolid'}</a></p>\n";
    #print "<p>.</p><p><a href=\'$httpreadcgi?list=all\'>Общий список в основной таблице</a></p>\n";
}
#####################################################################################
############################ CREATE LESSON SUB ######################################
#####################################################################################
sub createLessonSub { &printjavascript(); print "</p>"; $myclr = $yelclr; $cnt = 0; &getGroupSub(); $clsGrpId = $whatis{'groupid'};
    print "<form method='post' action=\'$indexcgi\' name = 'createnewlesson' onsubmit='return checkAllFunction();'>
    <table><tr $yelclr>
    <td><a href='#' onclick='return checkFunction(1, 5);'>Укажите тему урока:</a> <input type='hidden' name='topic' value=''></td>
    <td><p id='topic'></p></td></tr>
    <tr><td><input type='hidden' name = 'schoolid' value= \'$whatis{'schoolid'}\'></td>
    <td><input type='hidden' name='date' value=\'$datenow\'></td></tr>
    <tr $yelclr1><td>Укажите номер урока: </td><td><select name = 'lesson'><option value = ''>Укажите № урока</option>\n"; # The lesson's number
    $clsCnt = 0; while ( $clsCnt < 33 ) { $clsCnt++; print "<option value = \'$clsCnt\'>Урок № $clsCnt</option>\n"; }
    print "</select></td></tr><tr><td><input type='hidden' name = 'groupid' value= \'$whatis{'groupid'}\'></td>
    <td><input type='hidden' name = 'action' value= 'record'></td></tr>
    <tr $yelclr><td><a href='#' onclick='return checkFunction(1, 7);'>Изменить дату урока</a> [DD.MM.YYYY]: </td>
    <td><p id='date'>$daynow\.$ai{$monthnow}\.$yearnow</p></td></tr>
    <tr $yelclr1><td>Волонтёр: $b1 $OEP_VolunteerOne{$clsGrpId} $b2</td><td><select name = 'volone'>
   <option value = 'false'>Не пришел</option><option value = 'true'>Пришел</option></select></td></tr>
    <tr $yelclr><td>Волонтёр: $b1 $OEP_VolunteerTwo{$clsGrpId} $b2</td><td><select name = 'voltwo'>
   <option value = 'false'>Не пришел</option><option value = 'true'>Пришел</option></select></td></tr>
    </table>\n"; # The lesson's date
    print "<p> </p><table>
    <caption><a href=\'$httpreadcgi?list=groups\&schoolid=$whatis{'schoolid'}\'>$whatis{'schoolid'}-ая</a> Школа [группа № $whatis{'groupid'}]</caption>\n";
    print "<tr $myclr><td>N</td><td>Students Name</td><td>Participation</td><td>Late</td><td>LIFT [-]</td>";
    print "<td>Test %</td><td>LIFT [+]</td><td>Total</td><td>Evaluation</td><td>Comments</td><td>Homework Quality</td></tr>\n";
    foreach $stdid (@studentUniqueNumList){
       if($studentGroupNum{$stdid} =~ $whatis{'groupid'}){
          if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
          $cnt++;
print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' name = 'userid' value= \'$stdid\'></td>";
print "<td id='name'><a href='#' onclick='return checkFunction($cnt, 1);'>$studentFirstName{$stdid} $studentThirdName{$stdid} $studentSecondName{$stdid}</a></td>\n"; #Students name
print "<td id='part'><p id='part_$stdid\'>Пришел на урок?</p>
<input type='hidden' name='part_$stdid\' value='0'></td>\n"; # Participation
print "<td id='late'><a href='#' onclick='return checkFunction($cnt, 2);'>Опоздал?</a><p id='late_$stdid\'></p>
<input type='hidden' name='late_$stdid\' value='0'></td>\n"; # Late
print "<td id='liftminus'><p id='liftMinus_$stdid\'></p><input type='hidden' name='liftMinus_$stdid\' value='0'></td>\n"; # LIFT minus
print "<td id='test'><a href='#' onclick='return checkFunction($cnt, 3);'>Тестирование?</a>
<p id='test_$stdid\'></p><input type='hidden' name='test_$stdid\' value='0'></td>\n"; # Test %
print "<td id='liftplus'><p id='liftPlus_$stdid\'></p><input type='hidden' name='liftPlus_$stdid\' value='0'></td>\n"; # LIFT plus
print "<td id='total'><p id='totalPoints_$stdid\'></p><input type='hidden' name='totalPoints_$stdid\' value='0'></td>\n"; # TOTAL POINTS
print "<td id='eval'><a href='#' onclick='return checkFunction($cnt, 4);'>Оценить?</a><p id='eval_$stdid\'></p>
<input type='hidden' name='eval_$stdid\' value='0'></td>
<td><input type='text' name='comm_$stdid\' value=''></td><td><select name='home_$stdid\'><option value='' selected>Choose one</option>
<option value='1'>1</option><option value='2'>2</option><option value='3'>3</option><option value='4'>4</option><option value='5'>5</option>
<option value='6'>6</option><option value='7'>7</option><option value='8'>8</option><option value='9'>9</option><option value='10'>10</option>
</select></td></tr>\n"; 
        }
    } #<h4 id="text1" style="display:none">This is some toggleable text</h4>
print "</table>\n<input type='hidden' id = 'totalusers' name = 'totalusers' value= \'$cnt\'><a href='#' onclick='return showFunction();'>Комментарии?</a>\n
<table id='comments' style='display:none'> <tr $yelclr> <td>.</td> <td>Вопросы по проведенному занятию:</br>
Были ли проблемы в целом, какие - опишите!</br>
Какие из упражнений понравились ученикам, какие - опишите!</br>
Сталкивались вы с техническими проблемами, какие - опишите!</br>
Что именно не получилось сделать в ходе проведенного занятия - опишите!</td>
<td><textarea rows='10' cols='50' name ='comments'></textarea></td></tr></table>
<table><tr><td $ac><input type = 'reset' value = 'Reset' style='height:50px; width:150px'></td>
<td> -[-]-[-]-[-]- </td><td $ac><input type = 'submit' value = 'Record Data' style='height:50px; width:150px'></td></tr></table>\n";
  #  print "<br>\n <p><a href=\'$httpreadcgi?list=all\'>Общий список в основной таблице</a></p>\n";
}
#####################################################################################
########################## RECORD LESSON SUB ########################################
#####################################################################################
sub recordLessonSub { &getGroupSub(); $cnt = 1; $myclr = $yelclr; $rlsGrpId = $whatis{'groupid'};
    print "<table><tr $yelclr><td>Parameters</td><td>Values</td></tr>
    <tr $yelclr1><td>School</td><td><a href=\'$httpreadcgi?list=groups\&schoolid=$whatis{'schoolid'}\'>$whatis{'schoolid'}</a></td></tr>
    <tr $yelclr><td>Group</td><td>$whatis{'groupid'}</td></tr><tr $yelclr1><td>Lesson Number</td><td>$whatis{'lesson'}</td></tr>
    <tr $yelclr><td>Date</td><td>$whatis{'date'}</td></tr><tr $yelclr1><td>Topic</td><td>$whatis{'topic'}</td></tr></table>\n
    <table><tr $yelclr><td>N</td><td>Students name</td><td>Participation</td><td>Late</td><td>LIFT [-]</td><td>Test %</td>
    <td>LIFT [+]</td><td>Total</td><td>Evaluation</td></tr>\n"; 
    foreach $stdid (@studentUniqueNumList) { $myclr = $yelclr;
        if ( $studentGroupNum{$stdid} =~ $whatis{'groupid'} ) {
           $rlspart = 'part_' . $stdid; $rlslate = 'late_' . $stdid; $rlstest = 'test_' . $stdid;  
           $rlseval = 'eval_' . $stdid; $rlscomm = 'comm_' . $stdid; $rlshome = 'home_' . $stdid; 
           if ( $whatis{$rlspart} eq '1' ) {
              $rlsLiftMinus{$stdid} = $whatis{$rlslate} * 10; if($whatis{$rlstest} > 50){$rlsLiftPlus{$stdid} = ($whatis{$rlstest} - 50) * 10;}
              $rlsTotalPoints{$stdid} = 1200 - $rlsLiftMinus{$stdid} + $rlsLiftPlus{$stdid};  
              $cnt1 = $cnt / 2; $cnt2 = int( $cnt / 2 ); if ( $cnt1 == $cnt2 ) { $myclr = $yelclr; } else { $myclr = $yelclr1; }
              print "<tr $myclr><td>$cnt</td><td>$studentFirstName{$stdid} $studentThirdName{$stdid} $studentSecondName{$stdid}</td> 
              <td>$whatis{$rlspart}</td> <td>$whatis{$rlslate}</td> <td>$rlsLiftMinus{$stdid}</td> <td>$whatis{$rlstest}</td>
               <td>$rlsLiftPlus{$stdid}</td> <td>$rlsTotalPoints{$stdid}</td> <td>$whatis{$rlseval}</td></tr>\n";
              $newline = $newline . "OEP_Participation\_$stdid: $whatis{$rlspart}\n";
              $newline = $newline . "OEP_LateMinutes\_$stdid: $whatis{$rlslate}\n";
              $newline = $newline . "OEP_LiftMinus\_$stdid: $rlsLiftMinus{$stdid}\n";
              $newline = $newline . "OEP_Tests\_$stdid: $whatis{$rlstest}\n";
              $newline = $newline . "OEP_LiftPlus\_$stdid: $rlsLiftPlus{$stdid}\n";
              $newline = $newline . "OEP_TotalPoints\_$stdid: $rlsTotalPoints{$stdid}\n";
              $newline = $newline . "OEP_Eval\_$stdid: $whatis{$rlseval}\n";
              $newline = $newline . "OEP_UserComment\_$stdid: $whatis{$rlscomm}\n";
              $newline = $newline . "OEP_HomeWork\_$stdid: $whatis{$rlshome}\n";
           }
           else{
           $cnt1 = $cnt / 2; $cnt2 = int( $cnt / 2 ); if ( $cnt1 == $cnt2 ) { $myclr = $yelclr; } else { $myclr = $yelclr1; }
           print "<tr $myclr><td>$cnt</td><td>$studentFirstName{$stdid} $studentThirdName{$stdid} $studentSecondName{$stdid}</td> 
           <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td></tr>\n";}
            $cnt++; 
        }
    }
    $whatis{'comments'} =~s/\n/<br>/g; $whatis{'comments'} =~s/\n//g; $whatis{'comments'} =~s/\n//g;
    print "</table>\n<br><table><tr $myclr><td>Comments and remarks: </td><td>$whatis{'comments'}</td></tr></table>\n";
    $group_file = $groups_folder . $whatis{'groupid'} . '.txt';
    $generateRandomNumber =  $gotusrid . '-' .  $yearnow . $daynow . $ai{$monthnow} .  $hournow . $minutenow . $secondnow;
    open(OEPDATA,">>$group_file");
    #binmode(OEPDATA, ":utf8");
    print OEPDATA "\n<start of new project = $generateRandomNumber>\n";
    if ( $whatis{'volone'} eq 'true' ) { print OEPDATA "OEP_VolunteerOneWas: $OEP_VolunteerOneCode{$rlsGrpId}\n"; }
    if ( $whatis{'voltwo'} eq 'true' ) { print OEPDATA "OEP_VolunteerTwoWas: $OEP_VolunteerTwoCode{$rlsGrpId}\n"; }
    print OEPDATA "OEP_School: $whatis{'schoolid'}\n";
    print OEPDATA "OEP_Group: $whatis{'groupid'}\n";
    print OEPDATA "OEP_Lesson: $whatis{'lesson'}\n";
    print OEPDATA "OEP_Date: $whatis{'date'}\n";
    print OEPDATA "OEP_Topic: $whatis{'topic'}\n";
    print OEPDATA $newline;
    print OEPDATA "OEP_Comments: $whatis{'comments'}\n";
    close(OEPDATA);
    print "<p>.</p><p><a href=\'$httpreadcgi?list=schools\'>Список всех школ</a></p>\n";
 #   print "<br>\n <p>.</p><p><a href=\'$httpreadcgi?list=all\'>Общий список в основной таблице</a></p>\n";
}
#####################################################################################
########################## FINISH END BODY #########################################
#####################################################################################

if($userlogged == 1){
   if ( $gotusrid eq '6' || $gotusrid eq '8' || $gotusrid eq '3' ){
      open(INF, $adminText_file); @adminTextList = <INF>; close(INF); print @adminTextList; 
      &printfile($end, $title);
   }
}
else {print "</body></html>";}
#if($userbrowser eq 'desktop'){print "<p><a href=\'$httpindexcgi\?browser=mobile\'>MOBILE</p>\n";}
#else{print "<p><a href=\'$httpindexcgi\?browser=desktop\'>DESKTOP</p>\n";}

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