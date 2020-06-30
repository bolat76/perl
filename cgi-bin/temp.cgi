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
        if($cookiekey =~ /socialliftproject/){$gotcookie = $hotcookie; }
    }
#$gotcookie = $ENV{'HTTP_COOKIE'};
$cookie_file = '../../oedata/sl_cookies.txt';
$users_file = '../../oedata/sl_usrdata.txt';
###################### end of cookie part #########################
$oe_folder = '../../oedata/';
$sl_log_folder = '../../oedata/logs/';
$slTempData_file = $oe_folder . 'sl_tempdata.txt';
$slBallData_file = $oe_folder . 'sl_balls.txt';
$bas = $oe_folder  . 'basl.txt';
$end = $oe_folder . 'endsl.txt';
$indexcgi = 'lift.cgi';
$httpindexcgi = 'http://alteginber.kz/cgi-bin/' . $indexcgi;
$title = 'Lift';

open(INF, $slBallData_file); 
@slBallData_list = <INF>;
close(INF);
foreach $i(@slBallData_list){
    chomp($i); #3<tab>300000<tab>Tue Jul 2 14:16:01 2019<tab>reserve
    #$tslusernum<tab>$tsluserball<tab>$tslballtime<tab>$rest
    ($tslusernum, $tsluserball, $tslballtime, @other) = split (/<tab>/, $i);
    $slGlobalUserBalls{$tslusernum} = $tsluserball;
    $slGlobalUserBallsTime{$tslusernum} = $tslballtime;
}

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
          #1<tab>user1<tab>6<tab>777<tab>email<tab>13.03.2013<tab>rest
          #$usernum<tab>$username<tab>$userlevel<tab>$userpwd<tab>$useremail<tab>$other
          ($tusrnum, $tusrnam, $tusrlvl, $tusrpwd, $tusreml, @other) = split (/<tab>/, $i);
          $username{$tusrnum} = $tusrnam; $userpwd{$tusrnum} = $tusrpwd; $usereml{$tusrnum} = $tusreml;  
          $userEmailExist{$tusreml} = 1;  $username{$tusreml} = $tusrnam; $userpwd{$tusreml} = $tusrpwd;
          ($userfirstname{$tusrnum}, $userlastname{$tusrnum}) = split(/ /, $tusrnam);
          $userlevel{$tusrnum} = $tusrlvl; $usernumber{$tusrnum} = $tusrnum; $usernumber{$tusreml} = $tusrnum;
          $usernumber{$tusrnam} = $tusrnum;   $userslist++;    push(@loginuserslist, $tusrnam);
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
&checkcookies();
print "\n";
&printfile($bas, $title);


#####################################################################################
############################# LOGIN CHECK PART ######################################
#####################################################################################
print "<p> </p>";


#####################################################################################
########################### START MAIN BODY #########################################
#####################################################################################

&printfile($end, $title);
##################################################################################################################
######################################### Sub homePageSub ########################################################
##################################################################################################################
sub homePageSub {

    #$slGlobalUserBalls{$tslusernum} = $tsluserball;    $slGlobalUserBallsTime{$tslusernum} = $tslballtime;
    print "<p>Привет $username{$gotusrid},<br> Ваш системный номер: [$gotusrid] и у Вас [$slGlobalUserBalls{$gotusrid}] баллов Лифт</p>\n";
    $hpsLogId = $yearnow . '.' . $ai{$monthnow};    &checkLogFileSub($hpsLogId);  $hpsListLen = scalar @clfGlobList;  $myclr = $yelclr;   $cnt = 1;
    if($hpsListLen > 0){
        print "<table><caption>История транзакций за определенное время</caption><tr $myclr><td>№</td><td>Пользователь переслал баллы</td>
        <td>количество баллов</td><td>Пользователь получил баллы</td><td>Времы транзакции</td></tr>\n";
        foreach $i(@clfGlobList){
            chomp($i); #3<tab>3000<tab>2<tab>Tue Jul 2 14:16:01 2019<tab>reserve
            #$tllusernumfrom<tab>$tlluserball<tab>$tllusernumto<tab>$tlltransfertime<tab>$rest
            ($tllusernumfrom, $tlluserball, $tllusernumto, $tlltransfertime, @other) = split (/<tab>/, $i);
            if($myclr eq $yelclr){$myclr = $yelclr1;}  else{$myclr = $yelclr;}
            print "<tr $myclr><td>$cnt</td><td>$username{$tllusernumfrom} [$tllusernumfrom]</td><td>$tlluserball</td>
            <td>$username{$tllusernumto} [$tllusernumto]</td>$tlltransfertime<td></td></tr>\n";     $cnt++;
        }
        print "</table>\n";
    }

}
##################################################################################################################
####################################### Sub openSendFormSub ######################################################
##################################################################################################################
sub openSendFormSub {

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
          $newcookie = "socialliftproject\=999999\_$newUsrRegRndNum\_desktop\; expires=$live_time\; path=/\;";
          print "Set-Cookie: " . $newcookie . "\n";  return;
    }
    if($gotcookie =~ /socialliftproject/ && $whatis{'action'} ne 'logout' && $whatis{'action'} ne 'login'){  $iwashere = 1;
       if($oeusercookiernd{$gcusrnum} eq $gcusrrnd){
            if ( $userlevel{$gcusrnum} < 10 ){
                $userlogged = 1;   $gotusrid = $gcusrnum;
                $newcookie = "socialliftproject\=$gcusrnum\_$gcusrrnd\_$gcusrbrowser\; expires=$live_time\; path=/\;";
                print "Set-Cookie: " . $newcookie . "\n";
            }
       }
       else{$errorlogin = "$rf $b1 User not identified or no permission to access! $b2 $f2";}
    } #$userEmailExist{$tusreml} = 1;  $username{$tusreml} = $tusrnam; $userpwd{$tusreml} = $tusrpwd; $usernumber{$tusreml} = $tusrnum;
    elsif($whatis{'action'} eq 'login' || $whatis{'action'} eq 'logout'){
        if($whatis{'action'} eq 'logout'){
            $userlogged = 0;   $gotusrid = $gcusrnum;     $oeusercookiernd{$gotusrid} = '1234567890';
            $oeusercookiedate{$gotusrid} = $timedatenow;  $oeusercookieip{$gotusrid} = $userip;
            $newcookie = "socialliftproject=0_1234567890_desktop\; expires=$live_time\; path=/\;";
            print "Set-Cookie: " . $newcookie . "\n";  $iwashere = 2;
        }
        elsif($whatis{'action'} eq 'login'){
            if($whatis{'userpwd'} eq $userpwd{$whatis{'email'}} && $whatis{'userpwd'} ne ''){
                  $whatis{'usernamenumber'} = $usernumber{$whatis{'email'}};
                  if($userlevel{$whatis{'usernamenumber'}} < 10 ){
                      if($whatis{'usernamenumber'} > 0){$gotusrid = $whatis{'usernamenumber'};}
                      else{$gotusrid = 0;}
                      $randnum = int(rand(10)*1000000000000);       $oeusercookiernd{$gotusrid} = $randnum;
                      $oeusercookiedate{$gotusrid} = $timedatenow;  $oeusercookieip{$gotusrid} = $userip;
                      $newcookie = "socialliftproject\=$gotusrid\_$randnum\_desktop\; expires=$live_time\; path=/\;";
                      print "Set-Cookie: " . $newcookie . "\n";       $userlogged = 1;    $iwashere = 3;
                      $ccDataLine = "$gotusrid<tab>$randnum<tab>$timedatenow<tab>$userip<tab>desktop";
                  }  
            }
            else{$errorlogin = "$rf $b1 Wrong email or password! $b2 $f2";}
        }
        else{$errorlogin = "$rf $b1 Login error! Try again... $b2 $f2";}
        $cnt = 999999;
        open(INF, $cookie_file); @cookie_list = <INF>; close(INF);
        foreach $i (@cookie_list){
            chomp($i);
            if($i =~ /$usernumber{$whatis{'email'}}/){ $donothing = 1; }
            else { push(@ccNewCookieList, $i); }
        }
        open(D,">$cookie_file");
        foreach $i (@ccNewCookieList){ print D "$i\n"; }
        print D "$ccDataLine\n";
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