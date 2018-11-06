import os
from shutil import copyfile
from os.path import isfile,join

productFilename	="cleanAndLabeled.txt";
facetsFilename	="facetsOUT.csv";
mergedFilename	="OUT/merged.csv";
productCSVFilename = "OUT/product.csv";
if os.path.exists(mergedFilename):
	print('Old indexes file deleted');
	os.remove(mergedFilename);
if os.path.exists(productCSVFilename):
	print('Old product CSV file deleted');
	os.remove(productCSVFilename);
	
copyfile(productFilename,productCSVFilename);

with open(facetsFilename,"r") as hFacets:
	facetsLines = hFacets.readlines();

# Read again the product CSV
with open(productCSVFilename,"r") as hProduct:
	productLines = hProduct.readlines();
	
productLabel = productLines[0];
del productLines[0]; # Remove the labelling line
validIDs=[];
for line in productLines:
	# Read the productLines, grab the ID and create an array with the valid IDS
	validIDs.append(line.split(',',1)[0]);

facetLabel = facetsLines[0];
del facetsLines[0] #remove facets labelling
index=0;
hMerged = open(mergedFilename,"a");
for productLine in productLines:
	for facetline in facetsLines:
		if productLine.split(',',1)[0] == facetline.split(',',1)[0]:
			str_ = productLine +","+facetline
			str_ = str_.replace("\n","");
			hMerged.write( str_+"\n");
hMerged.close();