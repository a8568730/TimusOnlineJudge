import sys
import math

arr = ""
for input in sys.stdin:
	arr += input

for item in arr.split()[::-1]:
	print("{0:.4f}".format(math.sqrt(float(item)))) 
	