import sys
from matplotlib import pyplot as plt
import os

def robot_nr(path):
	r_list = []
	for filename in os.listdir(path):
		count = 0
		with open(os.path.join(path, filename), 'r') as f:
			results = f.read()
			results = results.splitlines()
			for i in results:
				if("Solution time" in i):
					count = count + 1
		r_list.append(count)
	r_list.sort()
	return r_list
	
def plot(title, ma, methods, programs):
	plt.style.use('ggplot')
	for i in methods:
		plt.scatter(ma[:len(i)], i) 
	plt.title(title)
	plt.gca().set_aspect('equal')
	ax = plt.gca()
	ax.set_xlim(0,max(max(ma_robots),max(max(method_robots)))+10)
	ax.set_ylim(0,max(max(ma_robots),max(max(method_robots)))+10)
	plt.xlabel("Maximum Robots in Asprilo")
	plt.ylabel("Maximum Robots in Solving Method")
	plt.legend(programs)
	ax.plot([0, 1], [0, 1], transform=ax.transAxes)
	plt.show()




title = sys.argv[1]  #Instance Name
path = sys.argv[2]	#Path to Results for the Instance
programs = sys.argv[3:]  #Programs you want results for

ma_robots = robot_nr(path + "\\Modified-Asprilo\\")

method_robots = []
for i in programs:
	method_robots.append(robot_nr(path + "\\" + i + "\\"))

plot(title, ma_robots, method_robots, programs)
	


	
