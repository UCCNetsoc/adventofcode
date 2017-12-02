<?php

$file = file_get_contents( 'd1.in' );
$lines = explode("\n", $file);

foreach ($lines as $input) {
  $stringlen = (int) strlen($input);
  // If empty string, continue on
  if ($stringlen == 0){ continue; }

  $sum = 0;
  $last = -1;
  for ($i=0; $i < $stringlen + 1; $i++) {
    $index = ($i % $stringlen);
    $number = (int) $input[ $index ];
    if( $number == $last ){
      $sum += $number;
    }

    $last = $number;
  }
  echo "{$sum} \n";
}
