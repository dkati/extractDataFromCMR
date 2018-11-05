import os
allIDs_FileName 	= '_allIDs.txt';
validIDs_FileName 	= '_validIDs.txt' ;
product_FileName 	= '_product.txt';
debug__alldata__ 	= 'debug__ALLDATA__.txt';
debug__validids__ 	= 'debug__VALIDIDS__.txt';

if os.path.exists('labelizeOUT/cleanAndLabeled.txt'):
	print('Clean product file deleted');
	os.remove('labelizeOUT/cleanAndLabeled.txt');
if os.path.exists('labelizeOUT/_product.txt'):
	print('Product file deleted');
	os.remove('labelizeOUT/_product.txt');
if os.path.exists(allIDs_FileName):
	print('results file deleted');
	os.remove(allIDs_FileName);
if os.path.exists(validIDs_FileName):
	print('IDs file deleted');
	os.remove(validIDs_FileName);
if os.path.exists(debug__alldata__):
	print('DEBUG file of all data deleted');
	os.remove(debug__alldata__);
if os.path.exists(debug__validids__):
	print('DEBUG file of all valid IDs deleted');
	os.remove(debug__validids__);

cleanProd = input('Remove product file? (y/n)\n')
while cleanProd != 'y' and cleanProd != 'n':
	print('Incorrect input.Please type (y/n)\n')
	cleanProd = input('Remove product file? (y/n)\n')

if cleanProd == 'y':
	if os.path.exists(product_FileName):
		print('Product file deleted');
		os.remove(product_FileName);
