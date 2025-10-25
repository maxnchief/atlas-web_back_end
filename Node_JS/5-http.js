/**
 * Simple HTTP server that serves two routes and delegates student data processing.
 */
const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');

    if (req.url === '/') {
        res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
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
    } else {
        res.end('Hello Holberton School!');
    }
});

app.listen(1245);

module.exports = app;