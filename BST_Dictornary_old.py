from collections import defaultdict
from pathlib import Path
import os
import sys

class BST_Dictionary:
    @staticmethod
    def main(args):
        tree = BST()
        tree.insert(2)
        tree.insert(4)
        tree.insert(1)
        tree.insert(20)
        tree.insert(90)
        tree.insert(32)
        tree.insert(12)
        tree.inorder()

class Node:
	left = None
	val = 0
	right = None

	def __init__(self, val):
		self.val = val

class BST:
	root = None

	def insert(self, key):
		node = Node(key)
		if (self.root == None):
			self.root = node
			return
		prev = None
		temp = self.root
		while (temp != None):
			if (temp.val > key):
				prev = temp
				temp = temp.left
			elif(temp.val < key):
				prev = temp
				temp = temp.right
		if (prev.val > key):
			prev.left = node
		else:
			prev.right = node

	def __getitem__(self,key):
		return 1
	
	def __setitem__(self, key, newvalue):
		a=2
		
if __name__ == "__main__":
	inputFilePath = Path(__file__).with_name('inputPS09.txt')
	outputFilePath = Path(__file__).with_name('outputPS031.txt')
    
    #Delete output file if it exists    
	try:
		if os.path.exists(outputFilePath):
			os.remove(outputFilePath)
	except:
		print("Error while deleting file ", outputFilePath)
	
	# Create Output file in Append Mode
	outputfile=open(outputFilePath,"a")

	if (os.path.exists(inputFilePath)==False):
		outputfile.write("Input file does not present. Exiting the program \n")
		outputfile.close()
		sys.exit(0)
	
	# Read All lines from input file
	with open(inputFilePath,"r") as f:
		lines=f.readlines()
	f.close()
	
    #Check if file has content of not. If it empty than exit the program
	if (lines.count==0):
		outputfile.write("Input file is empty. Exiting the program \n")
		outputfile.close()
		sys.exit(0)
		