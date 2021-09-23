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
            
            </div>
    
           
            
    
    
    
        
     
    </body>  
    </html>  