<?php
session_start();
// Generate a random 6-digit OTP
function generateOTP() {
 return str_pad(rand(0, 999999), 6, '0', STR_PAD_LEFT);
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
 $email = $_POST['email'];
 $otp = generateOTP();
 // Store OTP in the session
 $_SESSION['otp'] = $otp;
 // Send the OTP to the user's email (in a real application, you would send an email here)
 echo "An OTP has been sent to your email: $otp";
}
if (isset($_POST['verify'])) {
  $enteredOTP = $_POST['enteredOTP'];
 if ($_SESSION['otp'] === $enteredOTP) {
 echo "OTP verified successfully. User is now verified!";
 // Mark the user as verified in the database (in a real application)
 } else {
 echo "Invalid OTP. Please try again.";
 }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>User Registration and Verification</title>
</head>
<body>
 <h1>User Registration</h1>
 <form action="" method="POST">
 <label for="email">Email:</label>
 <input type="email" id="email" name="email" required><br><br>
 <input type="submit" value="Send OTP">
 </form>
<h2>Verify OTP</h2>
 <form action="" method="POST">
 <label for="enteredOTP">Enter OTP:</label>
 <input type="text" id="enteredOTP" name="enteredOTP" required><br><br>
 <input type="submit" name="verify" value="Verify OTP">
 </form>
</body>
</html>
