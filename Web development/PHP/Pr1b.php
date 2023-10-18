<?php

// Function to swap two numbers

function swapNumbers(&$a, &$b) {

 $temp = $a;

 $a = $b;

 $b = $temp;

}

// Initial values of the numbers

$num1 = 10;

$num2 = 20;

echo "Before swapping: num1 = $num1, num2 = $num2 ";

// Swapping the numbers

swapNumbers($num1, $num2);

echo "\n After swapping: num1 = $num1, num2 = $num2";

?>
