#! /usr/bin/env python3
#
# A script to replace *** codes in transcripts with one-minute timesatmps in ascending order
# By Aaron Cogbill acogbill@focusfwd.com

ORIGINAL = 4;

import sys, re

def main(start, filename):
	transcript = open(filename, encoding='cp1252', errors='ignore')
	text = transcript.readlines()
	transcript.close()

	# why is this block failing?
	stampRE=re.compile(r'\*\*\*');
	timestamps=[]
	for line in range(len(text)):
		if (stampRE.findall(text[line]) != []):
			timestamps.append(line)

	for line in timestamps:
		parts = text[line].split('***')
		new = parts[0] + stampify(start) + parts[1]
		start += 1
		text[line] = new

    # join the lines into one string
	interpolated_text = ''.join(text)
	interpolated_text.strip()
 
    # write the string to a new file - 'originalfilename ck0.txt'
	argparts = filename.split('.')
	argparts[-2] += ' ck0'
	newname = '.'.join(argparts)
	interpolated_file = open(newname,'w')
	interpolated_file.write(interpolated_text)
	interpolated_file.close()
	print('Wrote version ck0.')


def stampify(min):
	return "(00:" + str(min).rjust(2,'0') + ":00)"


main(4, sys.argv[1])
