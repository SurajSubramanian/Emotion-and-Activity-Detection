const io = require('socket.io-client');

const socket = io('http://localhost:5000/');

socket.on('connect', () => {
	socket.emit('event','from client');
});

socket.on('message', console.log);