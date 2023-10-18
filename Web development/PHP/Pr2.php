<?php

// Function to calculate the sum of an array

function calculateSum($arr) {

 return array_sum($arr);

}

// Function to calculate the average of an array

function calculateAverage($arr) {

 if (count($arr) === 0) {

 return 0;

 }

 return array_sum($arr) / count($arr);

}

// Function to find the maximum value in an array

function findMax($arr) {

 if (count($arr) === 0) {

 return null;

 }

 return max($arr);

}

// Sample array of numbers

$numbers = [10, 20, 30, 40, 50];
// Display the array

echo "Array: " . implode(', ', $numbers) ;

// Calculate sum

$sum = calculateSum($numbers);

echo "\nSum: $sum\n";

// Calculate average

$average = calculateAverage($numbers);

echo "Average: $average";

// Find the maximum value

$maxValue = findMax($numbers);

echo "\nMaximum Value: $maxValue";

?>
