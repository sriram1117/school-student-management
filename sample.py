print("""
    <div>
    <center>
    <form action="" class="col-md-5" name="image" method="post" enctype="multipart/form-data">
    <center><h2><b>UPDATE FORM</b></h2></center>
        <input class="form-control" type="text" placeholder="staff_id" value="%s" readonly required name="stfid"><br>
        <input class="form-control" type="text" name="name" value="%s" placeholder="Name" maxlength="20" required><br>
        <input class="form-control" type="date" name="dob" value="%s" placeholder="Dob" maxlength="20" required><br>
        <input class="form-control" type="text" name="depart" value="%s" placeholder="Username" maxlength="20" required><br>
        <input class="form-control" type="text" name="phone" value="%s" placeholder="contact no" maxlength="20" required><br>
        <input class="form-control" type="mail" name="mail" value="%s" placeholder="Email_id" maxlength="30" required><br>
        <input class="form-control" type="text" name="address" value="%s" placeholder="Address" maxlength="100"><br>
        <input class="form-control" type="text" name="city" value="%s" placeholder="Username" maxlength="20" required><br>
        <input class="form-control" type="text" name="state" value="%s" placeholder="Username" maxlength="20" required><br>
        <input class="form-control" type="text" name="uname" value="%s" placeholder="Username" maxlength="20" required><br>
        <input class="form-control" type="text" name="pwd" value="%s" placeholder="Password" maxlength="20" required><br>
         <input class="form-control" type="text" name="num" value="%s" placeholder="Password" maxlength="20" required><br>
        <input class="btn btn-info btn-lg" type="submit" name="login" value="update"><br><br><br>
    </form>
    </center>
    """ % (staff_id, name, dob, department, contact, emailid, address, city, state, uname, pwd, salary))