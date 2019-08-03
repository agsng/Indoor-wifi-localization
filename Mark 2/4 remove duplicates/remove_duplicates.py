lines_seen = set() # holds lines already seen
c=0
l1={1:['(0,2)p.csv',c],2:['(0,4)p.csv',c],3:['(0,6)p.csv',c],4:['(0,8)p.csv',c],5:['(0,0)p.csv',c],6:['(2,0)p.csv',c],7:['(4,0)p.csv',c],8:['(6,0)p.csv',c],9:['(8,0)p.csv',c],10:['(0,-2)p.csv',c],11:['(0,-4)p.csv',c],12:['(0,-6)p.csv',c],13:['(0,-8)p.csv',c],14:['(0,-10)p.csv',c],15:['(-2,0)p.csv',c],16:['(-4,0)p.csv',c],17:['(-6,0)p.csv',c],18:['(-8,0)p.csv',c],19:['(4,4)p.csv',c],20:['(6,4)p.csv',c],21:['(5,-4)p.csv',c],22:['(-6,5)p.csv',c],23:['(-4,-4)p.csv',c],24:['(-6,-8)p.csv',c]}
l2={1:['(0,2)u.csv',c],2:['(0,4)u.csv',c],3:['(0,6)u.csv',c],4:['(0,8)u.csv',c],5:['(0,0)u.csv',c],6:['(2,0)u.csv',c],7:['(4,0)u.csv',c],8:['(6,0)u.csv',c],9:['(8,0)u.csv',c],10:['(0,-2)u.csv',c],11:['(0,-4)u.csv',c],12:['(0,-6)u.csv',c],13:['(0,-8)u.csv',c],14:['(0,-10)u.csv',c],15:['(-2,0)u.csv',c],16:['(-4,0)u.csv',c],17:['(-6,0)u.csv',c],18:['(-8,0)u.csv',c],19:['(4,4)u.csv',c],20:['(6,4)u.csv',c],21:['(5,-4)u.csv',c],22:['(-6,5)u.csv',c],23:['(-4,-4)u.csv',c],24:['(-6,-8)u.csv',c]}
count=-1
for lines in l1:
    #count=count+1
    #print(lines,end=",")
    outfile = open(l2[lines][0], "w")
    infile = open("/home/nk/Documents/mark 2/Processing Vault/pool data/"+l1[lines][0], "r")
    for line in infile:
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    infile.close()
    outfile.close()
    lines_seen.clear()
