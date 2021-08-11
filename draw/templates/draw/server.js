var app = require('express') ()
var http = require('http').createServer(app)
var io = require('socket.io')(http)
app.get('/messages_chat', (req, res) => {
    res.sendFile(__dirname + '/messages_chat.html');
})

var server_port = process.env.PORT || 8000
http.listen(server_port)