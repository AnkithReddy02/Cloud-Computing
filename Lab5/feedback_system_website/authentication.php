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
    $conn = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
    if(mysqli_connect_errno()) {
        die("Failed to connect with MySQL: ". mysqli_connect_error());
    }
    $username = $_POST['user'];
    echo($username);
    $password = $_POST['pass'];

        //to prevent from mysqli injection
        $username = stripcslashes($username);
        $password = stripcslashes($password);
        $username = mysqli_real_escape_string($conn, $username);
        $password = mysqli_real_escape_string($conn, $password);

        if(!TableExists("login", $conn, DB_DATABASE))
        {
            $query = "CREATE TABLE login (
                username VARCHAR(15) PRIMARY KEY,
                password VARCHAR(15)
            )";

            if(!mysqli_query($conn, $query)) 
            {
                echo("<p>Error creating table.</p>");
            }

            $query = "insert into login values('admin','admin')";

            if(!mysqli_query($conn, $query)) 
            {
                echo("<p>Error creating 1.</p>");
            }

            $query = "insert into login values('ankith02','ankith02')";

            if(!mysqli_query($conn, $query)) 
            {
                echo("<p>Error creating 2.</p>");
            }

            $query = "insert into login values('joe3','joe3')";

            if(!mysqli_query($conn, $query)) 
            {
                echo("<p>Error creating 3.</p>");
            }
        }

        $sql = "select *from login where username = '$username' and password = '$password'";
        $result = mysqli_query($conn, $sql);
        $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
        $count = mysqli_num_rows($result);

        mysqli_close($conn);

        if($count == 1){
          
          $username = strtolower($username);
          $_SESSION['user'] = $username;
          if($username == "admin"){
            header("Location: feedback.php");
          }
          else{
            header("Location: customerhome.php");
          }
        }
        else{
            $_SESSION["error"] = "Invalid Credentials";
            header("Location: index.php");

        }
?>