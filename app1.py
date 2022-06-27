from flask import Flask

# create flask instance
app =Flask(__name__)

# create first route
@app.route('/')


def hello_world():
    
    return 'Hello world'