<!DOCTYPE html>
<html>
<body>

<?php
$GenRanNumb = rand(1,100000);
$Number = array(" Number "=> $GenRanNumb);
echo json_encode($Number);
?>

</body>
</html>