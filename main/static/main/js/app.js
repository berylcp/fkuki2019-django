function cekPassword() {
    var password = document.getElementById("kotakPassword");
    var isiPassword = password.value;
    if (isiPassword == "cobapassword") {
        return true;
    } else {
        alert("Password salah! Silahkan ulangi.");
        return false;
    }
}