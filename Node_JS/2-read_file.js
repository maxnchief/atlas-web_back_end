/**
 * Read a CSV file synchronously, count students and group them by the 'field' column,
 * then print a brief summary to the console.
 */
const fs = require('fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf8');
        const lines = data.split('\n').filter(line => line.trim() !== '');
        if (lines.length === 0) {
            console.log('Number of students: 0');
            return;
        }
        const headers = lines[0].split(',');
        const fieldIndex = headers.indexOf('field');
        const firstNameIndex = headers.indexOf('firstname');

        const studentsByField = {};
        let total = 0;

        for (let i = 1; i < lines.length; i++) {
            const line = lines[i].trim();
            if (line === '') continue;
            const values = line.split(',');
            if (values.length < headers.length) continue;
            const field = values[fieldIndex];
            const firstName = values[firstNameIndex];
            if (!studentsByField[field]) {
                studentsByField[field] = [];
            }
            studentsByField[field].push(firstName);
            total += 1;
        }

        console.log(`Number of students: ${total}`);
        for (const [field, names] of Object.entries(studentsByField)) {
            console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }
    } catch (err) {
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;