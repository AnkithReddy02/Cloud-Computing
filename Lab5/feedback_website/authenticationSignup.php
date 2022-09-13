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

        $sql = "select * from login where username = '$username'";
        $result = mysqli_query($conn, $sql);
        $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
        $count = mysqli_num_rows($result);
        
        mysqli_close($conn);

        if($count == 1)
        {
            $_SESSION["error"] = "Username already exists";
            header("Location: index.php");
          
        }
        else
        {
            
            $conn = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
            $sql = "insert into login values('$username', '$password')";
            $result = mysqli_query($conn, $sql);

            $username = strtolower($username);
            $_SESSION['user'] = $username;
            if($username == "admin"){
                header("Location: feedback.php");
            }
            else{
                header("Location: customerhome.php");
            }

        }
?>