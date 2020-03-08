#Solving Transportaion Problem Using Modified Distribution Method
import numpy as np

total=0
def row_panelty(arr,m,n):
	r = 0
	c = 0
	id = []
	while (r < m):
		first = 1000
		second = 1000
		for c in range(0,n):

			if(arr[r][c] <= first):
				second = first
				first = arr[r][c]

			elif(arr[r][c]<second and arr[r][c]>first):
				second = arr[r][c]
					
			c= c+1

			
		x = second - first
		id.append(x)
		r = r + 1
	return id

def column_panelty(arr,m,n):

	q = 0
	w = 0

	su = []
	while (q < n):
		first = 1000
		second = 1000
		for w in range(0,m):

			if(arr[w][q] <= first):
				second = first
				first = arr[w][q]

			elif(arr[w][q]<second and arr[w][q]>first):
				second = arr[w][q]
				
			w= w+1

		
		x = second - first
		su.append(x)
		q = q + 1
	return su

#while(m > 0 and n > 0):
#	row = row_panelty(arr,m,n)
#	column = column_panelty(arr,m,n)
#	max_p = max(max(row),max(column))
#	
#	f = 0
#	l = 0
#	if max_p in row:
#		if(row.index(max_p)>=0):
#			max_i = [row.index(max_p),0]
#	if max_p in column:	
#		if(column.index(max_p)>=0):
#			max_i = [0,column.index(max_p)]
#	
#	f,l = max_i
#
#	minval = 100000
#	x  = 0
#	y = 0
#	for i in range(f,m):
#	    for j in range(l,n):
#	        if(arr[i][j]<minval):
#	            minval = arr[i][j]
#	            x,y = i,j
#	
#	if(d[x]<s[y]):
#		total = total + minval*d[x]
#
#		s[y] = s[y]-d[x]
#		d[x] = 0
#		arr = np.delete(arr,x,axis =0)
#		del d[x]
#
#		m = m-1
#		
#	elif(d[x]==s[y]):
#		total = total + minval*d[x]
#		s[y] = 0
#		d[x] = 0
#		arr = np.delete(arr,x,axis =0)
#		del d[x]
#		m = m-1
#
#	elif(d[x]>s[y]):
#		total = total + minval*s[y]
#		d[x] = d[x]-s[y]
#		s[y] = 0
#		arr = np.delete(arr,y,axis =1)
#		del s[y]
#		n = n-1
#	print(total)
#print('Final Total using Vogels Approximation Method: ',total)

#MODI METHOD

arr = np.array([[19,30,50,10],[70,30,40,60],[40,8,70,20]])
m,n = arr.shape
print(arr)
alloc = np.array([[5,0,0,2],[0,0,7,2],[0,8,0,10]])
print('allocation matrix:')
print(alloc)
m,n = alloc.shape
if(m+n-1==6):
	print('allocation matrix is balanced')
count = 1


while(count==1):
	
	u = [0,0,0]
	v = [0,0,0,0]

	for _ in range(3):
		for i in range(m):
			for j in range(n):
				if(alloc[i][j]!=0):
					if(i ==0):
						v[j] = arr[i][j]
					if(v[j]==0 and u[i]!=0):
						v[j] = arr[i][j] - u[i]
					elif(v[j]!=0 and u[i]==0):
						u[i] = arr[i][j] -v[j]
	
	c = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
	for i in range(m):
		for j in range(n):
			if(alloc[i][j]==0):
				c[i][j] = arr[i][j]-u[i]-v[j] 

	for i in range(m):
		for j in range(n):
			if(c[i][j]<0):
				count = count+1
	if(count>1):
		print(alloc)
		print("soln not optimal,modification required.")
		
		count = 1
	else:
		print(alloc)
		print("soln is optimal,No,modification required.")
		count = 0
		

		break
	minc = np.amin(c)
	for i in range(m):
	    for j in range(n):
	        if(c[i][j]==minc):
	            x,y = i,j
	
	for i in range(1,2):
	    for j in range(1,3):
	    	if(alloc[x][y]==0):
	    		if(alloc[x+i][y]!= 0 ):

	    			if(alloc[x+i][y+j]!=0):
	    				if(alloc[x][y+j]!=0):
	    					a = alloc[x+i][y]
	    					b = alloc[x+i][y+j]
	    					c = alloc[x][y+j]
	    					d = alloc[x][y]
	    					mina = min(a,b,c) 
	    					alloc[x+i][y] = a-mina
	    					alloc[x+i][y+j] = b+mina
	    					alloc[x][y+j] = c-mina
	    					alloc[x][y] = mina

	    			elif(alloc[x+i][y-j]!=0):
	    				if(alloc[x][y-j]!=0):
	    					a = alloc[x+i][y]
	    					b = alloc[x+i][y-j]
	    					c = alloc[x][y-j]
	    					d = alloc[x][y]
	    					mina = min(a,b,c) 
	    					alloc[x+i][y] = a-mina
	    					alloc[x+i][y-j] = b+mina
	    					alloc[x][y-j] = c-mina
	    					alloc[x][y] = mina

	    		elif(alloc[x-i][y]!=0):	
	    			if(alloc[x-i][y+j]!=0):
	    				if(alloc[x][y+j]!=0):
	    					a = alloc[x-i][y]
	    					b = alloc[x-i][y+j]
	    					c = alloc[x][y+j]
	    					d = alloc[x][y]
	    					
	    					mina = min(a,b,c) 
	    					alloc[x-i][y] = a-mina
	    					alloc[x-i][y+j] = b+mina
	    					alloc[x][y+j] = c-mina
	    					alloc[x][y] = mina

	    			elif(alloc[x-i][y-j]!=0):
	    				if(alloc[x][y-j]!=0):
	    					a = alloc[x-i][y]
	    					b = alloc[x-i][y-j]
	    					c = alloc[x][y-j]
	    					d = alloc[x][y]
	    					mina = min(a,b,c) 
	    					alloc[x-i][y] = a-mina
	    					alloc[x-i][y-j] = b+mina
	    					alloc[x][y-j] = c-mina
	    					alloc[x][y] = mina
total = 0
for i in range(0,m):
	for j in range(0,n):
		total = total + alloc[i][j]*arr[i][j]
		
print('Optimal cost using Modi over Vogels approximation Method is: ',total)