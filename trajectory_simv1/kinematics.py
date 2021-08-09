import math
from initial_state_calc import initial_state_calculator


tafrc_gravity = -9.8
tafrc_air_density = 1.225
tafrc_ball_mass = 0.141748 # in grams

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