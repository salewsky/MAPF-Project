import random
import sys

open("instance.lp", "x")


x_max = int(input("Maximum x Coordinate:"))
y_max = int(input("Maximum y Coordinate:"))
robot_nr = int(input("Number of Robots:"))

sys.stdout = open('instance.lp', 'w')

x_rand = []
for i in range(robot_nr*2):
	n = random.randint(1,x_max)
	x_rand.append(n)
	
y_rand = []
for i in range(robot_nr*2):
	n = random.randint(1,y_max)
	y_rand.append(n)


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("% Grid Size X:                      " + str(x_max))
print("% Grid Size Y:                      " + str(y_max))       
print("% Number of Nodes:                  " + str(x_max*y_max))
print("% Number of Robots:                 " + str(robot_nr))
print("% Number of Shelves:                " + str(robot_nr))
print("% Number of Picking Stations:       1")
print("% Number of Products:               " + str(robot_nr))
print("% Number of Orders:                 " + str(robot_nr))
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("")
print("%Nodes")

i = 1
j = 1
k = 1
while(i <= x_max*y_max):
	print("init(object(node,"+str(i)+"),value(at,("+str(k)+","+str(j)+"))).")
	if(k+1 > x_max):
		k = 1
		if(j+1 <= y_max):
			j = j+1
	else:
		k = k+1
	i = i+1
	
print("")

for i in range(robot_nr):
	print("% Robot " + str(i+1))
	print("init(object(robot,"+str(i+1)+"),value(at,("+ str(x_rand[i])+","+str(y_rand[i])+"))).")
	print("init(object(shelf,"+str(i+1)+"),value(at,("+ str(x_rand[i+robot_nr])+","+str(y_rand[i+robot_nr])+"))).")
	print("init(object(order,"+str(i+1)+"),value(line,("+str(i+1)+",1))).")
	print("init(object(order,"+str(i+1)+"),value(pickingStation,1)).")
	print("init(object(product,"+str(i+1)+"),value(on,("+str(i+1)+",1))).")
	print("")

print("")
print("% Picking Station")
print("init(object(pickingStation,1),value(at,(1,1))).")

sys.stdout.close()