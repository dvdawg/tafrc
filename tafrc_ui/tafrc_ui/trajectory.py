import math

# create constants
tafrc_gravity = -9.8
tafrc_air_density = 1.225
tafrc_ball_mass = 0.141748 # in grams

class Trajectory():
    def __init__(self):
        self.title = 'Trajectory v1.0'
        self.paramlist={} #dictionary
        self.param_str = ['target_x(m)','target_y_height','target_z','shooter_height(m)','angle_vertical', 'angle_horizontal','initial_Velocity', 'time']
        self.default_val =[10, 5, 10, 1, 40, 20, 18, 5]

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
        
        # avoid divide by zero
        if (xVel == 0):
            #TODO: pass this message to UI so that it can be displaed in the UI
            print(f"error xVel is zero. cannot get accurate calculation!")
            x_time = 0
        else:
            x_time = position[0]/xVel

        # find correct air time
        airtime = x_time if x_time >= max_time else max_time
        return airtime

    def position_at_time(self, xVel, zVel, yVel, height, distance, time):
        position = [xVel * (time), zVel * (time), yVel * (time) + height + (tafrc_gravity/2) * ((time)**2), time]
        #return x, y for now. TODO: Later when the x-z, y-z plots are introduced, update the return values.
        return position[0], position[2], position[1]

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
        height = float(self.paramlist['shooter_height(m)'])
        #calculate distance
        distance = math.sqrt(float(self.paramlist['target_x(m)'])**2 + float(self.paramlist['target_y_height'])**2+ float(self.paramlist['target_z'])**2)
        theta_vertical = float(self.paramlist['angle_vertical'])
        theta_horizontal = float(self.paramlist['angle_horizontal'])
        iVel = float(self.paramlist['initial_Velocity'])
        time = float(self.paramlist['time'])
        
        x=[]
        y=[]
        z=[]
        for i in range(int(time)):
            x_val,y_val, z_val = self.trajectory_calculator(iVel, theta_vertical, theta_horizontal, height, distance, i)
            x.append(x_val)
            y.append(y_val)
            z.append(z_val)
        
        return x, y, z
