import clingo
import sys
import time
import re
import multiprocessing

def reading(program1, program2, instance):
	#Reading content of encoding
	encodings = open(program1, "r")
	encoding1 = encodings.read()
	encodings.close()

	encodings = open(program2, "r")
	encoding2 = encodings.read()
	encodings.close()
	
	#Reading content of instance
	benchmarks = open(instance, "r")
	instance = benchmarks.read()
	benchmarks.close()

	return encoding1, encoding2, instance

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
	
def solving(instance,encoding1, encoding2):
	j = 0
	robots = robot_count(instance)
	
	while(j<robots):
		j = j + 1
		print("Testing {} Robots".format(j))
		sys.stdout.flush()
		instance = new_robot(j,instance)
		combined = encoding1 + instance
		maxDist = min_horizon(instance, sys.argv[1], encoding1)
		i = maxDist
	
		start = time.time()
		solution = ""
		while(not solution):
			horizon = "#const horizon = {}.".format(i)
			asp = horizon + "\n" + combined
			#Starting clingo solving
			ctl = clingo.Control()
			ctl.add("base", [], asp)
			ctl.ground([("base", [])])
			with ctl.solve(yield_=True) as handle:
				for m in handle:
					solution = str(m)
					solution = solution.replace(" ", ".\n ")
					solution = solution + "."
					break
			i = i + 1
		
		end = time.time()
		abstime = end - start
		print("Abstraction time: " + str(abstime) + "s")
		sys.stdout.flush()
	
		new_instance = solution.replace("new_init", "init")
		combined = encoding2 + new_instance
		nodes = node_count(new_instance)
		maxDist = min_horizon(instance, sys.argv[2], encoding2)
		i = maxDist

		start = time.time()
		solution = ""
		while(not solution):
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
			if(i>nodes):
				print("UNSATISFIABLE")
				break	
		end = time.time()
		solvtime = end - start
		print("Solving time: " + str(solvtime) + "s")
		sys.stdout.flush()
		print("Solution time: " + str(abstime + solvtime) + "s\n")
		sys.stdout.flush()



if __name__ == '__main__':
	#Encoding and instance as system argument
        encoding1, encoding2, instance = reading(sys.argv[1],sys.argv[2], sys.argv[3])
	
        p = multiprocessing.Process(target=solving, name="Solving", args=(instance,encoding1, encoding2))
        p.start()
        p.join(600)
        if p.is_alive():
                p.terminate()
                p.join()
                print("Timeout")
	
	
	
	
		
	
	


