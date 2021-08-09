import math
import sympy


# create constants
tafrc_gravity = -9.8
tafrc_air_density = 1.225
tafrc_ball_mass = 0.141748 # in grams

def calculate_drag_force(velocity):
    # Fd = 1/2 (rho) (v^2) (Cd) (A)
    drag_coeff = 0.2
    ball_radius = 0.0889

    F_drag = (1/2)(tafrc_air_density)(velocity**2)(drag_coeff)((ball_radius**2) * math.pi)
    return F_drag

def calculate_magnus_force(velocity):
    lift_coeff = 0.2
    ball_radius = 0.0889
    F_magnus = (1/2)(tafrc_air_density)(velocity**2)(lift_coeff)((ball_radius**2) * math.pi)
    return F_magnus

def total_accel_by_force(F_drag, F_magnus):
    A_drag = F_drag/tafrc_ball_mass
    A_magnus = F_magnus/tafrc_ball_mass

    split_drag = split_vector(A_drag)
    split_magnus = split_vector(A_magnus)

    total_accel = [split_drag[0] + split_magnus[0], split_drag[1] + split_magnus[1], split_drag[1] + split_magnus[1]]

    return total_accel

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

def calculate_start_position(height, distance, theta_horizontal):
    perp_horizontal = theta_horizontal if theta_horizontal <= 90 else theta_horizontal - 90

    xPos = distance * math.sin((perp_horizontal/180)* math.pi) if theta_horizontal <= 90 else distance * math.cos((perp_horizontal/180)* math.pi)
    zPos = distance * math.cos((perp_horizontal/180)* math.pi) if theta_horizontal <= 90 else distance * math.sin((perp_horizontal/180)* math.pi)
    yPos = height
    position = [xPos, zPos, yPos]
    return position

def calculate_airtime(iVel, xVel, zVel, yVel, height, distance, theta_vertical, theta_horizontal):
    # init position
    position = calculate_start_position(height, distance, theta_horizontal)
    total_accel = total_accel_by_force(calculate_drag_force(iVel), calculate_magnus_force(iVel))

    # calculate possible air times
    quadsolve_discriminant = math.sqrt(yVel**2 - 4 * ((tafrc_gravity + total_accel[2])/2) * height)
    max_time = (-yVel + quadsolve_discriminant)/((tafrc_gravity + total_accel[2])/2) if (-yVel + quadsolve_discriminant)/((tafrc_gravity + total_accel[2])/2) > 0 else (-yVel - quadsolve_discriminant)/((tafrc_gravity + total_accel[2])/2)
    x_time = position[0]/xVel

    # find correct air time
    airtime = x_time if x_time >= max_time else max_time

    return airtime

def position_at_time(iVel, xVel, zVel, yVel, height, distance, time):
    total_accel = total_accel_by_force(calculate_drag_force(iVel), calculate_magnus_force(iVel))
    position = [xVel * (time) + total_accel[0]/2 * time**2, zVel * (time) + total_accel[1]/2 * time**2, yVel * (time) + height + (tafrc_gravity/2 + total_accel[2]/2) * ((time)**2), time]
    return position

def trajectory_calculator(iVel, theta_vertical, theta_horizontal, height, distance):
    # find vector components
    vel_components = split_vector(iVel, theta_vertical, theta_horizontal)
    # find how much time to map trajectory
    airtime = calculate_airtime(iVel, vel_components[0], vel_components[1], vel_components[2], height, distance, theta_vertical, theta_horizontal)
    #print position at time x
    print(airtime)
    for i in range (int(airtime * 100) + 1):
        temp = position_at_time(iVel, vel_components[0], vel_components[1], vel_components[2], height, distance, time=i/100)
        print("x: " + str(temp[0]) + " z: " + str(temp[1]) + " y: " + str(temp[2]) + " t: " + str(temp[3]))


trajectory_calculator(50, 40, 30, 10, 30)