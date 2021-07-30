import math
def calculate_position(height, distance, theta_horizontal):
    perp_horizontal = theta_horizontal if theta_horizontal <= 90 else theta_horizontal - 90

    xPos = distance * math.sin((perp_horizontal/180)* math.pi) if theta_horizontal <= 90 else distance * math.cos((perp_horizontal/180)* math.pi)
    zPos = distance * math.cos((perp_horizontal/180)* math.pi) if theta_horizontal <= 90 else distance * math.sin((perp_horizontal/180)* math.pi)
    yPos = height
    position = [xPos, zPos, yPos]
    return position

print(calculate_position(30, 50, 90))