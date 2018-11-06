import os 
from os import listdir
from os.path import isfile, join
from shutil import copyfile

CMRPath="cmr"

if os.path.exists('labelizeOUT/cleanAndLabeled.txt'):
	print('Clean product file deleted');
	os.remove('labelizeOUT/cleanAndLabeled.txt');

if os.path.exists('labelizeOUT/_product.txt'):
	print('Product file deleted');
	os.remove('labelizeOUT/_product.txt');


print('Grabbing _products.txt...')
if not os.path.exists('labelizeOUT'):
    os.makedirs('labelizeOUT')
copyfile('_product.txt','labelizeOUT/_product.txt');


hClean = open('labelizeOUT/cleanAndLabeled.txt', "a")
print('Working...')
onlyfiles = [f for f in listdir(CMRPath) if isfile(join(CMRPath, f))]
dirs = str(onlyfiles);
dirs = dirs.replace("]","");
dirs = dirs.replace("[","");
dirs = dirs.replace("'","");

hClean.write('IDs,'+str(dirs)+'\n');

with open ('labelizeOUT/_product.txt') as finalProduct:
	lines = finalProduct.readlines();
	for line in lines:
		line=line.replace("[","");
		line=line.replace("]","");
		hClean.write(line)
hClean.close()
print('Done...')