import matplotlib.pyplot as plt

#gp=open("graph_data.csv",'w')
c=0
files={1: ['(0,8)u.csv', c], 2: ['(0,8)1.csv', c], 3: ['(0,8)2.csv', c],4: ['(0,8)3.csv', c]}
y1=[]
y2=[]
y3=[]
y4=[]
y=[y1,y2,y3,y4]
maci="n"
for i in files.keys():
	dp=open(files[i][0])
	for line in dp:
		mac,signal=line.split("\t")
		#print(mac,signal)
		#if maci=="n" and int(signal)!=-110:
		#	print(signal)
		#	maci=mac
		if mac=="D4:68:4D:3E:8A:6C":
			maci=mac
			y[i-1].append(int(signal))

print(y1,y2,y3,y4)
t1=list(range(1,len(y1)+1))
t2=list(range(1,len(y2)+1))
t3=list(range(1,len(y3)+1))
t4=list(range(1,len(y4)+1))

#plt.axis([])
plt.title(files[1][0]+"  mac-->"+maci)
plt.plot(t1,y1,'-bo')
plt.plot(t2,y2,'-go')
plt.plot(t3,y3,'-yo')
plt.plot(t4,y4,'-ro')
plt.show()