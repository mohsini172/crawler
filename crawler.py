import os
import json
import sys
import datetime
from socket import *


log = open("slog.txt",'wb')
index = dict();



def createIndex(filename,path):
	onlyname =  os.path.splitext(filename)[0];
	onlyname = onlyname.split('-');
	for i in onlyname:

		if i in index:
			index[i].append(path);
		else:
			index[i] = [];
			index[i].append(path);

	indexpath = path.split('/');
	for i in indexpath:
		if i in index:
			index[i].append(path);
		else:
			index[i] = [];
			index[i].append(path);



	# print index;
	# print '-----------------------------------';
	inFile=open(path,'r');
	for line in inFile:
		line = line.split();
		for i in line:
			if i in index:
				index[i].append(path);
			else:
				index[i] = [];
				index[i].append(path);
	return

# createIndex('sample','/home/mohsin/abc/pintos/src/tests/userprog/sample.txt')

def search():
	result = {}
	for root, dirs, files in os.walk("/home"):
		for file in files:
			if file.endswith(".txt"):
				pathname = os.path.join(root, file);
				createIndex(file,pathname);

search();

print "--------------------------------------\n---------------------------------------\n";
print "Unit test\n";
#unit test
if "mmm" in index:
	print index["mmm"];
	print "---------------expected----------------\n";
	print ['/home/mohsin/Documents/aplab/a.txt', '/home/mohsin/Documents/aplab/abc.txt'];
	print "\n"



searchFileName = raw_input("Enter the name of the file\n");
if searchFileName in index:
	print index[searchFileName];


