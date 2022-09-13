<?php include "../inc/dbinfo.inc"; ?>
<?php
if ( !isset($_SESSION) ) session_start();

function TableExists($tableName, $connection, $dbName) {
  $t = mysqli_real_escape_string($connection, $tableName);
  $d = mysqli_real_escape_string($connection, $dbName);

  $checktable = mysqli_query($connection,
      "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_NAME = '$t' AND TABLE_SCHEMA = '$d'");

  if(mysqli_num_rows($checktable) > 0) return true;

  return false;
}

// error_reporting(E_ERROR | E_PARSE);


// Create connection
$conn = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
    
$data = $_POST["complaint"];

print_r($_POST);



// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

        if(!TableExists("feedback", $conn, DB_DATABASE))
        {
            $query = "CREATE TABLE feedback (
                username VARCHAR(30),
                feedback VARCHAR(90) 
            )";

            if(!mysqli_query($conn, $query)) 
            {
                echo("<p>Error creating table.</p>");
                exit();
            }
        }

$user = $_SESSION["user"];
$sql = "INSERT INTO feedback (username,feedback)
VALUES ('$user','$data')";

if (mysqli_query($conn, $sql)) {
  $_SESSION["s"] = "Recorded Successfully";
  
} else {
  $_SESSION["us"] = "ERROR";
 
}
mysqli_close($conn);

header("Location: customerhome.php");

?>