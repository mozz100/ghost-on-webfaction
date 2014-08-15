// # Example ghost configuration

var path = require('path'),
    config;

config = {
    // Configure your URL and mail settings here
    production: {
        url: 'http://www.example.com',
        mail: {},
        database: {
            client: 'sqlite3',
            connection: {
                filename: path.join(__dirname, '/content/data/ghost.db')
            },
            debug: false
        },
        server: {
            host: '127.0.0.1',
            port: '32606'
        }
    }
};

// Export config
module.exports = config;
