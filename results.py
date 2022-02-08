import sys
import pandas as pd
from matplotlib import pyplot as plt

result_dir = sys.argv[1]

results = []
for i in range(5):
	cur_result = open(result_dir + "\preset_{}."format(i+1), "r")
	instances.append(cur_instance.read())
	cur_instance.close()


times = []

for i in range(6):
	times.append([])

for i in range(len(instances)):
	split = instances[i].splitlines()
	for j in split:
		if("Solution time" in j):
			times[i].append(j[15:-1]

robots = 0
for i in times:
	robots = max(robots,len(i))
	
count = 0
sum = 0
for i in range(robots):
	for j in times:
		if(i<len(j)):
			sum = sum + j[i]
			count = count + 1
	times[5].append(sum/count)

print(times)

average = times[5]

plt.plot(range(robots), average) 
plt.title("Small open(16x16)")
plt.xlabel("Robot count")
plt.ylabel("Solution Time in s")
plt.legend(["CNC"])
plt.show()
