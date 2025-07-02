const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
    res.write('This is the list of our students\n');
    if (!database) {
        res.end('Cannot load the database');
        return;
    }
    // Patch console.log to write to res for this request
    const origLog = console.log;
    console.log = function (...args) {
        res.write(args.join(' ') + '\n');
    };
    countStudents(database)
        .then(() => {
            res.end();
        })
        .catch((err) => {
            res.end(err.message);
        })
        .finally(() => {
            console.log = origLog;
        });
});

app.listen(1245);

module.exports = app;