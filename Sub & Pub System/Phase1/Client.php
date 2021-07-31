<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Submit The Code</title>
</head>

<body>
    <h1>Enter your python code below</h1>
    <div>
        <form method="post">
            <textarea name="content" cols="50" rows="20"></textarea>
            <input type="submit" name="submit" value="Running">
        </form>
    </div>

    <?php


    if(isset($_POST['submit'])){
        $content = $_POST['content']; //Get the code from html after click submit.

        $myfile = fopen("testfile.py", "w") or die("Unable to open file"); //Open testfile.py

        fwrite($myfile,$content);  //Write code into testfile.py file

        fclose($myfile);  //Close testfile.py file

        $result = shell_exec('/usr/local/bin/docker build -t pythonCode .'); //Run command line that call docker build image for testfile.py python code

        $result2 = shell_exec('/usr/local/bin/docker run pythonCode'); //Call command line that run image and get result of python code save to $result2

        if($result2 != ""){
            echo "The Running Result : ";
            echo $result2;
        } // If code result is not empty then show code result in the website.
        else{
            echo "Please check your code correctly"; //else return error message
        }
    }

    ?>
</body>
</html>
