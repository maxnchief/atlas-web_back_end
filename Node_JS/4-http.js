/**
 * This module uses Node's built-in 'http' to create a server which sets a 200 status code
 * and the 'Content-Type' header to 'text/plain' for every incoming request, then ends the
 * response with 'Hello Holberton School!'.
 */
const http = require('http');

const app = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;