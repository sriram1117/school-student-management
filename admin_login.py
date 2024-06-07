#!C:\Users\aasho\AppData\Local\Programs\Python\Python310\python.exe
print("content-type:text/html \r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Login</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <script>
        var uname, pass;

        function validate() {
            uname = document.forms["login_form"]["uname"];
            pass = document.forms["login_form"]["pass"];

            if (uname.value == "") {
                alert("please enter your username");
                name.focus()
                return false;
            }

            if (pass.value == "") {
                alert("please enter your password");
                password.focus()
                return false;
            }

            if (uname.value == "Ashok" && pass.value == "111") {
                alert("login is succesful");
                return true;
            }

            else {
                alert("Invalid data");
                return false;
            }
        }
    </script>
</head>
<style>
    body {
        background-image: url(stud2.jpg);
        margin: 0;
        padding: 0;
    }

    h1 {
        font-size: medium;
        font-family: 'Times New Roman', Times, serif;
        color: white;
    }

    .form {
        position: absolute;
        top: 52%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 600px;
        min-height: 500px;
        background: #fff;
    }

    .footer {
        background-color: black;
        margin-top: 550px;
    }

    .footer p {
        color: aliceblue;
        text-align: center;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
    }

    .footer-title {
        text-align: center;
        color: aliceblue;
        font-weight: 300;
        font-size: 17px;
        font-family: 'Times New Roman', Times, serif;
        margin-top: 5px;

    }

    h2 {
        font-family: 'Times New Roman', Times, serif;
        color: blueviolet;
    }
    
    .f1 {
        float: left;
    }

    h3 {
        color: white;
        text-align: center;
    }

    h5 {
        color: white;
    }

    .text {
        text-align: left;
    }
</style>

<body>
    <!-- heading and navbar -->

    <nav class="navbar navbar-inverse">
        <div class="container-fluid">
            <div class="navbar-header">
                <img src="./logo/college logo.png" alt="" style="height: 50px; width: 50px; border-radius: 80%;">
                <a class="navbar-brand" href="#">KSG College of Arts and Science E-SERVICE</a>
            </div>

        </div>
    </nav>

    <!-- image -->

    <center>
        <div class="form">
            <center>
                <h2>ADMIN LOGIN</h2>
            </center>
            <img src="./Image/img admin.jpeg" alt="Avatar" class="avatar" height="200px" width="200px"><br><br>
            <form action="./admin_dashboard.py" method="post" name="login_form" style="width: 350px;"
                onsubmit=" return validate()">
                <div class="form-group mb-3">
                    <label><b>USERNAME</b></label>
                    <input placeholder="USERNAME" type="text" name="uname" class="form-control">
                </div>
                <div class="form-group mb-3">
                    <label><b>PASSWORD</b></label>
                    <input placeholder="PASSWORD" type="password" name="pass" class="form-control">
                </div>
                <div class="form-group mb-3" style="width: 150px;">
                    <input type="submit" class="btn btn-success">

                </div>
            </form>
        </div>
    </center>
    <!-- footer -->

    <footer class="footer" style="position: relative;">
        <div class="container">
            <div class="row">
                <div class="col-md-5">
                    <div class="footer-title">
                        <u>ABOUT</u>
                    </div>
                    <h3>KSG Educational Trust</h3>
                    <p class="text">The KSG Educational Trust was started on 4th July 1997 with the sole aim of
                        imparting quality
                        education to all the aspirants of the needy poor category in and around Coimbatore.</p>
                </div>
                <div class="col-md-4 ">
                    <div class="footer-title"><u>
                            ADDRESS</u> </div>
                    <p class="f1">
                    <h5><span class="glyphicon glyphicon-home"></span> 93, Kamaraj Road,
                        Uppilipalayam PO, Singanallur, Tamil Nadu 641015</span></h5>
                    </p>
                </div>
                <div class="col-md-3 ">
                    <div class="footer-title"> <u>CONTACT</u></div><br>
                    <p class="f1"><span class="glyphicon glyphicon-phone-alt"> +91 8148277777, 8148377777</span></p><br>
                    <p class="f1"><span class="glyphicon glyphicon-envelope"> ksgprincipal@gmail.com</span></p><br>
                    <p class="f1"><span class="glyphicon glyphicon-globe"> www.ksgcollege.com</span></p><br>
                </div>
            </div><br>
            <p> legal notice / privacy policy: <span class="glyphicon glyphicon-copyright-mark"></span>studentservices
            </p>
        </div>
    </footer>


</body>

</html>
""")