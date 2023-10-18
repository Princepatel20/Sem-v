<?php
If(isset($_POST)){
$id = $_POST['employeeName'];
$salary = $_POST['salary'];
$designation = $_POST['designation'];
$email = $_POST['email'];
$areaOfInterest = $_POST['areaOfInterest'];
$contactNumber = $_POST['contactNumber'];
}
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "Employee";
// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
die("Connection failed: " . mysqli_connect_error());
}
$sql = "INSERT INTO emp (emp_Id,salary,designation,email,area,contact)
VALUES ('$id','$salary','$designation','$email','$areaOfInterest','$contactNumber')";
