#!/usr/bin/env python 

import argparse
from Bio import SeqIO
import re

def fixfasta(fapath, outfile, headerid):
	handle = open(outfile, "w")
	record = next(SeqIO.parse(fapath, "fasta"))
	record.id = str(headerid)
	record.name = ""
	record.description = ""
	SeqIO.write(record, handle, "fasta")
	handle.close()

def getfasta(fapath, outfile, headerid):
	handle = open(outfile, "w")
	for record in SeqIO.parse(fapath, "fasta"):
		if re.search("fasta/", record.id):
			record.id = str(headerid)
			record.name = ""
			record.description = ""
			SeqIO.write(record, handle, "fasta")
			handle.close()

def parse_arguments():
	parser = argparse.ArgumentParser(description='Extraxt first sequence in Fasta and fix header')
	parser.add_argument("fa_path", help="Path to GFA-file")
	parser.add_argument("output", help="Output file")
	parser.add_argument("headerid", help="Id to use in header")
	args = parser.parse_args()
	return args

def main():
	args = parse_arguments()
	getfasta(args.fa_path, args.output, args.headerid)

if __name__ == '__main__':
    main()
