import clingo
import sys
import time
import re

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
	maxDist = max(maxDist, x_dis + y_dis)

i = maxDist
	
#Time measuring
start = time.time()

while(True):
	#ASP encoding
	horizon = "#const horizon = {}.".format(i)
	asp = horizon + "\n" + combined
	#Starting clingo solving
	ctl = clingo.Control()
	ctl.add("base", [], asp)
	ctl.ground([("base", [])])
	solution = ""
	#Saving solution
	with ctl.solve(yield_=True) as handle:
		for m in handle:
			solution = solution + str(m)
			break
			
	if(solution):
		break
	check = time.time()
	if((check - start) > 1800):
		solution = "Zeitüberschreitung. Aktueller horizon: " + str(i)
	i = i + 1

solution = solution.replace(" ", ". ")
solution = solution + "."

end = time.time()

print(solution)
print("Solution time: " + str(end - start) + "s")