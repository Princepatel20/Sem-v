<!DOCTYPE html>

<html lang="en">

<head>

 <meta charset="UTF-8">

 <meta name="viewport" content="width=device-width, initial-scale=1.0">

 <title>Employee Registration Form</title>

</head>

<body>

 <h1>Employee Registration Form</h1>

 <form action="process_registration.php" method="POST">

 <label for="employeeName">Employee Name:</label>

 <input type="text" id="employeeName" name="employeeName" required><br><br>

 <label for="birthdate">Birthdate:</label>

 <input type="date" id="birthdate" name="birthdate" required><br><br>
<label for="joiningDate">Joining Date:</label>

 <input type="date" id="joiningDate" name="joiningDate" required><br><br>

 <label for="salary">Salary:</label>

 <input type="number" id="salary" name="salary" required><br><br>

 <label for="designation">Designation:</label>

 <input type="text" id="designation" name="designation" required><br><br>

 <label for="email">Email:</label>

 <input type="email" id="email" name="email" required><br><br>

 <label for="areaOfInterest">Area of Interest:</label>

 <textarea id="areaOfInterest" name="areaOfInterest" rows="4" cols="50" 

required></textarea><br><br>

 <label for="contactNumber">Contact Number:</label>

 <input type="tel" id="contactNumber" name="contactNumber" required><br><br>

 <input type="submit" value="Register">

 </form>

</body>

</html>
