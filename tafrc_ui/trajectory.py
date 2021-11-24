import math

class Trajectory():
    def __init__(self):
        self.title = 'Trajectory'
        self.paramlist={} #dictionary
        self.param_str = ['distance','height','angle_vertical', 'angle_horizontal','iVel', 'time']

        for param in self.param_str:
            self.paramlist[param]=0

        self._traj_x =[]
        self._traj_y =[]
    
    def split_vector(self, vector, theta_vertical, theta_horizontal):
        # split 3d vector into plane and vector
        hComp = vector * math.cos((theta_vertical/180)* math.pi)
        yComp = vector * math.sin((theta_vertical/180)* math.pi)
        # split plane into 2 vectors
        xComp = hComp * math.sin((theta_horizontal/180) * math.pi)
        zComp = hComp * math.cos((theta_horizontal/180) * math.pi)
        # return the components found
        components = [xComp, zComp, yComp]
        return components

    def calculate_start_position(self, height, distance, theta_horizontal):
        perp_horizontal = theta_horizontal if theta_horizontal <= 90 else theta_horizontal - 90

        xPos = distance * math.sin((perp_horizontal/180)* math.pi) if theta_horizontal <= 90 else distance * math.cos((perp_horizontal/180)* math.pi)
        zPos = distance * math.cos((perp_horizontal/180)* math.pi) if theta_horizontal <= 90 else distance * math.sin((perp_horizontal/180)* math.pi)
        yPos = height
        position = [xPos, zPos, yPos]
        return position

    def calculate_airtime(self, xVel, zVel, yVel, height, distance, theta_vertical, theta_horizontal):
        # init position
        position = self.calculate_start_position(height, distance, theta_horizontal)

        # calculate possible air times
        quadsolve_discriminant = math.sqrt(yVel**2 - 4 * (tafrc_gravity/2) * height)
        max_time = (-yVel + quadsolve_discriminant)/tafrc_gravity if (-yVel + quadsolve_discriminant)/tafrc_gravity > 0 else (-yVel - quadsolve_discriminant)/tafrc_gravity
        x_time = position[0]/xVel

        # find correct air time
        airtime = x_time if x_time >= max_time else max_time
        return airtime

    def position_at_time(self, xVel, zVel, yVel, height, distance, time):
        position = [xVel * (time), zVel * (time), yVel * (time) + height + (tafrc_gravity/2) * ((time)**2), time]
        return position

    def trajectory_calculator(self, iVel, theta_vertical, theta_horizontal, height, distance, time):
        # find vector components
        vel_components = self.split_vector(iVel, theta_vertical, theta_horizontal)
        # find how much time to map trajectory
        airtime = self.calculate_airtime(vel_components[0], vel_components[1], vel_components[2], height, distance, theta_vertical, theta_horizontal)
        #print position at time x
        
        return self.position_at_time(vel_components[0], vel_components[1], vel_components[2], height, distance, time)
        
        #for i in range (int(airtime * 100) + 1):
        #    temp = position_at_time(vel_components[0], vel_components[1], vel_components[2], height, distance, time=i/100)
        #    print("x: " + str(temp[0]) + " z: " + str(temp[1]) + " y: " + str(temp[2]) + " t: " + str(temp[3]))
    
    def setparameters(self,index, value):
        self.paramlist[self.param_str[index]] = value

    def calculateTrajct(self):
        height = self.paramlist['height']
        distance = self.paramlist['distance']
        theta_vertical = self.paramlist['angle_vertical']
        theta_horizontal = self.paramlist['angle_horizontal']
        iVel = self.paramlist['iVel']
        time = self.paramlist['time']
        
        
        return self.trajectory_calculator(iVel, theta_vertical, theta_horizontal, height, distance, time)
