#!/usr/bin/python3

from sys import argv
from os.path import exists

script, from_file, to_file = argv

'''
in_file = open(from_file)
indata = in_file.read()


print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")

out_file = open(to_file, 'w')
out_file.write(indata)

print(f"{from_file} copied to {to_file}")
'''

open(to_file, 'w').write(open(from_file).read())
