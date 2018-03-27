#!/usr/bin/env python3
'''input file: 1 text file of 5C regions (bed file), 1 bed file from macs peak calling. 
Find the 5C regions overlap with narrow peaks , and return these peaks as bed file'''

from optparse import OptionParser
import os
import sys



if __name__=='__main__':

	parser = OptionParser()
	parser.add_option("-i", "--input1", type="string", dest="filename1",help="5C region file", metavar="FILE")
	parser.add_option("-j", "--input2", type="string", dest="filename2",help="Narrowpeaks bed file", metavar="FILE")
	parser.add_option("-o", "--output", type="string", dest="out_fname",help="Output file name. ", metavar="FILE")
	(options, args) = parser.parse_args()
	
	
	table1=[]
	table2=[]
	
	count1=0
	count2=0
	
	with open(options.filename1) as file1:
		for line in file1:
			linetemp=line.split()
			chrom=linetemp[0]
			a1=linetemp[1]
			a2=linetemp[2]
			table1.append([chrom, (int(a1),int(a2))])
			count1+=1

	
	with open(options.filename2) as file2:
		for line in file2:
			linetemp=line.split()
			chrom=linetemp[0]
			b1=linetemp[1]
			b2=linetemp[2]
			table2.append([chrom, (int(b1), int(b2))])
			count2 += 1
			
	dict1={}
	dict2={}
	
	for key, val in table1:
		dict1.setdefault(key,[]).append(val)
	for key, val in table2:
		dict2.setdefault(key,[]).append(val)
		
	count=0
	with open(options.out_fname,"w") as out_f:
		for chrom1 in dict1:
			for c1 in dict1[chrom1]:
				for c2 in dict2[chrom1]:
					if c1[1]>c2[0] and c1[0]<c2[1]:
						out_f.write('%s\t%s\t%s\n' %(chrom1,c2[0],c2[1]))
						count +=1
						
	print("number of peak overlaps %s" %count)
					
		
		
		