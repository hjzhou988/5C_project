#!/usr/bin/env python3
'''Given TF A coordinates and TF B coordinates, keep A coordinates that do not overlap with B by 
distance between summits less than Dstn. input file:  
1. summit bed files from TF A.  2. summit bed files from TF B.
'''

from optparse import OptionParser
import os
import sys



if __name__=='__main__':

	parser = OptionParser()
	parser.add_option("-i", "--input1", type="string", dest="filename1",help="Summit Bed file of TF A", metavar="FILE")
	parser.add_option("-j", "--input2", type="string", dest="filename2",help="Summit Bed file of TF B)", metavar="FILE")
	parser.add_option("-o", "--output", type="string", dest="out_fname",help="Output file name. ", metavar="FILE")
	(options, args) = parser.parse_args()
	
	Dstn=200
	
	table1=[]
	table2=[]
	table3=[]
	table4=[]
	
	count1=0
	count2=0
	count3=0
	count4=0
	
	with open(options.filename1) as file1:
		for line in file1:
			linetemp=line.split()
			chrom=linetemp[0]
			a1=linetemp[1]
			table1.append([chrom, int(a1)]) 
			count1+=1

	
	with open(options.filename2) as file2:
		for line in file2:
			linetemp=line.split()
			chrom=linetemp[0]
			b1=linetemp[1]
			table2.append([chrom, int(b1)])
			count2 += 1
			
	dict1={}
	dict2={}
	dict3={}
	dict4={}
	
	for key, val in table1:
		dict1.setdefault(key,[]).append(val)
	for key, val in table2:
		dict2.setdefault(key,[]).append(val)
		
	count=0
	countA=0

	with open(options.out_fname,'w') as out_f:
		for chrom1 in dict1:
			if chrom1 not in list(dict2.keys()):
				continue
			for c1 in dict1[chrom1]:
				counttemp=count
				for c2 in dict2[chrom1]:
					if abs(c1-c2) < Dstn:  # they overlap
						count +=1
						break
				if counttemp == count: # if count didn't increase, then TF A is by itself
					out_f.write('%s\t%s\t%s\n' %(chrom1,c1,c1+1))
					countA+=1
		print("TF A has %s unique sites." %countA)
		print("TF A and TF B have %s overlapping sites." %count)
		print("accounting for %.1f%% of %s counts in %s" %((float(countA)/count1*100),count1,options.filename1))


					
		
		
		