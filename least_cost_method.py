# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 23:07:09 2019
@author: Jarvis
"""
import numpy as np
n=4
m=5
optimal_solution=0
matrix=np.array([(19,30,50,10,7),(70,30,40,60,9),(40,8,70,20,18),(5,8,7,14,34)])
cost_matrix=matrix[0:n-1,0:m-1]
demand=matrix[n-1,0:m-1]
supply=matrix[0:n-1,m-1]
print('cost matrix : \n',cost_matrix,'\ndemand : ',demand,'\nSupply : ',supply)
"""condition for balanced matrix"""
if(demand.sum()==supply.sum()):
    while(cost_matrix.size>0):
        current_min=cost_matrix.min()
        indices = np.where(cost_matrix == current_min)
        listOfCoordinates= list(zip(indices[0], indices[1]))
        min_row=listOfCoordinates[0][0]
        min_column=listOfCoordinates[0][1]
        '''when demand is less than or equal to supply'''
        if((demand[min_column])<=(supply[min_row])):
            optimal_solution+=current_min*demand[min_column]
            supply[min_row]-=demand[min_column]
            demand=np.delete(demand,min_column)
            cost_matrix=np.delete(cost_matrix,min_column,axis=1)
            '''when supply is less than demand'''
        else:
            optimal_solution+=current_min*supply[min_row]
            demand[min_column]-=supply[min_row]
            supply=np.delete(supply,min_row)
            cost_matrix=np.delete(cost_matrix,min_row,axis=0)
    print('optiomal solution : ',optimal_solution)
else:
    print('The matrix is not balanced. Please wait for 2.0')