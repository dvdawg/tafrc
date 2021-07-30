import math
import sympy
import numpy

# create constants
tafrc_gravity = -9.8

def split_vector(iVel, theta_vertical, theta_horizontal):
    
     # split 3d vector into plane and vector
    hVel = iVel * math.cos((theta_vertical/180)* math.pi)
    yVel = iVel * math.sin((theta_vertical/180)* math.pi)
    # split plane into 2 vectors
    xVel = hVel * math.sin((theta_horizontal/180) * math.pi)
    zVel = hVel * math.cos((theta_horizontal/180) * math.pi)
    # return the components found
    components = [xVel, zVel, yVel]
    return components

def calculate_position(height, distance, theta_horizontal):
    perp_horizontal = theta_horizontal if theta_horizontal <= 90 else theta_horizontal - 90

    xPos = distance * math.sin((perp_horizontal/180)* math.pi) if theta_horizontal <= 90 else distance * math.cos((perp_horizontal/180)* math.pi)
    zPos = distance * math.cos((perp_horizontal/180)* math.pi) if theta_horizontal <= 90 else distance * math.sin((perp_horizontal/180)* math.pi)
    yPos = height
    position = [xPos, zPos, yPos]
    return position

def calculate_airtime(xVel, zVel, yVel, height, distance, theta_vertical, theta_horizontal):
    # init position
    position = calculate_position(height, distance, theta_horizontal)

    # calculate possible air times
    quadsolve_discriminant = math.sqrt(yVel**2 - 4 * (1/2) * tafrc_gravity * height)
    max_time = (yVel + quadsolve_discriminant)/tafrc_gravity if (yVel + quadsolve_discriminant)/tafrc_gravity > 0 else (yVel - quadsolve_discriminant)/tafrc_gravity
    x_time = position[0]/xVel

    # find correct air time
    airtime = x_time if x_time <= max_time else max_time

    return airtime

def position_at_time(xVel, zVel, yVel, height, distance, time):
    
    position = [xVel * (time), zVel * (time), yVel * (time) + height + (tafrc_gravity/2) * ((time)**2), time]
    return position

def trajectory_calculator(iVel, theta_vertical, theta_horizontal, height, distance):
    # find vector components
    vel_components = split_vector(iVel, theta_vertical, theta_horizontal)
    # find how much time to map trajectory
    airtime = calculate_airtime(vel_components[0], vel_components[1], vel_components[2], height, distance, theta_vertical, theta_horizontal)
    #print position at time x
    for i in range (int(airtime * 100) + 1):
        temp = position_at_time(vel_components[0], vel_components[1], vel_components[2], height, distance, time=i/100)
        print("x: " + str(temp[0]) + " z: " + str(temp[1]) + " y: " + str(temp[2]) + " t: " + str(temp[3]))


trajectory_calculator(50, 40, 30, 10, 30) 
    