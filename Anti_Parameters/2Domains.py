url = raw_input()
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
