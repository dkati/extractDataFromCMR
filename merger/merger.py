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
	
with open(productFilename,"r") as hProduct:
	productLines = hProduct.readlines();
with open(facetsFilename,"r") as hFacets:
	facetsLines = hFacets.readlines();

#clean out the '[' and ']', ...
index=0;
for line in productLines:
	productLines[index] = productLines[index].replace("[","");
	productLines[index] = productLines[index].replace("]","");
	index+=1;
#...and convert the file to csv
with open(productCSVFilename,"a") as hProduct:
	for line in productLines:
		hProduct.write(line);

	