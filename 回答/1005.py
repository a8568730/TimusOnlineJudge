import sys
import math

arr = []
for input in sys.stdin.read().split():
	arr.append(int(input))
length, *items = arr

所有石頭總和 = 0
for 石頭 in items:
	所有石頭總和 += 石頭

# sum=[]
最小差 = [所有石頭總和]
# 算出其中一堆的總和
def count(最多挑幾個, 目前挑了幾個, 全部石頭, 現在挑到叨位,目前總和):
	if 目前挑了幾個 == 最多挑幾個:
# 		 sum.append(目前總和)
		剩下另一堆的總和 = 所有石頭總和 - 目前總和
		目前的差 = abs(剩下另一堆的總和 - 目前總和) 
		if 目前的差 < 最小差[0]:
 			最小差[0]=目前的差
		return
	if 現在挑到叨位 == len(全部石頭):
		return	
	count(最多挑幾個, 目前挑了幾個+1, 全部石頭, 現在挑到叨位+1, 目前總和+全部石頭[現在挑到叨位])
	count(最多挑幾個, 目前挑了幾個, 全部石頭, 現在挑到叨位+1, 目前總和)
	
		
i=length
if length!=len(items):
	while True:
		pass
while i>0:
	count(i,0,items,0,0)
	i-=1
# 
# 兩堆石頭各別的總和 = []
# for 算過一堆的總和 in sum:
# 	兩堆石頭各別的總和.append((所有石頭總和 - 算過一堆的總和,算過一堆的總和))  
# 
# 兩堆石頭的差 = []
# for 每組總和 in 兩堆石頭各別的總和:
# 	兩堆石頭的差.append(abs(每組總和[0]-每組總和[1]))
# 
# 最小差 = 所有石頭總和
# for 目前的差 in 	兩堆石頭的差:
#  	if 目前的差 < 最小差:
#  		最小差=目前的差

print(最小差[0])	