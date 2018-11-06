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
	
del productLines[0]; # Remove the labelling line
validIDs=[];
for line in productLines:
	# Read the productLines, grab the ID and create an array with the valid IDS
	validIDs.append(line.split(',',1)[0]);

del facetsLines[0] #remove facets labelling
