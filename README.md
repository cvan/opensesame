opensesame
==========

Because the Internet should be open. And because Sesame Street™.


Installation
============

Acquire dependencies:

    pip install -r requirements.txt

Install redis and its launch agent (Mac OS X):

    brew install redis
    brew info redis

Play with redis:

    redis-cli

Keep an eye on redis:

    redis-cli monitor

To clear redis:

    redis-cli flushall


Development
===========

In one Terminal tab run:

    DEBUG=1 python app.py

In another tab run:

    DEBUG=1 python lesswatch.py

Then fire up your favourite browser and go to

    http://localhost:4000
