<html>
<body>

<form method="post" action="util.php">
<!--Hostnames:<input type="text"  name="hostnames">-->
<textarea rows="20" cols="36" id="hostnames" name="hostnames"></textarea>
<input type="submit" />
</form>


<?php
//foreach ($_POST as $item) 
//foreach ($_POST as $item) 
//echo htmlspecialchars($_POST['hostnames']);
$hostnames = $_POST['hostnames'];
//$hostname = explode("\r", $hostnames);
//$hostname = explode("\n", $hostnames);
$hostname = explode("\r\n", $hostnames);
//$hostname = explode(PHP_EOL, $hostnames);

foreach ($hostname as $value) 
{
	//echo "$value <br>";
	$value=preg_replace('/\s+/', '', $value);
	$ip = gethostbyname($value);
	echo "$ip <br>";
}

?>



</body>
</html>
