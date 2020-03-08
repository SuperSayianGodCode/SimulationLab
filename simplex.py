# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:04:34 2019

@author: BITTU
"""
import numpy as np
import math as m

#matrix=np.array([[1,1,1,0,450],[2,1,0,1,600]])
matrix=np.array([[6.0,8.0,-1.0,0.0,100.0],[7.0,12.0,0.0,-1.0,120.0]])
row,col=np.shape(matrix)

CBi=[0,0]

#Ci=[12,20,0,0]
Ci=[12,20,0,0]

Zj=[0 for i in range(col)]

BaseArray=[1 for i in range(col-1)]

#compute ratio vector
#Ratio=[0 for i in range(row)]
#Ratio=matrix[0:row,col-1]
Ratio=np.array([0,0])
for i in range(len(matrix[0:row,col-1])):
    Ratio[i]=matrix[i][col-1]
print("Ratio",Ratio)

print(row," ",col)

#calculating optimal solution
#while(sum(BaseArray)>0):
#calculation Zj vector using formula Zj=Cbi[i]*matrix[i][j]
for i in range(1):
    for j in range(col):
        Zj[j]=CBi[i]*matrix[i][j]

print("Zj=",Zj)
#calculating Ci-Zj values and storing it in BaseArray      
for k in range(col-1):     
    BaseArray[k]=Ci[k]-Zj[k]

print("BaseArray",BaseArray)

#finding max element from Ci-Zj and min element from solution vctor
maxelem=max(BaseArray)
print("maxelem",maxelem)
print(matrix)
#calculatig index for corresponding max and min elements
maxelemindex=int(np.where(BaseArray == maxelem)[0])
column_slice=matrix[:,maxelemindex]
for i in range(len(Ratio)):
    Ratio[i]=m.ceil(matrix[i][col-1]/column_slice[i])
print(matrix)   
print("After updation",Ratio)   
minelem=min(Ratio)
print("minelem",minelem)
minelemindex=int(np.where(Ratio == minelem)[0])
print("minelemindex",minelemindex)
print("maxelemindex",maxelemindex)


row_slice=matrix[minelemindex,0:col]
print("column_slice",column_slice)
print("row_slice",row_slice)

#print(matrix[minelemindex,minelemindex-1:col-1])

key_element=matrix[minelemindex][maxelemindex]

print("key_element",key_element)

#updating row with key element
#row_slice[:] = [float(x/key_element) for x in row_slice]
for i in range(len(row_slice)):
    row_slice[i]=float(row_slice[i])/key_element
print("Updated row slice",row_slice)

solution=0
count=0
kcv=column_slice[minelemindex-1]
print("kcv=",kcv)
#updating values in the other row
for y in matrix[minelemindex,minelemindex:col]:
    krv=matrix[minelemindex,count]
    print(" krv=",krv)
    print("elements before update",y)
    y=y-((kcv*krv)/key_element)
    print("elements after update",y)
    
#updating CBi vector with the value of Entry value,i.e value in Ci array at the index of key element
CBi[minelemindex]=Ci[maxelemindex]
print("CBi",CBi)
    
##for calculating optimal solution
#for i in range(len(CBi)):
#    solution+=CBi[i]*matrix[i][col-1]
    

print("sum of basearray=",sum(BaseArray))

for j in range(col):  
    for i in range(1):
#        Zj[j]+=CBi[i]*matrix[i][j]
        print("CBi[i]=",CBi[i]," ","matrix[i][j]=",matrix[i][j])

print("Zj=",Zj)
#    solution=Zj[col-1]
#    print("solution=",solution)
#       
#    for k in range(col-1):     
#        BaseArray[k]=Ci[k]-Zj[k]
#    
#    print("BaseArray",BaseArray)
#    
#    for i in range(len(Ratio)):
#        Ratio[i]=matrix[i][col-1]/column_slice[i]
    
print("\nend of loop\n\n")
