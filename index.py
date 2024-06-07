#!C:\Users\aasho\AppData\Local\Programs\Python\Python310\python.exe
print("content-type:text/html \r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<style>
    .carousel-inner {
        margin-top: -20px;

    }

    .footer {
        background-color: black;
        margin-top: 1px;
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
            <div class="collapse navbar-collapse" id="myNavbar">
                <ul class="nav navbar-nav navbar-right">
                    <li class="dropdown">
                        <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                            <span class="glyphicon glyphicon-user"></span>REGISTER<span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="./student_Reg.py">Student</a></li>
                        </ul>
                    </li>
                    <li class="dropdown">
                        <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                            <span class="glyphicon glyphicon-log-in"></span> LOGIN <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="./admin_login.py">ADMIN</a></li>
                            <li class="dropdown log">
                                <a class="dropdown-toggle" data-toggle="dropdown" href="#">STAFFS
                                    <span class="caret"></span></a>
                                <ul class="dropdown-log">
                                    <li><a href="./staff_login.py">Bca</a></li>
                                    <li><a href="./staff_login.py">B.sc IT</a></li>
                                    <li><a href="./staff_login.py">B.sc CS</a></li>
                                </ul>
                            </li>
                            <li><a href="./student_login.py">STUDENTS</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- image -->

    <div id="myCarousel" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
            <div class="item active">
                <img src="./Image/img.jpeg" alt="" class="img-thumbnail" style="width:100%;height: 450px;">
            </div>
        </div>
    </div>

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
                            ADDRESS</u> </div><br>
                    <p class="f1">
                    <h5><span class="glyphicon glyphicon-home"></span> 93, Kamaraj Road,
                        Uppilipalayam PO, Singanallur, Tamil Nadu 641015</span></h5>
                    </p>
                </div>
                <div class="col-md-3 ">
                    <div class="footer-title"> <u>CONTACT</u></div><br>
                    <p class="f1"><span class="glyphicon glyphicon-phone-alt"> 8148277777, 8148377777</span></p><br>
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