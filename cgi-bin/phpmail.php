<?php
// the message
$msg = "Hello!\n Please enter the number: 567456745645645\n Best regards,\n Open English team";
$headers = "From: noreply@accelerator.kvadra.kz" . "\r\n";
$rr = mail("b.jaidarinov@gmail.com","Registration email confirmation",$msg, $headers);
//print_r(error_get_last());
//print_r($rr);
//var_dump($rr);
?>
<html><body>Email had been sent successsfully!</body></html>