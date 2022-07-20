const http = require('http');
const hostname = '127.0.0.1';
const port = 3000;
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end("WELCOM TO THE AXEL SERVEUR");
});
server.listen(port, hostname, () => {
  console.log(`A.X.E.L SERVER IS RUNING AT  http://${hostname}:${port}/`);
});
