
ln=open("L(0,L)(1,+)(dir).csv")
d=[None]*19
timestamps=[]
#sline=1#int(input("start line"))
#eline=642#int(input("end line"))
count=0

for line in ln:
	count = count + 1
	if(count>2):
		d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13],d[14],d[15],d[16],d[17],d[18]=line.split("\t")
		timestamps.append(d[0])
count=0
print(range(len(timestamps)-1))
for i in range(len(timestamps)-1):
	count+=1
	if count>=1:
		_,m1,s1=timestamps[i-1].split(":")
		_,m2,s2=timestamps[i].split(":")
		t1=int(m1)*60+int(s1)
		t2=int(m2)*60+int(s2)
		t=abs(t2-t1)
		if t>15:
			print(i+2,end=" : ")
			print(t)

ln.close()
