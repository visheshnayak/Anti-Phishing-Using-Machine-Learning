url=raw_input()
d=0
for i in range(0,len(url)):
	if url[i]=='.':
		d=d+1
if d>=4:
	print "1"
else:
	print "0"
