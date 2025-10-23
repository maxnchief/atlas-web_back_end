/**
 * Node.js stdin example that prompts the user for their name,
 * reads input from standard input, echoes the provided name, and logs a closing
 * message when the input stream ends.
 */

process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('data', (data) => {
    const name = data.toString().trim();
    process.stdout.write(`Your name is: ${name}\n`);
});

process.stdin.on('end', () => {
    process.stdout.write('This important software is now closing\n');
});