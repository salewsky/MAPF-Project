import sys

instance = sys.argv[1]
instance_dir = sys.argv[2]

instances = []
for i in range(5):
	cur_instance = open(instance_dir + "\preset_{}."format(i+1), "r")
	instances.append(cur_instance.read())
	cur_instance.close()
for i in range(5):
	cur_instance = open(instance_dir + "\random_{}."format(i+1), "r")
	instances.append(cur_instance.read())	
	cur_instance.close()

times = []
for i in range(11):
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
	times[10].append(sum/count)



