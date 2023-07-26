
<?php
// Create an array of persons with IDs and names
$persons = array(
    array("id" => 101, "name" => "John"),
    array("id" => 104, "name" => "Alice"),
    array("id" => 103, "name" => "Bob"),
    array("id" => 102, "name" => "Charlie")
);

// Sort the array in ascending order based on IDs
usort($persons, function($a, $b) {
    return $a['id'] <=> $b['id'];
});

// Change the name where ID is 103
foreach ($persons as &$person) {
    if ($person['id'] == 103) {
        $person['name'] = "David";
    }
}

// Print the array in tabular format
echo "<table>\n";
echo "<tr><th>ID</th><th>Name</th></tr>\n";
foreach ($persons as $person) {
    echo "<tr>";
    echo "<td>".$person['id']."</td>";
    echo "<td>".$person['name']."</td>";
    echo "</tr>\n";
}
echo "</table>";
?>

