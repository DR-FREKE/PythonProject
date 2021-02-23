import webbrowser
import time;

num = 0;

while num < 3:
    time.sleep(10);
    webbrowser.open("http://localhost/Tubs/SignUp.php");
    num = num + 1;