# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:53:29 2019
@author: BITTU
"""
import numpy as np
(n,m)=(4,5)
total_cost=0
matrix=np.array([(1,2,1,4,30),(3,3,2,1,50),(4,2,5,9,20),(20,40,30,10,100)])
cost_matrix=matrix[0:n-1,0:m-1]
demand=matrix[n-1,0:m-1]
supply=matrix[0:n-1,m-1]
print('cost matrix : \n',cost_matrix,'\ndemand : ',demand,'\nSupply : ',supply)
if(demand.sum()==supply.sum()):
    while((n-1>1) and (m-1>1)):
        row_penalty=np.zeros(n-1)
        column_penalty=np.zeros(m-1)
        #Findings Row penalty
        for i in range(n-1):
            row_slice=cost_matrix[i,0:m-1]
            min_value1=row_slice.min()
            index1=np.argmin(row_slice)
            row_slice=np.delete(row_slice,index1)
            min_value2=row_slice.min()
            row_penalty[i]=abs(min_value1-min_value2)
        #Findings column penalty
        for i in range(m-1):
            column_slice=cost_matrix[0:n-1,i]
            min_value1=column_slice.min()
            index1=np.argmin(column_slice)
            column_slice=np.delete(column_slice,index1)
            min_value2=column_slice.min()
            column_penalty[i]=abs(min_value1-min_value2)
        curr_max=row_penalty.max() if row_penalty.max()>column_penalty.max() else column_penalty.max()
        indices1 = np.where(row_penalty == curr_max)
        indices2 = np.where(column_penalty == curr_max)
        max_min=999999;
        min_row=int()
        min_column=int()
        '''row max'''
        if(len(indices1[0])>0):
            for x in indices1:
                for a in x:
                    row_index=int(a)
                    select_row = cost_matrix[row_index,0:m-1]
                    select_min=select_row.min()
                    if(max_min>select_min):
                        max_min=select_min
                        min_row=row_index
                        min_column=np.argmin(select_row)
        '''column max'''
        if(len(indices2[0])>0):
            for x in indices2:
                for a in x:
                    col_index=int(a)
                    select_col = cost_matrix[0:n-1,col_index]
                    select_min=select_col.min()
                    if(max_min>select_min):
                        max_min=select_min
                        min_row=np.argmin(select_col)
                        min_column=col_index
        if((demand[min_column])<=(supply[min_row])):
            m-=1
            total_cost+=max_min*demand[min_column]
            supply[min_row]-=demand[min_column]
            demand=np.delete(demand,min_column)
            cost_matrix=np.delete(cost_matrix,min_column,axis=1)
            '''when supply is less than demand'''
        else:
            n-=1
            total_cost+=max_min*supply[min_row]
            demand[min_column]-=supply[min_row]
            supply=np.delete(supply,min_row)
            cost_matrix=np.delete(cost_matrix,min_row,axis=0)
    while(cost_matrix.size>0):
        if(n-1==1):
            select_min=cost_matrix.min()
            mi=np.argmin(cost_matrix)
            if(demand[mi]<supply[0]):
                total_cost+=select_min*demand[mi]
                supply[0]-=demand[mi]
                demand=np.delete(demand,mi)
                cost_matrix=np.delete(cost_matrix,mi,axis=1)
            else:
                total_cost+=select_min*supply[0]
                demand[mi]-=supply[0]
                supply=np.delete(supply,0)
                cost_matrix=np.delete(cost_matrix,0,axis=1)
        else:
            select_min=cost_matrix.min()
            mi=np.argmin(cost_matrix)
            if(demand[0]<supply[mi]):
                total_cost+=select_min*demand[0]
                supply[mi]-=demand[0]
                demand=np.delete(demand,0)
                cost_matrix=np.delete(cost_matrix,0,axis=0)
            else:
                total_cost+=select_min*supply[mi]
                demand[0]-=supply[mi]
                supply=np.delete(supply,mi)
                cost_matrix=np.delete(cost_matrix,mi,axis=0)
    print('Total Cost : ',total_cost)
else:
    print("the matrix is not balanced.")