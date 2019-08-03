
c=0
#l1={1:['(0,2).csv',c],2:['(0,4).csv',c],3:['(0,6).csv',c],4:['(0,8).csv',c],5:['(0,0).csv',c],6:['(2,0).csv',c],7:['(4,0).csv',c],8:['(6,0).csv',c],9:['(8,0).csv',c],10:['(0,-2).csv',c],11:['(0,-4).csv',c],12:['(0,0).csv',c],13:['(0,-8).csv',c],14:['(0,-10).csv',c],15:['(-2,0).csv',c],16:['(-4,0).csv',c],17:['(-6,0).csv',c],18:['(-8,0).csv',c],19:['(4,4).csv',c],20:['(6,4).csv',c],21:['(5,-4).csv',c],22:['(-6,5).csv',c],23:['(-4,-4).csv',c],24:['(-6,-8).csv',c]}
l1={1:['(0,2)ro.csv',c],2:['(0,4)ro.csv',c],3:['(0,6)ro.csv',c],4:['(0,8)ro.csv',c],5:['(0,0)ro.csv',c],6:['(2,0)ro.csv',c],7:['(4,0)ro.csv',c],8:['(6,0)ro.csv',c],9:['(8,0)ro.csv',c],10:['(0,-2)ro.csv',c],11:['(0,-4)ro.csv',c],12:['(0,-6)ro.csv',c],13:['(0,-8)ro.csv',c],14:['(0,-10)ro.csv',c],15:['(-2,0)ro.csv',c],16:['(-4,0)ro.csv',c],17:['(-6,0)ro.csv',c],18:['(-8,0)ro.csv',c],19:['(4,4)ro.csv',c],20:['(6,4)ro.csv',c],21:['(5,-4)ro.csv',c],22:['(-6,5)ro.csv',c],23:['(-4,-4)ro.csv',c],24:['(-6,-8)ro.csv',c]}
l2={1:['(0,2)g.csv',c],2:['(0,4)g.csv',c],3:['(0,6)g.csv',c],4:['(0,8)g.csv',c],5:['(0,0)g.csv',c],6:['(2,0)g.csv',c],7:['(4,0)g.csv',c],8:['(6,0)g.csv',c],9:['(8,0)g.csv',c],10:['(0,-2)g.csv',c],11:['(0,-4)g.csv',c],12:['(0,-6)g.csv',c],13:['(0,-8)g.csv',c],14:['(0,-10)g.csv',c],15:['(-2,0)g.csv',c],16:['(-4,0)g.csv',c],17:['(-6,0)g.csv',c],18:['(-8,0)g.csv',c],19:['(4,4)g.csv',c],20:['(6,4)g.csv',c],21:['(5,-4)g.csv',c],22:['(-6,5)g.csv',c],23:['(-4,-4)g.csv',c],24:['(-6,-8)g.csv',c]}


same_mac_sig = []
seen_mac = set()

for file in l1.keys():
	u=open("/home/nk/Documents/mark 2/Processing Vault/remove outliers/"+l1[file][0])
	print(l1[file][0])
	for line in u:
		mac,sig=line.split("\t")
		if mac not in seen_mac:
			seen_mac.add(mac)

			#same_mac_sig.append(sig)
			u2 = open("/home/nk/Documents/mark 2/Processing Vault/remove outliers/"+l1[file][0])
			for line2 in u2:                                       #looking for same mac
				mac1,sig1=line2.split("\t")
				#int(sig1)
				if mac1==mac:
					same_mac_sig.append(int(sig1))                      #creating list of all sig with same mac
					#same_mac_sig[len(same_mac_sig)-1].strip("\n")
			u2.close()


			same_mac_sig.sort(reverse=True)                      #sorting
			#print(same_mac_sig)

			ro = open("/home/nk/Documents/mark 2/Processing Vault/making ranges/"+l2[file][0], "a")
			ro.write(mac+"\t"+str(same_mac_sig[0])+"\t"+str(same_mac_sig[len(same_mac_sig)-1])+"\n")
			ro.close()
			same_mac_sig.clear()
	u.close()
	seen_mac.clear()


