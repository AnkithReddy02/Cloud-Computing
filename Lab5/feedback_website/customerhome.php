<?php include "../inc/dbinfo.inc"; ?>

<?php 
if ( !isset($_SESSION) ) session_start();

if(! isset($_SESSION["user"]))
{
    header("Location: index.php");
}

if($_SESSION["user"]=="admin")
{
    header("Location: feedback.php");
}

?>

<html>
    <head>
        
    
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
          <script src='https://kit.fontawesome.com/a076d05399.js' crossorigin='anonymous'></script>
          <!-- <a class="navbar-brand" href=""><i class="glyphicon glyphicon-home"></i>  Real-Estate</a> -->
    
    </head>  
    <body>  
    
    
            
    
            
            
            <br><br>
    
            <div class="container">

                <form action="logout.php">
                    <button> Logout</button>
                </form>
    
                <div class="d-flex justify-content-center align-items-center ">
                    <div class="row">
                        <div class="col-sm-4">
                            <h3><b>COMPLAINT PORTAL</b></h3>
                            <hr>
                        </div>
                    </div>
                    <div class="row">
                    
                        <div class="col-sm-4">

                            <?php
                                if(isset($_SESSION["s"]))
                                {
                                    echo "<p class=\"text-success\">",$_SESSION["s"],"</p>" ;
                                    unset($_SESSION["s"]);
                                }
                                if(isset($_SESSION["us"]))
                                {
                                    echo "<p class=\"text-danger\">",$_SESSION["us"],"</p>" ;
                                    unset($_SESSION["us"]);
                                }
                            ?>
                            
                            <form action = "customer.php"  method = "post">
                                Enter Complaint  : <input autocomplete="off" class="form-control" type="text" name="complaint" required="">
                                <br><br>
    
                               
                                
                                <button class="btn btn-primary">submit</button>
                            </form>
                        </div>
                    
                    </div>
                    
                </div>
                <?php
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

                       


                ?>
                <br>
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

            
            </div>
    
           
            
    
    
    
        
     
    </body>  
    </html>  