
#python filev derection 

import os
from posixpath import isfile

file_path = "part_9/stuff/test.txt"

if os.path.exists(file_path):
	print(f"the location '{file_path} exists")

	if os.path.isfile(file_path):
		print("that is a file")
	elif os.path.isdir(file_path):
		print("this is a derectory")

else:
	print("the location dosent exists")
