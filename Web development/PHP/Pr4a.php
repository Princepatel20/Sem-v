function calculateSimpleInterest($principal, $interestRate, $years) {
  $interest = $principal * $interestRate * $years / 100;
  echo "The simple interest is: " . $interest;
}

// Get input from user
$principal = readline("Enter principal amount: ");
$interestRate = readline("Enter annual interest rate (%): "); 
$years = readline("Enter number of years: ");

// Calculate simple interest
calculateSimpleInterest($principal, $interestRate, $years);
