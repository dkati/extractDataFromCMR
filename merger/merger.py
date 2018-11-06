import os
from os.path import isfile,join
productFilename	="_product.txt";
facetsFilename	="facetsOUT.csv";
mergedFilename	="OUT/merged.csv";
productCSVFilename = "OUT/product.csv";
if os.path.exists(mergedFilename):
	print('Old indexes file deleted');
	os.remove(mergedFilename);
if os.path.exists(productCSVFilename):
	print('Old product CSV file deleted');
	os.remove(productCSVFilename);
	
hCSVproduct = open(productCSVFilename,"a");
with open(productFilename,"r") as hProduct:
	productLines = hProduct.readlines();
	index=0;
	#clean out the '[' and ']'...
	for line in productLines:
		productLines[index] = productLines[index].replace("[","");
		productLines[index] = productLines[index].replace("]","");
		index+=1;
	#Convert to CSV and paste it to OUT folder
	for line in productLines:
		hCSVproduct.write(line);  
with open(facetsFilename,"r") as hFacets:
	facetsLines = hFacets.readlines();
hCSVproduct.close(); #Close the stream

# Read again the product CSV
with open(productCSVFilename,"r") as hProduct:
	productLines = hProduct.readlines();
	
validIDs=[];
for line in productLines:
	# Read the productLines, grab the ID and create an array with the valid IDS
	validIDs.append(line.split(',',1)[0]);
	