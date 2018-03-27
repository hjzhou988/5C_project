#!/usr/bin/env python3
# input file: 2 summit bed files. Find the intersection set. If the distance between summits  < Dstn, then they are overlapped. Output the summit coordinates of file 1.

from optparse import OptionParser
import os
import sys



if __name__=='__main__':

	parser = OptionParser()
	parser.add_option("-i", "--input1", type="string", dest="filename1",help="Input file 1", metavar="FILE")
	parser.add_option("-j", "--input2", type="string", dest="filename2",help="Input file 2", metavar="FILE")
	parser.add_option("-k", "--input3", type="string", dest="filename3",help="Input file 3", metavar="FILE")
	parser.add_option("-l", "--input4", type="string", dest="filename4",help="Input file 4", metavar="FILE")
	parser.add_option("-o", "--output", type="string", dest="out_fname",help="Output file name. ", metavar="FILE")
	(options, args) = parser.parse_args()
	
	Dstn=50
	
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
			end=linetemp[2]
			table1.append([chrom, int(end)])
			count1 += 1
	
	with open(options.filename2) as file2:
		for line in file2:
			linetemp=line.split()
			chrom=linetemp[0]
			end=linetemp[2]
			table2.append([chrom, int(end)])
			count2 += 1
	if options.filename3:
		with open(options.filename3) as file3:
			for line in file3:
				chrom,start,end=line.replace (':',' ').replace('-',' ').split()
				table3.append([chrom, (int(start)+int(end))/2])
				count3 += 1
	if options.filename4:
		with open(options.filename4) as file4:
			for line in file4:
				chrom,start,end=line.replace (':',' ').replace('-',' ').split()
				table4.append([chrom, (int(start)+int(end))/2])
				count4 += 1
			
	dict1={}
	dict2={}
	dict3={}
	dict4={}
	
	for key, val in table1:
		dict1.setdefault(key,[]).append(val)
	for key, val in table2:
		dict2.setdefault(key,[]).append(val)
	if table3:
		for key, val in table3:
			dict3.setdefault(key,[]).append(val)
	if table4:
		for key, val in table4:
			dict4.setdefault(key,[]).append(val)
		
	count=0
	
	if table3==[] and table4==[]:
		with open(options.out_fname,'w') as out_f:
			for chrom1 in dict1:
				if chrom1 not in list(dict2.keys()):
					continue
				for c1 in dict1[chrom1]:
					for c2 in dict2[chrom1]:
						if abs(c1-c2)<Dstn:
							count +=1
							out_f.write('%s\t%s\t%s\n' %(chrom1, c1-1,c1))
							break

						
			print("number of peak overlaps %s" %count)
			print("accounting for %.1f%% of %s counts in %s" %((float(count)/count1*100),count1,options.filename1))
			print("accounting for %.1f%% of %s counts in %s" %((float(count)/count2*100),count2,options.filename2))
		
	
	if table3!=[] and table4==[]:
		for chrom1 in dict1:
			if chrom1 not in list(dict2.keys()):
				continue
			if chrom1 not in list(dict3.keys()):
				continue
			for c1 in dict1[chrom1]:
				for c2 in dict2[chrom1]:
					if abs(c1-c2)<Dstn:
						for c3 in dict3[chrom1]:
							if abs(c1-c3)<Dstn and abs(c2-c3)<Dstn:
								count += 1
		print("number of peak overlaps %s" %count)
		print("accounting for %.1f%% of %s counts in %s" %((float(count)/count1*100),count1,options.filename1))
		print("accounting for %.1f%% of %s counts in %s" %((float(count)/count2*100),count2,options.filename2))
		print("accounting for %.1f%% of %s counts in %s" %((float(count)/count3*100),count3,options.filename3))
							
	if table3!=[] and table4!=[]:
		for chrom1 in dict1:
			if chrom1 not in list(dict2.keys()):
				continue
			if chrom1 not in list(dict3.keys()):
				continue
			if chrom1 not in list(dict4.keys()):
				continue
			for c1 in dict1[chrom1]:
				for c2 in dict2[chrom1]:
					if abs(c1-c2)<Dstn:
						for c3 in dict3[chrom1]:
							if abs(c1-c3)<Dstn and abs(c2-c3)<Dstn:
								for c4 in dict4[chrom1]:
									if abs(c1-c4)<Dstn and abs(c2-c4)<Dstn and abs(c3-c4)<Dstn:
										count +=1
		print("number of peak overlaps %s" %count)
		print("accounting for %.1f%% of %s counts in %s" %((float(count)/count1*100),count1,options.filename1))
		print("accounting for %.1f%% of %s counts in %s" %((float(count)/count2*100),count2,options.filename2))
		print("accounting for %.1f%% of %s counts in %s" %((float(count)/count3*100),count3,options.filename3))
		print("accounting for %.1f%% of %s counts in %s" %((float(count)/count4*100),count4,options.filename4))
	
					
		
		
		