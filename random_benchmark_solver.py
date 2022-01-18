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

def new_random(i, instance, robotrand, shelfrand):
	instance = instance + "\n\n% Robot " + str(i)
	
	splitinstance = instance.splitlines()
	x_max = int((re.findall(r"\d+", splitinstance[1]))[0])
	y_max = int((re.findall(r"\d+", splitinstance[2]))[0])
	
	while(True):
		n = random.randint(1,x_max)
		m = random.randint(1,y_max)
		if(not([n,m] in robotrand) and not ("%init(object(node,\d),value(at,({},{}))).".format(n,m) in instance)):
			robotrand.append([n,m])
			instance = instance + "\ninit(object(robot,{}),value(at,({},{}))).".format(i,n,m)
			break
	
	while(True):
		n = random.randint(1,x_max)
		m = random.randint(1,y_max)
		if(not([n,m] in shelfrand) and not ("%init(object(node,\d),value(at,({},{}))).".format(n,m) in instance)):
			shelfrand.append([n,m])
			instance = instance + "\ninit(object(shelf,{}),value(at,({},{}))).".format(i,n,m)
			break
	return instance, robotrand, shelfrand

def node_count(instance):
	splitinstance = instance.splitlines()
	count = 0
	for i in splitinstance:
		if "node" in i and not "%" in i:
			count = count + 1
	return count

def solving(combined,i,nodecount):
	start = time.time()
	solution = ""
	while(not solution and i<nodecount):
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
	print(solution)
	print("Solution time: " + str(end - start) + "s\n")	




if __name__ == '__main__':
	#Encoding and instance as system argument
	encoding,instance = reading(sys.argv[1],sys.argv[2])
	
	
	i = 0
	robotrand = []
	shelfrand = []
	
	nodes = node_count(instance)
	print(nodes)
	instance, robotrand, shelfrand = new_random(1,instance,robotrand,shelfrand)
	instance, robotrand, shelfrand = new_random(2,instance,robotrand,shelfrand)
	instance, robotrand, shelfrand = new_random(3,instance,robotrand,shelfrand)
	instance, robotrand, shelfrand = new_random(4,instance,robotrand,shelfrand)
	print(robotrand)
	print(shelfrand)
	
	
	
	# while(i<nodes):
		# i = i + 1
		# print("Testing {} Robots".format(i))
		# instance, robotrand, shelfrand = new_random(i,instance,robotrand,shelfrand)
		# combined = encoding + instance
		# # Starting horizon
		# maxDist = min_horizon(instance, sys.argv[1], encoding)
		# p = multiprocessing.Process(target=solving, name="Solving", args=(combined,maxDist,nodes))
		# p.start()
		# p.join(10)
		# if p.is_alive():
			# p.terminate()
			# p.join()
			# print("Timeout")
			# break
	
	
	
	
		
	
	


