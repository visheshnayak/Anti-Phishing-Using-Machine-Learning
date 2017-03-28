from flask import Flask
app = Flask(__name__)

def startServer() :
    #Start the server on port 5000
    app.run()

#Creating the webpage to which the browser will be redirected
@app.route('/')
def index():
    return """<html>
    <head>
    <title>Test</title>
    <meta charset=utf-8>
    <p>Website is suspicious</p>
    <a href="/trusted/">I trust this Website</a>
    </head>
    </html>
"""

#If trusted website is put in
@app.route('/trusted/')
def trusted():
    #Add to learning set
    print "Added to the dataset"
