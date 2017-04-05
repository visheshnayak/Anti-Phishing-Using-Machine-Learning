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
<link href='//fonts.googleapis.com/css?family=Aldrich' rel='stylesheet'>
<body>
<style>
button {
    background-color: #B22222;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
	font-family:"Lucida Sans Typewriter",Lucida Console,monaco,Bitstream Vera Sans Mono,monospace;

}
	
body {
background-image: url("pic1.jpg");
}

</style>
<section>
<center><font size ="6"><p style="color:#FF6347;font-family:'Lucida Sans Typewriter',Lucida Console,monaco,Bitstream Vera Sans Mono,monospace">This is a suspicious website</p></font></center>
<br><center><button title='You are about to enter a suspicious website'style="color:#FFDAB9">I trust this website and wish to proceed.</button></center><title="You are about to enter a suspicious website">
</section>
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

    dataset = open('list.txt', 'a')
    dataset.write(cururl + '\n')
    dataset.close()

    #Making the system learn again
    learning()

    return """
    <html>
    <head>
    <title>Trusted</title>
    </head>
    <body>
    <p>Added to the dataset<p>
    </body>
    </html>"""
