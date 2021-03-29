 <?php
 $afternoon="Good afternoon";
 $evening="Good evening";
 $late="Working late?";
 $morning="Good morning";
 $friday="Get ready for weekend!";
 $current_time=date('G');
 $current_day=date('I');
 if($current_time>=12 && $current_time<=16)
 {
     echo $afternoon;
 }
 elseif($current_time>=17 && $current_time<=24)
 {
     echo $evening;
     
 }
 elseif($current_time>=1 && $current_time<=5)
 {
     echo $late;
 }
 elseif($current_time>=6 && $current_time<=11)
 {
     echo $morning;
 }
 if($current_day=="friday")
 {
     echo $friday;
 }
 ?>
 
