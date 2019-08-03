import os, sys, time, threading, multiprocessing



#position.py code
from typing import TextIO

cells=[]
dict_wifi={}				#{}<=>dict()    ,dict() constructor creates a dictionary in Python. (collection of lists)
for i in range(0,60):
	dict_wifi[i]=[]			#every dict_wifi value contains '[]'

import subprocess
Process=subprocess.Popen(["iwlist","wlo1","scanning"],stdout=subprocess.PIPE,universal_newlines=True)
out,err=Process.communicate()			#command (exact) output going in "out"
#print(out)
new_l=out.split('\n')					#new_l is a list containing the output of command line by line(spllited "out" at every newline )
#print(type(new_l))
#print (new_l)

for line in new_l:
	line=line.lstrip()					#extra spaces in front deleted
	line=line.rstrip()					#extra spaces at back deleted
	if line.startswith("Cell"):			#litrally
		line1=line.split()				#split at every space . now line1 is a list with each word of line of "line" starting with "cell"
	#	print(line1)
	#	print (line1[4])
		cells.append(line1[4])			#mac address in there

	if line.startswith("Quality"):
		line5=line.split()
		line6=line5[2].split("=")
	#	print line6[1]
		cells.append(line6[1])


c=0
for i in range(0,len(cells)):
	if i%2==0:
		dict_wifi[c].append(cells[i])
		dict_wifi[c].append(cells[i+1])
		dict_wifi[c].append(str(	))
		c=c+1

# print(dict_wifi.keys())
"""for i in dict_wifi.keys():					#dict_wifi.keys()=indexes of this list(or "dictionary") i.e 0 to 19
	if dict_wifi[i]!=[]:
		print (i,'   ',)
		for j in dict_wifi[i]:
			print(j)
			#print (j,'    ',)				kya hai ye????
		print ('\n')"""
############################################################################################################

fp=open('input.csv','w')	# Open the file in writing mode
for  i in dict_wifi.keys():
	if dict_wifi[i]!=[]:
		fp.write(dict_wifi[i][0]+"	"+dict_wifi[i][1]+"\n")	# Writing to the file line by line
fp.close()

#.................................................................................................input done

c= 0
l={1:['(0,2)1.csv',c],2:['(0,4)1.csv',c],3:['(0,6)1.csv',c],4:['(0,8)1.csv',c],5:['(0,0)1.csv',c],6:['(2,0)1.csv',c],7:['(4,0)1.csv',c],8:['(6,0)1.csv',c],9:['(8,0)1.csv',c],10:['(0,-2).csv',c],11:['(0,-4).csv',c],12:['(0,-6).csv',c],13:['(0,-8).csv',c],14:['(0,-10).csv',c],15:['(-2,0).csv',c],16:['(-4,0).csv',c],17:['(-6,0).csv',c],18:['(-8,0).csv',c],19:['(4,4)1.csv',c],20:['(6,4)1.csv',c]}

numberOfCores=multiprocessing.cpu_count()
print(numberOfCores)

startTime = time.time()

def executeModel(cmd):
    print ("Processing for ", cmd[0])
    fpd = open(cmd[0])  # Open the file in reading mode

    for line1 in fpi:
        imac, istrength = line1.split("	")
        #print(imac, "-->", istrength)
        fpi = open("input.csv")
        for line in fpd:                        # checking line by line
            mac, strength = line.split("	")
            if mac == imac and strength == istrength:
                print("hulle hulare, hulle hulle hullare")
                cmd[1]  = cmd[1] + 1
        # print (mac,"-->",strength)
        fpi.close()
    fpd.close()


    print ("Done for", cmd[0],cmd[1])
    return
# ......................................................................................execute function over

c = 0

for i in l:

    t = threading.Thread(target=executeModel, args=(l[i],))
    t.start()
    c = c + 1
   # print("Running ...... ", c, "/", len(modelProgramName))  # change it!!
    # time.sleep(1)
    while True:
        if threading.activeCount() <= numberOfCores:
            break
        time.sleep(1)

while True:
    #print(threading.activeCount())
    if threading.activeCount() == 1:
        break
    time.sleep(5)
    print("Model Left ... ", threading.activeCount() - 1)

# --------------------------------------------------------------
# Step 9: printing max value
# --------------------------------------------------------------
maxval = 0
for a in l:
    print(l[a][0], " --> ", l[a][1])
    if l[a][1] > maxval:
        maxval = l[a][1]
        maxpos = l[a][0]
print("\nYou are here-->", maxpos, "=", maxval)

# --------------------------------------------------------------
# Step 10: Grand Total Running Time
# --------------------------------------------------------------
totalTime = time.time() - startTime
print("\n\nTotal Running Time:", totalTime, " sec")
print("\nFinished\n")

