from learn import learning
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
<title>Suspicious Website</title>
</head>
<body>
<h3>You are about to access a website that is deemed suspicious by our algorithm</h3>
<p>If you know this website and trust this website, then click <a href="localhost:5000/trusted/">here</a>.</p>
</body>
</html>
"""

#If trusted website is put in
@app.route('/trusted/')
def trusted():
    #Add to learning set
    urlnow = open('currenturl.txt', 'r')
    cururl = urlnow.read()
    urlnow.close()

    if cururl != 'http://localhost:5000/' or cururl != 'http://localhost:5000/trusted/' :
        dataset = open('verified_offline.csv', 'a')
        dataset.write(cururl + '\n')
        dataset.close()

    #Making the system learn again
    learning()

    return ""
