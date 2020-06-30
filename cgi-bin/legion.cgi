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
$bas = $oe_folder  . 'bas.txt';
$basm = $oe_folder  . 'basm.txt';
$end = $oe_folder . 'end.txt';
$indexcgi = 'legion.cgi';
$students_file = $oe_folder . 'students.txt';
$legion_file = $oe_folder . 'legion.txt';
$legiongroups_file = $oe_folder . 'legiongroups.txt';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httphomecgi = 'http://accelerator.kvadra.kz/cgi-bin/read.cgi?list=all';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Утвержденные волонтеры';

open(INF, $cookie_file); @cookielist = <INF>; close(INF); foreach $i(@cookielist){
    chomp($i); #8<tab>8250732421875<tab>Tue Apr 23 14:16:01 2013<tab>172.28.113.66<tab>reserve
    ($clusrnum, $clusrrnd, $clusrdate, $clusrip, @other) = split (/<tab>/, $i);
    $oeusercookiernd{$clusrnum} = $clusrrnd;
    $oeusercookiedate{$clusrnum} = $clusrdate;
    $oeusercookieip{$clusrnum} = $clusrip;
}

open(INF, $legion_file);   @legionlist = <INF>;   close(INF);
open(INF, $legiongroups_file);   @legiongroupslist = <INF>;   close(INF);
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
    if ( $whatis{'action'} eq 'edit' && $whatis{'legionerid'} ne '' ) { &editLegionerDataSub(); }
    elsif ( $whatis{'action'} eq 'save' && $whatis{'legionerid'} ne '' ) { &saveLegionerDataSub(); }
    elsif ( $whatis{'action'} eq 'assign' && $whatis{'legionerid'} ne '' ) { &assignGroupLegionSub(); }
    elsif ( $whatis{'action'} eq 'savegroup' && $whatis{'groupid'} ne '' && $whatis{'legionerid'} ne '' ) { &saveGroupDataSub(); }
    elsif ( $whatis{'action'} eq 'creategroup' && $whatis{'groupid'} =~ /GRP/ ) { &createGroupDataSub(); }
    elsif ( $whatis{'action'} eq 'editgroup' && $whatis{'groupid'} =~ /GRP/ ) { &editGroupDataSub(); }
    elsif ( $whatis{'action'} eq 'listgroup' && $whatis{'groupid'} =~ /GRP/ ) { &showGroupListSub(); }
    elsif ( $whatis{'action'} eq 'showgroups' ) { &showGroupListSub(); }
    elsif ( $whatis{'action'} eq 'newgroup' ) { &makeNewGroupSub(); }
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
######################### CREATE GROUP DATA SUB #####################################
#####################################################################################
sub createGroupDataSub { $cgdStyle = "style='height:50px; width:150px'"; 
   $cgdGrpId = $whatis{'groupid'}; $cgdGrpFound = 0; $cgdGrpNum = 0;
   print "<h2>Сохранение данных группы обучения волонтеров OpenEnglish</h2> <p> </p>\n";
   #1<tab>GRP1001<tab>Описание группы<tab>Active<tab>Sun Jul 28 20:15:48 2019<tab>reserve
   foreach $cgdLine (@legiongroupslist) { $cgdChompLine = $cgdLine; chomp($cgdChompLine); 
      ($tgrpnm, $tgrpid, $tgrpdscrp, $tgrpstat, $tgrpdate, @other) = split (/<tab>/, $cgdChompLine);
      $cgdGrpNewNum = $tgrpnm + 1; $cgdGrpNum = $tgrpnm; $cgdGrpCreated = $tgrpdate;
      if ( $cgdGrpId eq $tgrpid && $tgrpid ne '' ) { $cgdGrpFound = 1;
         $cgdNewLine = "$tgrpnm<tab>$whatis{'groupid'}<tab>$whatis{'descript'}<tab>$whatis{'status'}<tab>$tgrpdate<tab>reserve\n"; 
         push (@cgdNewLegionGroupsList, $cgdNewLine);  }
      else { push (@cgdNewLegionGroupsList, $cgdLine); }
   }
   $cgdNewLine = "$cgdGrpNewNum<tab>$whatis{'groupid'}<tab>$whatis{'descript'}<tab>$whatis{'status'}<tab>$timedatenow<tab>reserve\n";
   if ( $whatis{'grouptype'} eq 'old' ) { $cgdCreated = $whatis{'created'}; $cgdCreator = $whatis{'author'};
      open(CGDATA,">$legiongroups_file"); print CGDATA @cgdNewLegionGroupsList; close(CGDATA); 
      print "<p> </p><table $grnclr><tr><td><h3> Данные группы успешно сохранены! </h3></td></tr></table> <table>
      <tr $yelclr><td>Кто корректировал данные: </td><td $ac>$username{$gotusrid}</td><td>Дата изменений: </td><td $ac>$timedatenow</td></tr>
      <tr $yelclr1><td>Уникальный ID группы: </td><td $ac>$cgdGrpNewNum</td><td>Уникальное описание группы: </td><td $ac>$whatis{'descript'}</td></tr>
      <tr $yelclr><td>статус группы: </td><td $ac>$whatis{'status'}</td><td>Название Тренинга: </td><td $ac>$whatis{'course'}</td></tr>
      <tr $yelclr1><td>Кто Ведет Тренинг: </td><td $ac>$whatis{'trainer'}</td><td>Дата начала обучения: </td><td $ac>$whatis{'startdate'}</td></tr>
      <tr $yelclr><td>Дата 1-го Занятия: </td><td $ac>$whatis{'firstdate'}</td><td>Время 1-го Занятия: </td><td $ac>$whatis{'firsttime'}</td></tr>
      <tr $yelclr1><td>Дата 2-го Занятия: </td><td $ac>$whatis{'seconddate'}</td><td>Время 2-го Занятия: </td><td $ac>$whatis{'secondtime'}</td></tr>
      <tr $yelclr><td>Дата 3-го Занятия: </td><td $ac>$whatis{'firstdate'}</td><td>Время 3-го Занятия: </td><td $ac>$whatis{'firsttime'}</td></tr>
      <tr $yelclr1><td>Дата 4-го Занятия: </td><td $ac>$whatis{'seconddate'}</td><td>Время 4-го Занятия: </td><td $ac>$whatis{'secondtime'}</td></tr>
      <tr $yelclr><td>Дата 5-го Занятия: </td><td $ac>$whatis{'firstdate'}</td><td>Время 5-го Занятия: </td><td $ac>$whatis{'firsttime'}</td></tr>
      <tr $yelclr1><td>Дата 6-го Занятия: </td><td $ac>$whatis{'seconddate'}</td><td>Время 6-го Занятия: </td><td $ac>$whatis{'secondtime'}</td></tr>
      <tr $yelclr><td>Дата Коучинг Занятия: </td><td $ac>$whatis{'couchdate'}</td><td>Время Коучинг Занятия: </td><td $ac>$whatis{'couchtime'}</td></tr>
      <tr $yelclr1><td>Дата Пробного Занятия: </td><td $ac>$whatis{'testdate'}</td><td>Время Пробного Занятия: </td><td $ac>$whatis{'testtime'}</td></tr>
      </table>\n"; }
   elsif ( $whatis{'grouptype'} eq 'new' ) { $cgdCreated = $timedatenow; $cgdCreator = $gotusrid;
      open(CGDATA,">>$legiongroups_file"); print CGDATA $cgdNewLine; close(CGDATA); 
      print "<p> </p><table $grnclr><tr><td><h3> Новая группа успешно создана! </h3></td></tr></table> <table>
      <tr $yelclr><td>Кто создал группу: </td><td $ac>$username{$gotusrid}</td><td>Дата создания: </td><td $ac>$timedatenow</td></tr>
      <tr $yelclr1><td>Уникальный ID группы: </td><td $ac>$cgdGrpNewNum</td><td>Уникальное описание группы: </td><td $ac>$whatis{'descript'}</td></tr>
      <tr $yelclr><td>статус группы: </td><td $ac>$whatis{'status'}</td><td>Название Тренинга: </td><td $ac>$whatis{'course'}</td></tr>
      <tr $yelclr1><td>Кто Ведет Тренинг: </td><td $ac>$whatis{'trainer'}</td><td>Дата начала обучения: </td><td $ac>$whatis{'startdate'}</td></tr>
      <tr $yelclr><td>Дата 1-го Занятия: </td><td $ac>$whatis{'firstdate'}</td><td>Время 1-го Занятия: </td><td $ac>$whatis{'firsttime'}</td></tr>
      <tr $yelclr1><td>Дата 2-го Занятия: </td><td $ac>$whatis{'seconddate'}</td><td>Время 2-го Занятия: </td><td $ac>$whatis{'secondtime'}</td></tr>
      <tr $yelclr><td>Дата 3-го Занятия: </td><td $ac>$whatis{'firstdate'}</td><td>Время 3-го Занятия: </td><td $ac>$whatis{'firsttime'}</td></tr>
      <tr $yelclr1><td>Дата 4-го Занятия: </td><td $ac>$whatis{'seconddate'}</td><td>Время 4-го Занятия: </td><td $ac>$whatis{'secondtime'}</td></tr>
      <tr $yelclr><td>Дата 5-го Занятия: </td><td $ac>$whatis{'firstdate'}</td><td>Время 5-го Занятия: </td><td $ac>$whatis{'firsttime'}</td></tr>
      <tr $yelclr1><td>Дата 6-го Занятия: </td><td $ac>$whatis{'seconddate'}</td><td>Время 6-го Занятия: </td><td $ac>$whatis{'secondtime'}</td></tr>
      <tr $yelclr><td>Дата Коучинг Занятия: </td><td $ac>$whatis{'couchdate'}</td><td>Время Коучинг Занятия: </td><td $ac>$whatis{'couchtime'}</td></tr>
      <tr $yelclr1><td>Дата Пробного Занятия: </td><td $ac>$whatis{'testdate'}</td><td>Время Пробного Занятия: </td><td $ac>$whatis{'testtime'}</td></tr>
      </table>\n"; 

   }
   else { print "<p> </p><h3>$rf Нет данных для записи! $f2</h3>\n"; }
   $cgdGroupFile = $groups_folder . $cgdGrpId . '_data.txt';
   open( CGDATA,">$cgdGroupFile");
   print CGDATA "\n<start of new project = $cgdCreated>\n";
   print CGDATA "LEG_Created: $cgdCreated\n";
   print CGDATA "LEG_Creator: $cgdCreator\n";
   print CGDATA "LEG_LastEdited: $timedatenow\n";
   print CGDATA "LEG_Editor: $gotusrid\n";
   print CGDATA "LEG_Description: $whatis{'descript'}\n";
   print CGDATA "LEG_Status: $whatis{'status'}\n";
   print CGDATA "LEG_Course: $whatis{'course'}\n";
   print CGDATA "LEG_Traineer: $whatis{'trainer'}\n";
   print CGDATA "LEG_Group: $whatis{'groupid'}\n";
   print CGDATA "LEG_StartDate: $whatis{'startdate'}\n";
   print CGDATA "LEG_DayOne: $whatis{'firstdate'}\n";
   print CGDATA "LEG_DayTwo: $whatis{'seconddate'}\n";
   print CGDATA "LEG_DayThree: $whatis{'thirddate'}\n";
   print CGDATA "LEG_DayFour: $whatis{'forthdate'}\n";
   print CGDATA "LEG_DayFive: $whatis{'fifthdate'}\n";
   print CGDATA "LEG_DaySix: $whatis{'sixthdate'}\n";
   print CGDATA "LEG_CouchDay: $whatis{'couchdate'}\n";
   print CGDATA "LEG_TestDay: $whatis{'testdate'}\n";
   print CGDATA "LEG_TimeOne: $whatis{'firsttime'}\n";
   print CGDATA "LEG_TimeTwo: $whatis{'secondtime'}\n";
   print CGDATA "LEG_TimeThree: $whatis{'thirdtime'}\n";
   print CGDATA "LEG_TimeFour: $whatis{'forthtime'}\n";
   print CGDATA "LEG_TimeFive: $whatis{'fifthtime'}\n";
   print CGDATA "LEG_TimeSix: $whatis{'sixthtime'}\n";
   print CGDATA "LEG_CouchTime: $whatis{'couchtime'}\n";
   print CGDATA "LEG_TestTime: $whatis{'testtime'}\n";
   close(CGDATA);
   
   print "<p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";
}

#####################################################################################
########################### EDIT GROUP DATA SUB #####################################
#####################################################################################
sub editGroupDataSub { &printjavascript(); $egdGrpFound = 0; &getGroupSub();
   $egdStyle = "style='height:50px; width:150px'"; $egdGrpId = $whatis{'groupid'}; 
   print "<h2>Редактирование группы обучения волонтеров OpenEnglish</h2> <p> </p>
   <form method='post' action=\'$httpindexcgi\' onsubmit='return checkNewGrpFunction();'>
   <input type = 'hidden' name = 'action' value = 'creategroup'><input type = 'hidden' name = 'grouptype' value = 'old'>
   <input type = 'hidden' name = 'groupid' value = \'$egdGrpId\'><input type = 'hidden' name = 'author' value = \'$LEG_Editor{$egdGrpId}\'>
   <input type = 'hidden' name = 'created' value = \'$LEG_Created{$egdGrpId}\'><table>\n";
   #1<tab>GRP1001<tab>Описание группы<tab>Active<tab>Sun Jul 28 20:15:48 2019<tab>reserve
   foreach $egdLine (@legiongroupslist) { $egdChompLine = $egdLine; chomp($egdChompLine); 
      ($tgrpnm, $tgrpid, $tlgrpdscrp, $tlgrpstat, @other) = split (/<tab>/, $egdChompLine);
      if ( $egdGrpId eq $tgrpid && $tgrpid ne '' ) { $egdGrpFound = 1; $egdUserName = $username{$LEG_Editor{$egdGrpId}};
         print "<tr $yelclr><td>Уникальное описание группы</td><td><input type = 'text' name = 'descript' value = \'$tlgrpdscrp\'></td>
         <td>Выберите статус группы</td><td><select name = 'status'>\n";
         if ( $tlgrpstat ne '' ) { print "<option value = \'$tlgrpstat\' selected>$tlgrpstat</option>\n"; }
         print "<option value = 'Active'>Active</option><option value = 'Frozen'>Frozen</option>
         <option value = 'Finished'>Finished</option><option value = 'Cancelled'>Cancelled</option></select></td></tr>
         <tr $yelclr1><td>Название Тренинга: </td><td><input type = 'text' name = 'course' value = \'$LEG_Course{$egdGrpId}\'></td>
         <td>Кто Ведет Тренинг: </td><td><input type = 'text' name = 'trainer' value = \'$LEG_Traineer{$egdGrpId}\'></td></tr>
         <tr $yelclr><td>Дата начала обучения: </td><td><input type = 'text' name = 'startdate' value = \'$LEG_StartDate{$egdGrpId}\'></td>
         <td>Кто и когда создал группу: </td><td $ac><b>$egdUserName $LEG_Created{$egdGrpId}</b></td></tr>
         <tr $yelclr1><td>Дата 1-го Занятия: </td><td><input type = 'text' name = 'firstdate' value = \'$LEG_DayOne{$egdGrpId}\'></td>
         <td>Время 1-го Занятия: </td><td><input type = 'text' name = 'firsttime' value = \'$LEG_TimeOne{$egdGrpId}\'></td></tr>
         <tr $yelclr><td>Дата 2-го Занятия: </td><td><input type = 'text' name = 'seconddate' value = \'$LEG_DayTwo{$egdGrpId}\'></td>
         <td>Время 2-го Занятия: </td><td><input type = 'text' name = 'secondtime' value = \'$LEG_TimeTwo{$egdGrpId}\'></td></tr>
         <tr $yelclr1><td>Дата 3-го Занятия: </td><td><input type = 'text' name = 'thirddate' value = \'$LEG_DayThree{$egdGrpId}\'></td>
         <td>Время 3-го Занятия: </td><td><input type = 'text' name = 'thirdtime' value = \'$LEG_TimeThree{$egdGrpId}\'></td></tr>
         <tr $yelclr><td>Дата 4-го Занятия: </td><td><input type = 'text' name = 'forthdate' value = \'$LEG_DayFour{$egdGrpId}\'></td>
         <td>Время 4-го Занятия: </td><td><input type = 'text' name = 'forthtime' value = \'$LEG_TimeFour{$egdGrpId}\'></td></tr>
         <tr $yelclr1><td>Дата 5-го Занятия: </td><td><input type = 'text' name = 'fifthdate' value = \'$LEG_DayFive{$egdGrpId}\'></td>
         <td>Время 5-го Занятия: </td><td><input type = 'text' name = 'fifthtime' value = \'$LEG_TimeFive{$egdGrpId}\'></td></tr>
         <tr $yelclr><td>Дата 6-го Занятия: </td><td><input type = 'text' name = 'sixthdate' value = \'$LEG_DaySix{$egdGrpId}\'></td>
         <td>Время 6-го Занятия: </td><td><input type = 'text' name = 'sixthtime' value = \'$LEG_TimeSix{$egdGrpId}\'></td></tr>
         <tr $yelclr1><td>Дата Коучинг Занятия: </td><td><input type = 'text' name = 'couchdate' value = \'$LEG_CouchDay{$egdGrpId}\'></td>
         <td>Время Коучинг Занятия: </td><td><input type = 'text' name = 'couchtime' value = \'$LEG_CouchTime{$egdGrpId}\'></td></tr>
         <tr $yelclr><td>Дата Пробного Занятия: </td><td><input type = 'text' name = 'testdate' value = \'$LEG_TestDay{$egdGrpId}\'></td>
         <td>Время Пробного Занятия: </td><td><input type = 'text' name = 'testtime' value = \'$LEG_TestTime{$egdGrpId}\'></td></tr>\n";
      }
   }
   if ( $egdGrpFound == 1 ) {
      print "<tr $yelclr><td $ac><input type='reset' value = 'ОТМЕНИТЬ' $egdStyle></td><td></td>
   <td $ac><input type = 'submit' value = 'ЗАПИСАТЬ' $egdStyle></td><td></td></tr></table></form>\n";
   }
   else { print "</table></form><h3>Нет группы для редактирования.</h3>\n"; }
   print "<p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";
}

#####################################################################################
############################ MAKE NEW GROUP SUB #####################################
#####################################################################################
sub makeNewGroupSub { $mngStyle = "style='height:50px; width:150px'"; &printjavascript();
   #1<tab>GRP1001<tab>Описание группы<tab>Active<tab>Sun Jul 28 20:15:48 2019<tab>reserve
   foreach $mngLine (@legiongroupslist) { $mngChompLine = $mngLine; chomp($mngChompLine); 
      ($tgrpnm, $tgrpid, $tlgrpdscrp, $tlgrpstat, @other) = split (/<tab>/, $mngChompLine);
      if ( $tgrpid =~ /GRP/ ) { $mngGrpNm = $tgrpnm; $mngGrpIndx = $tgrpid; }  }
   if ( $mngGrpIndx =~ /GRP/ ) { $mngGrpNm++;
      ( $other, $mngGrpId ) = split ( /GRP/, $mngGrpIndx ); $mngGrpId++; $mngGrpIndx = 'GRP' . $mngGrpId; }
   print "<h2>Создание новой группы обучения волонтеров OpenEnglish</h2> <p> </p>
   <form method='post' action=\'$httpindexcgi\' onsubmit='return checkNewGrpFunction();'>
   <input type = 'hidden' name = 'groupid' value = \'$mngGrpIndx\'><input type = 'hidden' name = 'grouptype' value = 'new'>
   <input type = 'hidden' name = 'action' value = 'creategroup'><table>
   <tr $yelclr><td>Уникальное описание группы: </td><td><input type = 'text' name = 'descript' value = ''></td>
   <td>Выберите статус группы: </td><td><select name = 'status'>
   <option value = 'Active'>Active</option><option value = 'Frozen'>Frozen</option>
   <option value = 'Finished'>Finished</option><option value = 'Cancelled'>Cancelled</option></select></td></tr>
   <tr $yelclr1><td>Название Тренинга: </td><td><input type = 'text' name = 'course' value = ''></td>
   <td>Кто Ведет Тренинг: </td><td><input type = 'text' name = 'trainer' value = ''></td></tr>
   <tr $yelclr><td>Дата начала обучения: </td><td><input type = 'text' name = 'startdate' value = ''></td><td></td><td></td></tr>
   <tr $yelclr1><td>Дата 1-го Занятия: </td><td><input type = 'text' name = 'firstdate' value = ''></td>
   <td>Время 1-го Занятия: </td><td><input type = 'text' name = 'firsttime' value = ''></td></tr>
   <tr $yelclr><td>Дата 2-го Занятия: </td><td><input type = 'text' name = 'seconddate' value = ''></td>
   <td>Время 2-го Занятия: </td><td><input type = 'text' name = 'secondtime' value = ''></td></tr>
   <tr $yelclr1><td>Дата 3-го Занятия: </td><td><input type = 'text' name = 'thirddate' value = ''></td>
   <td>Время 3-го Занятия: </td><td><input type = 'text' name = 'thirdtime' value = ''></td></tr>
   <tr $yelclr><td>Дата 4-го Занятия: </td><td><input type = 'text' name = 'forthdate' value = ''></td>
   <td>Время 4-го Занятия: </td><td><input type = 'text' name = 'forthtime' value = ''></td></tr>
   <tr $yelclr1><td>Дата 5-го Занятия: </td><td><input type = 'text' name = 'fifthdate' value = ''></td>
   <td>Время 5-го Занятия: </td><td><input type = 'text' name = 'fifthtime' value = ''></td></tr>
   <tr $yelclr><td>Дата 6-го Занятия: </td><td><input type = 'text' name = 'sixthdate' value = ''></td>
   <td>Время 6-го Занятия: </td><td><input type = 'text' name = 'sixthtime' value = ''></td></tr>
   <tr $yelclr1><td>Дата Коучинг Занятия: </td><td><input type = 'text' name = 'couchdate' value = ''></td>
   <td>Время Коучинг Занятия: </td><td><input type = 'text' name = 'couchtime' value = ''></td></tr>
   <tr $yelclr><td>Дата Пробного Занятия: </td><td><input type = 'text' name = 'testdate' value = ''></td>
   <td>Время Пробного Занятия: </td><td><input type = 'text' name = 'testtime' value = ''></td></tr>
   <tr $yelclr><td $ac><input type='reset' value = 'ОТМЕНИТЬ' $mngStyle></td><td></td>
   <td $ac><input type = 'submit' value = 'ЗАПИСАТЬ' $mngStyle></td><td></td></tr></table></form>   
   <p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";
}

#####################################################################################
########################### SHOW GROUP LIST SUB #####################################
#####################################################################################
sub showGroupListSub { $sglStyle = "style='height:50px; width:150px'"; $myclr = $yelclr; 
   #1<tab>GRP1001<tab>Описание группы<tab>Active<tab>Sun Jul 28 20:15:48 2019<tab>reserve
   print "<h2>Список групп обучения волонтеров OpenEnglish</h2> <p> </p><table>
   <tr $myclr><td>No</td><td>Состав</td><td>Описание</td><td>Статус</td><td>Редактировать</td></tr>\n"; 
   foreach $sglLine (@legiongroupslist) { $sglChompLine = $sglLine; chomp($sglChompLine); 
      ($tgrpnm, $tgrpid, $tgrpinfo, $tlgrpstat, @other) = split (/<tab>/, $sglChompLine);
      $sglGrpNum{$tgrpid} = $tgrpnm; $sglGrpInfo{$tgrpid} = $tgrpinfo; $sglGrpStat{$tgrpid} = $tlgrpstat;
      if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; }
      print "<tr $myclr><td $ac>$tgrpnm</td><td>
      <button onclick=\"window.location.href = \'$httpindexcgi\?action=listgroup\&groupid\=$tgrpid'\;\">
      Открыть</button></td><td>$tgrpinfo</td><td>$tlgrpstat</td><td>
      <button onclick=\"window.location.href = \'$httpindexcgi\?action=editgroup\&groupid\=$tgrpid'\;\">
      Редактировать</button></td></tr>\n"; $sglGrpNm = $tgrpnm + 1;
   }
   $myclr = $yelclr; $cnt = 0; $sglGrpId = $whatis{'groupid'};
   if ( $whatis{'action'} eq 'listgroup' && $whatis{'groupid'} ne '' ) { &getGroupSub();
      print "</table><p> </p><table><caption><h3>Номер группы [$sglGrpId]</h3></caption>
         <tr $yelclr><td>Кто создал группу: </td><td $ac>$username{$LEG_Creator{$sglGrpId}}</td>
         <td>Когда создали группу: </td><td $ac>$LEG_Created{$sglGrpId}</td></tr>
         <tr $yelclr1><td>Кто редактировал<br>данные группы последним: </td><td $ac>$username{$LEG_Editor{$sglGrpId}}</td>
         <td>Когда последний раз<br>редактировали данные группы: </td><td $ac>$LEG_LastEdited{$sglGrpId}</td></tr>
         <tr $yelclr><td>Уникальное описание группы: </td><td $ac>$sglGrpInfo{$sglGrpId}</td>
         <td>Статус группы: </td><td $ac>$sglGrpStat{$sglGrpId}</td></tr>
         <tr $yelclr1><td>Название Тренинга: </td><td $ac>$LEG_Course{$sglGrpId}</td>
         <td>Кто Ведет Тренинг: </td><td $ac>$LEG_Traineer{$sglGrpId}</td></tr>
         <tr $yelclr><td>Дата начала обучения: </td><td $ac>$LEG_StartDate{$sglGrpId}</td>
         <td>Кто и когда создал группу: </td><td $ac>$LEG_Editor{$sglGrpId} $LEG_Created{$sglGrpId}</td></tr>
         <tr $yelclr1><td>Дата 1-го Занятия: </td><td $ac>$LEG_DayOne{$sglGrpId}</td>
         <td>Время 1-го Занятия: </td><td $ac>$LEG_TimeOne{$sglGrpId}</td></tr>
         <tr $yelclr><td>Дата 2-го Занятия: </td><td $ac>$LEG_DayTwo{$sglGrpId}</td>
         <td>Время 2-го Занятия: </td><td $ac>$LEG_TimeTwo{$sglGrpId}</td></tr>
         <tr $yelclr1><td>Дата 3-го Занятия: </td><td $ac>$LEG_DayThree{$sglGrpId}</td>
         <td>Время 3-го Занятия: </td><td $ac>$LEG_TimeThree{$sglGrpId}</td></tr>
         <tr $yelclr><td>Дата 4-го Занятия: </td><td $ac>$LEG_DayFour{$sglGrpId}</td>
         <td>Время 4-го Занятия: </td><td $ac>$LEG_TimeFour{$sglGrpId}</td></tr>
         <tr $yelclr1><td>Дата 5-го Занятия: </td><td $ac>$LEG_DayFive{$sglGrpId}</td>
         <td>Время 5-го Занятия: </td><td $ac>$LEG_TimeFive{$sglGrpId}</td></tr>
         <tr $yelclr><td>Дата 6-го Занятия: </td><td $ac>$LEG_DaySix{$sglGrpId}</td>
         <td>Время 6-го Занятия: </td><td $ac>$LEG_TimeSix{$sglGrpId}</td></tr>
         <tr $yelclr1><td>Дата Коучинг Занятия: </td><td $ac>$LEG_CouchDay{$sglGrpId}</td>
         <td>Время Коучинг Занятия: </td><td $ac>$LEG_CouchTime{$sglGrpId}</td></tr>
         <tr $yelclr><td>Дата Пробного Занятия: </td><td $ac>$LEG_TestDay{$sglGrpId}</td>
         <td>Время Пробного Занятия: </td><td $ac>$LEG_TestTime{$sglGrpId}</td></tr>
         </table><p> </p><table><caption><h3>Список участников группы</h3></caption>
         <tr $myclr><td>No</td><td>ФИО волонтера</td><td>Номер группы</td></tr>\n";
      foreach $sgdLine (@legionlist) { $sgdChompLine = $sgdLine; chomp($sgdChompLine);
         ($tlgnrnm, $tlgnrid, $tlgnrgrpid, $tlgndrusrid, $tlgnrctgr, $tlgnrfrstnam, $tlgnrscndnam, $tlgnrthrdnam, 
         $tlgnrpwd, $tlgnrphnnum, $tlgnrtype, $tlgnreml, $tlgnrcreated, $tlgnrbrthday, $tlgnrgndr, $tlgnrwrkplc, 
         $tlgnrprsnid, $tlgnrindvdid, $tlgnrstats, $tlgnrschlid, @other) = split (/<tab>/, $sgdChompLine);
         if ( $whatis{'groupid'} eq $tlgnrgrpid ) { $tlgnreml = lc $tlgnreml; $tlgnreml =~s/ //g;
            if ( $myclr eq $yelclr ) { $myclr = $yelclr1; }  else { $myclr = $yelclr; } $cnt++;
            print "<tr $myclr><td>$cnt</td><td>$tlgnrfrstnam $tlgnrthrdnam $tlgnrscndnam</td>
            <td>$sglGrpNum{$tlgnrgrpid} - $sglGrpInfo{$tlgnrgrpid}</td></tr>\n"; 
         }
      }
   }
   print "</table><p> </p> <button onclick=\"window.location.href = \'$httpindexcgi\?action=newgroup\'\;\" 
   $sglStyle>Создать новую группу</button> <p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";
}

#####################################################################################
########################### SAVE GROUP DATA SUB #####################################
#####################################################################################
sub saveGroupDataSub { $sgdLgnrId =  $whatis{'legionerid'}; $sgdStyle = "style='height:50px; width:150px'"; 
   $sgdGenderRuName{'Male'} = 'Мужской';    $sgdGenderRuName{'Female'} = 'Женский';  $sgdLgnrFound = 0;
   $sgdGenderRuName{'Мужской'} = 'Мужской'; $sgdGenderRuName{'Женский'} = 'Женский'; 
   $sgdGenderEnName{'Male'} = 'Male';       $sgdGenderEnName{'Female'} = 'Female'; 
   $sgdGenderEnName{'Мужской'} = 'Male';    $sgdGenderEnName{'Женский'} = 'Female';
   print "<h2>Сохранить номер группы обучения волонтера OpenEnglish</h2> <p> </p>\n";
   foreach $sgdLine (@legionlist) { $sgdChompLine = $sgdLine; chomp($sgdChompLine);
      ($tlgnrnm, $tlgnrid, $tlgnrgrpid, $tlgndrusrid, $tlgnrctgr, $tlgnrfrstnam, $tlgnrscndnam, $tlgnrthrdnam, 
      $tlgnrpwd, $tlgnrphnnum, $tlgnrtype, $tlgnreml, $tlgnrcreated, $tlgnrbrthday, $tlgnrgndr, $tlgnrwrkplc, 
      $tlgnrprsnid, $tlgnrindvdid, $tlgnrstats, $tlgnrschlid, @other) = split (/<tab>/, $sgdChompLine);
      $tlgnreml = lc $tlgnreml; $tlgnreml =~s/ //g;
      if ( $sgdLgnrId eq $tlgnrid && $tlgnrid ne '' && $whatis{'email'} eq $tlgnreml ) { $sgdLgnrFound = 1;
         $sgdLgnrEmail = $tlgnreml; $sgdLgnrCreated = $tlgnrcreated; $sgdLgnrFullName = "$tlgnrfrstnam $tlgnrthrdnam $tlgnrscndnam";
         $sgdLgnrLine = "$tlgnrnm<tab>$sgdLgnrId<tab>$whatis{'groupid'}<tab>$tlgndrusrid<tab>$tlgnrctgr<tab>";
         $sgdLgnrLine = $sgdLgnrLine . "$tlgnrfrstnam<tab>$tlgnrscndnam<tab>$tlgnrthrdnam<tab>$tlgnrpwd<tab>";
         $sgdLgnrLine = $sgdLgnrLine . "$tlgnrphnnum<tab>$tlgnrtype<tab>$tlgnreml<tab>$tlgnrcreated<tab>";
         $sgdLgnrLine = $sgdLgnrLine . "$tlgnrbrthday<tab>$sgdGenderEnName{$tlgnrgndr}<tab>$tlgnrwrkplc<tab>";
         $sgdLgnrLine = $sgdLgnrLine . "$tlgnrprsnid<tab>$tlgnrindvdid<tab>$tlgnrstats<tab>$tlgnrschlid<tab>reserve\n";
         push(@sgdNewLegionList, $sgdLgnrLine);
      }
      else { push(@sgdNewLegionList, $sgdLine); }
   }
   if ( $sgdLgnrFound == 1 ) { 
      foreach $sgdGrpLine (@legiongroupslist) { $sgdGrpChompLine = $sgdGrpLine; chomp($sgdGrpChompLine); 
         ($tgrpnm, $tgrpid, $tgrpinfo, $tgrpstat, $tgrpdate, @other) = split (/<tab>/, $sgdGrpChompLine);
         $sgdGrpNum{$tgrpid} = $tgrpnm; $sgdGrpInfo{$tgrpid} = $tgrpinfo; }
      open(SLDATA,">$legion_file");    print SLDATA @sgdNewLegionList;    close(SLDATA);
      print "<table $grnclr><tr><td><h2>Следующие данные сохранены!</h2></td></tr></table>\n<p> </p><table>
      <tr $yelclr><td>Дата регистрации: </td><td>$b1 $sgdLgnrCreated $b2</td></tr>
      <tr $yelclr1><td>ФИО волонтера: </td><td>$sgdLgnrFullName</td></tr>
      <tr $yelclr><td>Группа обучения: </td><td>$b1 $sgdGrpNum{$whatis{'groupid'}} - $sgdGrpInfo{$whatis{'groupid'}} $b2</td></tr>
      <tr $yelclr1><td>EMAIL: </td><td>$b1 $sgdLgnrEmail $b2</td></tr></table>\n"; 
   }
   else { print "<h2>$rf Неверные данные! проверьте еще раз.. $f2</h2>\n"; }
   print "<p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";
}

#####################################################################################
######################## ASSIGN GROUP LEGION SUB ####################################
#####################################################################################
sub assignGroupLegionSub {  $cnt = 1; $myclr = $yelclr; &printjavascript(); 
  $agsStyle = "style='height:50px; width:150px'"; $agsLgnrId =  $whatis{'legionerid'};
  print "<h2>Указать номер группы обучения волонтера OpenEnglish</h2>\n 
  <form method='post' action=\'$httpindexcgi\' name = 'updatedata' onsubmit='return checkGrpFunction();'><table>\n";
  foreach $agsLine (@legionlist) { $agsChompLine = $agsLine; chomp($agsChompLine);
     ($tlgnrnm, $tlgnrid, $tlgnrgrpid, $tlgndrusrid, $tlgnrctgr, $tlgnrfrstnam, $tlgnrscndnam, $tlgnrthrdnam, 
     $tlgnrpwd, $tlgnrphnnum, $tlgnrtype, $tlgnreml, $tlgnrcreated, $tlgnrbrthday, $tlgnrgndr, $tlgnrwrkplc, 
     $tlgnrprsnid, $tlgnrindvdid, $tlgnrstats, $tlgnrschlid, @other) = split (/<tab>/, $agsChompLine);
     $tlgnreml = lc $tlgnreml; $tlgnreml =~s/ //g;
     if ($agsLgnrId eq $tlgnrid && $tlgnrid ne '' && $tlgnrtype eq 'confirmed' && $tlgnrctgr eq 'Volonteer' ) { 
         if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
         print "<tr $yelclr><td>Дата регистрации: </td><td>$b1 $tlgnrcreated $b2 
         <input type = 'hidden' name = 'action' value = 'savegroup'><input type = 'hidden' name = 'email' value = \'$tlgnreml\'>
         <input type = 'hidden' name = 'legionerid' value = \'$agsLgnrId\'></td></tr>
         <tr $yelclr1><td>ФИО волонтера: </td><td>$tlgnrfrstnam $tlgnrthrdnam $tlgnrscndnam</td></tr>
         <tr $yelclr><td>EMAIL: </td><td>$b1 $tlgnreml $b2</td></tr>
         <tr $yelclr1><td>Номер группы: </td><td><select name = 'groupid'>
         <option value = ''>Выберите группу обучения</option>\n";
         foreach $agsLine (@legiongroupslist) { $agsChompLine = $agsLine; chomp($agsChompLine); 
            ($tgrpnm, $tgrpid, $tgrpinfo, $tgrpstat, $tgrpdate, @other) = split (/<tab>/, $agsChompLine);
            $agsGrpNum{$tgrpid} = $tgrpnm; $agsGrpInfo{$tgrpid} = $tgrpinfo; 
            print "<option value = \'$tgrpid\'>$tgrpnm - $tgrpinfo</option>\n";
         }
         if ( $agsGrpInfo{$tlgnrgrpid} ne '' ) { 
            print "<option value = \'$tlgnrgrpid\' selected>$agsGrpNum{$tlgnrgrpid} - $agsGrpInfo{$tlgnrgrpid}</option>\n"; }
         print "</select></td></tr>
         <tr $yelclr><td $ac><input type='reset' value = 'ОТМЕНИТЬ' $agsStyle></td>
         <td $ac><input type = 'submit' value = 'ЗАПИСАТЬ' $agsStyle></td></tr>\n";
     }
  }
  print "</table></form> <p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";
}

#####################################################################################
######################### EDIT LEGIONER DATA SUB ####################################
#####################################################################################
sub editLegionerDataSub {  $cnt = 1; $myclr = $yelclr; &printjavascript(); $eldLgnrId =  $whatis{'legionerid'};
  $eldGenderRuName{'Male'} = 'Мужской';  $eldGenderRuName{'Female'} = 'Женский'; $eldStyle = "style='height:50px; width:150px'";
  $eldGenderRuName{'Мужской'} = 'Мужской';  $eldGenderRuName{'Женский'} = 'Женский';
  $eldGenderEnName{'Male'} = 'Male';  $eldGenderEnName{'Female'} = 'Female'; 
  $eldGenderEnName{'Мужской'} = 'Male';  $eldGenderEnName{'Женский'} = 'Female';
  print "<h2>Редактировать данные волонтера OpenEnglish</h2>\n 
  <form method='post' action=\'$httpindexcgi\' name = 'updatedata' onsubmit='return checkAllFunction();'><table>\n";
  foreach $eldLine (@legionlist) { $eldChompLine = $eldLine; chomp($eldChompLine);
     ($tlgnrnm, $tlgnrid, $tlgnrgrpid, $tlgndrusrid, $tlgnrctgr, $tlgnrfrstnam, $tlgnrscndnam, $tlgnrthrdnam, 
     $tlgnrpwd, $tlgnrphnnum, $tlgnrtype, $tlgnreml, $tlgnrcreated, $tlgnrbrthday, $tlgnrgndr, $tlgnrwrkplc, 
     $tlgnrprsnid, $tlgnrindvdid, $tlgnrstats, $tlgnrschlid, @other) = split (/<tab>/, $eldChompLine);
     $tlgnreml = lc $tlgnreml; $tlgnreml =~s/ //g;
     if ($eldLgnrId eq $tlgnrid && $tlgnrid ne '' && $tlgnrtype eq 'confirmed' && $tlgnrctgr eq 'Volonteer' ) { 
         if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
         print "<tr $yelclr><td>Дата регистрации: </td><td>$b1 $tlgnrcreated $b2 <input type = 'hidden' name = 'groupid' value = \'$tlgnrgrpid\'>
         <input type = 'hidden' name = 'action' value = 'save'> <input type = 'hidden' name = 'legionernum' value = \'$tlgnrnm\'>
         <input type = 'hidden' name = 'legionerid' value = \'$eldLgnrId\'><input type = 'hidden' name = 'legioneruserid' value = \'$tlgndrusrid\'>
         <input type = 'hidden' name = 'category' value = \'$tlgnrctgr\'><input type = 'hidden' name = 'type' value = \'$tlgnrtype\'>
         <input type = 'hidden' name = 'email' value = \'$tlgnreml\'><input type = 'hidden' name = 'created' value = \'$tlgnrcreated\'></td></tr>
         <tr $yelclr1><td>Имя волонтера: </td><td><input type = 'text' name = 'firstname' value = \'$tlgnrfrstnam\'></td></tr>
         <tr $yelclr><td>Фамилия: </td><td><input type = 'text' name = 'secondname' value = \'$tlgnrscndnam\'></td></tr>
         <tr $yelclr1><td>Отчество: </td><td><input type = 'text' name = 'thirdname' value = \'$tlgnrthrdnam\'></td></tr>
         <tr $yelclr><td>Телефон: </td><td><input type = 'text' name = 'phone' value = \'$tlgnrphnnum\'></td></tr>
         <tr $yelclr1><td>EMAIL: </td><td>$b1 $tlgnreml $rf Не меняется! $f2 $b2</td></tr>
         <tr $yelclr><td>День рождения: </td><td><input type = 'text' name = 'birthday' value = \'$tlgnrbrthday\'></td></tr>
         <tr $yelclr1><td>Пол волонтера: </td><td><select name = 'gender'><option value = ''>Выберите пол</option>\n";
         if ( $tlgnrgndr ne '' ) { print "<option value = \'$eldGenderEnName{$tlgnrgndr}\' selected>$eldGenderRuName{$tlgnrgndr}</option>\n"; }
         print "<option value = 'Male'>Мужской</option>\n<option value = 'Female'>Женский</option>\n</select></td></tr>
         <tr $yelclr><td>Род деятельности: </td><td><select name = 'status'><option value = ''>Выберите род деятельности</option>\n";
         if ( $tlgnrstats ne '' ) { print "<option value = \'$tlgnrstats\' selected>$tlgnrstats</option>\n"; }
         print "<option value = 'Школьник'>Школьник</option>\n<option value = 'Студент'>Студент</option>
         <option value = 'Работаю'>Работаю</option>\n</select></td></tr>
         <tr $yelclr1><td>Место работы / учебы: </td><td><input type = 'text' name = 'workplace' value = \'$tlgnrwrkplc\'></td></tr>
         <tr $yelclr><td>Удостоверение: </td><td><input type = 'text' name = 'personid' value = \'$tlgnrprsnid\'></td></tr>
         <tr $yelclr1><td>ИИН: </td><td><input type = 'text' name = 'individid' value = \'$tlgnrindvdid\'></td></tr>
         <tr $yelclr><td $ac><input type='reset' value = 'ОТМЕНИТЬ' $eldStyle></td>
         <td $ac><input type = 'submit' value = 'ЗАПИСАТЬ' $eldStyle></td></tr>\n";
     }
  }
  print "</form></table> <p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";
}

#####################################################################################
######################## SAVE LEGIONER DATA SUB #####################################
#####################################################################################
sub saveLegionerDataSub { $sldLgnrId =  $whatis{'legionerid'}; $sldStyle = "style='height:50px; width:150px'"; 
   $sldGenderRuName{'Male'} = 'Мужской';    $sldGenderRuName{'Female'} = 'Женский';  $sldLgnrFound = 0;
   $sldGenderRuName{'Мужской'} = 'Мужской'; $sldGenderRuName{'Женский'} = 'Женский'; 
   $sldGenderEnName{'Male'} = 'Male';       $sldGenderEnName{'Female'} = 'Female'; 
   $sldGenderEnName{'Мужской'} = 'Male';    $sldGenderEnName{'Женский'} = 'Female';
   print "<h2>Сохранить данные волонтера OpenEnglish</h2> <p> </p>\n";
   foreach $sldLine (@legionlist) { $sldChompLine = $sldLine; chomp($sldChompLine);
      ($tlgnrnm, $tlgnrid, $tlgnrgrpid, $tlgndrusrid, $tlgnrctgr, $tlgnrfrstnam, $tlgnrscndnam, $tlgnrthrdnam, 
      $tlgnrpwd, $tlgnrphnnum, $tlgnrtype, $tlgnreml, $tlgnrcreated, $tlgnrbrthday, $tlgnrgndr, $tlgnrwrkplc, 
      $tlgnrprsnid, $tlgnrindvdid, $tlgnrstats, $tlgnrschlid, @other) = split (/<tab>/, $sldChompLine);
      $tlgnreml = lc $tlgnreml; $tlgnreml =~s/ //g;
      if ( $sldLgnrId eq $tlgnrid && $tlgnrid ne '' && $whatis{'email'} eq $tlgnreml ) { $sldLgnrFound = 1;
         $sldLgnrEmail = $tlgnreml; $sldLgnrCreated = $tlgnrcreated;
         $sldLgnrLine = "$tlgnrnm<tab>$sldLgnrId<tab>$tlgnrgrpid<tab>$tlgndrusrid<tab>$tlgnrctgr<tab>";
         $sldLgnrLine = $sldLgnrLine . "$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}";
         $sldLgnrLine = $sldLgnrLine . "<tab>$tlgnrpwd<tab>$whatis{'phone'}<tab>$tlgnrtype<tab>$tlgnreml<tab>$tlgnrcreated<tab>";
         $sldLgnrLine = $sldLgnrLine . "$whatis{'birthday'}<tab>$sldGenderEnName{$whatis{'gender'}}<tab>$whatis{'workplace'}<tab>";
         $sldLgnrLine = $sldLgnrLine . "$whatis{'personid'}<tab>$whatis{'individid'}<tab>$whatis{'status'}<tab>$tlgnrschlid<tab>reserve\n";
         push(@newLegionList, $sldLgnrLine);
      }
      else { push(@newLegionList, $sldLine); }
   }
   if ( $sldLgnrFound == 1 ) { 
      open(SLDATA,">$legion_file");    print SLDATA @newLegionList;    close(SLDATA);
      print "<table $grnclr><tr><td><h2>Следующие данные сохранены!</h2></td></tr></table>\n<p> </p><table>
      <tr $yelclr><td>Дата регистрации: </td><td>$b1 $sldLgnrCreated $b2</td></tr>
      <tr $yelclr1><td>Имя волонтера: </td><td>$whatis{'firstname'}</td></tr>
      <tr $yelclr><td>Фамилия: </td><td>$whatis{'secondname'}</td></tr>
      <tr $yelclr1><td>Отчество: </td><td>$whatis{'thirdname'}</td></tr>
      <tr $yelclr><td>Телефон: </td><td>$whatis{'phone'}</td></tr>
      <tr $yelclr1><td>EMAIL: </td><td>$b1 $sldLgnrEmail $b2</td></tr>
      <tr $yelclr><td>День рождения: </td><td>$whatis{'birthday'}</td></tr>
      <tr $yelclr1><td>Пол волонтера: </td><td>$sldGenderEnName{$whatis{'gender'}}</td></tr>
      <tr $yelclr><td>Род деятельности: </td><td>$whatis{'status'}</td></tr>
      <tr $yelclr1><td>Место работы / учебы: </td><td>$whatis{'workplace'}</td></tr>
      <tr $yelclr><td>Удостоверение: </td><td>$whatis{'personid'}</td></tr>
      <tr $yelclr1><td>ИИН: </td><td>$whatis{'individid'}</td></tr></table>\n"; 
   }
   else { print "<h2>$rf Неверные данные! проверьте еще раз.. $f2</h2>\n"; }
   print "<p> </p> <p><a href=\'$httpindexcgi\'>Вернуться НАЗАД</a></p>\n";
}

#####################################################################################
########################### SHOW BLANK PAGE SUB #####################################
#####################################################################################
sub blankPageSub {  $cnt = 1; $myclr = $yelclr; &printjavascript(); $bpsStyle = "style='height:50px; width:150px'"; 
  print "<h2>утвержденные списки кандидатов в волонтеры OpenEnglish</h2>\n 
  <table><tr $myclr><td>No</td><td>ФИО кандидата</td><td>Состоит в группе</td><td>Включить в группу</td><td>Телефон</td>
  <td>Редактировать</td><td>Емэйл</td><td>Дата<br> регистрации</td><td>Дата<br>рождения</td><td>Пол</td>
  <td>Место работы<br>/ учебы</td><td>Номер<br>удостоверения</td><td>ИИН</td></tr>\n";
  foreach $bpsGrpLine (@legiongroupslist) { $bpsGrpChompLine = $bpsGrpLine; chomp($bpsGrpChompLine); 
     ($tgrpnm, $tgrpid, $tgrpinfo, $tgrpstat, $tgrpdate, @other) = split (/<tab>/, $bpsGrpChompLine);
     $bpsGrpNum{$tgrpid} = $tgrpnm; $bpsGrpInfo{$tgrpid} = $tgrpinfo; }
  
  foreach $bpsLine (@legionlist) { $bpsChompLine = $bpsLine; chomp($bpsChompLine);
     ($tlgnrnm, $tlgnrid, $tlgnrgrpid, $tlgndrusrid, $tlgnrctgr, $tlgnrfrstnam, $tlgnrscndnam, $tlgnrthrdnam, 
     $tlgnrpwd, $tlgnrphnnum, $tlgnrtype, $tlgnreml, $tlgnrcreated, $tlgnrbrthday, $tlgnrgndr, $tlgnrwrkplc, 
     $tlgnrprsnid, $tlgnrindvdid, $tlgnrstats, $tlgnrschlid, @other) = split (/<tab>/, $bpsChompLine);
     $tlgnreml = lc $tlgnreml; $tlgnreml =~s/ //g;
     if ($tlgnrfrstnam ne '' && $tlgnrscndnam ne '' && $tlgnrtype eq 'confirmed' ) { 
         if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
         if ( $tlgnrctgr eq 'Volonteer' ) {
            $bpsButtonTxt = "<button onclick=\"return checkAssignFunction\($cnt\)\;\">Назначить Группу</button>"; }
         else { $bpsButtonTxt = ''; }
         $bpsEditButtonTxt = "<button onclick=\"return checkEditFunction\($cnt\)\;\">Редактировать данные</button>";
         print "<tr $myclr><td>$cnt <input type='hidden' id = \'$cnt\' value = \'$tlgnrid\'></td><td>$tlgnrfrstnam $tlgnrthrdnam $tlgnrscndnam</td>
         <td>$bpsGrpNum{$tlgnrgrpid} - $bpsGrpInfo{$tlgnrgrpid}</td><td>$bpsButtonTxt</td><td>$tlgnrphnnum</td><td>$bpsEditButtonTxt</td><td>$tlgnreml</td>
         <td>$tlgnrcreated</td><td>$tlgnrbrthday</td><td>$tlgnrgndr</td><td>$tlgnrwrkplc</td><td>$tlgnrprsnid</td><td>$tlgnrindvdid</td></tr>\n";
         $cnt++; }
  } 
  print "</table><p> </p><button onclick=\"window.location.href = \'$httpindexcgi\?action=showgroups\'\;\" 
  $bpsStyle>Открыть Список Групп Обучения</button>  <p> </p> <p><a href=\'$httphomecgi\'>Вернуться НАЗАД</a></p>\n";
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
     var userlink = \'$httpindexcgi\?action=edit\&legionerid=' + document.getElementById(cnt).value;
     var usr = confirm('Редактировать?');
     if(usr){window.location.href = userlink;}     else{return false;}
 }
 function checkAssignFunction (cnt) {
     var userlink = \'$httpindexcgi\?action=assign\&legionerid=' + document.getElementById(cnt).value;
     var usr = confirm('Включить в группу обучения?');
     if(usr){window.location.href = userlink;}     else{return false;}
 }
 function checkNewGrpFunction() {
   if(document.getElementsByName('descript')[0].value == ''){alert('Описание группы?'); return false;}
   if(document.getElementsByName('course')[0].value == ''){alert('Название Тренинга?'); return false;}
   if(document.getElementsByName('trainer')[0].value == ''){alert('Кто Ведет Тренинг?'); return false;}
   var usr = document.getElementsByName('startdate')[0].value;
   if(document.getElementsByName('startdate')[0].value == ''){alert('Дата начала обучения?'); return false;}
   else { if (isValidDate(usr)) { document.getElementsByName('startdate')[0].value = usr; }
   else {alert('Неправильная дата начала обучения: [' + usr + ']!'); return false;}   }
   usr = document.getElementsByName('firstdate')[0].value;
   if (usr != '' ) {if (isValidDate(usr)) { document.getElementsByName('firstdate')[0].value = usr; }
                    else {alert('Неправильная дата 1-го Занятия: [' + usr + ']!'); return false;}   }
   usr = document.getElementsByName('seconddate')[0].value;
   if (usr != '' ) {if (isValidDate(usr)) { document.getElementsByName('seconddate')[0].value = usr; }
                    else {alert('Неправильная дата 2-го Занятия: [' + usr + ']!'); return false;}   }
   usr = document.getElementsByName('thirddate')[0].value;
   if (usr != '' ) {if (isValidDate(usr)) { document.getElementsByName('thirddate')[0].value = usr; }
                    else {alert('Неправильная дата 3-го Занятия: [' + usr + ']!'); return false;}   }
   usr = document.getElementsByName('forthdate')[0].value;
   if (usr != '' ) {if (isValidDate(usr)) { document.getElementsByName('forthdate')[0].value = usr; }
                    else {alert('Неправильная дата 4-го Занятия: [' + usr + ']!'); return false;}   }
   usr = document.getElementsByName('fifthdate')[0].value;
   if (usr != '' ) {if (isValidDate(usr)) { document.getElementsByName('fifthdate')[0].value = usr; }
                    else {alert('Неправильная дата 5-го Занятия: [' + usr + ']!'); return false;}   }
   usr = document.getElementsByName('sixthdate')[0].value;
   if (usr != '' ) {if (isValidDate(usr)) { document.getElementsByName('sixthdate')[0].value = usr; }
                    else {alert('Неправильная дата 6-го Занятия: [' + usr + ']!'); return false;}   }
   usr = document.getElementsByName('couchdate')[0].value;
   if (usr != '' ) {if (isValidDate(usr)) { document.getElementsByName('couchdate')[0].value = usr; }
                    else {alert('Неправильная дата Коучинг Занятия: [' + usr + ']!'); return false;}   }
   usr = document.getElementsByName('testdate')[0].value;
   if (usr != '' ) {if (isValidDate(usr)) { document.getElementsByName('testdate')[0].value = usr; }
                    else {alert('Неправильная дата Пробного Занятия: [' + usr + ']!'); return false;}   }
 }
 function checkGrpFunction() {
   if(document.getElementsByName('groupid')[0].value == ''){alert('Номер группы?'); return false;}
 }
 function checkAllFunction () {
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