
<?php 
        if ( !isset($_SESSION) ) session_start();

        if(isset($_SESSION["user"]))
        {
            header("Location: customerhome.php");
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

	    	<div class="d-flex justify-content-center align-items-center ">
	    		<div class="row">
	    			<div class="col-sm-4">
	    				<h3><b>LOGIN</b></h3>
	    			    <hr>
	    			</div>
	    		</div>
	    		<div class="row">
	    		
	    			<div class="col-sm-4">
                    <?php 

                            if(isset($_SESSION["error"]))
                            {
                                echo "<p class=\"text-danger\">",$_SESSION["error"],"</p>" ;
                                unset($_SESSION["error"]);
                            }
                            


                    ?>

	    				
	    				<form action = "authentication.php"  method = "POST">
							UserName  : <input autocomplete="off" class="form-control" type="text" name="user" required="">
							<br><br>

							Password  : <input autocomplete="off" class="form-control" type="password" name="pass" required="">
							<br><br>
							
							<button class="btn btn-primary"><span class="glyphicon glyphicon-log-in"></span> Login</button>
				        </form>
	    			</div>
	    		
	    	    </div>
	    		
	    	</div>
    	
        </div>

       
		



	
 
</body>  
</html>  