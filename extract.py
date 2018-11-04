
import os
from os import listdir
from os.path import isfile, join
from collections import Counter
import bisect
		
mypath="cmr"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

allIDs_FileName 	= '_allIDs.txt';
validIDs_FileName 		= '_validIDs.txt' ;
productName 		= '_product.txt';
debug__ALLDATA__ 	= 'debug__ALLDATA__.txt';
debug__validids__ 	= 'debug__VALIDIDS__.txt';
#Clean out first
if os.path.exists(allIDs_FileName):
	print('results file deleted');
	os.remove(allIDs_FileName);
if os.path.exists(validIDs_FileName):
	print('IDs file deleted');
	os.remove(validIDs_FileName);
if os.path.exists(productName):
	print('Product file deleted');
	os.remove(productName);
if os.path.exists(debug__ALLDATA__):
	print('DEBUG file of all data deleted');
	os.remove(debug__ALLDATA__);
if os.path.exists(debug__validids__):
	print('DEBUG file of all valid IDs deleted');
	os.remove(debug__validids__);
	
hResults = open(allIDs_FileName, "a")

print('Working...')

# our big array
__ALLDATA__ 	= [];
__VALIDIDS__ 	= []; 													# mem prealloc
#grab all the ids
for myfile in onlyfiles:
	with open('cmr/'+ myfile) as f:
		lines = f.readlines();
		for line in lines:
			id_,value_ = line.split(" ")
			__ALLDATA__.append(											# hack into the string and remove the \n char
			[id_,float(value_.replace("\n",""))]
			)	
			hResults.write(id_+'\n')
hResults.close()

#Read the produced-all IDs and sort em 
#in order to help Counter()
sortedResults=[]; 														# mem prealloc
with open(allIDs_FileName) as f:
	lines = f.readlines();
for line in lines:
	sortedResults.append( int (line) ) 									# an inline type casting is required here. #PYTHONIZED
sortedResults.sort(); 


c = Counter(sortedResults); # tailing the list
with open (validIDs_FileName,"a") as validIDs_:
	for id in sortedResults:								
		if c[id] == len(onlyfiles):										# If you find that ID , `len(onlyfiles)` times...
			validIDs_.write(str(id)+"\n") 								# ...append it to the new file
			del c[id] 													# ...and remove it from the queue


#Read the valid IDs now (reopening the fstream)
with open (validIDs_FileName) as validIDsAgain_:
	__VALIDIDS__ = validIDsAgain_.readlines();

if __debug__:
	with open('debug__VALIDIDS__.txt','w') as f:
   		f.writelines("%s\n" % item for item in __VALIDIDS__)
	with open('debug__ALLDATA__.txt','w') as f:
   		f.writelines("%s\n" % item for item in __ALLDATA__)

		
index=0;
maxIDs = len(__VALIDIDS__)
#Create the final product
with open (productName,"a") as product_:
	for validid in __VALIDIDS__:
		values=[];
		for globalData in __ALLDATA__:
			gID = int(globalData[0])
			gvalue = float(globalData[1])
			print(str(gID) + "<--->" + str(validid))
			print("Index of parsing ID:"+ str(index)+"/"+str(maxIDs))	# #PYTHONIZED
			if gID == int(validid): 
				values.append(gvalue)
		myappend=str(int(validid))+","+str(values); 					# #PYTHONIZED
		product_.write(myappend);
		print('...')
		index+=1


print('Done...')
print('Happy Easter')	
