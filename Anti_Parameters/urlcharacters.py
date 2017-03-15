url=raw_input()
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
