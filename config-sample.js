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
            port: '<insert port here>'
        },
        paths: {
            contentPath: path.join(__dirname, '/content/')  // see https://github.com/mozz100/ghost-on-webfaction/issues/1
        }
    }
};

// Export config
module.exports = config;
