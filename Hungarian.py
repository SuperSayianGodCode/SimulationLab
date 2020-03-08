# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:40:48 2019

@author: BITTU
"""

import numpy as np,collections


boxedzeros=0
originalmatrix=np.array([[82,83,69,92],
                [77,37,49,92],
                [11,69,5,86],
                [8,9,98,23]])

workingmatrix=np.copy(originalmatrix)

row,col=np.shape(originalmatrix)

#rowmin=[]
#colmin=[]

for i in range(row):
    rowmin=min(workingmatrix[i,0:col])
    #print(matrix[i,0:col])
    #print(rowmin)
    workingmatrix[i,0:col] = [(x-rowmin) for x in workingmatrix[i,0:col]]
    
print("Row Reuction\n",workingmatrix)

for j in range(col):
    colmin=min(workingmatrix[:,j])
    #print(workingmatrix[:,j])
    #print(colmin)
    workingmatrix[:,j] = [(y-colmin) for y in workingmatrix[:,j]]
    
print("Column Reduction\n",workingmatrix)


#while(boxedzeros!=col):
for r in range(row):
    count=collections.Counter(workingmatrix[i,0:col])
    print(count)