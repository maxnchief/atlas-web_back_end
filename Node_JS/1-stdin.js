process.stdout.write('Welcome to Holberton School! What is your name?\n');

process.stdin.on('data', (data) => {
    const name = data.toString()
})