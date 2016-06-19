'''
Patrick Mogianesi

fileinfo script

This program will get the information of a chosen file
The size of the file
The Name of file


(.stat function)
'''
#the user inputs the path for the file

import os, os.path
import sys

def main():
	print "CTRL-C to exit"
	path = raw_input("Input path of file > ")
	
	
	x = [os.path.basename(path) , os.path.getsize(path), os.path.getmtime(path)]
	
	print "The files name is %r." % x[0]
	
	print "The program is %r bytes big." % x[1]

	print "The file is %r seconds old." % x[2]
	
	main()
	


main()