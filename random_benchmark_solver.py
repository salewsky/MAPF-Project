import clingo
import sys
import time
import re
import multiprocessing
import random

def reading(programs, instances):
	#Reading content of encoding
	encodings = open(programs, "r")
	encoding = encodings.read()
	encodings.close()

	#Reading content of instance
	benchmarks = open(instances, "r")
	instance = benchmarks.read()
	benchmarks.close()

	return encoding, instance

def min_horizon(instance,programs,encoding):
	maxDist = 1
	robots = []
	splitinstance = instance.splitlines()
	for i in range(len(splitinstance)):
		if("% Robot" in splitinstance[i] and not "%" in splitinstance[i+1]):
			robots.append(i)

	combining = False		

	if("node combining" in programs):
		combining = True
		splitencoding = encoding.splitlines()
		x_size = re.findall(r'\d+', splitencoding[0])
		y_size = re.findall(r'\d+', splitencoding[1])
		

	for i in robots:
		r_num = re.findall(r'\d+', splitinstance[i+1])
		s_num = re.findall(r'\d+', splitinstance[i+2])
		x_dis = abs(int(r_num[1]) - int(s_num[1]))
		y_dis = abs(int(r_num[2]) - int(s_num[2]))
		if(combining):
			x_dis = int(x_dis/int(x_size[0]))
			y_dis = int(y_dis/int(y_size[0]))
		maxDist = max(maxDist, x_dis + y_dis)
	
	return maxDist

def node_list(instance):
	splitinstance = instance.splitlines()
	nodelist = []
	for i in splitinstance:
		if "node" in i and not "%" in i:
			list = (re.findall(r"\d+", i))
			nodelist.append([int(list[1]),int(list[2])])
	return nodelist

def new_random(i, instance, robotrand, shelfrand, nodeslist):
	instance = instance + "\n\n% Robot " + str(i)
	
	while(True):
		n = random.randint(0,len(nodeslist)-1)
		if(not(n in robotrand)):
			robotrand.append(n)
			instance = instance + "\ninit(object(robot,{}),value(at,({},{}))).".format(i,nodeslist[n][0],nodeslist[n][1])
			break
	
	while(True):
		n = random.randint(0,len(nodeslist)-1)
		if(not(n in shelfrand)):
			shelfrand.append(n)
			instance = instance + "\ninit(object(shelf,{}),value(at,({},{}))).".format(i,nodeslist[n][0],nodeslist[n][1])
			break
	return instance, robotrand, shelfrand


def solving(instance,encoding):
	nodes = node_list(instance)
	j = 0
	robotrand = []
	shelfrand = []

	while(j<len(nodes)):
		j = j + 1
		print("Testing {} Robots".format(j))
		instance, robotrand, shelfrand = new_random(j,instance,robotrand,shelfrand,nodes)
		combined = encoding + instance
		maxDist = min_horizon(instance, sys.argv[1], encoding)
		i = maxDist
		
		start = time.time()
		solution = ""
		while(not solution):
			#print("Testing Horizon: " + str(i))
			#ASP encoding
			horizon = "#const horizon = {}.".format(i)
			asp = horizon + "\n" + combined
			#Starting clingo solving
			ctl = clingo.Control()
			ctl.add("base", [], asp)
			ctl.ground([("base", [])])
			with ctl.solve(yield_=True) as handle:
				for m in handle:
					solution = str(m)
					solution = solution.replace(" ", ". ")
					solution = solution + "."
					break
			i = i + 1
		end = time.time()
		print("Solution time: " + str(end - start) + "s\n")	




if __name__ == '__main__':
	#Encoding and instance as system argument
	encoding,instance = reading(sys.argv[1],sys.argv[2])
	
	seed = random.randrange(sys.maxsize)
	random.seed(seed)
	print("Seed: ", seed)
	
	
	p = multiprocessing.Process(target=solving, name="Solving", args=(instance,encoding))
	p.start()
	p.join(600)
	if p.is_alive():
		p.terminate()
		p.join()
		print("Timeout")
	
	
	
	
		
	
	


