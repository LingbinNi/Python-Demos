#/usr/bin/env python
#written by Lingbin

#Extract sequences from diverse genomes

import os
import pysam
import fnmatch

f = open("/home/share/TIANDATA13/lbni/02.SNPAnalysis/03.SNVAnalysis/04.BoundaryNonSVSNV/02.BoundaryNonSVSNV/BoundaryNonSVSNV.table")
out1 = open("BoundaryNonSVSNV.fa","a+")
out2 = open("BoundaryNonSVNonSNV.fa","a+")

for line in f.readlines():
		line = line.strip()
		list = line.split("\t")
		chr = list[0]
		start = list[1]
		end = list[2]
		sample = list[4]
		type = list[-1]
		if type == "SNP":
			ref = pysam.FastaFile(os.path.join("/home/share/TIANDATA13/lbni/DataBase/04.genome", "".join(fnmatch.filter(os.listdir("/home/share/TIANDATA13/lbni/DataBase/04.genome"),sample+'.v*.fasta'))))
			out1.write(">" + "-".join((sample,chr,start,end)) + "\n")
			out1.write(ref.fetch(chr)[int(start)-1:int(end)] + "\n")
		if type == "NonSNP":
			ref = pysam.FastaFile(os.path.join("/home/share/TIANDATA13/lbni/DataBase/04.genome", "".join(fnmatch.filter(os.listdir("/home/share/TIANDATA13/lbni/DataBase/04.genome"),sample+'.v*.fasta'))))
			out2.write(">" + "-".join((sample,chr,start,end)) + "\n")
			out2.write(ref.fetch(chr)[int(start)-1:int(end)] + "\n")

f.close()
out1.close()
out2.close()
