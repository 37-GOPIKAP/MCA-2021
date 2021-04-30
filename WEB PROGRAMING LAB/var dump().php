Var_dump.php
<html>
<head>
<title>
Variable Function:var_dump()
</title>
</head>
<body>
<?php
$val1 = 678;
$val2 = "a678";
$val3 = "678";
$val4 = "BetterThanLike.com";
$val5 = 698.99;
$val6 = +125689.66;
echo var_dump($val1)."<br>";
echo var_dump($val2)."<br>";
echo var_dump($val3)."<br>";
echo var_dump($val4)."<br>";
echo var_dump($val5)."<br>";
echo var_dump($val6)."<br>";
 ?>
</body>
</html>

Substr.php


<html>
<head>
<title> String Function: Substr():3 </title>
</head>
<body>
<?php
echo substr("Bipin R. Prajapati",0,1)."<br/>";
echo substr("Bipin R. Prajapati",1,3)."<br/>";
echo substr("Bipin R. Prajapati",5,2)."<br/>";
echo substr("Bipin R. Prajapati",8,9)."<br/>";
echo substr("Bipin R. Prajapati",-3,3)."<br/>";
echo substr("Bipin R. Prajapati",-9,-3)."<br/>";
echo substr("Bipin R. Prajapati",1,-10)."<br/>";
 ?>
</body>
</html>



Strcmp.php


<html>
<head><title> String Function:strcmp() </title></head>
<body>
<?php
$str1 = 'a';
$str2 = 'b';
echo strcmp($str1, $str2)."<br/>";
$str3 = 'b';
$str4 = 'a';
echo strcmp($str3, $str4)."<br/>";
$str5 = "Anil";
$str6 = "anil";
echo strcmp($str5, $str6)."<br/>";
 ?>
</body></html>




 
Strpos.php



<html>
<head>
<title> String Function:strpos():2 </title>
</head>
<body>
<?php
$string = "I am anil";
$pos = strpos($string,"i");
 if($pos === false)
 {
echo "Not found.";
 }
 else
 {
echo "Found at $pos. .!";
 }
 ?>
</body></html>















 















