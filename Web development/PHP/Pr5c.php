<?php

$servername = "localhost";

$username = "root"; // Replace with your MySQL username

$password = ""; // Replace with your MySQL password

$dbname = "Employee"; // Replace with your database name

$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection

if ($conn->connect_error) {

 die("Connection failed: " . $conn->connect_error);

}

// Retrieve employee data from the database

$sql = "SELECT * FROM emp";

$result = mysqli_query($conn, $sql);

$check = mysqli_num_rows($result);

if ($check > 0) {

 echo "<table border='1'>

 <tr>

 <th>Employee ID</th>

 <th>Employee Name</th>

 <th>Salary</th>

 <th>Designation</th>

 <th>Email</th>

 <th>Area of Interest</th>
 <th>Contact Number</th>

 </tr>";

 while ($row = mysqli_fetch_assoc($result)) {

 echo "<tr>

 <td>{$row['emp_Id']}</td>

 <td>{$row['Name']}</td>

 <td>{$row['salary']}</td>

 <td>{$row['designation']}</td>

 <td>{$row['email']}</td>

 <td>{$row['area']}</td>

 <td>{$row['contact']}</td>

 </tr>";

 }

 echo "</table>";

} else {

 echo "No employee records found.";

}

$conn->close();

?>
