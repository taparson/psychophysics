import matplotlib.pyplot as plt
import json

json_data=open('output112.json')
data = json.load(json_data)
json_data.close()

trials = data["trials"] #list of trial objects
trial = trials[0]
trial_number = trial["number"]
obstacles = trial["obstacles"]
output_list = trial["output"]

xvals = []
yvals = []
for obj in output_list:
	xvals.append(obj["position"][0])
	yvals.append(obj["position"][1]) 

#print (xvals);

#for key, value in data.iteritems():

plt.plot(xvals,yvals)

x = []
y = []
for obj in obstacles:
	x.append(obj["location"][0])
	y.append(obj["location"][1])

plt.plot(x,y,'ro')
plt.plot(0,70,'bo')
plt.axis([-8,15,-10,80])
plt.ylabel('y position')
plt.xlabel('x position')
plt.show()
