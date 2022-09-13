<form action="logout.php">
        <button> Logout</button>
    </form>
    <?php include "../inc/dbinfo.inc"; ?>
<?php
if ( !isset($_SESSION) ) session_start();

if(! isset($_SESSION["user"]))
{
    header("Location: index.php");
}

if($_SESSION["user"]!="admin")
{
    header("Location: index.php");
}

function TableExists($tableName, $connection, $dbName) {
  $t = mysqli_real_escape_string($connection, $tableName);
  $d = mysqli_real_escape_string($connection, $dbName);

  $checktable = mysqli_query($connection,
      "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_NAME = '$t' AND TABLE_SCHEMA = '$d'");

  if(mysqli_num_rows($checktable) > 0) return true;

  return false;
}



// Create connection

$conn = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
    
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

        if(!TableExists("feedback", $conn, DB_DATABASE))
        {
            $query = "CREATE TABLE feedback (
                feedback VARCHAR(90) 
            )";

            if(!mysqli_query($connection, $query)) 
            {
                echo("<p>Error creating table.</p>");
                exit();
            }
        }


?>
<table border="1" cellpadding="2" cellspacing="2">
  <tr>
    <td>UserName</td>
    <td>Feedback</td>
  </tr>

<?php

$result = mysqli_query($conn, "SELECT * FROM feedback");

while($query_data = mysqli_fetch_row($result)) {
  echo "<tr>";
  echo "<td>",$query_data[0], "</td>",
       "<td>",$query_data[1], "</td>";
       
  echo "</tr>";
}
mysqli_close($conn);
?>


</table>
