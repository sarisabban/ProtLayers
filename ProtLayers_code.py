#!/usr/bin/python3

import re , itertools , numpy , sys , Bio.PDB 

filename=sys.argv[1]						#file input from command line
								#_
p = Bio.PDB.PDBParser()						# |
structure = p.get_structure('X' , filename)			# |Standard structure to setup biopython's DSSP to calculate SASA using Wilke constants
model = structure[0]						# |
dssp = Bio.PDB.DSSP(model , filename , acc_array='Wilke')	#_|

lis = list()
count = 0
for x in dssp:							#Loop to isolate SASA for each amino acid
	if x[1]=='A' : sasa=129*(x[3])
	elif x[1]=='V' : sasa=174*(x[3])
	elif x[1]=='I' : sasa=197*(x[3])
	elif x[1]=='L' : sasa=201*(x[3])
	elif x[1]=='M' : sasa=224*(x[3])
	elif x[1]=='P' : sasa=159*(x[3])
	elif x[1]=='Y' : sasa=263*(x[3])
	elif x[1]=='F' : sasa=240*(x[3])
	elif x[1]=='W' : sasa=285*(x[3])
	elif x[1]=='R' : sasa=274*(x[3])
	elif x[1]=='N' : sasa=195*(x[3])
	elif x[1]=='C' : sasa=167*(x[3])
	elif x[1]=='Q' : sasa=225*(x[3])
	elif x[1]=='E' : sasa=223*(x[3])
	elif x[1]=='G' : sasa=104*(x[3])
	elif x[1]=='H' : sasa=224*(x[3])
	elif x[1]=='K' : sasa=236*(x[3])
	elif x[1]=='S' : sasa=155*(x[3])
	elif x[1]=='T' : sasa=172*(x[3])
	elif x[1]=='D' : sasa=193*(x[3])
	lis.append((x[2] , sasa))

#Label each amino acid depending on its SASA position according to the parameters highlighted in the paper by (Koga et.al., 2012 - PMID: 23135467). The parameters are as follows:
#Surface:
#	Helix or Sheet:	SASA => 60
#	Loop:		SASA => 40
#
#Boundry:
#	Helix or Sheet:	15 < SASA < 60
#	Loop:		25 < SASA < 40
#
#Core:
#	Helix or Sheet:	SASA =< 15
#	Loop:		SASA =< 25
#
#DSSP:
#Loop =		- or T or S
#Helix =	G or H or I
#Sheet =	B or E

core = list()
boundary = list()
surface = list()
count = 0
for x , y in lis:
	count = count + 1

	if y <= 25 and (x == '-' or x == 'T' or x == 'S'):		#Loop
		core.append(count)
	elif 25 < y < 40 and (x == '-' or x == 'T' or x == 'S'):	#Loop
		boundary.append(count)
	elif y >= 40 and (x == '-' or x == 'T' or x == 'S'):		#Loop
		surface.append(count)

	elif y <= 15 and (x == 'G' or x == 'H' or x == 'I'):		#Helix
		core.append(count)
	elif 15 < y < 60 and (x == 'G' or x == 'H' or x == 'I'):	#Helix
		boundary.append(count)
	elif y >= 60 and (x == 'G' or x == 'H' or x == 'I'):		#Helix
		surface.append(count)

	elif y <= 15 and (x == 'B' or x == 'E'):			#Sheet
		core.append(count)
	elif 15 < y < 60 and (x == 'B' or x == 'E'):			#Sheet
		boundary.append(count)
	elif y >= 60 and (x == 'B' or x == 'E'):			#Sheet
		surface.append(count)

Surf = '+'.join(str(z) for z in surface)
Bound = '+'.join(str(z) for z in boundary)
Core = '+'.join(str(z) for z in core)

#Print the custom PYMOL commands to select the different protein layers according to each amino acid's SASA.
print('select Surf , resi' , Surf)
print('select Bound , resi' , Bound)
print('select Core , resi' , Core)
print('color red , Core')
print('color magenta , Bound')
print('color green , Surf')
print('hide all')
print('show cartoon')
