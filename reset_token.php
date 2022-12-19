<?php
$key = $_GET['key'];
$is_found = false;
foreach(scandir("tokens") as $t){
    $token = fopen("tokens/$t",'r');
    if(fread($token,filesize("tokens/$t")) == $key){
        fclose($token);
        fopen("keys/$key.txt",'a');
        unlink("tokens/$t");
        $is_found = true;
    }
}
if($is_found == true){
    echo "done";
}else{
    echo "error";
}
?>