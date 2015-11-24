Python has long been a stable of web development. In the recent world
of “web apps”, though, the browser is playing a larger role. More of the
application in a web app is done in JavaScript, in the “frontend”, with
Python running UI-less data services in the “backend”.

This is a series aimed at the Python developer, to explain this
JavaScript frontend world, from the perspective of Python. It’s a
polyglot view, aimed at a Python perspective, hence the series name of
“Pylyglot”. We'll be using PyCharm throughout, showing how it excels at
both the backend (Python) and the frontend (JS, HTML, CSS) due to its
IntelliJ foundation.

Remain Calm
-----------

I'm the oldest of oldsters in Python. I'm sympathetic. Python is
beautiful, and this new world...well, isn't. At every step along the
way, you'll say "This is stupid." I feel ya'. But rather than howl at
the moon in defiance, embrace the suck and dive in, because
realistically, you don't have a choice.

I think you'll find that, much to your surprise, there's a lot of
normalcy in modern JavaScript development. And in fact, there are
places where their toolchain excels in areas where we are banging
multiple heads against various walls. But, as this series will show, it
is a universe that is rebuilding the airplane in mid-flight, on a
minutely basis, and thus it takes a thick skin to get to a decently
Pythonic happy spot.

So with that inspirational message, let's press on.

Ditch the Browser, Go With Node
===============================

- Make the case for Pythonic development outside the browser
- Get Node installed
- Write a JS file
    - Function
    - Call it from a console.log
    - Run it
- Connect into an HTML page
- Launch the HTML page with PyCharm
- (Q) Does node have the if __name__ convention?
    - http://goo.gl/hWhLNe
    - If it works, remove console.log
- Commentary
    - Explain iojs
    - Think about both contexts, Node and browser, but start with Node
    - Think about making the frontend first, then make the backend

Developer Tooling with NPM
==========================

- Get mocha via Preferences

TDD with Mocha
==============

- PyCharm continuous run mode
- Debugger and breakpoints
- Split screen in PyCharm

Debugging in Both Contexts
==========================

- Show the PyCharm Mocha debugger in Node
- Show the JS Debugger in browser

Packaging with package.json
===========================

- npm init
- In this step, only about letting others get to this starting point
- npm run script for test
- You could hook this up to Travis and point at npm test
- PyCharm npm integration (but stop doing npm installs via Preferences)

Classes with ES6
================

- Prove that you can do ES6 in browsers as well as Node
- Explain kangax

Linting with eslint
===================

- Hook into PyCharm
- npm run script
- Consider making part of TravisCI build test case


Modules with CommonJS and Webpack
=================================

- Refactor tests to import
- Explain why we are ignoring ES6 imports for now
- Update npm run scripts
- Webpack-dev-server for super-cool development cycle
- For now, ignore sourcemaps and minify

Convert to Package Structure
============================

- src (or app) directory
- index.js as equivalent of __init__
- I like to put my browser-bits in there
- Sort out the test implications

Using npm Packages in Web Apps
==============================

- Let's do an Angular alert
- Get Angular via npm and add to dependencies
- Explain you can also get browserless NodeJS packages

ES6 Template Strings
====================

- Multi-line
- Parameterized

More ES6
========

- Arrow functions
- Array stuff
- rest parameter stuff
- ES6 Array extras
- Rest operator and “extended iterable unpacking"
- Maps and Sets
- https://github.com/bevacqua/es6

- let and const (and this one really pushes the ES6 browser compat
  envelope)

Mocking the REST API
====================

- Switch from dummy data to REST calls

Flask
=====

- Plug back in Python
- No authentication for now
- Use PyCharm's "Test REST service"

#####

Transpiling with Babel
======================

- Explain
    - You just cut off old browsers, and maybe you didn't want to
    - There are great ES7 features, like decorators, not in either
      context (Node or browser)
    - I wouldn't bring it up if it wasn't for modules
- Add to "dev" dependencies
- Change both contexts to use Babel
    - npm run script
    - PyCharm mocha options
- .babelrc
- Commentary
    - Downside: CPU fan

ES6 Next
========

- Iterators
- Generators
- Decorators
- async/await

######

Optional Typing with TypeScript
===============================

- Interfaces

- Optional typing

- tslint

- Automatic assignment of constructor

- Using type inferencing with dependency injection