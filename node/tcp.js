var net = require('net');
var server = net.createServer(function (socket) {
  //new connection
  socket.on('data', function( data) {
    socket.write("hello");
  });

  socket.on('end', function () {
    console.log('connection close');
  });
  socket.write("welcome ");
});
  server.listen(8124, function (){
    console.log('server bound');
  });
