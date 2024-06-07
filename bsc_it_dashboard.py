#!C:\Users\aasho\AppData\Local\Programs\Python\Python310\python.exe
import os

print("content-type:text/html \r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
    <!------ Include the above in your HEAD tag ---------->


    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">

    <link rel="icon" type="image/x-icon" href="./media/logoonly.png">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

    <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">



    <style>
        .nav-side-menu {
            overflow: auto;
            font-family: verdana;
            font-size: 12px;
            font-weight: 200;
            background-color: #2e353d;
            position: fixed;
            top: 0px;
            width: 300px;
            height: 100%;
            color: #e1ffff;
        }

        .nav-side-menu .brand {
            background-color: #21e69a;
            line-height: 50px;
            display: block;
            text-align: center;
            font-size: 14px;
        }

        .nav-side-menu .toggle-btn {
            display: none;
        }

        .nav-side-menu ul,
        .nav-side-menu li {
            list-style: none;
            padding: 0px;
            margin: 0px;
            line-height: 35px;
            cursor: pointer;

            .collapsed {
                .arrow:before {
                    font-family: FontAwesome;
                    content: "\f053";
                    display: inline-block;
                    padding-left: 10px;
                    padding-right: 10px;
                    vertical-align: middle;
                    /* float: right; */
                }
            }

        }

        .nav-side-menu ul :not(collapsed) .arrow:before,
        .nav-side-menu li :not(collapsed) .arrow:before {
            font-family: FontAwesome;
            content: "\f078";
            display: inline-block;
            padding-left: 10px;
            padding-right: 10px;
            vertical-align: middle;
            /* float: right; */
        }

        .nav-side-menu ul .active,
        .nav-side-menu li .active {
            border-left: 3px solid #d19b3d;
            background-color: #4f5b69;
        }

        .nav-side-menu ul .sub-menu li.active,
        .nav-side-menu li .sub-menu li.active {
            color: #d19b3d;
        }

        .nav-side-menu ul .sub-menu li.active a,
        .nav-side-menu li .sub-menu li.active a {
            color: #d19b3d;
        }

        .nav-side-menu ul .sub-menu li,
        .nav-side-menu li .sub-menu li {
            background-color: #181c20;
            border: none;
            line-height: 28px;
            border-bottom: 1px solid #23282e;
            margin-left: 0px;
        }

        .nav-side-menu ul .sub-menu li:hover,
        .nav-side-menu li .sub-menu li:hover {
            background-color: #020203;
        }

        .nav-side-menu ul .sub-menu li:before,
        .nav-side-menu li .sub-menu li:before {
            font-family: FontAwesome;
            content: "\f105";
            display: inline-block;
            padding-left: 10px;
            padding-right: 10px;
            vertical-align: middle;
        }

        .nav-side-menu li {
            padding-left: 0px;
            border-left: 3px solid #2e353d;
            border-bottom: 1px solid #23282e;
        }

        .nav-side-menu li a {
            text-decoration: none;
            color: #e1ffff;
        }

        .nav-side-menu li a i {
            padding-left: 10px;
            width: 20px;
            padding-right: 20px;
        }

        .nav-side-menu li:hover {
            border-left: 3px solid #d19b3d;
            background-color: #4f5b69;
            -webkit-transition: all 1s ease;
            -moz-transition: all 1s ease;
            -o-transition: all 1s ease;
            -ms-transition: all 1s ease;
            transition: all 1s ease;
        }

        @media (max-width: 767px) {
            .nav-side-menu {
                position: relative;
                width: 100%;
                margin-bottom: 10px;
            }

            .nav-side-menu .toggle-btn {
                display: block;
                cursor: pointer;
                position: absolute;
                right: 10px;
                top: 10px;
                z-index: 10 !important;
                padding: 3px;
                background-color: #ffffff;
                color: #000;
                width: 40px;
                text-align: center;
            }

            .brand {
                text-align: left !important;
                font-size: 22px;
                padding-left: 20px;
                line-height: 50px !important;
            }
        }

        @media (min-width: 767px) {
            .nav-side-menu .menu-list .menu-content {
                display: block;
            }
        }

        body {
            margin: 0px;
            padding: 0px;
        }

        .main {
            margin-left: 300px;
            /* Same as the width of the sidenav */
            font-size: 20px;
            /* Increased text to enable scrolling */
            padding: 0px 10px;
        }
    </style>

</head>

<body>

    <div class="nav-side-menu">
        <div class="brand"><img src="./logo/college_cover_image.jpg" style="height: 90px; width: 300px"></div>
        <i class="fa fa-bars fa-2x toggle-btn" data-toggle="collapse" data-target="#menu-content"></i>

        <div class="menu-list">
            <li data-toggle="collapse" data-target="#service" class="collapsed">
                <a href="#">Student Details

                    <span class="fa fa-angle-down"></span></a>
            </li>
            <ul class="sub-menu collapse" id="service">

                <li><a href="./staff_it_dep_view.py">B.Sc IT DEPARTMENT</a></li>
            </ul>
            <li data-toggle="collapse" data-target="#new" class="collapsed">
                <a href="#">Student Requests <span class="fa fa-angle-down"></span></a>
            </li>
            <ul class="sub-menu collapse" id="new">
                
                <li><a href="./staff_certificate_req_view.py">View</a></li>
            </ul>

            <li data-toggle="collapse" data-target="#new2" class="collapsed">
                <a href="#">Leave reguest <span class="fa fa-angle-down"></span></a>
            </li>
            <ul class="sub-menu collapse" id="new2">
                <li><a href="./staff_leave_req.py">add</a></li>
                <li><a href="./staff_leave_req_view.py">view</a></li>
            </ul>
            
            <li>
                <a href="./staff_salary_view.py">
                    Salary View
                </a>
            </li>

            <li>
                <a href="./index.py">
                    Logout
                </a>
            </li>

        </div>
    </div>
    
</body>

</html>
""")
import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = conn.cursor()

form = cgi.FieldStorage()
pid = form.getvalue('id')

q = """select * from staff_detail where id="%s" """ % (pid)
cur.execute(q)
rec = cur.fetchall()

for i in rec:
    fn = "Media/" + i[13]

    print("""
        <center>
            <h3>
            <p>Welcome to B.sc IT %s</p>
            </h3>
            <img src="%s" height=160 width=160>
            
        """ % (i[2], fn))
    print("""
                <html>
                <body>
            """)
    for i in rec:
        print("""
            <center>
               <p>%s</p>
               <p>%s</p><br>
               <div class="col-md-5"></div>
                <form class="container col-md-2"  name="profile_img" method="post" enctype="multipart/form-data">
                    <input class="form-control" type="file" name="img" placeholder="Update Profile" maxlenghth="20" required><br>
                    <input class="form-control btn btn-info" type="Submit" name="sub" value="update" maxlength="10"><br><br><br>
                </form>
            </center>
               """ % (i[1], i[2]))

        print("""

            </div>
            </body>
            </html>
            """)
    psubmit = form.getvalue("sub")
    if psubmit != None:
        if len(form) != 0:

            # print(pid)
            pimage = form['img']

            if pimage.filename:
                fs = os.path.basename(pimage.filename)
                open("Media/" + fs, "wb").write(pimage.file.read())
                q = """update staff_detail set image='%s' where id="%s" """ % (fs, pid)
                cur.execute(q)
                conn.commit()

                print("""
                        <script>
                            alert("Updated successfully");
                        </script>
                    """)
conn.close()