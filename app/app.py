from flask import Flask,render_template
import socket
import os

app = Flask(__name__)

@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        secret = (os.environ['PASSWORD'])
        return render_template('index.html', hostname=host_name, ip=host_ip, secret=secret)
    except:
        return render_template('error.html')


    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
