url = raw_input()
d=0
flag=0
for i in range(0,len(url)):
	if url[i]=='.':
		d=d+1
for i in range(0,3):
	if url[i].isdigit()=="True" or url[2]=='.' or url[3]=='.':
		flag=1
		
if d==3 and flag==1:
	print "1"
else:
	print "0"
