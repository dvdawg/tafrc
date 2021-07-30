import math

tafrc_air_density = 1.225

def calculate_drag_force(velocity):
    # Fd = 1/2 (rho) (v^2) (Cd) (A)
    drag_coeff = 0.2
    ball_radius = 0.0889

    F_drag = (1/2)*(tafrc_air_density)(velocity**2)(drag_coeff)((0.0889**2) * math.pi)
    return F_drag


def calculate_magnus(velocity, )
