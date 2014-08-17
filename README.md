Ghost have [stated][1] that they'll be doing frequent releases in future.

Webfaction have [stated][2] that their one-click installers will always be that (installers, not upgraders).  Fair enough.

This is way to get the best of both worlds, and am looking for feedback.  Anyone else up for giving this a go?

Since ghost can operate as an npm module, create one of Webfactions node.js 1-click installers and then, in webapps/<app>, add a package.json and an index.js.

* Use webfaction 1-click installer to create a Node.js 0.10.24 application in your account

cd ~/webapps/<appname>
cat hello-world.js # make a note of the allocated port number (e.g. 32606)
git clone --no-checkout git@github.com:mozz100/ghost-on-webfaction.git ./checkout.tmp
mv checkout.tmp/.git . && rm -r checkout.tmp
git reset --hard HEAD
bin/npm install
sed -i -e "s/hello-world/index/" -e "s/nohup/NODE_ENV=production nohup/" bin/start
cp -r node_modules/ghost/content ./content
NODE_ENV=production bin/node index.js




  [1]: http://blog.ghost.org/ghost-0-5/
  [2]: https://community.webfaction.com/questions/15432/update-ghost