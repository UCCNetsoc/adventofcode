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
        // For each number, look forward in the list for something that
        // it can divide into or be divided by evenly
        $next = (int) $numberList[$j];
        if ( in_array(0, [($number % $next), ($next % $number)] ) ){
          $sum += ($number > $next) ? ($number / $next) : ($next / $number);
          // Break out of the entire line
          break 2;
        }
      }
    }
  }
}

echo $sum ."\n";
