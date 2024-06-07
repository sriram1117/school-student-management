#!C:\Users\aasho\AppData\Local\Programs\Python\Python310\python.exe

print("content-type:text/html \r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Employee Leave Form</title>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f8f9fa;
        }

        .leave-form {
            max-width: 500px;
            margin: 50px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
    <script>
        function calculateDays() {
            const startDate = new Date(document.getElementById('start-date').value);
            const endDate = new Date(document.getElementById('end-date').value);
            const resultTextBox = document.getElementById('result');

            if (startDate && endDate) {
                const difference = Math.abs(endDate - startDate);
                const daysDifference = Math.ceil(difference / (1000 * 60 * 60 * 24));
                resultTextBox.value = daysDifference;
            } 
            else {
                resultTextBox.value = '';
            }
        }
    </script>
</head>

<body>
    

    <div class="container">
        <div class="leave-form">
            <h2 class="text-center mb-4">Request for Leave</h2>
            
            <form action="#" class="loginform" method="post" enctype="multipart/form-data" onsubmit=" return login()" onchange="remdays();">
            <div class="form-group">
                    
                    <input type="text" class="form-control"  name="empid" placeholder="Enter your id">
                </div>
                <div class="form-group">
                   
                    <input type="text" class="form-control"  name="ename" placeholder="Enter your name">
                </div>

                <div class="form-group">
                    
                    <select class="form-control" name="type">
                        <option>Select Leave Type</option>
                        <option>Vacation Leave</option>
                        <option>Sick Leave</option>
                        <option>Personal Leave</option>
                    </select>
                </div>
                <div class="form-group">
                    <input type="date" class="form-control" name="startDate" id="start-date" oninput="calculateDays()">
                </div>
                <div class="form-group">
                    <input type="date" class="form-control" name="endDate" id="end-date" oninput="calculateDays()">
                </div>
                <div class="form-group">
                    
                    <input type="text" class="form-control" rows="3" id="result" placeholder="No.Of.Days" name="result" readonly>
                </div>
                <center>
                    <input class="form-control btn btn-success" type="Submit" name="login" value="Submit"><br><br><br>
                </center>
            </form>
        </div>
    </div>

</body>

</html>
""")

import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="Localhost", user="root", password="", database="project")
cur = conn.cursor()

form = cgi.FieldStorage()
pid = form.getvalue("empid")
pname = form.getvalue("ename")
pleave = form.getvalue("type")
pstart = form.getvalue("startDate")
pend = form.getvalue("endDate")
preas = form.getvalue("result")
psubmit = form.getvalue("login")

if psubmit != None:
    q= """insert into staff_leave_req_detail (stf_id,name,type,start_date,end_date,leave_taken)
        values ('%s','%s','%s','%s','%s','%s')""" % (pid,pname, pleave, pstart, pend, preas)
    cur.execute(q)
    conn.commit()
    print("""
        <script>
           alert("Data inserted successfully")
        </script>
    """)
conn.close()