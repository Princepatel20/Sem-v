<?php

$servername = "localhost";

$username = "root";

$password = "";

$dbname = "employee";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {

die("Connection failed: " . $conn->connect_error);}

if (isset($_GET['id'])) {

$employeeId = $_GET['id'];

$sql = "SELECT * FROM MyGuests WHERE id = $employeeId";

$result = $conn->query($sql);

if ($result->num_rows == 1)

{

$row = $result->fetch_assoc();

echo "<h3>Update Employee Details</h3>";

echo "<form method='post' action='update_employee.php?id=$employeeId'>";
  echo "Employee Name: <input type='text' name='employee_name'

value='{$row['emp_name']}'><br>";

echo "Birthdate: <input type='date' name='birthdate'

value='{$row['emp_birthdate']}'><br>";

echo "<input type='submit' name='update' value='Update'>";

echo "</form>";

if (isset($_POST['update'])) {

// Update the employee details in the database

$newName = $_POST['employee_name'];

$newBirthdate = $_POST['birthdate'];

$updateSql = "UPDATE MyGuests SET emp_name = '$newName', emp_birthdate =

'$newBirthdate' WHERE id = $employeeId";

if ($conn->query($updateSql) === TRUE) {

echo "Record updated successfully.";

} else {

echo "Error updating record: " . $conn->error;

} }

} else {

echo "Employee not found or multiple records found with the same ID."; }}

?>
