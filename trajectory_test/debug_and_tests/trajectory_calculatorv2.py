import math
import sympy

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

    xPos = distance * math.cos((perp_horizontal/180)* math.pi)
    zPos = distance * math.sin((perp_horizontal/180)* math.pi)
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

def trajectory_calculator(iVel, theta_vertical, theta_horizontal, height, distance):
    # find vector components
    vel_components = split_vector(iVel, theta_vertical, theta_horizontal)
    # find how much time to map trajectory
    airtime = calculate_airtime(vel_components[0], vel_components[1], vel_components[2], height, distance, theta_vertical, theta_horizontal)


    for i in range (int(airtime * 100) + 1):
        print("X: " + str(vel_components[0] * (i/100))+ " Z: " + str(vel_components[1] * i/100) + " Y: " + str(vel_components[2] * (i/100) + height + (tafrc_gravity/2) * ((i/100)**2)))


trajectory_calculator(50, 40, 30, 10, 30)