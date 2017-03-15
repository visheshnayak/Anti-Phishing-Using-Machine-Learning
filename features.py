def domainCheck(url):
    w=0
    d=0
    flag=0
    phish=0
    for i in range(0,4):
        if url[i]=='w':
		    w=w+1
    if url[3]=='.':
	       flag=1
    for i in range(4,len(url)-3):
	    if url[i]=='w' and url[i+1]=='w' and url[i+2]=='w' and url[i+3]=='.':
		    phish=1
    if w<4 and flag==1 and phish==0:
	    print "0"
    else:
        print "1"

def urlChar(url):
    flag=0
    for i in range(0,len(url)):
	    flag=0
	    if url[i]=='@' or url[i]=='#':
		    flag=1
		    break
    if flag==1:
	    print "1"
    else:
        print "0"

def urlDot(url):
    d=0
    for i in range(0,len(url)):
	    if url[i]=='.':
		    d=d+1
    if d>=4:
	    print "1"
    else:
        print "0"

def urlLength(url):
    print (len(url))

def urlSens(url):
    if 'secur' in url :
        print('1')
    elif 'login' in url:
        print('1')
    elif 'signin' in url:
        print('1')
    elif 'webscr' in url:
        print('1')
    elif 'ebayisapi' in url:
        print('1')
    elif 'banking' in url:
        print('1')
    elif 'confirm' in url:
        print('1')
    else:
        print('0')

def urlHttps(url) :
    if 'https://' in url :
        print "0"
    else :
        print "1"
