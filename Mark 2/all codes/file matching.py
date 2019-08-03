#percentage of lines that match
fp = open("(0,8).csv")

rows1 = 0
rows2 = 0
count = 0

for i in fp :
    rows1 = rows1 +1
    mac1, sig1 = i.split("	")
    #print(mac1,"-->",sig1)
    fp1 = open("(0,8)1.csv")
    for j in fp1 :
        rows2 = rows2 + 1
        mac2, sig2 = j.split("	")
        if mac1==mac2 and sig1 == sig2:
            #print("hi there")
            count = count + 1
            break
    fp1.close()
fp.close()

print("rows1",rows1)
print("rows1",rows2)
print("count",count)
a = (count/rows1)*100
print("percentage of match :", a)


