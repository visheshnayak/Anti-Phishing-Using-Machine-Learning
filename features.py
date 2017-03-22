def domainCheck(url):
    wc = url.count("www.")
    return wc
#    w=0
#    d=0
#    flag=0
#    phish=0
#    for i in range(0,4):
#        if url[i]=='w':
#		    w=w+1
#    if url[3]=='.':
#	       flag=1
#    for i in range(4,len(url)-3):
#	    if url[i]=='w' and url[i+1]=='w' and url[i+2]=='w' and url[i+3]=='.':
#		    phish=1
#    if w<4 and flag==1 and phish==0:
#	    print "0"
#    else:
#        print "1"

def urlChar(url):
    at = url.count("@")
    return at
#    flag=0
#    for i in range(0,len(url)):
#	    flag=0
#	    if url[i]=='@' or url[i]=='#':
#		    flag=1
#		    break
#    if flag==1:
#	    print "1"
#    else:
#        print "0"


def urlCharHash(url):
    hashh = url.count("#")
    return hashh

def urlDot(url):
    dot = url.count(".")
    return dot
#    for i in range(0,len(url)):
#	    if url[i]=='.':
#		    d=d+1
#    if d>=4:
#	    print "1"
#    else:
#        print "0"

def urlLength(url):
    urllen = len(url)
    return urllen

def urlSens(url):
    secur = url.count("secur")
    login = url.count("login")
    signin = url.count("signin")
    webscr = url.count("webscr")
    ebayisapi = url.count("ebayisapi")
    banking = url.count("banking")
    confirm = url.count("confirm")
#    if 'secur' in url :
#        print('1')
#    elif 'login' in url:
#        print('1')
#    elif 'signin' in url:
#        print('1')
#    elif 'webscr' in url:
#        print('1')
#    elif 'ebayisapi' in url:
#        print('1')
#    elif 'banking' in url:
#        print('1')
#    elif 'confirm' in url:
#        print('1')
#    else:
#        print('0')

def urlHttps(url) :
    httpc = url.count("https://")
    return httpc

def ipcheck(url) :
    d=0
    flag=0
    d = url.count(".")
    for i in range(0,3):
	    if url[i].isdigit()=="True" or url[2]=='.' or url[3]=='.':
		    flag=1

    if d==3 and flag==1:
	    return 1
    else:
        return 0
