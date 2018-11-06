import os
from os.path import isfile,join
productFilename	="_product.txt";
facetsFilename	="facetsOUT.csv";
mergedFilename	="OUT/merged.csv";
if os.path.exists(mergedFilename):
	print('Old indexes file deleted');
	os.remove(mergedFilename);
	
with open(productFilename,"r") as hProduct:
	productLines = hProduct.readlines();
with open(facetsFilename,"r") as hFacets:
	facetsLines = hFacets.readlines();
	