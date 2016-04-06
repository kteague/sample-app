# sample-app

Simple "Hello World" Pyramid/Python 3 web application.

Runs a pretend data analysis.


## Install and run

For development, to install use the buildout.cfg supplied:

    python3.5 bootstrap.py
    ./bin/buildout
    
    
Then run the HTTP server with:

    ./bin/pserve development.ini

This should start-up at the address http://0.0.0.0:6543

