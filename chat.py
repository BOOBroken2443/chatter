from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

users = {}  # Dictionary to store usernames, mapping client socket IDs to usernames

@app.route('/')
def chat():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(data):
    username = users.get(request.sid, 'Anonymous')
    message = data['message']
    emit('message', {'username': username, 'message': message}, broadcast=True)

@socketio.on('set_username')
def set_username(data):
    username = data['username']
    users[request.sid] = username

if __name__ == '__main__':
    host = '0.0.0.0'  # Listen on all available network interfaces
    port = 80  # Use the desired port, e.g., 80 for HTTP
    debug = False  # Set to False for production

    socketio.run(app, debug=debug, host=host, port=port)


    socketio.run(app, debug=debug, host=host, port=port)




