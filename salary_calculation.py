#!C:\Users\aasho\AppData\Local\Programs\Python\Python310\python.exe
print("content-type:text/html \r\n\r\n")

import pymysql
import cgi, cgitb
from datetime import date

today = date.today()
year = today.year

form = cgi.FieldStorage()

pid = form.getvalue("staff_id")

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

    <link href="//netdna.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <script src="//netdna.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
    <!------ Include the above in your HEAD tag ---------->

    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
    <link rel="icon" type="image/x-icon" href="./media/logoonly.png">
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
            background-color: #000000;
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
                    float: right;
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
            float: right;
        }

        .nav-side-menu ul .active,
        .nav-side-menu li .active {
            border-left: 3px solid rgb(140, 209, 61);
            background-color: #4f5b69;
        }

        .nav-side-menu ul .sub-menu li.active,
        .nav-side-menu li .sub-menu li.active {
            color: rgb(140, 209, 61);
        }

        .nav-side-menu ul .sub-menu li.active a,
        .nav-side-menu li .sub-menu li.active a {
            color: rgb(140, 209, 61);
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
            border-left: 3px solid rgb(140, 209, 61);
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

        body {
            background-color: rgb(238, 238, 238);
        }

        *[role="form"] {
            max-width: 530px;
            padding: 15px;
            margin: 0 auto;
            background-color: rgb(238, 238, 238);
            border-radius: 0.3em;
        }

        *[role="form"] h2 {
            margin-left: 5em;
            margin-bottom: 1em;
        }
    </style>

    <script type="text/javascript">
     function calc(){
     var ch=loginform.mon.selectedIndex;
     if(ch==0)
        loginform.wdays.value="31";
        if(ch==1)
        loginform.wdays.value="28";
        if(ch==2)
        loginform.wdays.value="31";
        if(ch==3)
        loginform.wdays.value="30";
        if(ch==4)
        loginform.wdays.value="31";
        if(ch==5)
        loginform.wdays.value="30";
        if(ch==6)
        loginform.wdays.value="31";
        if(ch==7)
        loginform.wdays.value="31";
        if(ch==8)
        loginform.wdays.value="30";
        if(ch==9)
        loginform.wdays.value="31";
        if(ch==10)
        loginform.wdays.value="30";
        if(ch==11)
        loginform.wdays.value="31";
    }
    function remdays(){
    var wdays=parseInt(loginform.wdays.value);
    var ldays=parseInt(loginform.pleavetaken.value);
    var perdays=wdays-ldays;
    loginform.pdays.value=perdays;    
    }

    function gross(){
    var sal=parseInt(loginform.salary.value);
    var present=parseInt(loginform.pdays.value);
    var work=parseInt(loginform.wdays.value);
    var gross=Math.round((sal * present)/work);
    loginform.grosssalary.value=gross;    
    }
    </script>
</head>

<body>

    <div class="nav-side-menu">
        <div class="brand"><img src="./logo/college_cover_image.jpg" style="height: 90px; width: 300px"></div>
        <i class="fa fa-bars fa-2x toggle-btn" data-toggle="collapse" data-target="#menu-content"></i>

        <div class="menu-list">


            <li data-toggle="collapse" data-target="#products" class="collapsed active">
                <a href="#">Staff Details <span class="fa fa-angle-down"></span></a>
            </li>
            <ul class="sub-menu collapse" id="products">
                <li><a href="./admin_staff_add.py">Add</a></li>
                <li><a href="./admin_staff_view.py">View</a></li>
            </ul>


           <li data-toggle="collapse" data-target="#service" class="collapsed">
                <a href="#">Student Details

                    <span class="fa fa-angle-down"></span></a>
            </li>
            <ul class="sub-menu collapse" id="service">
                <li><a href="./all_dep.py">All DEPARTMENT</a></li>
                <li><a href="./bca_dep.py">BCA DEPARTMENT</a></li>
                <li><a href="./bsc_it_dep.py">B.Sc IT DEPARTMENT</a></li>
                <li><a href="./bsc_cs_dep.py">B.Sc CS DEPARTMENT</a></li>
            </ul>

            <li data-toggle="collapse" data-target="#new" class="collapsed">
                <a href="#">Student Requests <span class="fa fa-angle-down"></span></a>
            </li>
            <ul class="sub-menu collapse" id="new">
                
                <li><a href="./admin_stu_req_view.py">View</a></li>
            </ul>

            <li data-toggle="collapse" data-target="#new2" class="collapsed">
                <a href="#">Leave reguest <span class="fa fa-angle-down"></span></a>
            </li>
            <ul class="sub-menu collapse" id="new2">
                <li><a href="#">New</a></li>

                <li><a href="#">Exist</a></li>
            </ul>
            <li>
                <a href="./salary_cal_view.py">
                    Salary Calculation
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

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="project")
cur = conn.cursor()

q = """select * from staff_detail where staff_id="%s" """ % (pid)
cur.execute(q)
res = cur.fetchall()

for i in res:
    salary = i[12]
    Emp = i[0]
    name = i[1]

    print("""
    <div style="margin-left:410px;"> 
        <div>
            <center>
                <div class="col-md-5 mar1">
                    <span onclick="document.getElementById('more').style.display='none'">
                    <h4 class="text-center heading">Salary Details</h4>
                </div>
            </center>
        </div>

        <form style="margin-top:150px;" name="loginform" onsubmit="return login()">
        <div class="col-md-5"></div>
        <div clss="col-md-4 mar" style="padding:50px;">
            <div class="input-container">
      <input class="form-control type="text" name="emp" value="%s" readonly maxlength="20" required><br>
      """ % (Emp))
    print("""
      <input class="form-control type="text" name="year" value="%s" .readonly maxlength="20" required><br>
      """ % (year))
    print("""
        <select class="form-control" type="text" name="mon" maxlength="20" onchange="calc();remdays();gross();" required><br>
        <option value="Jan">Jan</option>
        <option value="Feb">Feb</option>
        <option value="March">March</option>
        <option value="April">April</option>
        <option value="May">May</option>
        <option value="June">June</option>
        <option value="July">July</option>
        <option value="Aug">Aug</option>
        <option value="Sep">Sep</option>
        <option value="Oct">Oct</option>
        <option value="Nov">Nov</option>
        <option value="Dec">Dec</option>
        </select><br>
    """)

    print("""
        <input class="form-control" type="text" value="%s" name="salary" readonly placeholder="Salary" maxlength="20" required><br>
        """ % (salary))
    print("""
        <input class="form-control" type="text" name="wdays"   placeholder="Working days" maxlength="20" required><br>
        <input class="form-control" type="text" name="pdays"  placeholder="Present days" maxlength="20" required><br>
    """)

    q1 = """select * from staff_leave_req_detail where id="%s" """ % (Emp)
    cur.execute(q1)
    r = cur.fetchall()

    for i in r:
        print("""
            <input class="form-control" type="text" readonly name="pleavetaken" value="%s" placeholder="Leave taken" maxlength="20" required><br>
        """ % i[6])
        print("""
            <input class="form-control" type="text" name="grosssalary"  placeholder="Gross Salary" maxlength="20" required><br>
            <div style="width:'30px;'">
            <center>
            <input class=" btn btn-success" type="Submit" name="login" value="submit" ><br><br><br>
            </center>
            </div>
        </form>
        """)
        print("""
            </table>
            </div>
            <body>
            </html>
        """)

import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", database="project")
cur = conn.cursor()

q1 = """select * from salary_detail"""
cur.execute(q1)
r = cur.fetchall()

form = cgi.FieldStorage()

pemailid = form.getvalue("emp")
pyear = form.getvalue("year")
pmonth = form.getvalue("mon")
psalary = form.getvalue("salary")
pwdays = form.getvalue("wdays")
ppdays = form.getvalue("pdays")
pleave = form.getvalue("pleavetaken")
pgross_salary = form.getvalue("grosssalary")
psubmit = form.getvalue("login")
if psubmit != None:
    q = """insert into salary_detail(stf_id,year,month,salary,wdays,pdays,leave_taken,gross_salary)
        values('%s','%s','%s','%s','%s','%s','%s','%s')""" % (
        pemailid, pyear, pmonth, psalary, pwdays, ppdays, pleave, pgross_salary)
    cur.execute(q)
    print("""
        <script>
            alter("Data inserted successfully")
        </script>
    """)

conn.commit()
conn.close()