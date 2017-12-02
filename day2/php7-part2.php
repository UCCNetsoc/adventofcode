<?php

$file = file_get_contents('d2.in');
$lines = explode(PHP_EOL, $file);

$sum = 0;
foreach ($lines as $line) {
  // $numberList = explode(" ", $line); // For test input
  $numberList = explode("\t", $line);   // For solution input

  if( !empty( $numberList ) ){
    for ($i=0; $i < count($numberList); $i++) {
      $number = (int) $numberList[$i];
      for ($j = $i + 1; $j < count($numberList); $j++) {
        $next = (int) $numberList[$j];
        if( ($number % $next) == 0 || ($next % $number) == 0){
          $sum += ($number > $next) ? $number / $next : $next / $number;
          break 2;
        }
      }
    }
  }
}

echo $sum ."\n";
