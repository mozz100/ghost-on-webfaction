Ghost have [stated][1] that they'll be doing frequent releases in future.

Webfaction have [stated][2] that their one-click installers will always be that (installers, not upgraders).  Fair enough.

I wanted a way to install ghost on webfaction but still be able to benefit from the simplest possible upgrade 
route when new versions are released.

This is my way to get the best of both worlds.  It installs ghost as an npm module, so that it can be updated
by just issuing `bin/stop; bin/npm update; bin/start`.  The content directory is completely separate from the ghost install (which is within the `node_modules` folder).

This custom install script for Webfaction installs a node.js app, then checks out the contents of this repo
(basically a package.json file and an index.js).  It creates a config.js containing the correct port, so things just work
on Webfaction.  Did I mention I love webfaction?

[Click here to install in your webfaction account][3] - note that it takes a while, because the npm install isn't too quick.  The
Webfaction "spinner" might be on screen for a minute or two: be patient!

This might have disadvantages I haven't thought of. I am looking for feedback.  Anyone else up for giving this a go? Pull requests and
suggestions very welcome (please use github issues).

As an extra bonus, this could easily scale up such that one `index.js` could serve multiple ghost blogs from a single process (if
you wanted to do that, to save memory, perhaps).  You'd need to create extra applications in the Webfaction control panel, note their
port numbers, and then extend `index.js` and create extra `config.js` files.


  [1]: http://blog.ghost.org/ghost-0-5/
  [2]: https://community.webfaction.com/questions/15432/update-ghost
  [3]: https://my.webfaction.com/new-application?script_url=https%3A%2F%2Fraw.githubusercontent.com%2Fmozz100%2Fghost-on-webfaction%2Fmaster%2Fwebfaction_install.py