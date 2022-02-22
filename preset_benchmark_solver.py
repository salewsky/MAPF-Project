import clingo
import sys
import time
import re
import multiprocessing
from json import dumps

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

def new_robot(i, instance):
	instance = instance.replace("%init(object(robot,{})".format(i), "init(object(robot,{})".format(i))
	instance = instance.replace("%init(object(shelf,{})".format(i), "init(object(shelf,{})".format(i))
	
	return instance

def node_count(instance):
	splitinstance = instance.splitlines()
	count = 0
	for i in splitinstance:
		if "node" in i and not "%" in i:
			count = count + 1
	return count

def robot_count(instance):
	splitinstance = instance.splitlines()
	count = 0
	for i in splitinstance:
		if "% Robot" in i:
			count = count + 1
	return count
	
def solving(instance,encoding):
	j = 0
	nodes = node_count(instance)
	robots = robot_count(instance)
	
	while(j<robots):
		j = j + 1
		print("Testing {} Robots".format(j))
		sys.stdout.flush()
		instance = new_robot(j,instance)
		combined = encoding + instance
		maxDist = min_horizon(instance, sys.argv[1], encoding)
		i = maxDist
	
		start = time.time()
		solution = ""
		while(not solution):
			horizon = "#const horizon = {}.".format(i)
			asp = horizon + "\n" + combined
			#Starting clingo solving
			ctl = clingo.Control(['--stats'])
			ads = time.time()
			ctl.add("base", [], asp)
			ade = time.time()
			print("Adding time: " + str(round(float(ade - ads),2)) + "s")
			sys.stdout.flush()
			gs = time.time()
			ctl.ground([("base", [])])
			ge = time.time()
			print("Grounding time: " + str(round(float(ge - gs),2)) + "s")
			sys.stdout.flush()
			sst = time.time()
			with ctl.solve(yield_=True) as handle:
				for m in handle:
					solution = str(m)
					solution = solution.replace(" ", ". ")
					solution = solution + "."
					break
			se = time.time()
			print("Solving time: " + str(round(float(se - sst),2)) + "s")
			sys.stdout.flush()
			i = i + 1
		
		end = time.time()
		print("Solution time: " + str(round(float(end - start),2)) + "s\n")
		sys.stdout.flush()
		print("Clingo Grounding: {}s".format(round(float(dumps(ctl.statistics['summary']['times']['total'], sort_keys=True, indent=4, separators=(',', ': ')))-float(dumps(ctl.statistics['summary']['times']['solve'], sort_keys=True, indent=4, separators=(',', ': ')))),2))
		sys.stdout.flush()
		print("Clingo Total: {}s\n".format(round(float(dumps(ctl.statistics['summary']['times']['total'], sort_keys=True, indent=4, separators=(',', ': ')))),2))
		sys.stdout.flush()		




if __name__ == '__main__':
	#Encoding and instance as system argument
	encoding,instance = reading(sys.argv[1],sys.argv[2])
	
	p = multiprocessing.Process(target=solving, name="Solving", args=(instance,encoding))
	p.start()
	p.join(600)
	if p.is_alive():
		p.terminate()
		p.join()
		print("Timeout")
	
	
	
	
		
	
	


