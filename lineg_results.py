import sys
from matplotlib import pyplot as plt
import os

def get_times(path):
	times = []

	for filename in os.listdir(path):
		with open(os.path.join(path, filename), 'r') as f:
			times.append([])
			results = f.read()
			results = results.splitlines()
			for i in results:
				if("Solution time" in i):
					times[len(times)-1].append(float(i[15:-1]))
	return times
      

def get_avg(time_list):
	averages = []
	
	robots = 0
	for i in time_list:
		robots = max(robots,len(i))  #Max oder Min
	
	count = 0
	time_sum = 0
	for i in range(robots):
		for j in time_list:
			if(i<len(j)):
				time_sum = time_sum + j[i]
				count = count + 1
		averages.append(time_sum/count)
		
	return averages

def plot(title, averages, programs):
	plt.style.use('ggplot')
	for i in averages:
		plt.plot(range(1,len(i)+1), i) 
		plt.title(title)
	ax = plt.gca()
	ax.set_xlim(0)
	ax.set_ylim(0)
	plt.xlabel("Robot count")
	plt.ylabel("Average Solution Time in s")
	plt.legend(programs)
	plt.show()



title = sys.argv[1]  #Instance Name
path = sys.argv[2]	#Path to Results for the Instance
programs = sys.argv[3:]  #Programs you want results for
times = []
averages = []

for i in programs:
	#print("Results for {}: \n".format(i))
	times.append(get_times(path + "\\" + i + "\\"))

for i in times:
	averages.append(get_avg(i))

plot(title, averages, programs)



