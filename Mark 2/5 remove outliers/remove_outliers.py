
count=0
c=0
#l1={1:['(0,2).csv',c],2:['(0,4).csv',c],3:['(0,6).csv',c],4:['(0,8).csv',c],5:['(0,0).csv',c],6:['(2,0).csv',c],7:['(4,0).csv',c],8:['(6,0).csv',c],9:['(8,0).csv',c],10:['(0,-2).csv',c],11:['(0,-4).csv',c],12:['(0,0).csv',c],13:['(0,-8).csv',c],14:['(0,-10).csv',c],15:['(-2,0).csv',c],16:['(-4,0).csv',c],17:['(-6,0).csv',c],18:['(-8,0).csv',c],19:['(4,4).csv',c],20:['(6,4).csv',c],21:['(5,-4).csv',c],22:['(-6,5).csv',c],23:['(-4,-4).csv',c],24:['(-6,-8).csv',c]}
l1={1:['(0,2)r1.csv',c],2:['(0,4)r1.csv',c],3:['(0,6)r1.csv',c],4:['(0,8)r1.csv',c],5:['(0,0)r1.csv',c],6:['(2,0)r1.csv',c],7:['(4,0)r1.csv',c],8:['(6,0)r1.csv',c],9:['(8,0)r1.csv',c],10:['(0,-2)r1.csv',c],11:['(0,-4)r1.csv',c],12:['(0,-6)r1.csv',c],13:['(0,-8)r1.csv',c],14:['(0,-10)r1.csv',c],15:['(-2,0)r1.csv',c],16:['(-4,0)r1.csv',c],17:['(-6,0)r1.csv',c],18:['(-8,0)r1.csv',c],19:['(4,4)r1.csv',c],20:['(6,4)r1.csv',c],21:['(5,-4)r1.csv',c],22:['(-6,5)r1.csv',c],23:['(-4,-4)r1.csv',c],24:['(-6,-8)r1.csv',c]}
l2={1:['(0,2)ro.csv',c],2:['(0,4)ro.csv',c],3:['(0,6)ro.csv',c],4:['(0,8)ro.csv',c],5:['(0,0)ro.csv',c],6:['(2,0)ro.csv',c],7:['(4,0)ro.csv',c],8:['(6,0)ro.csv',c],9:['(8,0)ro.csv',c],10:['(0,-2)ro.csv',c],11:['(0,-4)ro.csv',c],12:['(0,-6)ro.csv',c],13:['(0,-8)ro.csv',c],14:['(0,-10)ro.csv',c],15:['(-2,0)ro.csv',c],16:['(-4,0)ro.csv',c],17:['(-6,0)ro.csv',c],18:['(-8,0)ro.csv',c],19:['(4,4)ro.csv',c],20:['(6,4)ro.csv',c],21:['(5,-4)ro.csv',c],22:['(-6,5)ro.csv',c],23:['(-4,-4)ro.csv',c],24:['(-6,-8)ro.csv',c]}

same_mac_sig = []
seen_mac = set()

d=[]

for file in l1.keys():
	u=open("/home/nk/Documents/mark 2/Processing Vault/remove -110/"+l1[file][0])
	print(l1[file][0])
	for line in u:
		mac,sig=line.split("\t")
		if mac not in seen_mac:
			seen_mac.add(mac)

			#same_mac_sig.append(sig)
			u2 = open("/home/nk/Documents/mark 2/Processing Vault/remove -110/"+l1[file][0])
			for line2 in u2:                                       #looking for same mac
				mac1,sig1=line2.split("\t")
				if mac1==mac:
					same_mac_sig.append(int(sig1))                      #creating list of all sig with same mac
			u2.close()
			same_mac_sig.sort(reverse=True)                      #sorting

			i = 0
			while i < len(same_mac_sig) - 1:
				#print(same_mac_sig[i])
				if (int(same_mac_sig[i]) - int(same_mac_sig[i + 1])) > 5:
					same_mac_sig.pop(i + 1)
					count+=1
					i = i - 1
				i = i + 1
			#print(count)
			if count>5:
				d.append(l1[file][0]+mac+" c="+str(count))
			count = 0
			ro = open("/home/nk/Documents/mark 2/Processing Vault/remove outliers/"+l2[file][0], "a")
			for j in same_mac_sig:
				ro.write(mac+"\t"+str(j)+"\n")
			ro.close()
			same_mac_sig.clear()
	u.close()
	seen_mac.clear()

print(d)

