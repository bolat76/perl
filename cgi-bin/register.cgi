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
        if($cookiekey =~ /candidatesproject/){$gotcookie = $hotcookie; }
    }
#$gotcookie = $ENV{'HTTP_COOKIE'};
$cookie_file = '../oedata/cn_cookies.txt';
$users_file = '../oedata/cn_usrdata.txt';
###################### end of cookie part #########################
$oe_folder = '../oedata/';
$upload_folder = '../oedata/';
$log_file = "../oedata/logs/$yearnow\.$ai{$monthnow}_log.txt";
$cnTempData_file = $oe_folder . 'can_tempdata.txt';
$bas = $oe_folder  . 'bas.txt';
$end = $oe_folder . 'end.txt';
$indexcgi = 'register.cgi';
$cnmailphp = '../phpmail.php';
$cnSmtpMailPhp = '../smtp.php'; #$httpSmtpEmailPhp
$httpEmailPhp = 'http://accelerator.kvadra.kz/phpmail.php';
$httpSmtpEmailPhp = 'http://accelerator.kvadra.kz/smtp.php';
$httpindexcgi = 'http://accelerator.kvadra.kz/cgi-bin/' . $indexcgi;
$httphomecgi = 'http://accelerator.kvadra.kz/cgi-bin/limbo.cgi';
$uploadcgi  = '/cgi-bin/upload.cgi';
$title = 'Register';

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

$glbClmnName{'0'} = 'Порядковый номер'; $glbClmnName{'1'} = 'Категория'; $glbClmnName{'2'} = 'Ваше имя';
$glbClmnName{'3'} = 'Фамилия'; $glbClmnName{'4'} = 'Отчество'; $glbClmnName{'5'} = 'Ваш пароль';
$glbClmnName{'6'} = 'Номер телефона'; $glbClmnName{'7'} = 'Уровень'; $glbClmnName{'8'} = 'Ваш EMAIL';
$glbClmnName{'9'} = 'Дата регистрации в системе'; $glbClmnName{'10'} = 'Дата рождения'; $glbClmnName{'11'} = 'Ваш пол';
$glbClmnName{'12'} = 'Место учебы / работы'; $glbClmnName{'13'} = 'Номер удостоверения'; $glbClmnName{'14'} = 'Ваш ИИН';
$glbClmnName{'15'} = 'Занятость'; $glbClmnName{'16'} = 'Школа';  
   
open(INF, $users_file); @userlist = <INF>; close(INF); $userslist = 0;
foreach $i(@userlist){ 
   #3<tab>Болатхан<tab>Джайдаринов<tab><tab>america<tab>8 777 277 0326<tab>candidate<tab>b.jaidarinov@gmail.com
   #<tab>25.07.2019<tab>12.07.1976<tab>Male<tab>85 room<tab>1233333<tab>12341556688<tab>reserve
   ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, 
   $tusrtype, $tusreml, $tusrcreated, $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, 
   $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $i); $tusreml = lc $tusreml;
   $usernumber{$tusreml} = $tusrid; $userCategory{$tusrid} = $tusrctgr; $userFullName{$tusrid} = "$tusrfrstnam $tusrthrdname $tusrscndnam";
   $userFirstName{$tusrid} = $tusrfrstnam; $userSecondName{$tusrid} = $tusrscndnam; $userThirdName{$tusrid} = $tusrthrdname;
   $userpwd{$tusreml} = $tusrpwd; $userpwd{$tusrid} = $tusrpwd; $userPhoneNumber{$tusrid} = $tusrphnnum;
   $userType{$tusrid} = $tusrtype; $userEmail{$tusrid} = $tusreml; $userEmailExist{$tusreml} = 1; 
   $userCreateDate{$tusrid} = $tusrcreated; $userBirthDay{$tusrid} = $tusrbrthday; $userGender{$tusrid} = $tusrgndr;
   $userWorkPlace{$tusrid} = $tusrwrkplc; $userPersonId{$tusrid} = $tusrprsnid; $userIndivideId{$tusrid} = $tusrindvdid;
   $userStatus{$tusrid} = $tusrstats; $userSchoolId{$tusrid} = $tusrschlid; $userGlobalDataList{$tusrid} = $i;
   if ( $tusrid ne '' ) { $userslist = $tusrid; }   push(@loginuserslist, $tusrid); 
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
$userlogged = 0; &checkcookies(); print "\n"; &printfile($bas, $title);

if ( $whatis{'action'} ne '' ) { open(GURD,">>$log_file");
print GURD "Time: [$timedatenow] User ID: [$gotusrid] IP address: [$userip] User action: [$whatis{'action'}] Script: [$indexcgi] \n";
close(GURD); }

#####################################################################################
############################# LOGIN CHECK PART ######################################
#####################################################################################
print "<p> </p>"; 
if ( $userlogged == 1 ) {
    print "Hello $b1 $userFirstName{$gotusrid}!$b2 <a href = \'$indexcgi?action=logout\'>Logout</a>\n";
    if ( $whatis{'action'} eq 'show' ) { &ShowPersonDataSub() ; }   # print the personal data 
    elsif ( $whatis{'action'} eq 'edit' ) { &UpdateEmailSub() ; }   # send email to user and open form for personal data to update
    elsif ( $whatis{'action'} eq 'update' ) { &UpdateDataSub() ; }  # update the personal data 
    else { print "<p><a href=\'$httphomecgi\'>Welcome HOME</a></p>
    <p> </p><p><a href=\'$indexcgi?action=show\'>Персональные данные</a></p>\n"; }
}
elsif ( $userlogged == 0 ) {
    if ( $whatis{'action'} eq 'register' ) { &openEmailFormSub() ; }   # open the form to enter email to send validation number for registration
    elsif ( $whatis{'action'} eq 'sendemail' ) { &sendLinkToEmailSub(); } # sendemail
    elsif ( $whatis{'action'} eq 'record' ) { &recordUserDataSub() ; } # record the personal data and register new user
    elsif ( $whatis{'validnum'} ne '' ) { &openDataFieldsSub() ; }   # send email to user and open form for personal data to enter
    elsif ( $whatis{'action'} eq 'reset' ) { &openResetFormSub() ; }   # open the form to enter email to send validation number for reset
    elsif ( $whatis{'action'} eq 'updatepwd' ) { &recordNewPwdSub() ; }# record the updated password
    elsif ( $whatis{'action'} eq 'resetemail' ) { &ResetEmailSub() ; } # send email to user and open form for personal data to update
    #elsif ( $whatis{'action'} eq 'update' ) { &UpdateDataSub() ; }     # update the personal data 
    else { if ( $whatis{'action'} eq 'login' && $userlogged != 1) { print "<p>$rf $errorlogin $f2</p>\n" ; } 
       print "<form method='post' action=\'$httphomecgi\'> <table><caption>Введите ваши данные</caption><tr><td>Email: </td>
       <td><input type = 'text'  name = 'email'></td>  <td>Пароль: </td><td><input type = 'password'  name = 'userpwd'> </td>
       <td><input type = 'hidden' name = 'action' value = 'login'>  <input type = 'submit' value = 'Enter'></td></tr></table></form>
       <p><a href=\'$indexcgi?action=register\'>РЕГИСТРАЦИЯ</a> -[]-[]-[]-[]- <a href=\'$indexcgi?action=reset\'>ЗАБЫЛИ ПАРОЛЬ?</a></p>";
    }
}
else {
   print "<form method='post' action=\'$httphomecgi\'> <table><caption>Введите ваши данные</caption><tr><td>Email: </td>
   <td><input type = 'text'  name = 'email'></td>  <td>Пароль: </td><td><input type = 'password'  name = 'userpwd'> </td>
   <td><input type = 'hidden' name = 'action' value = 'login'>  <input type = 'submit' value = 'Enter'></td></tr></table></form>
   <p><a href=\'$indexcgi?action=register\'>РЕГИСТРАЦИЯ</a> -[]-[]-[]-[]- <a href=\'$indexcgi?action=reset\'>ЗАБЫЛИ ПАРОЛЬ?</a></p>";
}

#####################################################################################
########################### START MAIN BODY #########################################
#####################################################################################

print "</center></body></html>\n";
#&printfile($end, $title);

##################################################################################################################
################################## SHOW PERSONAL DATA SUB ########################################################
##################################################################################################################
sub ShowPersonDataSub {

   # ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, 
   # $tusrtype, $tusreml, $tusrcreated, $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, 
   # $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $i);
   # $usernumber{$tusreml} = $tusrid; $userCategory{$tusrid} = $tusrctgr; $userFullName{$tusrid} = "$tusrfrstnam $tusrthrdname $tusrscndnam";
   # $userFirstName{$tusrid} = $tusrfrstnam; $userSecondName{$tusrid} = $tusrscndnam; $userThirdName{$tusrid} = $tusrthrdname;
   # $userpwd{$tusreml} = $tusrpwd; $userpwd{$tusrid} = $tusrpwd; $userPhoneNumber{$tusrid} = $tusrphnnum;
   # $userType{$tusrid} = $tusrtype; $userEmail{$tusrid} = $tusreml; $userEmailExist{$tusreml} = 1; 
   # $userCreateDate{$tusrid} = $tusrcreated; $userBirthDay{$tusrid} = $tusrbrthday; $userGender{$tusrid} = $tusrgndr;
   # $userWorkPlace{$tusrid} = $tusrwrkplc; $userPersonId{$tusrid} = $tusrprsnid; $userIndivideId{$tusrid} = $tusrindvdid;
   # $userStatus{$tusrid} = $tusrstats; $userSchoolId{$tusrid} = $tusrschlid; $userGlobalDataList{$tusrid} = $i;
  
   $spdStyle = "style='height:50px; width:250px'";   $spdCategory = $userCategory{$gotusrid}; $myclr = $yelclr1;
   ( @spdUserData ) = split(/<tab>/, $userGlobalDataList{$gotusrid});
   
   if ( $spdCategory eq 'Volonteer' ) { @spdShowClmnsList = ('2', '3', '4','6', '8', '9', '10', '11', '12', '13', '14', '15'); }
   elsif ( $spdCategory eq 'Parent' ) { @spdShowClmnsList = ('2', '3', '4','6', '8', '9', '16'); }
   elsif ( $spdCategory eq 'School' ) { @spdShowClmnsList = ('2', '3', '4','6', '8', '9', '16'); }
   print "<p> </p>\n<table><caption><h3>Ваши персональные данные</h3></caption>";
   foreach $i (@spdShowClmnsList) {
      if ( $myclr eq $yelclr ) { $myclr = $yelclr1; } else { $myclr = $yelclr; }
      print "<tr $myclr><td>$glbClmnName{$i}: </td><td>$spdUserData[$i]</td></tr>\n"
   }
   print "</table><p> </p>
   <button onclick=\"window.location.href = \'$httpindexcgi\?action=edit\'\;\" $spdStyle>Изменить персональные данные</button>
   <p> </p><p><a href=\'$httphomecgi\'>Back to HOME Page</a> </p>\n";
}
##################################################################################################################
######################################### UPDATE DATA SUB ########################################################
##################################################################################################################
sub UpdateDataSub {
  ($udsCookieKey, $udsCookieParameters) = split(/=/, $gotcookie);  ($udsUsrNum, $udsCookieUsrRnd, $udsUsrBrowser) = split(/_/, $udsCookieParameters);
  open(INF, $cnTempData_file);       @slTempData_list = <INF>;       close(INF); 
  foreach $i (@slTempData_list) { chomp ( $i );  if ( $i =~ /$udsCookieUsrRnd/ ) { ($udsEmail, $udsCookieRndNum, $udsRndNum) = split(/<tab>/, $i); } }
 # print "<p>udsCookieUsrRnd: [$udsCookieUsrRnd] udsCookieRndNum: [$udsCookieRndNum] udsRndNum: [$udsRndNum] Validation number: [$whatis{'validnum'}]</p>\n";
  if ( $udsCookieUsrRnd eq  $udsCookieRndNum &&  $udsRndNum eq $whatis{'validnum'} ) {
      if ( $userEmailExist{$udsEmail} != 1) { $udsErrorLine = ' Email not ! ' ; 
         print "<p>$rf Email [ $b1 $rudsEmail $b2 ] не найден! проверьте еще раз.. $f2</p>\n <p><a href=\'$indexcgi?action=reset\'>REGISTER</a> </p>"; }
      else {
         if ( $whatis{'email'} ne '' ) { $udsUserId = $usernumber{$whatis{'email'}}; }
         else { $udsUserId = $gotusrid; }
         $whatis{'firstname'} =~s/ //g; $whatis{'firstname'} =~s/ //g;  $whatis{'secondname'} =~s/ //g;  $whatis{'secondname'} =~s/ //g;
         $whatis{'thirdname'} =~s/ //g; $whatis{'thirdname'} =~s/ //g;  $whatis{'pwd'} =~s/ //g;  $whatis{'pwd'} =~s/ //g; 
        
   # ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, 
   # $tusrtype, $tusreml, $tusrcreated, $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, 
   # $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $i);
   # $usernumber{$tusreml} = $tusrid; $userCategory{$tusrid} = $tusrctgr; $userFullName{$tusrid} = "$tusrfrstnam $tusrthrdname $tusrscndnam";
   # $userFirstName{$tusrid} = $tusrfrstnam; $userSecondName{$tusrid} = $tusrscndnam; $userThirdName{$tusrid} = $tusrthrdname;
   # $userpwd{$tusreml} = $tusrpwd; $userpwd{$tusrid} = $tusrpwd; $userPhoneNumber{$tusrid} = $tusrphnnum;
   # $userType{$tusrid} = $tusrtype; $userEmail{$tusrid} = $tusreml; $userEmailExist{$tusreml} = 1; 
   # $userCreateDate{$tusrid} = $tusrcreated; $userBirthDay{$tusrid} = $tusrbrthday; $userGender{$tusrid} = $tusrgndr;
   # $userWorkPlace{$tusrid} = $tusrwrkplc; $userPersonId{$tusrid} = $tusrprsnid; $userIndivideId{$tusrid} = $tusrindvdid;
   # $userStatus{$tusrid} = $tusrstats; $userSchoolId{$tusrid} = $tusrschlid; $userGlobalDataList{$tusrid} = $i;
    
         if ( $whatis{'pwd'} eq '' ) { $whatis{'pwd'} = $userpwd{$udsEmail}; }
         if ( $userCreateDate{$udsUserId} eq '' ) { $userCreateDate{$udsUserId} = $whatis{'created'}; }
         $udsDataLine = "$whatis{'category'}<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>$whatis{'thirdname'}<tab>";
         $udsDataLine = $udsDataLine . "$whatis{'pwd'}<tab>$whatis{'phone'}<tab>candidate<tab>$udsEmail<tab>";
         $udsDataLine = $udsDataLine . "$userCreateDate{$udsUserId}<tab>$whatis{'birthday'}<tab>$whatis{'gender'}<tab>";
         $udsDataLine = $udsDataLine . "$whatis{'workplace'}<tab>$whatis{'personid'}<tab>$whatis{'individid'}<tab>";
         $udsDataLine = $udsDataLine . "$whatis{'status'}<tab>$whatis{'schoolid'}<tab>reserve";
         foreach $i(@userlist){  chomp($i);
            if ( $i =~ /$udsEmail/ ) { ($udsUserNum, @others) = split(/<tab>/, $i); 
               $udsDataLine = "$udsUserNum<tab>$udsDataLine"; push(@udsNewUserList, $udsDataLine); }
            else { push(@udsNewUserList, $i); }   }
         
         open(D,">$users_file");  foreach $i(@udsNewUserList){ print D "$i\n"; } close(D); 

         print "<p>Добро пожаловать на наш сайт</p>\n<table><caption><h3>Ваши данные сохранены!</h3></caption>";
         print "<tr $yelclr><td>Дата регистрации в системе: </td><td>$b1 $userCreateDate{$udsUserId} $b2</td></tr>
         <tr $yelclr1><td>Ваше имя: </td><td>$whatis{'firstname'}</td></tr>  <tr $yelclr><td>Фамилия: </td><td>$whatis{'secondname'}</td></tr>
         <tr $yelclr1><td>Отчество: </td><td>$whatis{'thirdname'}</td></tr><tr $yelclr><td>Номер телефона: </td><td>$whatis{'phone'}</td></tr>
         <tr $yelclr1><td>EMAIL: </td><td>$udsEmail</td></tr>\n";
         if ( $whatis{'category'} eq 'School' || $whatis{'category'} eq 'Parent' ) { 
            print "<tr $yelclr><td>Школа: </td><td>$whatis{'schoolid'}</td></tr>\n"; }
         elsif ( $whatis{'category'} eq 'Volonteer' ) {   
            print "<tr $yelclr><td>Дата рождения: </td><td>$whatis{'birthday'}</td></tr>
            <tr $yelclr1><td>Пол: </td><td>$whatis{'gender'}</td></tr> <tr $yelclr><td>Место учебы / работы: </td><td>$whatis{'workplace'}</td></tr>
            <tr $yelclr1><td>Номер удостоверения: </td><td>$whatis{'personid'}</td></tr><tr $yelclr><td>ИИН: </td><td>$whatis{'individid'}</td></tr>
            <tr $yelclr1><td>Занятость: </td><td>$whatis{'status'}</td></tr>\n";
         }
         print "</table> <p> </p> <p><a href=\'$httphomecgi\'>Open LOGIN Page</a> </p>";
      }
  }
  else { print "<p>$rf Incorrect validation number!  Please check and try again.. $f2</p>\n <p><a href=\'$indexcgi?action=reset\'>FORGOT PASSWORD?</a> </p>"; }
}

##################################################################################################################
######################################## UPDATE EMAIL SUB ########################################################
##################################################################################################################
sub UpdateEmailSub {
   if ( $userEmailExist{$whatis{'email'}} == 1 || $userlogged == 1 ) { 
      &printjavascript();  $resRandNum = int(rand(10)*1000000000000);  $uesStyle = "style='height:50px; width:150px'";
      ($resCookieKey, $resCookieParameters) = split(/=/, $gotcookie);  ($resUsrNum, $resCookieUsrRnd, $resUsrBrowser) = split(/_/, $resCookieParameters);
      if ( $whatis{'email'} ne '' ) { $resUserId = $usernumber{$whatis{'email'}}; }
      else { $resUserId = $gotusrid; $whatis{'email'} = $userEmail{$gotusrid}; $newUsrRegRndNum = $resCookieUsrRnd; }
      open(INF, $cnTempData_file);          @cnTempDataList = <INF>;           close(INF); 
      foreach $i ( @cnTempDataList ) {  chomp($i);     if ( $i =~ /$datenow/ && $i !~ /$whatis{'email'}/  ) { push ( @newCnTempDataList, $i ) ; }  }
      $resNewTempTxtLine = "$whatis{'email'}<tab>$newUsrRegRndNum<tab>$resRandNum<tab>$datenow<tab>\n";
      open(RESDATA,">$cnTempData_file"); foreach $i ( @newCnTempDataList ) { print RESDATA "$i\n"; } print RESDATA  $resNewTempTxtLine; close(RESDATA); 
      print "<p>We sent a validation number to your email [$whatis{'email'}]. 
      <br>Please check your email box! If problems <a href = \'$httpindexcgi\'>try again..</a></p>\n";
      if ( $userCategory{$resUserId} eq 'Volonteer' ) { 
         $uesJavaFuncName = "'return checkAllFunction();'"; } else { $uesJavaFuncName = "'return checkParFunction();'"; }
      print "<h2>$rf ВНИМАНИЕ! Все изменения должны быть утверждены координатором! $f2</h2>\n <p> </p>
      <form method='post' action=\'$httpindexcgi\' name = 'updatedata' onsubmit = $uesJavaFuncName >
      <input type = 'hidden' name = 'action' value = 'update'><input type = 'hidden' name = 'type' value = \'$userType{$resUserId}\'>
      <input type = 'hidden' name = 'created' value = \'$userCreateDate{$resUserId}\'>
      <input type = 'hidden' name = 'category' value = \'$userCategory{$resUserId}\'>
      <table><tr $yelclr1><td>Дата регистрации в системе: </td><td>$b1 $userCreateDate{$resUserId} $b2</td></tr>
      <tr $yelclr><td>Ваш номер валидации: </td><td><input type = 'text'  name = 'validnum' value = ''> был отправлен вам на почту</td></tr>
      <tr $yelclr1><td>Ваше имя: </td><td><input type = 'text'  name = 'firstname' value = \'$userFirstName{$resUserId}\'></td></tr>
      <tr $yelclr><td>Фамилия: </td><td><input type = 'text'  name = 'secondname' value = \'$userSecondName{$resUserId}\'></td></tr>
      <tr $yelclr1><td>Отчество: </td><td><input type = 'text'  name = 'thirdname' value = \'$userThirdName{$resUserId}\'></td></tr>
      <tr $yelclr><td>Номер телефона: </td><td><input type = 'text'  name = 'phone' value = \'$userPhoneNumber{$resUserId}\'></td></tr>
      <tr $yelclr1><td>EMAIL: </td><td>$b1 $whatis{'email'} $rf Емэйл нельзя изменить! $f2 $b2</td></tr>
      <tr $yelclr><td>Ваш Пароль: </td><td><input type = 'password' name = 'pwd' value = \'$userpwd{$resUserId}\'> Введите новый пароль</td></tr>
      <tr $yelclr1><td>Повторите Пароль: </td><td><input type = 'password' name = 'samepwd' value = \'$userpwd{$resUserId}\'> Повторите новый пароль</td></tr>\n";
      if ( $userCategory{$resUserId} eq 'School' || $userCategory{$resUserId} eq 'Parent' ) { 
         print "<tr $yelclr><td>Школа: </td><td><input type = 'text' name = 'schoolid' value = \'$userSchoolId{$resUserId}\'></td></tr>"; }
      elsif ( $userCategory{$resUserId} eq 'Volonteer' ) {
         print "<tr $yelclr><td>Дата рождения: </td><td><input type = 'text'  name = 'birthday' value = \'$userBirthDay{$resUserId}\'> FORMAT: DD.MM.YYYY</td></tr>
         <tr $yelclr1><td>Пол: </td><td><select name = 'gender'><option value = ''>Выберите пол</option>";
         if ( $userGender{$resUserId} ne '' ) { print "<option value = \'$userGender{$resUserId}\' selected>$userGender{$resUserId}</option>\n"; }
         print "<option value = 'Male'>Male</option> <option value = 'Female'>Female</option></select></td></tr>
         <tr $yelclr><td>Пол: </td><td><select name = 'status'><option value = ''>Выберите род деятельности</option>";
         if ( $userStatus{$resUserId} ne '' ) { print "<option value = \'$userStatus{$resUserId}\' selected>$userStatus{$resUserId}</option>\n"; }
         print "<option value = 'Школьник'>Школьник</option> <option value = 'Студент'>Студент</option>
         <option value = 'Работаю'>Работаю</option></select></td></tr>
         <tr $yelclr1><td>Место учебы / работы: </td><td><input type = 'text'  name = 'workplace' value = \'$userWorkPlace{$resUserId}\'></td></tr>
         <tr $yelclr><td>Номер удостоверения: </td><td><input type = 'text'  name = 'personid' value = \'$userPersonId{$resUserId}\'></td></tr>
         <tr $yelclr1><td>ИИН: </td><td><input type = 'text'  name = 'individid' value = \'$userIndivideId{$resUserId}\'></td></tr>\n"; 
      }
      print "<tr $yelclr1><td><input type='reset' value = 'Reset' $uesStyle></td>
      <td><input type = 'submit' value = 'Enter' $uesStyle></td></tr></table></form>\n";
      $resPhpEmailTxt = "<?php\n\$msg = \"Hello!\\n Please use the validation number: " . $resRandNum . '\n Best regards,\n Open English team";';
      $resPhpEmailTxt = $resPhpEmailTxt . "\n" . '$headers = "From: noreply@alteginber.kz" . "\r\n";';
      $resPhpEmailTxt = $resPhpEmailTxt . "\n" . '$rr = mail("' . $whatis{'email'} . '","Registration - email confirmation",$msg, $headers);';
      $resPhpEmailTxt = $resPhpEmailTxt . "\n\?>\n<html><body $grnclr>Email had been sent successsfully!</body></html>\n" ;
      open(SESD,">$cnmailphp");
      print SESD $resPhpEmailTxt;
      close(SESD); 
      print "<iframe src=\'$httpEmailPhp\' width='350' height='40'> </iframe>";
   }
   else { print "<p>Incorrect email address! Please check & try again..</p>\n <p><a href=\'$indexcgi\'>HOME</a> </p>";  }
}

##################################################################################################################
###################################### RECORD NEW PWD SUB ########################################################
##################################################################################################################
sub recordNewPwdSub {
  ($rnpCookieKey, $rnpCookieParameters) = split(/=/, $gotcookie);    ($rnpUsrNum, $rnpCookieUsrRnd, $rnpUsrBrowser) = split(/_/, $rnpCookieParameters);
  open(INF, $cnTempData_file);       @slTempData_list = <INF>;       close(INF); 
  foreach $i (@slTempData_list) {    chomp ( $i );   if ( $i =~ /$rnpCookieUsrRnd/ ) { ($rnpEmail, $rnpCookieRndNum, $rnpRndNum) = split(/<tab>/, $i); }      }
  #print "<p>rudsCookieUsrRnd: [$rnpCookieUsrRnd] rudsCookieRndNum: [$rnpCookieRndNum] rudsRndNum: [$rnpRndNum] Validation number: [$whatis{'validnum'}]</p>\n";
  if ( $rnpCookieUsrRnd eq  $rnpCookieRndNum &&  $rnpRndNum eq $whatis{'validnum'} ) { 
     if ( $userEmailExist{$rnpEmail} != 1) { $rnpErrorLine = ' Email do not found! ' ; 
        print "<p>$rf Ваш Email [$rnpEmail] не найден! Пожалуйста проверьте.. $f2</p>\n <p> <a href=\'$indexcgi\'>HOME</a> </p>";} 
     else {
        $whatis{'pwd'} =~s/ //g;  $whatis{'pwd'} =~s/ //g; $rnpUserId = $usernumber{$rnpEmail};
        
   # ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, 
   # $tusrtype, $tusreml, $tusrcreated, $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, 
   # $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $i);
   # $usernumber{$tusreml} = $tusrid; $userCategory{$tusrid} = $tusrctgr; $userFullName{$tusrid} = "$tusrfrstnam $tusrthrdname $tusrscndnam";
   # $userFirstName{$tusrid} = $tusrfrstnam; $userSecondName{$tusrid} = $tusrscndnam; $userThirdName{$tusrid} = $tusrthrdname;
   # $userpwd{$tusreml} = $tusrpwd; $userpwd{$tusrid} = $tusrpwd; $userPhoneNumber{$tusrid} = $tusrphnnum;
   # $userType{$tusrid} = $tusrtype; $userEmail{$tusrid} = $tusreml; $userEmailExist{$tusreml} = 1; 
   # $userCreateDate{$tusrid} = $tusrcreated; $userBirthDay{$tusrid} = $tusrbrthday; $userGender{$tusrid} = $tusrgndr;
   # $userWorkPlace{$tusrid} = $tusrwrkplc; $userPersonId{$tusrid} = $tusrprsnid; $userIndivideId{$tusrid} = $tusrindvdid;
   # $userStatus{$tusrid} = $tusrstats; $userSchoolId{$tusrid} = $tusrschlid; $userGlobalDataList{$tusrid} = $i;
        
        $rnpDataLine = "$userCategory{$rnpUserId}<tab>$userFirstName{$rnpUserId}<tab>$userSecondName{$rnpUserId}<tab>";
        $rnpDataLine = $rnpDataLine . "$userThirdName{$rnpUserId}<tab>$whatis{'pwd'}<tab>$userPhoneNumber{$rnpUserId}<tab>";
        $rnpDataLine = $rnpDataLine . "$userType{$rnpUserId}<tab>$rnpEmail<tab>$userCreateDate{$rnpUserId}<tab>$userBirthDay{$rnpUserId}";
        $rnpDataLine = $rnpDataLine . "<tab>$userGender{$rnpUserId}<tab>$userWorkPlace{$rnpUserId}<tab>$userPersonId{$rnpUserId}<tab>";
        $rnpDataLine = $rnpDataLine . "$userIndivideId{$rnpUserId}<tab>$userStatus{$rnpUserId}<tab>$userSchoolId{$rnpUserId}<tab>reserve";
        foreach $i(@userlist){
           chomp($i);
           if ( $i =~ /$udsEmail/ ) {
              ($rnpUserNum, @others) = split(/<tab>/, $i);
              $rnpDataLine = "$rnpUserNum<tab>$rnpDataLine";
              push(@rnpNewUserList, $rnpDataLine);
           }
           else { push(@rnpNewUserList, $i); }
        }
         
        open(D,">$users_file");
        foreach $i(@rnpNewUserList){
           print D "$i\n";
        }
        close(D);  
        print "<p>Добро пожаловать на наш сайт</p>\n<h3>Ваш новый пароль сохранен.</h3>
        <p> </p> <p> <a href=\'$httphomecgi\'>АВТОРИЗАЦИЯ</a> </p>";
     }
  }
  else { print "<p>$rf Incorrect validation number!  Please check and try again.. $f2</p>\n <p><a href=\'$indexcgi?action=register\'>REGISTER</a> </p>"; }
}
##################################################################################################################
######################################### SEND LINK TO EMAIL SUB #################################################
##################################################################################################################
sub sendLinkToEmailSub {  $emailPattern= '^([a-zA-Z0-9][\w\_\.]{6,20})\@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,4})$';
  if ( $whatis{'email'} =~ /$emailPattern/ ) { $sesStyle = "style='height:50px; width:150px'";
     if ( $userEmailExist{$whatis{'email'}} == 1 ) { 
     print "<p>Ваш email [$whatis{'email'}] уже используется!<br> <br>Может Вы <a href=\'$indexcgi?action=reset\'>ЗАБЫЛИ ПАРОЛЬ?</a> </p>";  return; }
     $sesRandNum = int(rand(10)*1000000000000);  #  $cnmailphp = '../phpmail.php';  $httpEmailPhp = 'http://accelerator.kvadra.kz/phpmail.php';
     open(INF, $cnTempData_file);          @cnTempDataList = <INF>;           close(INF); 
     foreach $i ( @cnTempDataList ) {  chomp($i);     if ( $i =~ /$datenow/ && $i !~ /$whatis{'email'}/  ) { push ( @newCnTempDataList, $i ) ; }   }
     $sesNewTempTxtLine = "$whatis{'email'}<tab>$timestamp<tab>$sesRandNum<tab>$datenow<tab>$whatis{'category'}<tab>\n";
     open(SESDATA,">$cnTempData_file");   foreach $i ( @newCnTempDataList ) { print SESDATA "$i\n"; }   print SESDATA  $sesNewTempTxtLine;  close(SESDATA); 
     &printjavascript();     #$cnSmtpMailPhp = '../smtp.php'; #$httpSmtpEmailPhp
     open(INF, $cnSmtpMailPhp);          @cnSmtpMailList = <INF>;           close(INF); 
     $roeNewPhpLine = "smtpmail('User', \'$whatis{'email'}\', 'Open English Registration Email Form', ";
     $roeNewPhpLine = $roeNewPhpLine . "'Добрый день! Чтобы зарегистрироваться в проекте OPEN ENGLISH прошу ";
      $roeNewPhpLine = $roeNewPhpLine . "<a href=\"$httpindexcgi?validnum\=$sesRandNum\&time\=$timestamp\">кликнуть сюда</a>');";
     foreach $i ( @cnSmtpMailList ) {  chomp($i);
        if ( $i =~/Open English Registration Email Form/ ) { push (@newRoeSmtpMailList, $roeNewPhpLine); }
        else { push (@newRoeSmtpMailList, $i); }
     }
     print "<p> </p><h3>На указанный Вами адрес Email почты мы направили письмо со ссылкой.</h3>
     <p> </p><p>Проверьте Вашу почту пожалуйста, чтобы продолжить регистрацию. Спасибо!</p>
     <p> </p><p><a href=\'$httpindexcgi\'>Вернуться ДОМОЙ</a> </p>\n";
     open(SESD,">$cnSmtpMailPhp"); foreach $i ( @newRoeSmtpMailList ) { print SESD "$i\n"; }  close(SESD); 
     print "<iframe src=\'$httpSmtpEmailPhp\' width='350' height='40'> </iframe>";
  }
  else { print "<p>Некорректный адрес email почты! Проверьте еще раз..</p>\n <p><a href=\'$indexcgi?action=register\'>REGISTER</a> </p>";  }
}

##################################################################################################################
######################################### RESET EMAIL SUB ########################################################
##################################################################################################################
sub ResetEmailSub {
   if ( $userEmailExist{$whatis{'email'}} == 1 || $userlogged == 1 ) { 
      &printjavascript();  $resRandNum = int(rand(10)*1000000000000);   $resStyle = "style='height:50px; width:150px'";
      ($resCookieKey, $resCookieParameters) = split(/=/, $gotcookie);  ($resUsrNum, $resCookieUsrRnd, $resUsrBrowser) = split(/_/, $resCookieParameters);
      if ( $whatis{'email'} ne '' ) { $resUserId = $usernumber{$whatis{'email'}}; }
      else { $resUserId = $gotusrid; $whatis{'email'} = $userEmail{$gotusrid}; $newUsrRegRndNum = $resCookieUsrRnd; }
      open(INF, $cnTempData_file);          @cnTempDataList = <INF>;           close(INF); 
      foreach $i ( @cnTempDataList ) {  chomp($i);     if ( $i =~ /$datenow/ && $i !~ /$whatis{'email'}/  ) { push ( @newCnTempDataList, $i ) ; }  }
      $resNewTempTxtLine = "$whatis{'email'}<tab>$newUsrRegRndNum<tab>$resRandNum<tab>$datenow<tab>\n";
      open(RESDATA,">$cnTempData_file"); foreach $i ( @newCnTempDataList ) { print RESDATA "$i\n"; } print RESDATA  $resNewTempTxtLine; close(RESDATA); 
      print "<p>We sent a validation number to your email [$whatis{'email'}]. 
      <br>Please check your email box! If problems <a href = \'$httpindexcgi?action=reset\'>try again..</a></p>\n";
      print "<form method='post' action=\'$httpindexcgi\' name = 'updatedata' onsubmit='return checkPwdFunction();' >
      <input type = 'hidden' name = 'action' value = 'updatepwd'>
      <table><tr $yelclr><td>Ваш номер валидации: </td><td><input type = 'text'  name = 'validnum' value = ''> был отправлен вам на почту</td></tr>
      <tr $yelclr1><td>Ваш Пароль: </td><td><input type = 'password'  name = 'pwd' value = \'$userpwd{$resUserId}\'> Введите новый пароль</td></tr>
      <tr $yelclr><td>Повторите Пароль: </td><td><input type = 'password'  name = 'samepwd' value = \'$userpwd{$resUserId}\'> Повторите новый пароль</td></tr>
      <tr $yelclr1><td><input type='reset' value = 'Reset' $resStyle></td><td><input type = 'submit' value = 'Enter' $resStyle></td></tr></table></form>\n";
      $resPhpEmailTxt = "<?php\n\$msg = \"Hello!\\n Please use the validation number: " . $resRandNum . '\n Best regards,\n Open English team";';
      $resPhpEmailTxt = $resPhpEmailTxt . "\n" . '$headers = "From: noreply@alteginber.kz" . "\r\n";';
      $resPhpEmailTxt = $resPhpEmailTxt . "\n" . '$rr = mail("' . $whatis{'email'} . '","Registration - email confirmation",$msg, $headers);';
      $resPhpEmailTxt = $resPhpEmailTxt . "\n\?>\n<html><body $grnclr>Email had been sent successsfully!</body></html>\n" ;
      open(SESD,">$cnmailphp");
      print SESD $resPhpEmailTxt;
      close(SESD); 
      print "<iframe src=\'$httpEmailPhp\' width='350' height='40'> </iframe> <p> </p><p><a href=\'$indexcgi\'>HOME</a> </p>";
   }
   else { print "<p>Incorrect email address! Please check & try again..</p>\n <p><a href=\'$indexcgi\'>HOME</a> </p>";  }
}

##################################################################################################################
######################################### BLANK FORM SUB #########################################################
##################################################################################################################

sub blankFormSub {
   $emailPattern= '^([a-zA-Z0-9][\w\_\.]{6,20})\@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,4})$';
   if ( $whatis{'email'} !~ /$emailPattern/ ) {
      print "<h3>Емэйл адрес [$whatis{'email'}] некорректный! Пожалуйста проверьте..</h3>
      <p> </p><p><a href=\'$httpindexcgi\'>HOME</a> </p>\n";
   }
   else { 
      print "<h3>Форма регистрации еще не готова. Пожалуйста ждите..</h3>
      <p> </p><p><a href=\'$httpindexcgi\'>HOME</a> </p>\n";
   }
}
##################################################################################################################
################################### OPEN RESET FORM SUB ##########################################################
##################################################################################################################

sub openResetFormSub {
   print "<p>Please enter your email address. <br>We will send validation number to you!</p>\n";
   print "<form method='post' action=\'$httpindexcgi\'> <p>Email: <input type = 'text'  name = 'email' value = ''>
   <input type = 'hidden' name = 'action' value = 'resetemail'> <input type = 'submit' value = 'Enter'></p></form>
   <p> </p><p><a href=\'$httpindexcgi\'>HOME</a> </p>\n";
}
##################################################################################################################
#################################### OPEN EMAIL FORM SUB #########################################################
##################################################################################################################

sub openEmailFormSub {
   print "<p>Пожалуйста введите ваш Email адрес Вашей почты.<br> <br>Мы направим Вам ссылку для дальнейших действий..</p>
   <form method='post' action=\'$httpindexcgi\'><table><tr $yelclr><td>Выберите категорию: </td><td>Ваш Email: </td></tr>
   <tr $yelclr1><td><select name = 'category'><option value = 'Volonteer'>ВОЛОНТЁР</option><option value = 'Parent'>РОДИТЕЛЬ</option>
   <option value = 'School'>Представитель Школы</option></select></td><td><input type = 'text'  name = 'email' value = ''></td></tr> 
   <tr $yelclr><td><input type = 'hidden' name = 'action' value = 'sendemail'></td><td><input type = 'submit' value = 'Enter'></td></tr>
   </table></form><p> </p><p><a href=\'$httpindexcgi\'>HOME</a> </p>\n";
}

##################################################################################################################
####################################### OPEN DATA FIELDS SUB #####################################################
##################################################################################################################

sub openDataFieldsSub {    $odfStyle = "style='height:50px; width:150px'"; $odfFound = 'false';
   open(INF, $cnTempData_file);          @cnTempDataList = <INF>;           close(INF); 
   foreach $i ( @cnTempDataList ) {  chomp($i);     if ( $i =~ /$whatis{'time'}/ && $i =~ /$whatis{'validnum'}/  ) { 
      ($odfEmail, $odfTimeStamp, $odfRandNum, $odfDateNow, $odfCategory, @rest ) = split (/<tab>/, $i); $odfFound = 'true';
   } }
   &printjavascript();
   if ( $odfCategory eq 'Volonteer' ) { 
         $odfJavaFuncName = "'return checkAllFunction();'"; } else { $odfJavaFuncName = "'return checkParFunction();'"; }
   if ( $odfFound eq 'true' ) { print "<p> </p><h2>Прошу заполнить поля для регистрации на сайте</h2>
     <p> </p><form method='post' action=\'$httpindexcgi\' name = 'savenewuser' onsubmit\=$odfJavaFuncName >
     <input type = 'hidden' name = 'action' value = 'record'><input type = 'hidden' name = 'type' value = 'candidate'>
     <input type = 'hidden' name = 'category' value = \'$odfCategory\'><input type = 'hidden' name = 'time' value = \'$whatis{'time'}\'>
     <table><tr $yelclr><td>Ваш номер валидации: $rf * $f2</td>
     <td><input type = 'hidden' name = 'validnum' value = \'$whatis{'validnum'}\'> $b1 $whatis{'validnum'} $b2</td></tr>
     <tr $yelclr1><td>Ваше имя: $rf * $f2</td><td><input type = 'text'  name = 'firstname' value = ''></td></tr>
     <tr $yelclr><td>Фамилия: $rf * $f2</td><td><input type = 'text'  name = 'secondname' value = ''></td></tr>
     <tr $yelclr1><td>Отчество: </td><td><input type = 'text'  name = 'thirdname' value = ''></td></tr>
     <tr $yelclr><td>Номер телефона: $rf * $f2</td><td><input type = 'text'  name = 'phone' value = ''></td></tr>
     <tr $yelclr1><td>EMAIL: </td><td>$b1 $odfEmail $rf Емэйл нельзя изменить! $f2 $b2</td></tr>
     <tr $yelclr><td>Ваш Пароль: $rf * $f2</td><td><input type = 'password'  name = 'pwd' value = ''> Введите Ваш Пароль</td></tr>
     <tr $yelclr1><td>Повторите Пароль: $rf * $f2</td>
     <td><input type = 'password'  name = 'samepwd' value = ''> Повторите Ваш Пароль</td></tr>\n";
     if ( $odfCategory eq 'School' || $odfCategory eq 'Parent' ) { 
        print "<tr $yelclr><td>Школа: $rf * $f2</td><td><input type = 'text' name = 'schoolid' value = ''></td></tr>"; }
     if ( $odfCategory eq 'Volonteer' ) { 
        print "<tr $yelclr><td>Дата рождения: $rf * $f2</td><td><input type = 'text'  name = 'birthday' value = ''> FORMAT: DD.MM.YYYY</td></tr>
        <tr $yelclr1><td>Пол: $rf * $f2</td><td><select name = 'gender'><option value = ''>Выберите пол</option>
        <option value = 'Male'>Male</option> <option value = 'Female'>Female</option></select></td></tr>
        <tr $yelclr><td>Род деятельности: $rf * $f2</td><td><select name = 'status'><option value = ''>Выберите род деятельности</option>
        <option value = 'Школьник'>Школьник</option> <option value = 'Студент'>Студент</option>
        <option value = 'Работаю'>Работаю</option></select></td></tr>
        <tr $yelclr1><td>Место учебы / работы: $rf * $f2</td><td><input type = 'text'  name = 'workplace' value = ''></td></tr>
        <tr $yelclr><td>Номер удостоверения:$rf * $f2 </td><td><input type = 'text'  name = 'personid' value = ''></td></tr>
        <tr $yelclr1><td>ИИН: $rf * $f2</td><td><input type = 'text'  name = 'individid' value = ''></td></tr>\n";
     }
     print "<tr $yelclr1><td><input type='reset' value = 'Reset' $odfStyle></td>
     <td><input type = 'submit' value = 'Enter' $odfStyle></td></tr></table></form>
     <p> </p><h2><a href=\'$httpindexcgi\'>Вернуться ДОМОЙ</a></h2>\n";
   }
   else { print "<p>$rf Incorrect validation number!  Please check and try again.. $f2</p>\n <p><a href=\'$indexcgi?action=register\'>REGISTER</a> </p>"; }
}

##################################################################################################################
#################################### RECORD USER DATA SUB ########################################################
##################################################################################################################

sub recordUserDataSub {
  open(INF, $cnTempData_file); @rudTempDataList = <INF>; close(INF);  $rudFound = 'false'; $rudErrorTxt = '';
  foreach $i ( @rudTempDataList ) {  chomp($i);     if ( $i =~ /$whatis{'time'}/ && $i =~ /$whatis{'validnum'}/  ) { 
      ($rudEmail, $rudTimeStamp, $rudRandNum, $rudCategory, @rest ) = split (/<tab>/, $i); $rudFound = 'true';
  } }
  if ( $whatis{'firstname'} eq '' ) { $rudErrorTxt = $rudErrorTxt . '<br>Не указано имя. '; }
  if ( $whatis{'secondname'} eq '' ) { $rudErrorTxt = $rudErrorTxt . '<br>Не указана Фамилия. '; }
  if ( $whatis{'phone'} eq '' ) { $rudErrorTxt = $rudErrorTxt . '<br>Не указан телефон. '; }
  if ( $whatis{'pwd'} eq '' ) { $rudErrorTxt = $rudErrorTxt . '<br>Не указан пароль. '; }
  if ( $whatis{'pwd'} ne $whatis{'samepwd'} ) { $rudErrorTxt = $rudErrorTxt . '<br>Пароли не совпадают. '; }
  if ( $whatis{'schoolid'} eq '' ) { $rudErrorTxt = $rudErrorTxt . '<br>Не указан номер школы. '; }
  if ( $rudErrorTxt ne '' ) { print "<h2>$rf Вы ввели не полные данные.<br> Прошу вернуться и заполнить все обязательные поля! $f2</h2>
     <p> </p> <p>$rudErrorTxt </p> <p> </p>  <p><a href='javascript:history.go(-1)'>[Назад]</a> </p>";  return;  }
  if ( $rudFound eq 'true' ) { 
     if ( $userEmailExist{$rudsEmail} == 1) { $rudsErrorLine = ' Email already exist! ' ; 
        print "<p>$rf Email [$rudsEmail] already exist! Please check and try again.. $f2</p> 
        <p><a href=\'$indexcgi?action=register\'>REGISTER</a> </p>";} 
     else {
        $whatis{'firstname'} =~s/ //g; $whatis{'firstname'} =~s/ //g;  $whatis{'secondname'} =~s/ //g;  $whatis{'secondname'} =~s/ //g;
        $whatis{'thirdname'} =~s/ //g; $whatis{'thirdname'} =~s/ //g;  $whatis{'pwd'} =~s/ //g;  $whatis{'pwd'} =~s/ //g; $userslist++; 

   # ($tusrid, $tusrctgr, $tusrfrstnam, $tusrscndnam, $tusrthrdname, $tusrpwd, $tusrphnnum, 
   # $tusrtype, $tusreml, $tusrcreated, $tusrbrthday, $tusrgndr, $tusrwrkplc, $tusrprsnid, 
   # $tusrindvdid, $tusrstats, $tusrschlid, @other) = split (/<tab>/, $i);
   # $usernumber{$tusreml} = $tusrid; $userCategory{$tusrid} = $tusrctgr; $userFullName{$tusrid} = "$tusrfrstnam $tusrthrdname $tusrscndnam";
   # $userFirstName{$tusrid} = $tusrfrstnam; $userSecondName{$tusrid} = $tusrscndnam; $userThirdName{$tusrid} = $tusrthrdname;
   # $userpwd{$tusreml} = $tusrpwd; $userpwd{$tusrid} = $tusrpwd; $userPhoneNumber{$tusrid} = $tusrphnnum;
   # $userType{$tusrid} = $tusrtype; $userEmail{$tusrid} = $tusreml; $userEmailExist{$tusreml} = 1; 
   # $userCreateDate{$tusrid} = $tusrcreated; $userBirthDay{$tusrid} = $tusrbrthday; $userGender{$tusrid} = $tusrgndr;
   # $userWorkPlace{$tusrid} = $tusrwrkplc; $userPersonId{$tusrid} = $tusrprsnid; $userIndivideId{$tusrid} = $tusrindvdid;
   # $userStatus{$tusrid} = $tusrstats; $userSchoolId{$tusrid} = $tusrschlid; $userGlobalDataList{$tusrid} = $i;

        $rudsDataLine = "$userslist<tab>$whatis{'category'}<tab>$whatis{'firstname'}<tab>$whatis{'secondname'}<tab>";
        $rudsDataLine = $rudsDataLine . "$whatis{'thirdname'}<tab>$whatis{'pwd'}<tab>$whatis{'phone'}<tab>$whatis{'type'}";
        $rudsDataLine = $rudsDataLine . "<tab>$rudEmail<tab>$timedatenow<tab>$whatis{'birthday'}<tab>$whatis{'gender'}";
        $rudsDataLine = $rudsDataLine . "<tab>$whatis{'workplace'}<tab>$whatis{'personid'}<tab>$whatis{'individid'}<tab>";
        $rudsDataLine = $rudsDataLine . "$whatis{'status'}<tab>$whatis{'schoolid'}<tab>reserve";
        open(D,">>$users_file");        print D "$rudsDataLine\n";        close(D); 
 
        print "<h2>Добро пожаловать на наш сайт</h2>\n<table><caption><h3>Ваши данные сохранены</h3></caption>
        <tr $yelclr><td>Дата регистрации в системе: </td><td>$timedatenow</td></tr> <tr $yelclr1><td>EMAIL: </td><td>$rudEmail</td></tr>
        <tr $yelclr><td>Ваше имя: </td><td>$whatis{'firstname'}</td></tr>  <tr $yelclr1><td>Фамилия: </td><td>$whatis{'secondname'}</td></tr>
        <tr $yelclr><td>Отчество: </td><td>$whatis{'thirdname'}</td></tr><tr $yelclr1><td>Номер телефона: </td><td>$whatis{'phone'}</td></tr>\n";
        if ( $whatis{'category'} eq 'School' || $whatis{'category'} eq 'Parent' ) { print "<tr $yelclr><td>Школа: </td><td>$whatis{'schoolid'}</td></tr>\n"; }
        elsif ( $whatis{'category'} eq 'Volonteer' ) { 
            print "<tr $yelclr><td>Дата рождения: </td><td>$whatis{'birthday'}</td></tr> \n<tr $yelclr1><td>Пол: </td><td>$whatis{'gender'}</td></tr>
            <tr $yelclr><td>Род деятельности: </td><td>$whatis{'status'}</td></tr>\n<tr $yelclr1><td>Место учебы / работы: </td><td>$whatis{'workplace'}</td></tr>
            <tr $yelclr><td>Номер удостоверения: </td><td>$whatis{'personid'}</td></tr>\n<tr $yelclr1><td>ИИН: </td><td>$whatis{'individid'}</td></tr>\n";  
        }
        print "</table> <p> </p>  <p><a href=\'$httphomecgi\'>Open LOGIN Page</a> </p>";
     }
  }
  else { print "<p>$rf Incorrect validation number!  Please check and try again.. $f2</p>\n <p><a href=\'$indexcgi?action=register\'>REGISTER</a> </p>"; }
}
#######################################################################################
########################## JAVASCRIPT PART ############################################
#######################################################################################
sub printjavascript {
print  <<EOT;
 <script>
 function checkPwdFunction (){
   if(document.getElementsByName('validnum')[0].value == ''){alert('No validation number!'); return false;}
   if(document.getElementsByName('pwd')[0].value == ''){alert('No password!'); return false;}
   if(document.getElementsByName('samepwd')[0].value == ''){alert('No repeated password!'); return false;}
   if(document.getElementsByName('samepwd')[0].value != document.getElementsByName('pwd')[0].value){alert('Passwords are not equal!'); return false;}
 }
 function checkParFunction (){  
   if(document.getElementsByName('validnum')[0].value == ''){alert('Номер валидации!'); return false;}
   if(document.getElementsByName('firstname')[0].value == ''){alert('Ваше имя?'); return false;}
   if(document.getElementsByName('secondname')[0].value == ''){alert('Фамилия?'); return false;}
   if(document.getElementsByName('phone')[0].value == ''){alert('Номер телефона?'); return false;}
   if(document.getElementsByName('pwd')[0].value == ''){alert('Введите пароль!'); return false;}
   if(document.getElementsByName('samepwd')[0].value == ''){alert('Повторите пароль!'); return false;}
   if(document.getElementsByName('samepwd')[0].value != document.getElementsByName('pwd')[0].value){alert('Пароли не одинаковы!'); return false;}
   if(document.getElementsByName('schoolid')[0].value == ''){alert('Номер школы?'); return false;}
 }
 function checkAllFunction (){
   if(document.getElementsByName('validnum')[0].value == ''){alert('No validation number!'); return false;}
   if(document.getElementsByName('firstname')[0].value == ''){alert('Ваше имя?'); return false;}
   if(document.getElementsByName('secondname')[0].value == ''){alert('Фамилия?'); return false;}
   if(document.getElementsByName('phone')[0].value == ''){alert('Номер телефона?'); return false;}
   if(document.getElementsByName('pwd')[0].value == ''){alert('No password!'); return false;}
   if(document.getElementsByName('samepwd')[0].value == ''){alert('No repeated password!'); return false;}
   if(document.getElementsByName('samepwd')[0].value != document.getElementsByName('pwd')[0].value){alert('Passwords are not equal!'); return false;}
   if(document.getElementsByName('birthday')[0].value == ''){alert('Дата рождения?'); return false;}
   var usr = document.getElementsByName('birthday')[0].value;
   if (isValidDate(usr)) { document.getElementsByName('birthday')[0].value = usr; }
   else {alert('Неправильная дата: [' + usr + ']!'); return false;}
   if(document.getElementsByName('gender')[0].value == ''){alert('Укажите Ваш пол!'); return false;}
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
################################# Sub checkcookies ###############################################################
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
    if ( $whatis{'action'} eq 'sendemail' || $whatis{'action'} eq 'resetemail') {
       $newUsrRegRndNum = int(rand(10)*1000000000000);
       $newcookie = "candidatesproject\=999999\_$newUsrRegRndNum\_desktop\; expires=$live_time\; path=/\;";
       print "Set-Cookie: " . $newcookie . "\n";  return;
    }
    elsif ( $gotcookie =~ /candidatesproject/ && $whatis{'action'} ne 'logout' && $whatis{'action'} ne 'login' ) { $iwashere = 1;
       if ( $oeusercookiernd{$gcusrnum} eq $gcusrrnd && $userip eq $oeusercookieip{$gcusrnum} ) {  
          $userlogged = 1;   $gotusrid = $gcusrnum;
          $newcookie = "candidatesproject\=$gcusrnum\_$gcusrrnd\_$gcusrbrowser\; expires=$live_time\; path=/\;";
          print "Set-Cookie: " . $newcookie . "\n";
       }
       else { $errorlogin = "$rf $b1 User not identified or no permission to access! $b2 $f2"; }
    } #$userEmailExist{$tusreml} = 1;  $username{$tusreml} = $tusrnam; $userpwd{$tusreml} = $tusrpwd; $usernumber{$tusreml} = $tusrnum;
    elsif ( $whatis{'action'} eq 'login' || $whatis{'action'} eq 'logout' ) {
       if ( $whatis{'action'} eq 'logout' ) {
          $userlogged = 0;   $gotusrid = $gcusrnum;     $oeusercookiernd{$gotusrid} = '1234567890';
          $oeusercookiedate{$gotusrid} = $timedatenow;  $oeusercookieip{$gotusrid} = $userip;
          $newcookie = "candidatesproject=0_1234567890_desktop\; expires=$live_time\; path=/\;";
          print "Set-Cookie: " . $newcookie . "\n";  $iwashere = 2;
       }
       elsif ( $whatis{'action'} eq 'login' ) {
          if ( $whatis{'userpwd'} eq $userpwd{$whatis{'email'}} && $whatis{'userpwd'} ne '' ) {
              $ccUserNumber = $usernumber{$whatis{'email'}};
              if($ccUserNumber > 0 ) { $gotusrid = $ccUserNumber; }
              else{$gotusrid = 0;}
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