import math

# create constants
tafrc_gravity = -9.8
tafrc_air_density = 1.225
tafrc_ball_mass = 0.141748 # in grams

def split_vector(vector, theta_vertical, theta_horizontal):
    # split 3d vector into plane and vector
    hComp = vector * math.cos((theta_vertical/180)* math.pi)
    yComp = vector * math.sin((theta_vertical/180)* math.pi)
    # split plane into 2 vectors
    xComp = hComp * math.sin((theta_horizontal/180) * math.pi)
    zComp = hComp * math.cos((theta_horizontal/180) * math.pi)
    # return the components found
    components = [xComp, zComp, yComp]
    return components

class initial_state_calculator:
    def __init__(self, iVel, theta_vertical, theta_horizontal, height, distance):
        self.iVel = iVel
        self.theta_vertical = theta_vertical
        self.theta_horizontal = theta_horizontal
        self.height = height
        self.distance = distance

    def split_velocity(self):
         # split 3d vector into plane and vector
        hComp = self.iVel * math.cos((self.theta_vertical/180)* math.pi)
        yComp = self.iVel * math.sin((self.theta_vertical/180)* math.pi)
        # split plane into 2 vectors
        xComp = hComp * math.sin((self.theta_horizontal/180) * math.pi)
        zComp = hComp * math.cos((self.theta_horizontal/180) * math.pi)
        # return the components found
        components = [xComp, zComp, yComp]
        return components

    def calculate_start_position(self):
        perp_horizontal = self.theta_horizontal if self.theta_horizontal <= 90 else self.theta_horizontal - 90

        xPos = self.distance * math.sin((perp_horizontal/180)* math.pi) if self.theta_horizontal <= 90 else self.distance * math.cos((perp_horizontal/180)* math.pi)
        zPos = self.distance * math.cos((perp_horizontal/180)* math.pi) if self.theta_horizontal <= 90 else self.distance * math.sin((perp_horizontal/180)* math.pi)
        yPos = self.height
        position = [xPos, zPos, yPos]
        return position

class kinematics_calculator:
    def __init__(self, xVel, zVel, yVel, theta_vertical, theta_horizontal, height, distance):
        self.xVel = xVel
        self.zVel = zVel
        self.yVel = yVel
        self.theta_vertical = theta_vertical
        self.theta_horizontal = theta_horizontal
        self.height = height
        self.distance = distance 

    def calculate_airtime(self, start_position):
        # init position
        position = start_position

        # calculate possible air times
        quadsolve_discriminant = math.sqrt(self.yVel**2 - 4 * (tafrc_gravity/2) * self.height)
        max_time = (-self.yVel + quadsolve_discriminant)/tafrc_gravity if (-self.yVel + quadsolve_discriminant)/tafrc_gravity > 0 else (-self.yVel - quadsolve_discriminant)/tafrc_gravity
        x_time = position[0]/self.xVel

        # find correct air time
        airtime = x_time if x_time >= max_time else max_time

        return airtime

    def position_at_time(self, time):
        position = [self.xVel * (time), self.zVel * (time), self.yVel * (time) + self.height + (tafrc_gravity/2) * ((time)**2), time]
        return position

# class spin_calculator:
#     def __init__(self, iVel):
#         self.iVel = iVel

#     def calculate_drag_force(self, velocity):
#         # Fd = 1/2 (rho) (v^2) (Cd) (A)
#         drag_coeff = 0.2
#         ball_radius = 0.0889

#         F_drag = (1/2)(tafrc_air_density)(velocity**2)(drag_coeff)((ball_radius**2) * math.pi)
#         return F_drag

#     def calculate_magnus(self, velocity):
#         lift_coeff = 0.2
#         ball_radius = 0.0889
#         F_magnus = (1/2)(tafrc_air_density)(velocity**2)(lift_coeff)((ball_radius**2) * math.pi)
#         return F_magnus

#     def force_on_trajectory(self, force, theta_horizontal, theta_vertical):
#         acceleration_vector = force/tafrc_ball_mass
#         return self.split_vector(acceleration_vector, theta_vertical, theta_horizontal)

class trajectory_calculator:
    def __init__(self, iVel, theta_vertical, theta_horizontal, height, distance):
        self.iVel = iVel
        self.theta_vertical = theta_vertical
        self.theta_horizontal = theta_horizontal
        self.height = height
        self.distance = distance

    def calculate_trajectory(self):
        
        #define objects
        initial_state = initial_state_calculator(self.iVel, self.theta_vertical, self.theta_horizontal, self.height, self.distance)
        #define initial velocity, position
        start_pos = initial_state.calculate_start_position()
        velocity_vector = initial_state.split_velocity()

        #define kinematics object
        kinematics = kinematics_calculator(velocity_vector[0], velocity_vector[1], velocity_vector[2], self.theta_vertical, self.theta_horizontal, self.height, self.distance)
        #find airtime
        airtime = kinematics.calculate_airtime(start_pos)

        #print position at time x
        for i in range (int(airtime * 100) + 1):
            temp = kinematics.position_at_time(time=i/100)
            print("x: " + str(temp[0]) + " z: " + str(temp[1]) + " y: " + str(temp[2]) + " t: " + str(temp[3]))

my_bot = trajectory_calculator(50, 40, 30, 10, 30)
my_bot.calculate_trajectory()