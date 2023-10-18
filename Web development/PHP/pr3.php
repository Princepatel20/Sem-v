<?php

class Dakota {

public function add($n1, $n2) {

return $n1 + $n2;}

public function sub($n1, $n2) {

return $n1 - $n2;}}

$DakotaObj = new Dakota();

$result = $DakotaObj->add(10, 30);

$result_sub = $DakotaObj->sub(60, 10);
echo "The sum is: " . $result;

echo "<br>";

echo "The sub is: ".$result_sub;

?>
