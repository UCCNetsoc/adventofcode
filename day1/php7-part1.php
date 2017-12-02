<?php

$file = file_get_contents( 'd1.in' );
$lines = explode("\n", $file);

foreach ($lines as $input) {
  $stringlen = (int) strlen($input);
  // If empty string, continue on
  if ($stringlen == 0){ continue; }

  $sum = 0;
  for ($i=0; $i <= $stringlen; $i++) {
    $index = (($i + 1) % $stringlen);
    $number = (int) $input[ $index ];
    if( $number == $input[$i] ){
      $sum += $number;
    }
  }
  echo "{$sum} \n";
}
