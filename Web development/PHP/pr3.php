<!DOCTYPR html>
<html>
<body>
<?php

interface Shape {
  public function area($a,$b);
}

class circle implements shape {
  public function area($r,$b=0) {
    echo $r*$r*3.14;
    echo "<br>";
  }
}
class rectangle implements shape
  {
    public function area ($a,$b)
    {
      echo $a*$b;
    }
  }

echo "Hello world";
?>
</body>
</html>
