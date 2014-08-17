#-----BEGIN WEBFACTION INSTALL SCRIPT-----
#!/usr/local/bin/python2.5

"""
Ghost as an npm module on webfaction
"""

import sys
import xmlrpclib

def create(app_name, server, session_id):
    app = server.create_app(session_id, app_name, 'node-0.10.24')

    # Run commands to install from github.
    lines = (
        # Git checkout files (remember current dir is non-empty).
        'git clone -q --no-checkout https://github.com/mozz100/ghost-on-webfaction.git ./checkout.tmp',
        'mv checkout.tmp/.git . && rm -r checkout.tmp',
        'git reset --hard HEAD',
        # Install modules into node_modules.
        'bin/npm install --loglevel silent 2> /dev/null',
        # Modify bin/start to run index.js and set NODE_ENV.
        'sed -i -e "s/hello-world/index/" -e "s/nohup/NODE_ENV=production nohup/" bin/start',
        # Initial content directory and config file.
        'cp -r node_modules/ghost/content ./content',
        'cp config-sample.js config.js',
        # Remove hello-world.js
        'rm hello-world.js'
    )
    for line in lines:
        server.system(session_id, line)

    server.replace_in_file(session_id, 'config.js', ['<insert port here>', str(app['port'])])

    # Restart the app
    server.system(session_id, 'bin/stop && bin/start')

def delete(app_name, server, session_id):
    server.delete_app(session_id, app_name)

def main(action, username, password, machine, app_name, autostart, extra_info):
    server = xmlrpclib.Server('https://api.webfaction.com/')
    if machine=="":
        session_id, account = server.login(username, password)
    else:
        session_id, account = server.login(username, password, machine)

    # Create/Delete Application
    globals()[action](app_name, server, session_id)

if __name__ == '__main__':
    try:
        main(*sys.argv[1:])
    except xmlrpclib.Fault, e:
        print e.faultString

#-----END WEBFACTION INSTALL SCRIPT-----
