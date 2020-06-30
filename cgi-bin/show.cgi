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
@glbRateListText = ('Нет слов', 'Восхитительно', 'Прекрасно','Замечательно', 'Отлично', 'Великолепно');
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$glMonthPayValue = 5500;
$indexcgi = 'show.cgi';
$students_file = $oe_folder . 'students.txt';
$lessons_file = $oe_folder . 'lessons.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httplimbocgi = 'http://accelerator.kvadra.kz/cgi-bin/limbo.cgi';
$httpschlviewcgi = 'http://accelerator.kvadra.kz/cgi-bin/schoolview.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Уроки';

open(INF, $lessons_file); @lessonslist = <INF>; close(INF); foreach $i(@lessonslist){  chomp($i); 
    ($lesspwd, $lessnum, $lessgrp, $lesschl, $lessdate, $lesstime, @other) = split (/<tab>/, $i);
    $lessonNumber{$lesspwd} = $lessnum; $lessonGroup{$lesspwd} = $lessgrp; 
    $lessonSchool{$lesspwd} = $lesschl; $lessonDate{$lesspwd} = $lessdate;
    if ( $lessdate eq $datenow ) { $lessonExist{$lesspwd} = 1; } $lessonTime{$lesspwd} = $lesstime;
}

open(INF, $students_file); 
@studentslist = <INF>; 
close(INF); 
@uniqueSchoolNumList = "";  @uniqueGroupNumList = "";  @studentUniqueNumList = "";
foreach $i(@studentslist){ 
   ($tstudnum, $tstudid, $tstudfirstnam, $tstudscndnam, $tstudthrdnam, $tstudschl, $tstudgrp, @other) = split (/<tab>/, $i);
   if ( $tstudgrp ne '' && $tstudschl ne '' ) { $studentFullName{$tstudid} = "$tstudfirstnam $tstudscndnam";
      $studentFirstName{$tstudid} = $tstudfirstnam; $studentSecondName{$tstudid} = $tstudscndnam;
      $studentThirdName{$tstudid} = $tstudthrdnam; $studentPositionNum{$tstudid} = $tstudnum; 
      $studentSchoolNum{$tstudid} = $tstudschl; $studentGroupNum{$tstudid} = $tstudgrp; 
      $studentGroupList{$tstudgrp} = $studentGroupList{$tstudgrp} . '<tab>' . $tstudid;
   }
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

print "\n"; &printfile($bas, $title);

if ( $whatis{'action'} ne '' ) { open(GURD,">>$log_file");
print GURD "Time: [$timedatenow] User ID: [$gotusrid] IP address: [$userip] User action: [$whatis{'action'}] Script: [$indexcgi] \n";
close(GURD); }

#####################################################################################
########################## LOGIN CHECK PART #######################################
#####################################################################################
print "<p> </p>";

if ( $whatis{'action'} eq 'show' && $whatis{'code'} ne '' ) { 
   if ( $lessonExist{$whatis{'code'}} == 1 ) { &openLessonSub(); }
   else { print "<h3>По данному коду [$whatis{'code'}] открытых уроков не обнаружено!</h3>\n"; &openBlankPage(); } }
elsif ( $whatis{'action'} eq 'save' && $whatis{'studid'} ne '' && $whatis{'groupid'} ne '' ) { &saveMyDataSub(); }
else { &openBlankPage(); }
 
print "<p> </p><p><a href=\'$httpindexcgi\'>[ Вернуться ДОМОЙ ]</a></p>\n"; 



#####################################################################################
########################### START MAIN BODY #########################################
#####################################################################################
sub openBlankPage {
   print "<h2>Введите кодовое слово чтобы открыть урок</h2>\n<p> </p>
   <form method='post' action=\'$httpindexcgi\'><input type = 'hidden' name = 'action' value = 'show'>
   <table><tr $yelclr><td>Ваш код урока: </td><td><input type = 'text' name = 'code' value = \'$whatis{'code'}\'>
   </td></tr></table><input type = 'submit' value = 'ENTER' style='height:50px; width:150px'></form>\n";
}

#####################################################################################
########################### SAVE MY DATA SUB ########################################
#####################################################################################
sub saveMyDataSub { $smdId = $whatis{'studid'}; $smdPrt = $whatis{'participate'}; $smdRt = $whatis{'rate'};
   $smdPartTxt{'true'} = 'Был на уроке'; $smdPartTxt{'false'} = 'Не был на уроке';
   print "<h2>Присутствие ученика на уроке</h2>\n<p> </p>
   <table $grnclr><caption><h3>Ваши данные записаны</h3></caption>
   <tr $yelclr><td>Группа: </td><td $ac>$whatis{'groupid'}</td><td>№ урока: </td><td>$whatis{'lessid'}</td></tr>
   <tr $yelclr1><td>Дата: </td><td $ac>$whatis{'date'}</td><td>Время урока: </td><td>$whatis{'time'}</td></tr>
   <tr $yelclr><td>Имя ученика: </td><td $ac>$studentFirstName{$smdId}</td><td>Фамилия: </td><td>$studentSecondName{$smdId}</td></tr>
   <tr $yelclr1><td>Присутствие: </td><td $ac>$smdPartTxt{$smdPrt}</td><td>Впечатления: </td><td>$glbRateListText[$smdRt]</td></tr>
   </table><p> </p>\n";
   ($smdSchoolId, @oters) = split(/-/, $whatis{'groupid'}); $smdFileName = $groups_folder . $whatis{'groupid'} . '_part.txt';
   $smdLineTxt = "$whatis{'code'}<tab>$whatis{'studid'}<tab>$smdSchoolId<tab>$whatis{'groupid'}<tab>$whatis{'lessid'}<tab>$whatis{'date'}";
   $smdLineTxt = $smdLineTxt . "<tab>$whatis{'time'}<tab>$whatis{'participate'}<tab>$whatis{'rate'}<tab>$timedatenow<tab>rest\n";
   open(SMDATA,">>$smdFileName");   print SMDATA $smdLineTxt;   close(SMDATA);
   &checkPartDataSub($whatis{'groupid'}, $whatis{'lessid'}, $whatis{'code'});
}

#####################################################################################
############################### OPEN LESSON SUB #####################################
#####################################################################################
sub openLessonSub { $olsLessCode = $whatis{'code'}; $olsGrpId = $lessonGroup{$olsLessCode};
   (@olsStudList) = split(/<tab>/, $studentGroupList{$olsGrpId});
   ($olsHour, $olsMins, $olsSecs) = split(/\:/, $lessonTime{$olsLessCode});
   $olsTimeIndx = $hournow - $olsHour;  if( $olsTimeIndx > 2 ) { print "<h3>Урок уже завершился!</h3>"; return; }
   print "<p> </p><form method='post' action=\'$httpindexcgi\'><input type = 'hidden' name = 'action' value = 'save'>
   <input type = 'hidden' name = 'groupid' value = \'$lessonGroup{$olsLessCode}\'>
   <input type = 'hidden' name = 'lessid' value = \'$lessonNumber{$olsLessCode}\'>
   <input type = 'hidden' name = 'date' value = \'$lessonDate{$olsLessCode}\'>
   <input type = 'hidden' name = 'time' value = \'$lessonTime{$olsLessCode}\'>
   <input type = 'hidden' name = 'code' value = \'$olsLessCode\'>
   <table><caption>$lessonSchool{$olsLessCode}-ая Школа</caption>
   <tr $yelclr><td>Группа №</td>  <td $ac>$lessonGroup{$olsLessCode}</td></tr>
   <tr $yelclr1><td>Номер урока</td><td $ac>$lessonNumber{$olsLessCode}</td></tr>
   <tr $yelclr><td>Дата урока</td><td $ac>$lessonDate{$olsLessCode}</td></tr></table><p> </p><table>
   <tr $yelclr1><td>№</td><td>Имя Фамилия</td><td>Посещение</td><td>Оценка за урок</td></tr>
   <tr $myclr><td>$cnt</td><td><select name = 'studid'><option value = ''>Выберите себя</option>\n";
   foreach $i ( @olsStudList ) { if ( $i ne '' ) { $cnt++; 
      if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; }
      print "<option value = \'$i\'>$studentFirstName{$i} $studentSecondName{$i}</option>\n";   
   } }
   print "</select></td><td $ac><select name = 'participate'><option value = 'false'>Не был на уроке</option>
   <option value = 'true'>Был на уроке</option></select></td><td><select name = 'rate'>
   <option value = '0'>$glbRateListText[0] 0</option><option value = '1'>$glbRateListText[1] 1</option>
   <option value = '2'>$glbRateListText[2] 2</option><option value = '3'>$glbRateListText[3] 3</option>
   <option value = '4'>$glbRateListText[4] 4</option><option value = '5'>$glbRateListText[5] 5</option></select></td>
   </tr></table><input type = 'submit' value = 'SAVE' style='height:50px; width:150px'></form><p> </p>\n";
   &checkPartDataSub($olsGrpId, $lessonNumber{$olsLessCode}, $olsLessCode);
}

#@glbRateListText = ('Нет слов', 'Восхитительно', 'Прекрасно','Замечательно', 'Отлично', 'Великолепно');
#####################################################################################
##################### CHECK PARTICIPATION DATA SUB ##################################
#####################################################################################
sub checkPartDataSub { ($cpdGrpId, $cpdLessId, $cpdCode) = @_; $cpdCnt = 0; $myclr = $yelclr;
   $cpdFileName = $groups_folder . $cpdGrpId . '_part.txt'; @cpdStudList = '';
   open(INF, $cpdFileName);   @cpdFileList = <INF>;   close(INF);
   foreach $cpdLine ( @cpdFileList ) { if ( $cpdLine ne '' ) { chomp($cpdLine);
      ($tcpdCode, $tcpdStudId, $tcpdSchlId, $tcpdGrpId, $tcpdLessId, $tcpdDate, 
      $tcpdTime, $tcpdPart, $tcpdRate, $tcpdTimeStamp, @other) = split (/<tab>/, $cpdLine);
      if ( $cpdCode eq $tcpdCode && $cpdGrpId eq $tcpdGrpId && $cpdLessId eq $tcpdLessId ) {
         if ( grep( /^$tcpdStudId$/, @cpdStudList ) ) { $done = 1; } else { push(@cpdStudList, $tcpdStudId); }
         $cpdSchlId{$tcpdStudId} = $tcpdSchlId; $cpdDate{$tcpdStudId} = $tcpdDate; 
         $cpdTime{$tcpdStudId} = $tcpdTime; $cpdRate{$tcpdStudId} = $tcpdRate;
         if ( $tcpdPart eq 'true' ) { $cpdPartTxt{$tcpdStudId} = 'Был на уроке'; } 
         else { $cpdPartTxt{$tcpdStudId} = 'Не был на уроке'; } 
      }
   } }
   
   print "<table><caption><h3>Список участников урока [$cpdLessId] группы [$cpdGrpId]</h3></caption>
   <tr $myclr><td>No</td><td>ФИО ученика</td><td>Присутствие</td><td>Оценка</td><td>Дата урока</td><td>Время урока</td></tr>\n";
   (@cpdStudList) = split(/<tab>/, $studentGroupList{$cpdGrpId});
   foreach $id (@cpdStudList) { if ( $id ne '' ) { $cdpIndx = $cpdRate{$id}; 
      if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; } $cpdCnt++;
      print "<tr $myclr><td>$cpdCnt</td><td>$studentFirstName{$id} $studentSecondName{$id}</td><td>$cpdPartTxt{$id}</td>
      <td>$glbRateListText[$cdpIndx]</td><td>$cpdDate{$id}</td><td>$cpdTime{$id}</td></tr>\n";
   } }
   print "</table>\n";
}

#####################################################################################
########################### FINISH END BODY #########################################
#####################################################################################

print "</center></body></html>";

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