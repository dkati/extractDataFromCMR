import os
from os import listdir
from os.path import isfile, join
from collections import Counter

CMRPath="cmr"
onlyfiles = [f for f in listdir(CMRPath) if isfile(join(CMRPath, f))]

allIDs_FileName 	= '_allIDs.txt';
validIDs_FileName 	= '_validIDs.txt' ;
product_FileName 	= '_product.txt';
debug__alldata__ 	= 'debug__ALLDATA__.txt';
debug__validids__ 	= 'debug__VALIDIDS__.txt';
#Clean out first
if os.path.exists(allIDs_FileName):
	print('results file deleted');
	os.remove(allIDs_FileName);
if os.path.exists(validIDs_FileName):
	print('IDs file deleted');
	os.remove(validIDs_FileName);
if os.path.exists(product_FileName):
	print('Product file deleted');
	os.remove(product_FileName);
if os.path.exists(debug__alldata__):
	print('DEBUG file of all data deleted');
	os.remove(debug__alldata__);
if os.path.exists(debug__validids__):
	print('DEBUG file of all valid IDs deleted');
	os.remove(debug__validids__);
	

print('Working...')

hResults = open(allIDs_FileName, "a")
ALLDATA__ 	= [];
VALIDIDS__ 	= []; 							# mem prealloc
#grab all the ids
for myfile in onlyfiles:
	with open('cmr/'+ myfile) as f:
		lines = f.readlines();
		for line in lines:
			id_,value_ = line.split(" ")
			ALLDATA__.append(				# hack into the string and remove the \n char
			[id_,float(value_.replace("\n",""))]
			)	
			hResults.write(id_+'\n')
hResults.close()

#Read the produced-all IDs and sort em 
#in order to help Counter()
sortedResults=[]; 							# mem prealloc
with open(allIDs_FileName) as f:
	lines = f.readlines();
for line in lines:
	sortedResults.append( int (line) ) 				# an inline type casting is required here. #PYTHONIZED
sortedResults.sort(); 


c = Counter(sortedResults); # tailing the list
with open (validIDs_FileName,"a") as validIDs_:
	for id in sortedResults:								
		if c[id] == len(onlyfiles):				# If you find that ID , `len(onlyfiles)` times...
			validIDs_.write(str(id)+"\n") 			# ...append it to the new file
			del c[id] 					# ...and remove it from the queue


#Read the valid IDs now (reopening the fstream)
with open (validIDs_FileName) as validIDsAgain_:
	VALIDIDS__ = validIDsAgain_.readlines();


with open(debug__validids__,'w') as f:
   	f.writelines("%s\n" % item for item in VALIDIDS__)
with open(debug__alldata__,'w') as f:
   	f.writelines("%s\n" % item for item in ALLDATA__)

		
index=0;
maxIDs = len(VALIDIDS__)

#max lines 893410
#Create the final product
smartIndex = 0;
myindex = 0;
with open (product_FileName,"a") as product_:
	for validid in VALIDIDS__:
		values=[];
		myindex=0;
		smartIndex=0;
		print("Index of parsing ID:"+ str(index)+"/"+str(maxIDs))	
		while myindex <= 893410:

			gID = int(ALLDATA__[myindex][0])
			gvalue = float(ALLDATA__[myindex][1])

			if gID == int(validid): 
				values.append(gvalue)
				myindex += 100;
				smartIndex+=1;
			else:
				myindex+=1;

			if smartIndex == 60:
				myindex=893410+1;
			

		#integrity check
		if len(values) == 60:
			myappend=str(int(validid))+","+str(values); 		
		else:
			myappend='Error on ID:'+str(int(validid));		
		product_.write(myappend+'\n');
		print('...')
		index+=1
		if index == 3:
			break;


print('Done...')
print('Happy Easter')	
