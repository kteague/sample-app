# sample-app

Simple "Hello World" Pyramid/Python 3 web application.

Runs a pretend data analysis.


## Install and run

To install this application for development, first install Python 3.5, then run:

    pyvenv sample-app-env
    cd sample-app-env
    source ./bin/activate
    git clone https://github.com/kteague/sample-app.git sample-app
    cd sample-app
    pip install pyramid==1.5.7
    pip install -e .

Then run the HTTP server with:

    pserve development.ini

This should start-up at the address http://0.0.0.0:6543

