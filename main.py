import socket

from flask import Flask, request, render_template
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


def is_port_open(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect((ip, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    ip = ""
    port = ""
    if request.method == 'POST':
        ip = request.form.get('ip')
        port = request.form.get('port')
        try:
            port = int(port)
            if 0 < port < 65536:  # Port number should be between 1 and 65535
                result = is_port_open(ip, port)
            else:
                result = "Invalid port number."
        except ValueError:
            result = "Invalid IP address or port number."
        except Exception as e:
            result = f"An error occurred: {str(e)}"
    return render_template('index.html', result=result, ip=ip, port=port)


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e
    # now you're handling non-HTTP exceptions only
    return render_template("500_generic.html", e=e), 500


if __name__ == "__main__":
    app.run(debug=False)
