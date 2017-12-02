<?php

$file = file_get_contents('d2.in');
$lines = explode(PHP_EOL, $file);

$sum = 0;
foreach ($lines as $line) {
  // $numberList = explode(" ", $line); // For test input
  $numberList = explode("\t", $line);   // For solution input

  if( !empty( $numberList ) ){
    // Init min and max to first item
    $max = $min = (int) $numberList[0];
    foreach ($numberList as $number) {
      $max = ($number > $max) ? (int) $number : $max;
      $min = ($number < $min) ? (int) $number : $min;
    }
    // Add the difference to the sum
    $sum += $max - $min;
  }
}

echo $sum ."\n";
