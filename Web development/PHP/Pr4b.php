
<?php
class Employee {
    private $name;
    private $designation;
    
    public function acceptDetails() {
        echo "Enter employee name: ";
        $this->name = readline();
        
        echo "Enter employee designation: ";
        $this->designation = readline();
    }
    
    public function printDetails() {
        echo "Employee Details:\n";
        echo "Name: ".$this->name."\n";
        echo "Designation: ".$this->designation."\n";
    }
}

// Creating an object of the Employee class
$employee = new Employee();

// Accepting the details
$employee->acceptDetails();

// Printing the details
$employee->printDetails();
?>

