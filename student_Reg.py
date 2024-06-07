#!C:\Users\aasho\AppData\Local\Programs\Python\Python310\python.exe


print("content-type:text/html \r\n\r\n")

import smtplib
import os
import pymysql
import cgi, cgitb


cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = conn.cursor()

q1="""select max(id) from student_detail"""
cur.execute(q1)
r=cur.fetchone()

if r[0]!=None:
    n=r[0]

else:
    n=0

z=""
if n<9:
    z="000"
elif n>=10 and n<99:
    z="00"
elif n>=100 and n<999:
    z="0"

form=cgi.FieldStorage()

stuid="STU"+z+str(n+1)

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

    <div class="main">
        <center>
            <h2 style="font-family:Georgia, 'Times New Roman', Times, serif; color: #230124; margin-left:20px;">Staff
                registration form</h2>
        </center><br>
        <div class="col-md-4"></div>
        <form action="" class="container col-md-5" name="image" method="post" enctype="multipart/form-data">
           """)
print("""
          <input class="form-control" type="text" placeholder="Stu_id" value="%s" readonly required name="stuid"><br>
            """ %stuid)

print("""
<input class="form-control" type="text" name="name" placeholder="Name" maxlength="20" required><br>
            <input class="form-control" type="date" name="dob" placeholder="Dob" maxlength="20" required><br>
            <select class="form-control" type="text" name="depart" maxlength="20" required>
                <option value="" disabled selected>Department</option>
                <optgroup label="UG">
                    <option value="BCA">BCA</option>
                    <option value="B.sc IT">B.sc IT</option>
                    <option value="B.sc CS">B.sc CS</option>
                </optgroup>
                <select><br>
                    <input class="form-control" type="text" name="phone" placeholder="contact no" maxlength="20"
                        required><br>
                    <input class="form-control" type="mail" name="mail" placeholder="Email_id" maxlength="30"
                        required><br>
                    <input class="form-control" type="text" name="address" placeholder="Address" maxlength="100"><br>
                    <select class="form-control" type="text" name="city" maxlength="20" required>
                        <option value="" disabled selected>Select city</option>
                        <option value="coimbatore">Coimbatore</option>
                        <option value="tiruppur">Tiruppur</option>
                        <option value="kochin">Kochin</option>
                    <select>
                    <br>
                    <select class="form-control" type="text" name="state" maxlength="20" required>
                        <option value="" disabled selected>Select state</option>
                        <option value="Tamilnadu">Tamilnadu</option>
                        <option value="kerala">Kerala</option>
                    <select>
                    <br>
                
                    <input class="form-control" type="text" name="uname" placeholder="Username"
                        maxlength="20" required><br>
                    <input class="form-control" type="text" name="pwd" placeholder="Password"
                        maxlength="20" required><br>
                    <input class="form-control" type="file" name="image"
                        placeholder="Upload Profile Picture" maxlength="20" required>
                    <br>
                    <input class="form-control btn btn-info btn-lg" type="Submit" name="login"
                        value="Register"><br><br><br>
        </form>

</body>

</html>
""")

pname = form.getvalue("name")
pdob=form.getvalue("dob")
pdep=form.getvalue("depart")
pcontact=form.getvalue("phone")
pemail_id=form.getvalue("mail")
paddr=form.getvalue("address")
pcity=form.getvalue("city")
pstate=form.getvalue("state")
puserna = form.getvalue("uname")
ppass = form.getvalue("pwd")
pstuid=form.getvalue("stuid")
if len(form) != 0:
    pimage = form['image']
    if pimage.filename:
        fn = os.path.basename(pimage.filename)
        open("Media/" + fn, "wb").write(pimage.file.read())
        q = """insert into Student_detail (stu_id,name,dob,department,contact,emailid,address,city,state,username,password,image)
         values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (pstuid,pname,pdob,pdep,pcontact,pemail_id,paddr,pcity,pstate,puserna,ppass,fn)
        cur.execute(q)
        conn.commit()
        print("""
            <script>
            alert("Data inserted successfully")
            </script>
            """)

conn.close()