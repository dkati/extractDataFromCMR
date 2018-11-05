import os 
from os import listdir
from os.path import isfile, join

CMRPath="cmr"

if os.path.exists('inputProduct/cleanAndLabeled.txt'):
	print('Product file deleted');
	os.remove('inputProduct/cleanAndLabeled.txt');

print('Grabbing _products.txt...')

hClean = open('inputProduct/cleanAndLabeled.txt', "a")


print('Working...')
onlyfiles = [f for f in listdir(CMRPath) if isfile(join(CMRPath, f))]
dirs = str(onlyfiles);
dirs = dirs.replace("]","");
dirs = dirs.replace("[","");
dirs = dirs.replace("'","");

hClean.write('IDs,'+str(dirs)+'\n');

with open ('inputProduct/_product.txt') as finalProduct:
	lines = finalProduct.readlines();
	for line in lines:
		line=line.replace("[","");
		line=line.replace("]","");
		hClean.write(line)
hClean.close()
print('Done...')