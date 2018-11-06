import os
from os.path import isfile,join
facetsFileName 	= "facets.stl"
facetsOutput	= "OUT/facetsOUT.csv"
facetsClean 	= "OUT/facetsClean_.csv"
if os.path.exists(facetsOutput):
	print('Old indexes file deleted');
	os.remove(facetsOutput);

with open(facetsFileName,"r") as hFacets:	#Read
	lines = hFacets.readlines();

#clean the hell out
del lines[0]; # thats the first line which is not needed
cleanindex = 0 ;
for line in lines:
	if "loop" in lines[cleanindex]:
		del lines[cleanindex]
	if "endfacet" in lines[cleanindex]:
		del lines[cleanindex]
	cleanindex+=1;

# Filtering
index=0;
facetID = 0;
hOut = open (facetsOutput,"a");
hOut.write("facetID,X,Y,Z,x1,y1,z1,x2,y2,z2,x3,y3,z3\n");
while index < len(lines):

	nullable,facet,type,X,Y,Z=lines[index].split(" ");
	index +=1;
	#first vertex
	nullable, nullable2, vertex, X1, Y1, Z1 = lines[index].split(" ");
	index+=1;
	#second vertex
	nullable, nullable2, vertex, X2, Y2, Z2 = lines[index].split(" ");
	index+=1;
	#third vertex
	nullable, nullable2, vertex, X3, Y3, Z3 = lines[index].split(" ");
	
	currAppend = str(facetID)+","+X+","+Y+","+Z+","+X1+","+Y1+","+Z1+","+X2+","+Y2+","+Z2+","+X3+","+Y3+","+Z3;
	currAppend = currAppend.replace("\n","");
	currAppend = currAppend.replace(" ","");
	hOut.write(currAppend+"\n");

	index+=2;
			
	facetID += 1;
	if "endsolid" in lines[index]:
		break;
hOut.close();