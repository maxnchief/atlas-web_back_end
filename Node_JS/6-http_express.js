/**
 * This module creates an Express application, registers a GET handler
 * for the root path that responds with "Hello Holberton School!"
 */

const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;