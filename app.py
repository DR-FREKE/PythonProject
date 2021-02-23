from flask import Flask, render_template
import os
app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html");

@app.route("/contact")
def contact():
    return render_template("contact.html");

if __name__ == '__main__':
    app.debug = True;
    ##app.run(): the run function can take parameters like the port number and host name. app.run(host='localhost', port=8000)
    app.run(host='localhost', port=5000);

file_name = os.listdir(r"C:\Users\KingSolo\Documents\Anan")
print(file_name)
print(os.getcwd())