const express = require('express');
const app = express();
const http = require('http').Server(app);
const io = require('socket.io')(http);

app.use(express.static('public')); // Serve your HTML and client-side scripts from the 'public' directory

io.on('connection', function(socket) {
    console.log('A user connected');

    socket.on('set_username', function(data) {
        // Handle setting username logic
    });

    socket.on('message', function(data) {
        io.emit('message', data); // Broadcast the message to all connected clients
    });

    socket.on('disconnect', function() {
        console.log('A user disconnected');
    });
});

const PORT = process.env.PORT || 3000;
http.listen(PORT, function() {
    console.log(`Server is running on port ${PORT}`);
});



