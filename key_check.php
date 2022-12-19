<?php
$key = $_GET['key'];
$final = '';
$is_correct = false;
if(file_exists("keys/$key.txt")){
    $is_correct = true;
}else{
    echo 'not ok';
    $is_correct = false;
}
if($is_correct == true){
    $step = 1;
    $tings = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    while(true){
        $final = $final.$tings[rand(1,strlen($tings) - 1)];
        $step = $step+1;
        if($step == 100){
            break;
        }
    }
    $token = fopen("tokens/$final.txt",'a+');
    fwrite($token,$key);
    fclose($token);
    unlink("keys/$key.txt");
    echo $final;
}
?>