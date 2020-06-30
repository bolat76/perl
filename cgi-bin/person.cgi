#!/usr/bin/perl

print "Content-Type: text/html\n";
#######################################################################################
######### defining initial data
#######################################################################################
srand();

$b1 = '<b>'; $b2 = '</b>'; $u1 = '<u>'; $u2 = '<u2>';
$rf = '<font color = red>'; $f2 = '</font>'; $cnt = 0;
$ct1 = '</center>'; $ct2 = '</center>'; $hr = '<hr>'; $br = '<br>';
$yelclr = 'bgcolor = Khaki'; $yelclr1 = 'bgcolor = LemonChiffon';
$grnclr = 'bgcolor = GreenYellow';  $redclr = 'bgcolor = #8a8ac1;';
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
        if($cookiekey =~ /volonteersproject/){$gotcookie = $hotcookie; }
    }
#$gotcookie = $ENV{'HTTP_COOKIE'};
$cookie_file = '../oedata/vl_cookies.txt';
$users_file = '../oedata/leaders.txt';
###################### end of cookie part #########################
$oe_folder = '../oedata/';
$upload_folder = '../oedata/';
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$vlTempData_file = $oe_folder . 'vl_tempdata.txt';
$activeText_file = $oe_folder . 'activehtml.txt';
$bas = $oe_folder  . 'bas.txt';
$end = $oe_folder . 'end.txt';
$indexcgi = 'person.cgi';
$slmailphp = '../phpmail.php';
$httpEmailPhp = 'http://accelerator.kvadra.kz/phpmail.php';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httpactivecgi = 'http://accelerator.kvadra.kz/cgi-bin/active.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Personal Data';

open(INF, $cookie_file); 
@cookielist = <INF>;
close(INF);
foreach $i(@cookielist){
    chomp($i); #8<tab>8250732421875<tab>Tue Apr 23 14:16:01 2013<tab>172.28.113.66<tab>reserve
    #$ccUserNum<tab>$oeusercookiernd{$ccUserNum}<tab>$oeusercookiedate{$ccUserNum}<tab>$oeusercookieip{$ccUserNum}<tab>desktop
    ($clusrnum, $clusrrnd, $clusrdate, $clusrip, @other) = split (/<tab>/, $i);
    $oeusercookiernd{$clusrnum} = $clusrrnd;
    $oeusercookiedate{$clusrnum} = $clusrdate;
    $oeusercookieip{$clusrnum} = $clusrip;
}


open(INF, $users_file); 
@userlist = <INF>; 
close(INF); 
foreach $i(@userlist){ 
   #3<tab>54LD4705<tab>Болатхан<tab>Джайдаринов<tab><tab>1<tab>85<tab>85-1-M2<tab>8 777 277 0326<tab>b.jaidarinov@gmail.com<tab>25.07.2019<tab>reserve
   ($tusrnum, $tusrid, $tusrfrstnam, $tusrscndnam, $tusrthrdnam, $tusrpwd, $tusrsclid, $tusrgrpid, $tusrphnnum, 
   $tusremail, $tusrcreated, $tusrbrthday, $tusrgender, $tusrwrkplc, $tusrprsnid, $tusrindvdid, @other) = split (/<tab>/, $i);
   if ( $tusrid ne '' ) { $tusremail = lc $tusremail;
       $userFullName{$tusrid} = "$tusrfrstnam $tusrthrdnam $tusrscndnam"; push(@loginuserslist, $tusrid);
       $userNumber{$tusrid} = $tusrnum; $userCode{$tusrnum} = $tusrid; $userCode{$tusremail} = $tusrid;
       $userFirstName{$tusrid} = $tusrfrstnam; $userSecondName{$tusrid} = $tusrscndnam; $userThirdName{$tusrid} = $tusrthrdnam;
       $userpwd{$tusrid} = $tusrpwd; $userSchoolId{$tusrid} = $tusrsclid; $userGroupId{$tusrid} = $tusrgrpid;
       $userPhoneNumber{$tusrid} = $tusrphnnum; $userEmail{$tusrid} = $tusremail; $userCreated{$tusrid} = $tusrcreated;
       $userBirthDay{$tusrid} = $tusrbrthday; $userGender{$tusrid} = $tusrgender; 
       $userWorkPlace{$tusrid} = $tusrwrkplc; $userPersonId{$tusrid} = $tusrprsnid; $userIndivId{$tusrid} = $tusrindvdid; 
       if ( $tusremail ne '' ) { $userEmailExist{$tusremail} = 1; $userpwd{$tusremail} = $tusrpwd; }
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
################## check COOKIES and LOG actions ######################################
#######################################################################################
if ( $whatis{'email'} ne '' ) { $whatis{'email'} = lc $whatis{'email'}; $whatis{'email'} =~s/ //g; }
&checkcookies(); print "\n"; &printfile($bas, $title);

if ( $whatis{'action'} ne '' ) { open(GURD,">>$log_file");
print GURD "Time: [$timedatenow] User ID: [$gotusrid] IP address: [$userip] User action: [$whatis{'action'}] Script: [$indexcgi] \n";
close(GURD); }

#####################################################################################
############################# LOGIN CHECK PART ######################################
#####################################################################################
print "<p> </p>";

if ( $userlogged == 1 ) {
   print "Hello $b1 $userfirstname{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>\n";
   if ( $whatis{'action'} eq 'show' )   { &PersonalDataSub() ; }     # show the personal data 
   elsif ( $whatis{'action'} eq 'update' ) { &EditDataSub() ; }      # send email to user and open form for personal data to enter
   elsif ( $whatis{'action'} eq 'save' )   { &SaveDataSub() ; }      # update the personal data 
   print "<p> </p> <p><a href=\'$httpactivecgi\'>ДОМОЙ</a></p>\n";
}
else{
   if ( $whatis{'action'} eq 'reset' ) { &openResetFormSub() ; }       # open the form to enter email to send validation number for reset
   elsif ( $whatis{'action'} eq 'resetpwd' ) { &EditPasswordSub() ; }  # open the form to enter new password
   elsif ( $whatis{'action'} eq 'editpwd' ) { &SaveNewPwdSub() ; }     # save new password
   else {   
      if ( $whatis{'action'} eq 'login' && $userlogged != 1) { print "<p>$rf $errorlogin $f2</p>\n" ; }  
      print "<form method='post' action=\'$httpactivecgi\'><table><caption>Enter Login Data</caption><tr><td>Email: </td>
      <td><input type = 'text'  name = 'email'></td>  <td>Пароль: </td><td><input type = 'password'  name = 'userpwd'> </td>
      <td><input type = 'hidden' name = 'action' value = 'login'>  <input type = 'submit' value = 'Enter'></td></tr></table></form>\n";
      print "<p><a href=\'$indexcgi?action=reset\'>Изменить Пароль?</a></p>";
      &printfile($activeText_file, $title);
   }
}

#####################################################################################
########################### START MAIN BODY #########################################
#####################################################################################

print "</center></body></html>";

##################################################################################################################
##################################### Sub PersonalDataSub ########################################################
##################################################################################################################
sub PersonalDataSub {
   $pdsUsrId = $gotusrid;
   if ( $userFirstName{$pdsUsrId} eq '' ) { return; }
   print "<h3>Ваши персональные данные</h3><p> </p>\n<table>
   <tr $yelclr><td>Ваше Имя: </td><td>$userFirstName{$pdsUsrId}</td></tr>
   <tr $yelclr1><td>Фамилия: </td><td>$userSecondName{$pdsUsrId}</td></tr>
   <tr $yelclr><td>Отчество: </td><td>$userThirdName{$pdsUsrId}</td></tr>
   <tr $yelclr1><td>Телефон: </td><td>$userPhoneNumber{$pdsUsrId}</td></tr>
   <tr $yelclr><td>EMAIL: </td><td>$userEmail{$pdsUsrId}</td></tr>
   <tr $yelclr1><td>Номер школы: </td><td>$userSchoolId{$pdsUsrId}</td></tr>
   <tr $yelclr><td>Номер группы: </td><td>$userGroupId{$pdsUsrId}</td></tr>
   <tr $yelclr1><td>Дата рождения: </td><td>$userBirthDay{$pdsUsrId}</td></tr>
   <tr $yelclr><td>Пол: </td><td>$userGender{$pdsUsrId}</td></tr>
   <tr $yelclr1><td>Место учебы/ работы: </td><td>$userWorkPlace{$pdsUsrId}</td></tr>
   <tr $yelclr><td>Номер удостоверения: </td><td>$userPersonId{$pdsUsrId}</td></tr>
   <tr $yelclr1><td>ИИН: </td><td>$userIndivId{$pdsUsrId}</td></tr></table>
   <p></p><p><a href=\'$httpindexcgi?action=update\'>Изменить Персональные Данные</a> </p>\n";
}

##################################################################################################################
####################################### Sub SaveNewPwdSub ########################################################
##################################################################################################################
sub SaveNewPwdSub {
  ($snpCookieKey, $snpCookieParameters) = split(/=/, $gotcookie);  ($snpUsrNum, $snpCookieUsrRnd, $snpUsrBrowser) = split(/_/, $snpCookieParameters);
  open(INF, $vlTempData_file);       @vlTempData_list = <INF>;       close(INF); 
  foreach $i (@vlTempData_list) { chomp ( $i ); if ( $i =~ /$snpCookieUsrRnd/ ) 
  { ($snpEmail, $snpCookieRndNum, $snpRndNum, $snpUsrIp, @others) = split(/<tab>/, $i); } }
  if ( $snpCookieUsrRnd eq  $snpCookieRndNum &&  $snpRndNum eq $whatis{'validnum'} && $whatis{'userid'} =~ /54LD/ ) {
     if ( $userEmailExist{$snpEmail} == 1 && $snpUsrIp eq $userip ) {
        $whatis{'pwd'} =~s/ //g;  $whatis{'pwd'} =~s/ //g;  $snpUsrId = $whatis{'userid'};
       
       # $userNumber{$snpUsrId} = $tusrnum; $userCode{$tusrnum} = $snpUsrId; $userCode{$tusremail} = $snpUsrId;
       # $userFirstName{$snpUsrId} = $tusrfrstnam; $userSecondName{$snpUsrId} = $tusrscndnam; $userThirdName{$snpUsrId} = $tusrthrdnam;
       # $userpwd{$snpUsrId} = $tusrpwd; $userSchoolId{$snpUsrId} = $tusrsclid; $userGroupId{$snpUsrId} = $tusrgrpid;
       # $userPhoneNumber{$snpUsrId} = $tusrphnnum; $userEmail{$snpUsrId} = $tusremail; $userCreated{$snpUsrId} = $tusrcreated;
       # $userBirthDay{$snpUsrId} = $tusrbrthday; $userGender{$snpUsrId} = $tusrgender; 
       # $userWorkPlace{$snpUsrId} = $tusrwrkplc; $userPersonId{$snpUsrId} = $tusrprsnid; $userIndivId{$snpUsrId} = $tusrindvdid; 
       #($tusrnum, $tusrid, $tusrfrstnam, $tusrscndnam, $tusrthrdnam, $tusrpwd, $tusrsclid, $tusrgrpid, $tusrphnnum, 
       # $tusremail, $tusrcreated, $tusrbrthday, $tusrgender, $tusrwrkplc, $tusrprsnid, $tusrindvdid, @other) = split (/<tab>/, $i);
      
        foreach $i(@userlist){ 
           chomp($i);
           if($i =~ /$snpEmail/ && $i =~ /$snpUsrId/){
              ($snpUserNum, @others) = split(/<tab>/, $i);
              $snpDataLine = "$snpUserNum<tab>$snpUsrId<tab>$userFirstName{$snpUsrId}<tab>$userSecondName{$snpUsrId}<tab>";
              $snpDataLine = $snpDataLine . "$userThirdName{$snpUsrId}<tab>$whatis{'pwd'}<tab>$userSchoolId{$snpUsrId}<tab>";
              $snpDataLine = $snpDataLine . "$userGroupId{$snpUsrId}<tab>$userPhoneNumber{$snpUsrId}<tab>$snpEmail<tab>";
              $snpDataLine = $snpDataLine . "$userCreated{$snpUsrId}<tab>$userBirthDay{$snpUsrId}<tab>$userGender{$snpUsrId}<tab>";
              $snpDataLine = $snpDataLine . "$userWorkPlace{$snpUsrId}<tab>$userPersonId{$snpUsrId}<tab>$userIndivId{$snpUsrId}<tab>reserve";
              push(@sdsNewUserList, $snpDataLine);
           }
           else { push(@sdsNewUserList, $i); }
        }
        open(D,">$users_file"); foreach $i(@sdsNewUserList){ if ( $i ne '' ) { print D "$i\n"; } }  close(D); 
        #print "<!-- [@sdsNewUserList] -->";
        print "<table $grnclr><tr><td>Ваши данные сохранены!</td></tr></table><p> </p>
        <table><tr $yelclr><td>Ваше имя: </td> <td>$userFirstName{$snpUsrId}</td></tr>
        <tr $yelclr1><td>Фамилия: </td> <td>$userSecondName{$snpUsrId}</td> </tr>
        <tr $yelclr><td>Отчество: </td> <td>$userThirdName{$snpUsrId}</td> </tr>
        <tr $yelclr1><td>Школа: </td> <td>$userSchoolId{$snpUsrId}</td> </tr>
        <tr $yelclr><td>Группа: </td> <td>$userGroupId{$snpUsrId}</td> </tr>
        <tr $yelclr1><td>Телефон: </td> <td>$userPhoneNumber{$snpUsrId}</td> </tr>
        <tr $yelclr><td>Email: </td> <td>$snpEmail</td> </tr>
        <tr $yelclr1><td>Дата изменений: </td> <td>$userCreated{$snpUsrId}</td> </tr>
        <tr $yelclr><td>Дата рождения: </td> <td>$userBirthDay{$snpUsrId}</td> </tr>
        <tr $yelclr1><td>Ваш пол: </td> <td>$userGender{$snpUsrId}</td> </tr>
        <tr $yelclr><td>Место работы / учебы: </td> <td>$userWorkPlace{$snpUsrId}</td> </tr>
        <tr $yelclr1><td>Номер удостоверения: </td> <td>$userPersonId{$snpUsrId}</td> </tr>
        <tr $yelclr><td>ИИН: </td> <td>$userIndivId{$snpUsrId}</td> </tr></table>
        <p><a href=\'$httpactivecgi\'>ДОМОЙ</a> </p>";
      }
      else { print "<p>$rf Email [$snpEmail] не найден! Пожалуйста проверьте.. $f2</p> <p><a href=\'$indexcgi\'>ДОМОЙ</a> </p>"; }
  }
  else { #print "<!-- sdsCookieUsrRnd:[$snpCookieUsrRnd] sdsCookieRndNum:[$snpCookieRndNum] sdsRndNum:[$snpRndNum] -->\n";
         #print "<!-- whatis{'validnum'}:[$whatis{'validnum'}] whatis{'userid'}:[$whatis{'userid'}] -->\n";
         #print "<!-- userEmailExist{$snpEmail}:[$userEmailExist{$snpEmail}] sdsUsrIp:[$snpUsrIp] userip:[$userip] -->\n";
         print "<p>$rf Неверный номер валидации! Пожалуйста проверьте.. $f2</p>  <p><a href=\'$indexcgi\'>ДОМОЙ</a> </p>"; }
}

##################################################################################################################
##################################### Sub EditPasswordSub ########################################################
##################################################################################################################
sub EditPasswordSub {
   if ( $userEmailExist{$whatis{'email'}} == 1 ) { 
       $edsRandNum = int(rand(10)*1000000000000);  #  $slmailphp = '../phpmail.php';  $httpEmailPhp = 'http://accelerator.kvadra.kz/phpmail.php';
       open(INF, $vlTempData_file);          @vlTempDataList = <INF>;           close(INF); 
       foreach $i ( @vlTempDataList ) {  chomp($i);     if ( $i =~ /$datenow/ && $i !~ /$whatis{'email'}/  ) { push ( @newVlTempDataList, $i ) ; }   }
       $edsNewTempTxtLine = "$whatis{'email'}<tab>$newUsrRegRndNum<tab>$edsRandNum<tab>$userip<tab>$datenow<tab>\n";
       open(EDSDATA,">$vlTempData_file"); foreach $i ( @newVlTempDataList ) { print EDSDATA "$i\n"; } print EDSDATA  $edsNewTempTxtLine; close(EDSDATA); 
       &printjavascript(); $edsUsrId = $userCode{$whatis{'email'}};
       print "<p>Мы отправили номер валидации на ваш email [$whatis{'email'}]. 
       <br>Проверьте вашу почту! В случае проблем <a href = \'$httpindexcgi\'>попробуйте еще раз..</a></p>\n";
       print "<form method='post' action=\'$httpindexcgi\' name = 'updatedata' onsubmit='return checkPwdFunction();' >
       <input type = 'hidden' name = 'action' value = 'editpwd'><input type = 'hidden' name = 'userid' value = \'$edsUsrId\'><table>
       <tr $yelclr><td>Номер валидации: </td><td><input type = 'text'  name = 'validnum' value = ''></td></tr>
       <tr $yelclr><td>Пароль: </td><td><input type = 'password'  name = 'pwd' value = ''></td></tr>
       <tr $yelclr1><td>Повторить пароль: </td><td><input type = 'password'  name = 'samepwd' value = ''></td></tr>
       <tr $yelclr><td><input type='reset' value = 'Reset'></td><td><input type = 'submit' value = 'Enter'></td></tr></table></form>\n";
       $edsPhpEmailTxt = "<?php\n\$msg = \"Hello!\\n Please use the validation number: " . $edsRandNum . '\n Best regards,\n Open English team";';
       $edsPhpEmailTxt = $edsPhpEmailTxt . "\n" . '$headers = "From: noreply@alteginber.kz" . "\r\n";';
       $edsPhpEmailTxt = $edsPhpEmailTxt . "\n" . '$rr = mail("' . $whatis{'email'} . '","Personal data - email confirmation",$msg, $headers);';
       $edsPhpEmailTxt = $edsPhpEmailTxt . "\n\?>\n<html><body $grnclr>Email had been sent successsfully!</body></html>\n" ;
       open(EDSD,">$slmailphp");
       print EDSD $edsPhpEmailTxt;
       close(EDSD); 
       print "<iframe src=\'$httpEmailPhp\' width='350' height='40'> </iframe>\n<p> </p>\n <p><a href=\'$indexcgi\'>ДОМОЙ</a> </p>";
   }
   else { print "<p>Incorrect email address! Please check & try again..</p>\n <p><a href=\'$indexcgi\'>ДОМОЙ</a> </p>";  }
}

##################################################################################################################
################################### Sub openEmailFormSub #########################################################
##################################################################################################################

sub openResetFormSub {
      print "<p>Введите ваш email адрес. <br>Мы отправим на почту номер валидации!</p>\n";
      print "<form method='post' action=\'$httpindexcgi\'><p>Email: <input type = 'text'  name = 'email' value = ''>
      <input type = 'hidden' name = 'action' value = 'resetpwd'> <input type = 'submit' value = 'Enter'></p></form>
      <p> </p>\n <p><a href=\'$indexcgi\'>ДОМОЙ</a> </p>\n";
}

##################################################################################################################
######################################### Sub SaveDataSub ########################################################
##################################################################################################################
sub SaveDataSub {
  ($sdsCookieKey, $sdsCookieParameters) = split(/=/, $gotcookie);  ($sdsUsrNum, $sdsCookieUsrRnd, $sdsUsrBrowser) = split(/_/, $sdsCookieParameters);
  open(INF, $vlTempData_file);       @vlTempData_list = <INF>;       close(INF); 
  foreach $i (@vlTempData_list) { chomp ( $i ); if ( $i =~ /$sdsCookieUsrRnd/ ) 
  { ($sdsEmail, $sdsCookieRndNum, $sdsRndNum, $sdsUsrIp, @others) = split(/<tab>/, $i); } }
  #print "<p>udsCookieUsrRnd: [$sdsCookieUsrRnd] udsCookieRndNum: [$sdsCookieRndNum] udsRndNum: [$sdsRndNum] Validation number: [$whatis{'validnum'}]</p>\n";
  $sdsUsrId = $whatis{'userid'};
  if ( $sdsCookieUsrRnd eq  $sdsCookieRndNum &&  $sdsRndNum eq $whatis{'validnum'} && $whatis{'userid'} =~ /54LD/ ) {
     if ( $userEmailExist{$sdsEmail} == 1 && $sdsUsrIp eq $userip ) {
        $whatis{'firstname'} =~s/ //g;  $whatis{'firstname'} =~s/ //g;  $whatis{'secondname'} =~s/ //g;  $whatis{'secondname'} =~s/ //g;  
        $whatis{'thirdname'} =~s/ //g;  $whatis{'thirdname'} =~s/ //g;  $whatis{'pwd'} =~s/ //g;  $whatis{'pwd'} =~s/ //g;
        
       # $userNumber{$tusrid} = $tusrnum; $userCode{$tusrnum} = $tusrid; $userCode{$tusremail} = $tusrid;
       # $userFirstName{$tusrid} = $tusrfrstnam; $userSecondName{$tusrid} = $tusrscndnam; $userThirdName{$tusrid} = $tusrthrdnam;
       # $userpwd{$tusrid} = $tusrpwd; $userSchoolId{$tusrid} = $tusrsclid; $userGroupId{$tusrid} = $tusrgrpid;
       # $userPhoneNumber{$tusrid} = $tusrphnnum; $userEmail{$tusrid} = $tusremail; $userCreated{$tusrid} = $tusrcreated;
       # $userBirthDay{$tusrid} = $tusrbrthday; $userGender{$tusrid} = $tusrgender; 
       # $userWorkPlace{$tusrid} = $tusrwrkplc; $userPersonId{$tusrid} = $tusrprsnid; $userIndivId{$tusrid} = $tusrindvdid; 
        
        foreach $i(@userlist){ 
           chomp($i);
           if($i =~ /$sdsEmail/ && $i =~ /$sdsUsrId/){
              ($sdsUserNum, @others) = split(/<tab>/, $i);
              $sdsDataLine = "$sdsUserNum<tab>$sdsUsrId<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}<tab>";
              $sdsDataLine = $sdsDataLine . "$whatis{'pwd'}<tab>$userSchoolId{$sdsUsrId}<tab>$userGroupId{$sdsUsrId}<tab>$whatis{'phone'}";
              $sdsDataLine = $sdsDataLine . "<tab>$sdsEmail<tab>$timedatenow<tab>$whatis{'birthday'}<tab>$whatis{'gender'}<tab>";
              $sdsDataLine = $sdsDataLine . "$whatis{'workplace'}<tab>$whatis{'personid'}<tab>$whatis{'individ'}<tab>reserve";
              push(@sdsNewUserList, $sdsDataLine);
           }
           else { push(@sdsNewUserList, $i); }
        }
        open(D,">$users_file"); foreach $i(@sdsNewUserList){ if ( $i ne '' ) { print D "$i\n"; } }  close(D); 
        #print "<!-- [@sdsNewUserList] -->";
        print "<table $grnclr><tr><td>Ваши данные сохранены!</td></tr></table><p> </p>
        <table><tr $yelclr><td>Ваше имя: </td> <td>$whatis{'firstname'}</td></tr>
        <tr $yelclr1><td>Фамилия: </td> <td>$whatis{'secondname'}</td> </tr>
        <tr $yelclr><td>Отчество: </td> <td>$whatis{'thirdname'}</td> </tr>
        <tr $yelclr1><td>Школа: </td> <td>$userSchoolId{$sdsUsrId}</td> </tr>
        <tr $yelclr><td>Группа: </td> <td>$userGroupId{$sdsUsrId}</td> </tr>
        <tr $yelclr1><td>Телефон: </td> <td>$whatis{'phone'}</td> </tr>
        <tr $yelclr><td>Email: </td> <td>$sdsEmail</td> </tr>
        <tr $yelclr1><td>Дата изменений: </td> <td>$timedatenow</td> </tr>
        <tr $yelclr><td>Дата рождения: </td> <td>$whatis{'birthday'}</td> </tr>
        <tr $yelclr1><td>Ваш пол: </td> <td>$whatis{'gender'}</td> </tr>
        <tr $yelclr><td>Место работы / учебы: </td> <td>$whatis{'workplace'}</td> </tr>
        <tr $yelclr1><td>Номер удостоверения: </td> <td>$whatis{'personid'}</td> </tr>
        <tr $yelclr><td>ИИН: </td> <td>$whatis{'individ'}</td> </tr></table>
        <p> </p>";
      }
      else { print "<p>$rf Email [$sdsEmail] не найден! Пожалуйста проверьте.. $f2</p> <p><a href=\'$indexcgi\'>ДОМОЙ</a> </p>"; }
  }
  else { #print "<!-- sdsCookieUsrRnd:[$sdsCookieUsrRnd] sdsCookieRndNum:[$sdsCookieRndNum] sdsRndNum:[$sdsRndNum] -->\n";
         #print "<!-- whatis{'validnum'}:[$whatis{'validnum'}] whatis{'userid'}:[$whatis{'userid'}] -->\n";
         #print "<!-- userEmailExist{$sdsEmail}:[$userEmailExist{$sdsEmail}] sdsUsrIp:[$sdsUsrIp] userip:[$userip] -->\n";
         print "<p>$rf Неверный номер валидации! Пожалуйста проверьте.. $f2</p>  <p><a href=\'$indexcgi\'>ДОМОЙ</a> </p>"; }
}

##################################################################################################################
######################################### Sub EditDataSub ########################################################
##################################################################################################################
sub EditDataSub {
   $edsUsrId = $gotusrid;  $whatis{'email'} = $userEmail{$edsUsrId};
   if ( $userEmailExist{$whatis{'email'}} == 1 ) { 
       ($edsCookieKey, $edsCookieParameters) = split(/=/, $gotcookie);  ($edsUsrNum, $edsCookieUsrRnd, $edsUsrBrowser) = split(/_/, $edsCookieParameters);
       $edsRandNum = int(rand(10)*1000000000000); &printjavascript(); 
       open(INF, $vlTempData_file);          @vlTempDataList = <INF>;           close(INF); 
       foreach $i ( @vlTempDataList ) {  chomp($i);     if ( $i =~ /$datenow/ && $i !~ /$whatis{'email'}/  ) { push ( @newVlTempDataList, $i ) ; }   }
       $edsNewTempTxtLine = "$userEmail{$edsUsrId}<tab>$edsCookieUsrRnd<tab>$edsRandNum<tab>$userip<tab>$datenow<tab>\n";
       open(EDSDATA,">$vlTempData_file"); foreach $i ( @newVlTempDataList ) { print EDSDATA "$i\n"; } print EDSDATA  $edsNewTempTxtLine; close(EDSDATA); 
       
       # $userFirstName{$edsUsrId} = $tusrfrstnam; $userSecondName{$edsUsrId} = $tusrscndnam; $userEmail{$tusrid} = $tusremail;
       #$userThirdName{$edsUsrId} = $tusrthrdnam; $userCode{$edsUsrId} = $tusrid; $userCode{$edsUsrId} = $tusrid;
       #$userPhoneNumber{$edsUsrId} = $tusrphnnum; $userBirthDay{$edsUsrId} = $tusrbrthday; $userGender{$edsUsrId} = $tusrgender; 
       #$userWorkPlace{$edsUsrId} = $tusrwrkplc; $userPersonId{$edsUsrId} = $tusrprsnid; $userIndivId{$edsUsrId} = $tusrindvdid; 
       
       print "<p>Мы отправили номер валидации на ваш email [$userEmail{$edsUsrId}]. 
       <br>Проверьте вашу почту! В случае проблем <a href = \'$httpactivecgi\'>попробуйте еще раз..</a></p>\n";
       print "<form method='post' action=\'$httpindexcgi\' name = 'updatedata' onsubmit='return checkAllFunction();' >
       <input type = 'hidden' name = 'action' value = 'save'><input type = 'hidden' name = 'userid' value = \'$edsUsrId\'><table>
       <tr $yelclr><td>Номер валидации: </td><td><input type = 'text'  name = 'validnum' value = ''></td></tr>
       <tr $yelclr1><td>Ваше Имя: </td><td><input type = 'text'  name = 'firstname' value = \'$userFirstName{$edsUsrId}\'></td></tr>
       <tr $yelclr><td>Фамилия: </td><td><input type = 'text'  name = 'secondname' value = \'$userSecondName{$edsUsrId}\'></td></tr>
       <tr $yelclr1><td>Отчество: </td><td><input type = 'text'  name = 'thirdname' value = \'$userThirdName{$edsUsrId}\'></td></tr>
       <tr $yelclr><td>Пароль: </td><td><input type = 'password'  name = 'pwd' value = \'$userpwd{$edsUsrId}\'></td></tr>
       <tr $yelclr1><td>Повторить пароль: </td><td><input type = 'password'  name = 'samepwd' value = \'$userpwd{$edsUsrId}\'></td></tr>
       <tr $yelclr><td>Телефон: </td><td><input type = 'text'  name = 'phone' value = \'$userPhoneNumber{$edsUsrId}\'></td></tr>
       <tr $yelclr1><td>Дата рождения: </td><td><input type = 'text'  name = 'birthday' value = \'$userBirthDay{$edsUsrId}\'></td></tr>
       <tr $yelclr><td>Пол: </td><td><select name = 'gender'><option value = ''>Выберите пол</option><option value = 'Male'>Male</option>\n";
       if ( $userGender{$edsUsrId} ne '' ) { print "<option value = \'$userGender{$edsUsrId}\' selected>$userGender{$edsUsrId}</option>"; }
       print "<option value = 'Female'>Female</option></select></td></tr>
       <tr $yelclr1><td>Место учебы/ работы: </td><td><input type = 'text'  name = 'workplace' value = \'$userWorkPlace{$edsUsrId}\'></td></tr>
       <tr $yelclr><td>Номер удостоверения: </td><td><input type = 'text'  name = 'personid' value = \'$userPersonId{$edsUsrId}\'></td></tr>
       <tr $yelclr1><td>ИИН: </td><td><input type = 'text'  name = 'individ' value = \'$userIndivId{$edsUsrId}\'></td></tr>
       <tr $yelclr><td><input type='reset' value = 'Reset'></td><td><input type = 'submit' value = 'Enter'></td></tr></table></form>\n";
       $edsPhpEmailTxt = "<?php\n\$msg = \"Hello!\\n Please use the validation number: " . $edsRandNum . '\n Best regards,\n Open English team";';
       $edsPhpEmailTxt = $edsPhpEmailTxt . "\n" . '$headers = "From: noreply@alteginber.kz" . "\r\n";';
       $edsPhpEmailTxt = $edsPhpEmailTxt . "\n" . '$rr = mail("' . $userEmail{$edsUsrId} . '","Personal data - email confirmation",$msg, $headers);';
       $edsPhpEmailTxt = $edsPhpEmailTxt . "\n\?>\n<html><body $grnclr>Email had been sent successsfully!</body></html>\n" ;
       open(EDSD,">$slmailphp");
       print EDSD $edsPhpEmailTxt;
       close(EDSD); 
       print "<iframe src=\'$httpEmailPhp\' width='350' height='40'> </iframe>\n<p> </p>\n <p> </p>";
   }
   else { print "<p>Incorrect email address! Please check & try again..</p>\n <p><a href=\'$indexcgi\'>ДОМОЙ</a> </p>";  }
}

#######################################################################################
########################## JAVASCRIPT PART ############################################
#######################################################################################
sub printjavascript {
print  <<EOT;
 <script>
 function checkAllFunction (){
   if(document.getElementsByName('validnum')[0].value == ''){alert('No validation number!'); return false;}
   if(document.getElementsByName('firstname')[0].value == ''){alert('No first name!'); return false;}
   if(document.getElementsByName('secondname')[0].value == ''){alert('No second name!'); return false;}
   if(document.getElementsByName('pwd')[0].value == ''){alert('No password!'); return false;}
   if(document.getElementsByName('samepwd')[0].value == ''){alert('No repeated password!'); return false;}
   if(document.getElementsByName('samepwd')[0].value != document.getElementsByName('pwd')[0].value){alert('Passwords are not equal!'); return false;}
 }
 function checkPwdFunction (){
   if(document.getElementsByName('validnum')[0].value == ''){alert('No validation number!'); return false;}
   if(document.getElementsByName('pwd')[0].value == ''){alert('No password!'); return false;}
   if(document.getElementsByName('samepwd')[0].value == ''){alert('No repeated password!'); return false;}
   if(document.getElementsByName('samepwd')[0].value != document.getElementsByName('pwd')[0].value){alert('Passwords are not equal!'); return false;}
 }
</script> 
EOT
}
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
    $logindata = "User number: [$gcusrnum] User RND: [$gcusrrnd] User's RND: [$oeusercookiernd{$gcusrnum}]";
    if ( $whatis{'action'} eq 'resetpwd' ) {
       $newUsrRegRndNum = int(rand(10)*1000000000000);
       $newcookie = "volonteersproject\=999999\_$newUsrRegRndNum\_desktop\; expires=$live_time\; path=/\;";
       print "Set-Cookie: " . $newcookie . "\n";  return;
    }
    elsif ( $gotcookie =~ /volonteersproject/ && $whatis{'action'} ne 'logout' && $whatis{'action'} ne 'login' ) { $iwashere = 1;
       if ( $oeusercookiernd{$gcusrnum} eq $gcusrrnd && $userip eq $oeusercookieip{$gcusrnum} && $userip ne '' ) {  
          $userlogged = 1;   $gotusrid = $gcusrnum;
          if($whatis{'browser'} eq 'mobile'){ $userbrowser = 'mobile'; }
          elsif($whatis{'browser'} eq 'desktop'){ $userbrowser = 'desktop'; }
          else{ $userbrowser = $gcusrbrowser; }
          $newcookie = "volonteersproject\=$gcusrnum\_$gcusrrnd\_$userbrowser\; expires=$live_time\; path=/\;";
          print "Set-Cookie: " . $newcookie . "\n";
       }
       else { $errorlogin = "$rf $b1 User not identified or no permission to access! $b2 $f2"; }
    } #$userpwd{$tusrid} = $tusrpwd; $userpwd{$tusremail} = $tusrpwd;
      #$userFirstName{$tusrid} = $tusrfrstnam; $userCode{$tusrid} = $tusrid; $userCode{$tusremail} = $tusrid;
      #$userSchoolId{$tusrid} = $tusrsclid; $userGroupId{$tusrid} = $tusrgrpid; 
    elsif ( $whatis{'action'} eq 'login' || $whatis{'action'} eq 'logout' ) {
       if ( $whatis{'action'} eq 'logout' ) {
          $userlogged = 0; $gotusrid = $gcusrnum; $oeusercookiernd{$gotusrid} = '1234567890';
          $oeusercookiedate{$gotusrid} = $timedatenow;  $oeusercookieip{$gotusrid} = $userip;
          $newcookie = "volonteersproject=0_1234567890_desktop\; expires=$live_time\; path=/\;";
          print "Set-Cookie: " . $newcookie . "\n";  $iwashere = 2;
       }
       elsif ( $whatis{'action'} eq 'login' ) {
          if ( $whatis{'userpwd'} eq $userpwd{$whatis{'email'}} && $whatis{'userpwd'} ne '' ) {
              $ccUserNumber = $userCode{$whatis{'email'}};
              if ( $ccUserNumber =~ /54LD/ ) { $gotusrid = $ccUserNumber; }  else { $gotusrid = 0; }
              $randnum = int(rand(10)*1000000000000);       $oeusercookiernd{$gotusrid} = $randnum;
              $oeusercookiedate{$gotusrid} = $timedatenow;  $oeusercookieip{$gotusrid} = $userip;
              $newcookie = "volonteersproject\=$gotusrid\_$randnum\_desktop\; expires=$live_time\; path=/\;";
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
          if($tclusrnum eq $userCode{$whatis{'email'}} && $tclusrnum ne '' ) { $donothing = 1; }
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
######################################## Sub printfile ###########################################################
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