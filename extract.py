
import os
from os import listdir
from os.path import isfile, join
from collections import Counter
import bisect
		
mypath="cmr"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

resultsFileName = '_results.txt';
allIDsFileName = '_validIDs.txt' ;
productName = '_product.txt';
debug_alldata = 'debug__ALLDATA__.txt';
debug__validids__ = 'debug__VALIDIDS__.txt';
#Clean out first
if os.path.exists(resultsFileName):
	print('results file deleted');
	os.remove(resultsFileName);
if os.path.exists(allIDsFileName):
	print('IDs file deleted');
	os.remove(allIDsFileName);
if os.path.exists(productName):
	print('Product file deleted');
	os.remove(productName);
if os.path.exists(debug_alldata):
	print('DEBUG file of all data deleted');
	os.remove(debug_alldata);
if os.path.exists(debug__validids__):
	print('DEBUG file of all valid IDs deleted');
	os.remove(debug__validids__);
	
hResults = open(resultsFileName, "a")

print('Working...')

# our big array
__ALLDATA__ = []; 								#mem alloc
#grab all the ids
for myfile in onlyfiles:
	with open('cmr/'+ myfile) as f:
		lines = f.readlines();
		for line in lines:
			id_,value_ = line.split(" ")
			__ALLDATA__.append(					#hack into the string and remove the \n char
			[id_,float(value_.replace("\n",""))]
			)	
			hResults.write(id_+'\n')
hResults.close()

#Read the produced-all IDs and sort em 
#in order to help Counter()
sortedResults=[]; 								#mem alloc
with open(resultsFileName) as f:
	lines = f.readlines();
for line in lines:
	sortedResults.append( int (line) ) 			# an inline type casting is required here. PYTHONIZED
sortedResults.sort(); 


c = Counter(sortedResults); # tailing the list
#print (c)
with open (allIDsFileName,"a") as validIDs_:
	for id in sortedResults:
		#If you find that ID , len(onlyfiles) times...
		if c[id] == len(onlyfiles):
			validIDs_.write(str(id)+"\n") 		# ...append it to the new file
			del c[id] 							# ...and remove it from the queue


#Read the valid IDs now (reopening the fstream)
__VALIDIDS__ = [] 								#mem alloc
with open (allIDsFileName) as validIDsAgain_:
	__VALIDIDS__ = validIDsAgain_.readlines();

#debug that shit
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
			print("Index of parsing ID:"+ str(index)+"/"+str(maxIDs))#pythonized
			if gID == int(validid): 
				values.append(gvalue)
		myappend=str(int(validid))+","+str(values); #pythonized
		product_.write(myappend);
		print('...')
		#exit(0)
		index+=1


print('Done...')
print('Happy Easter')	
