import math
 
 
iVel = 50
h = 10
d = 0
t = 0
theta = 40
g = -9.8
 
xVel = iVel * math.cos((theta/180)* math.pi)
yVel = iVel * math.sin((theta/180)* math.pi)
 
 
quadsolve = [(-yVel + math.sqrt(yVel**2 - 4*(g/2)*(10)))/(2*(g/2)), (-yVel - math.sqrt(yVel**2 - 4*(g/2)*(10)))/(2*(g/2))]
 
if quadsolve[0] >= 0:
 air_t = quadsolve[0]
else:
 air_t = quadsolve[1]
 
print(air_t)
 
for i in range(int(air_t * 100) + 1):
 print("X: " + str(xVel * (i/100)) + ', Y: ' + str(yVel * (i/100) + h + (g/2) * ((i/100)**2)) + ' T: ' + str(i/100))
