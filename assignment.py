import numpy as np
import matplotlib.pyplot as plt

count_list = list()
no_jobs = list()

def Activity(start, finish, n):
	j=0
	count = 1
	for i in range(1, n):
		if(start[i] >= finish[j]):
			count = count + 1
			print(start[i], finish[j])
			j = i
	count_list.extend([count])
	print(count)
	
def Draw_Graph():
	plt.plot(no_jobs, count_list, marker='o', markerfacecolor='blue', markersize=12)
	plt.xlabel("no_of_jobs")
	plt.ylabel("job_count")
	plt.show()

n = int(input("Enter the no of Random choices you want: "))
for i in range(n):
	n1 = int(input("Enter the no of Random jobs: "))
	start = np.random.randint(1, 100, n1)
	finish = np.random.randint(1, 100, n1)
	Activity(start, finish, n1)
	no_jobs.extend([n1])
Draw_Graph()
