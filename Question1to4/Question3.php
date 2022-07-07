<?php
$num = 16;
if ($num %2 == 0){
    echo("Please insert odd number by changing it inside the file variable called num");
}else {
     for ($x=1; $x <=$num; $x++){
         if ($x%2 != 0) {
            for ($k=$num; $k >= $x ;$k--){
             echo "*";             
            }
            print("\n");
         }
     }
    }