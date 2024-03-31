import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

os.environ['FLASK_ENV'] = 'development'

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='threading')


@socketio.on('message')
def handle_message(message):
    print("Received message:" + message)
    if message != "User connected!":
        send(message, broadcast=True)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, host="192.168.0.103", port=5000, debug=True, allow_unsafe_werkzeug=True)
