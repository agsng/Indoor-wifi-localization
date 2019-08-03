ln=open("L(9.9.18)(d=1,l'=3).csv")
nf=open("(-6,5)3.csv",'w')
d=[None]*19
sline=26426#int(input("start line"))
eline=26798#int(input("end line"))
count=0
for line in ln:
    count = count + 1
    if count >= sline and count <= eline:

        d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13],d[14],d[15],d[16],d[17],d[18]=line.split("\t")

        nf.write(d[2]+"\t"+d[11]+"\n")
    if count>eline:
        break
ln.close()
nf.close()



