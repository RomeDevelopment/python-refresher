import numpy as np


# calculates buoyancy in Newtons given Volume in cubic meters and density in kilograms per meters cubed
def calculate_buoyancy(V, density_fluid):
    if V or density_fluid <= 0:
        raise (ValueError)
    else:
        return density_fluid * 9.81 * V


# let's you know in simple terms if something will float, returns none if equal
def will_it_float(V, mass):
    Water_weight = V * 1000
    if Water_weight > mass:
        return True
    elif Water_weight < mass:
        return False
    elif Water_weight == mass:
        return None
    elif (V or mass) <= 0:
        raise (ValueError)


# tells you the pressure in pascals at any depth, assuming depth is considered positive
def calculate_pressure(depth):
    if depth < 0:
        raise (ValueError)
    elif depth == 0:
        return 101325
    else:
        return depth * 9.81 * 1000 + 101325


# Finds acceleration in m/s^2 given Force in Newtons and Mass in kilograms
def calculate_acceleration(F, m):
    if m > 0:
        return F / m
    else:
        raise (ValueError)


# Finds Angular acceleration given tau in Newtons-meters and moment of inertia in Kg-m^2
def calculate_angular_acceleration(tau, I):
    if I > 0:
        return tau / I
    else:
        raise (ValueError)


# Finds torque given Force in Newtons and radius in Meters
def calculate_torque(F_direction, F_magnitude, r):
    F_magnitude = abs(F_magnitude)
    F_direction = F_direction % 360
    if r > 0:
        return F_magnitude * np.sin(F_direction) * r
    else:
        raise (ValueError)


def calculate_moment_of_inertia(m, r):
    return m * (r**2)


def rotation_matrix(theta):
    rotation_matrix = np.array(
        [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
    )
    return rotation_matrix


def calculate_AUV_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5, theta=0
):
    ##rotation_matrix(theta)
    Force_x = F_magnitude * np.cos(F_angle)
    Force_y = F_magnitude * np.sin(F_angle)
    Acceleration_x = Force_x / mass
    Acceleration_y = Force_y / mass

    return [Acceleration_x, Acceleration_y]


def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, Inertia=1, thruster_distance=0.5
):
    return None
