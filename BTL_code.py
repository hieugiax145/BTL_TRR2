import math

class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y

P=[]

n=int(input('Nhap so diem: '))

print('Nhap toa do (x,y) cac diem: ')
for i in range (n):
	x,y=[float(x) for x in input().split()]
	P.append(Point(x,y))
print('Nhap khoang cach d: ')

d=float(input())

def check(i,j):
	a=(i.x,i.y)
	b=(j.x,j.y)
	return math.dist(a,b)<=d

visted=[]

def BFS(x):
	queue=[]
	visted.append(x)
	queue.append(x)
	while queue:
		u=queue.pop(0)
		print(u+1,end=' ')
		for i in range (n):
			if check(P[i],P[u]) and i not in visted:
				queue.append(i)
				visted.append(i)

def DFS(x):
	store=[]
	stack=[]
	visted.append(x)
	stack.append(x)
	while stack:
		u=stack.pop()
		if u not in store:
			print(u+1,end=' ')
			store.append(u)
		for i in range (n):
			if check(P[i],P[u]) and i not in visted:
				stack.append(u)
				stack.append(i)
				visted.append(i)
				break

dem=0
print('Danh sach thanh phan lien thong:')
for k in range (n):
	if k not in visted:
		dem+=1
		print('TP '+str(dem)+':',end=' ')
		# BFS(k)
		DFS(k)
		print()

'''
20 25
32 28
-17 -31
10 -7
7 38
42 28
5 -32
-15 28
30 -37
-38 36
40 -36
-32 21
-33 14
-2 3
24 13
-30 -31
34 -16
-3 -4
51 -10
52 -21
22 -39
'''