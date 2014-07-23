#new file for fixed dataset
fileW =  open("newfile.txt", "w")
#original dataset
fileR = open('table1.csv', 'r')
#loop through the data
i=1
for line in fileR:
	s=line.split(",")
	#use only rows that have 13 attributes. 
	if len(s)==13:
		print i, len(s)
		i = i+1
		#title attribute has commas (it ruins data import delimited by commas so we remove the title attribute)
		sw = ",".join([s[0],s[1],s[2],"TITLE HERE WITHOUT COMMAS",s[-9],s[-8],s[-7],s[-6],s[-5],s[-4],s[-3],s[-2],s[-1]])
		fileW.write(sw)

fileR.close()
fileW.close()
