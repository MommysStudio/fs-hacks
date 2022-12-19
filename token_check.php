<?php
$token = $_GET['token'];
if(file_exists("tokens/$token.txt")){
    echo "ok";
}else{
    echo "not ok";
}
?>