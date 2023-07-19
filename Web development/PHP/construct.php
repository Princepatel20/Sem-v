<?php

class Employee
{
	
	Public $name;

	Public $position;

	function __construct($name,$position)

	{

		$this->name=$name;
		$this->position=$position;


	}	
	function show_details()
	{
		echo $this->name." : ";
		echo "Your position is ".$this->position."\n";
	}
}
	
$employee_obj= new Employee("raj","developer");
$employee_obj->show_details();
	
$employee2= new Employee("Vikas","Manager");
$employee2->show_details();

?>
