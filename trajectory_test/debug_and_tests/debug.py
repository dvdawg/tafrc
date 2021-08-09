import math
tafrc_gravity = -9.8


def calculate_position(height, distance, theta_horizontal):
    perp_horizontal = theta_horizontal if theta_horizontal <= 90 else theta_horizontal - 90

    xPos = distance * math.sin((perp_horizontal/180)* math.pi) if theta_horizontal <= 90 else distance * math.cos((perp_horizontal/180)* math.pi)
    zPos = distance * math.cos((perp_horizontal/180)* math.pi) if theta_horizontal <= 90 else distance * math.sin((perp_horizontal/180)* math.pi)
    yPos = height
    position = [xPos, zPos, yPos]
    return position

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

def calculate_airtime(xVel, zVel, yVel, height, distance, theta_vertical, theta_horizontal):
    # init position
    position = calculate_position(height, distance, theta_horizontal)

    # calculate possible air times
    quadsolve_discriminant = math.sqrt(yVel**2 - 4 * (tafrc_gravity/2) * height)
    
    print(str((-yVel + quadsolve_discriminant)/tafrc_gravity))
    print(str((-yVel - quadsolve_discriminant)/tafrc_gravity))



temp = split_vector(50, 40, 30)
print(temp[0])
print(temp[1])
print(temp[2])

calculate_airtime(temp[0], temp[1], temp[2], 10, 30, 40, 30)
# print(calculate_airtime(temp[0], temp[1], temp[2], 10, 30, 40, 30))
