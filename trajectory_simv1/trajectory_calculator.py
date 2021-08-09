import math
from initial_state_calc import initial_state_calculator
from kinematics import kinematics_calculator
from spin import spin_calculator

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