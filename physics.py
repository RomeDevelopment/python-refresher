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
    F_direction = F_direction % (2 * np.pi)
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


# takes Magnitude in Newtons and angle in radians
#


def calculate_AUV_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    if inertia > 0:
        return F_magnitude * np.sin(F_angle) * thruster_distance
    else:
        return ValueError


# Calculates acceleration in m/s^2 taking a (1,4) shape Array, T
# and alpha and theta in radians.
# Mass has a default value of 100 kg, but other inputs can be used in kilograms also


def calculate_AUV2_acceleration(T, alpha, theta, mass=100):
    if type(T) != np.ndarray:
        return ValueError
    if np.shape(T) != (1, 4):
        return ValueError

    elif mass < 0:
        return ValueError

    # For future integration techniques, an initalization

    F_x = 0
    F_y = 0
    Force = [F_x, F_y]

    R = rotation_matrix(theta)
    Force = (
        R
        * np.ndarray(
            [
                [np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],
                [np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)],
            ]
        )
        * T
    )
    return Force / mass


# T is an np.ndarray, alpha is defined in radians with
# T_0 being the bottom right thruster, T_1 being top right, T_2 being top left, T_3 bottom left
# little l is horizontal, big L is vertical, inertia is defined in kg*m^2
def calculate_AUV2_angular_acceleration(T, alpha, l, L, inertia):
    if type(T) != np.ndarray:
        return ValueError
    elif inertia <= 0:
        return ValueError

    r = np.sqrt(l**2 + L**2)
    beta = np.arctan(L / l)
    new_force = T[0] + -T[1] + T[2] - T[3]
    return np.sin(alpha + beta) * r * new_force / inertia
