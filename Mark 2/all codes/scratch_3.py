
def main():
	#position.py code
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
			dict_wifi[c].append(str("	"))
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


	c=0
	#c1=0
	#c2=0
	#l = {1:['(0,2).csv',c],2:['(0,4).csv',c],3:['(0,6).csv',c],4:['(0,8).csv',c],5:['(0,0).csv',c],6:['(2,0).csv',c],7:['(4,0).csv',c],8:['(6,0).csv',c],9:['(8,0).csv',c],10:['(0,-2).csv',c],11:['(0,-4).csv',c],12:['(0,0).csv',c],13:['(0,-8).csv',c],14:['(0,-10).csv',c],15:['(-2,0).csv',c],16:['(-4,0).csv',c],17:['(-6,0).csv',c],18:['(-8,0).csv',c],19:['(4,4).csv',c],20:['(6,4).csv',c],21:['(5,-4).csv',c],22:['(-6,5).csv',c],23:['(-4,-4).csv',c],24:['(-6,-8).csv',c]}
	l = {1: ['(0,2)u.csv', c], 2: ['(0,4)u.csv', c], 3: ['(0,6)u.csv', c], 4: ['(0,8)u.csv', c], 5: ['(0,0)u.csv', c],6: ['(2,0)u.csv', c], 7: ['(4,0)u.csv', c], 8: ['(6,0)u.csv', c], 9: ['(8,0)u.csv', c], 10: ['(0,-2)u.csv', c],11: ['(0,-4)u.csv', c], 12: ['(0,-6)u.csv', c], 13: ['(0,-8)u.csv', c], 14: ['(0,-10)u.csv', c],15: ['(-2,0)u.csv', c], 16: ['(-4,0)u.csv', c], 17: ['(-6,0)u.csv', c], 18: ['(-8,0)u.csv', c],19: ['(4,4)u.csv', c], 20: ['(6,4)u.csv', c], 21: ['(5,-4)u.csv', c], 22: ['(-6,5)u.csv', c],23: ['(-4,-4)u.csv', c], 24: ['(-6,-8)u.csv', c]}

	fpi=open("input.csv")
	for line1 in fpi:
		#c2=c2+1
		imac,istrength=line1.split("	")
		#print(imac,"-->",istrength)
		for str1 in l:
			#print(l[str][0],type(l[str][0]))
			fpd=open(l[str1][0])		# Open the file in reading mode
			for line in fpd: # print line by line
				#c1=c1+1
				mac,strength=line.split("	")
				if mac==imac and strength==istrength:                   #sj1- if the file is unique, then break once found to avoid redundant search
					l[str1][1]=l[str1][1]+1
				#print (mac,"-->",strength)
			fpd.close()
	fpi.close()
	#print(l,type(l))
	#print(l[1][0])
	maxval=0
	for a in l:
		print(l[a][0]," --> ",l[a][1])
		if l[a][1]>maxval:
			maxval=l[a][1]
			maxpos=l[a][0]
	print("\nYou are here-->",maxpos,"=",maxval)
	#print(c1/c2)
																		# sj2-...? till last
	lc1 = maxpos.strip("()ucsv.")
	lc2 = lc1.split(",")

	r = open("cood.csv", 'a')
	r.write(lc2[0] + "\t" + lc2[1]+"\n")
	r.close()

if __name__ == "__main__":
    main()