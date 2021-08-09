import math

tafrc_gravity = -9.8
tafrc_air_density = 1.225
tafrc_ball_mass = 0.141748 # in grams

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