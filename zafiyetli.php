<?php
if(isset($_GET['Submit'])){
$id = $_GET['id'];
$getusername = "SELECT username FROM users WHERE userid = '$id'";
$result = mysql_query($getusername) or die(mysql_error());
$num = mysql_numrows($result);
$i = 0;
while ($i < $num) {
$username = mysql_result($result,$i);
$html .= '<pre>';
$html .= 'Username: ' . username;
$html .= '<pre>';
$i++;
}
}
?>