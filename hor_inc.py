import clingo
import sys
import time
import re
import multiprocessing


def solving(combined,i):
	start = time.time()
	while(True):
		print("Testing Horizon: " + str(i))
		#ASP encoding
		horizon = "#const horizon = {}.".format(i)
		asp = horizon + "\n" + combined
		#Starting clingo solving
		ctl = clingo.Control()
		ctl.add("base", [], asp)
		ctl.ground([("base", [])])
		#Saving solution
		solution = ""
		with ctl.solve(yield_=True) as handle:
			for m in handle:
				solution = str(m)
				solution = solution.replace(" ", ". ")
				solution = solution + "."
				break
		if(solution):
			break
		i = i + 1
		
	end = time.time()
	print(solution)
	print("Solution time: " + str(end - start) + "s")	

#Encoding and instance as system argument
programs = sys.argv[1]
instances = sys.argv[2]

#Reading content of encoding
encodings = open(programs, "r")
encoding = encodings.read()
encodings.close()

#Reading content of instance
benchmarks = open(instances, "r")
instance = benchmarks.read()
benchmarks.close()

combined = encoding + instance

#Starting horizon
maxDist = 0
robots = []
splitinstance = instance.splitlines()
for i in range(len(splitinstance)):
	if("% Robot" in splitinstance[i]):
		robots.append(i)
for i in robots:
	r_num = re.findall(r'\d+', splitinstance[i+1])
	s_num = re.findall(r'\d+', splitinstance[i+2])
	x_dis = abs(int(r_num[1]) - int(s_num[1]))
	y_dis = abs(int(r_num[2]) - int(s_num[2]))
	if("node combining" in programs):
		splitencoding = encoding.splitlines()
		x_size = re.findall(r'\d+', splitencoding[0])
		y_size = re.findall(r'\d+', splitinstance[1])
		x_dis = int(x_dis/int(x_size[0]))
		y_dis = int(y_dis/int(y_size[0]))
	maxDist = max(maxDist, x_dis + y_dis)


if __name__ == '__main__':
	p = multiprocessing.Process(target=solving, name="Solving", args=(combined,maxDist,))
	p.start()
	p.join(300)
	if p.is_alive():
		p.terminate()
		p.join()
		print("Timeout")


