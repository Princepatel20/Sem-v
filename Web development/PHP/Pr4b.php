class Employee {
    public $name;
    public $id;
    public $salary;
    public $department;

    public function __construct($name, $id, $salary, $department) {
        $this->name = $name;
        $this->id = $id;
        $this->salary = $salary;
        $this->department = $department;
    }

    public function accept_details() {
        $this->name = readline("Enter employee name: ");
        $this->id = readline("Enter employee ID: ");
        $this->salary = readline("Enter employee salary: ");
        $this->department = readline("Enter employee department: ");
    }

    public function print_details() {
        echo "Name: " . $this->name . "\n";
        echo "ID: " . $this->id . "\n";
        echo "Salary: " . $this->salary . "\n";
        echo "Department: " . $this->department . "\n";
    }
}
