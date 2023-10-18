<!DOCTYPE html>

<html>

<head>

<title>Simple Interest Calculator</title>

</head>

<body>

<h1>Simple Interest Calculator</h1>

<form method="post" action="<?php echo $_SERVER["PHP_SELF"]; ?>">

<label for="loanAmount">Loan Amount:</label>

<input type="number" name="loanAmount" required><br>

<label for="interestRate">Rate of Interest (%):</label>

<input type="number" name="interestRate" required><br>

<label for="years">Number of Years:</label>

<input type="number" name="years" required><br>

<input type="submit" value="Calculate">

</form>

<?php

function calculateSimpleInterest($loanAmount, $interestRate, $years) {

$simpleInterest = ($loanAmount * $interestRate * $years) / 100;

return $simpleInterest;

}

if ($_SERVER["REQUEST_METHOD"] == "POST") {

$loanAmount = $_POST["loanAmount"];

$interestRate = $_POST["interestRate"];

$years = $_POST["years"];

if (!empty($loanAmount) && !empty($interestRate) && !empty($years)) {

$simpleInterest = calculateSimpleInterest($loanAmount, $interestRate, $years);

echo "Loan Amount: $" . $loanAmount . "<br>";

echo "Rate of Interest: " . $interestRate . "%<br>";

echo "Number of Years: " . $years . "<br>";

echo "Simple Interest: $" . $simpleInterest;

} else {

echo "Please fill in all fields.";
    }

}

?>

</body>

</html>
