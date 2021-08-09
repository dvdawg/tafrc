import math

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

class spin_calculator:
    def __init__(self, iVel):
        self.iVel = iVel

    def calculate_drag_force(self, velocity):
        # Fd = 1/2 (rho) (v^2) (Cd) (A)
        drag_coeff = 0.2
        ball_radius = 0.0889

        F_drag = (1/2)(tafrc_air_density)(velocity**2)(drag_coeff)((ball_radius**2) * math.pi)
        return F_drag

    def calculate_magnus(self, velocity):
        lift_coeff = 0.2
        ball_radius = 0.0889
        F_magnus = (1/2)(tafrc_air_density)(velocity**2)(lift_coeff)((ball_radius**2) * math.pi)
        return F_magnus

    def force_on_trajectory(self, force, theta_horizontal, theta_vertical):
        acceleration_vector = force/tafrc_ball_mass
        return split_vector(acceleration_vector, theta_vertical, theta_horizontal)