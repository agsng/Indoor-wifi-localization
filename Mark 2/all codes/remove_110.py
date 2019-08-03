# removing the -110 values wale records from the  .csv file and creating new modified file at the desired location
c=0
l1={1:['(0,2)u.csv',c],2:['(0,4)u.csv',c],3:['(0,6)u.csv',c],4:['(0,8)u.csv',c],5:['(0,0)u.csv',c],6:['(2,0)u.csv',c],7:['(4,0)u.csv',c],8:['(6,0)u.csv',c],9:['(8,0)u.csv',c],10:['(0,-2)u.csv',c],11:['(0,-4)u.csv',c],12:['(0,-6)u.csv',c],13:['(0,-8)u.csv',c],14:['(0,-10)u.csv',c],15:['(-2,0)u.csv',c],16:['(-4,0)u.csv',c],17:['(-6,0)u.csv',c],18:['(-8,0)u.csv',c],19:['(4,4)u.csv',c],20:['(6,4)u.csv',c],21:['(5,-4)u.csv',c],22:['(-6,5)u.csv',c],23:['(-4,-4)u.csv',c],24:['(-6,-8)u.csv',c]}
l2={1:['(0,2)g.csv',c],2:['(0,4)g.csv',c],3:['(0,6)g.csv',c],4:['(0,8)g.csv',c],5:['(0,0)g.csv',c],6:['(2,0)g.csv',c],7:['(4,0)g.csv',c],8:['(6,0)g.csv',c],9:['(8,0)g.csv',c],10:['(0,-2)g.csv',c],11:['(0,-4)g.csv',c],12:['(0,-6)g.csv',c],13:['(0,-8)g.csv',c],14:['(0,-10)g.csv',c],15:['(-2,0)g.csv',c],16:['(-4,0)g.csv',c],17:['(-6,0)g.csv',c],18:['(-8,0)g.csv',c],19:['(4,4)g.csv',c],20:['(6,4)g.csv',c],21:['(5,-4)g.csv',c],22:['(-6,5)g.csv',c],23:['(-4,-4)g.csv',c],24:['(-6,-8)g.csv',c]}

for file in l1.keys():
    fp1 = open(l1[file][0])
    fp2 = open(l2[file][0], "w")       # the address at which i was storing the new file  /home/shubham/Desktop/tempo/

    for i in fp1:
        mac, sig = i.split("	")
        if (int(sig) != -110):
            fp2.write(i)

    fp1.close()
    fp2.close()
