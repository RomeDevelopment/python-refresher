import numpy as np
import matplotlib.pyplot as plt

def calculate_buoyancy(V, density_fluid):
    # calculates buoyancy in Newtons given Volume in cubic meters and density in kilograms per meters cubed
    if V or density_fluid <= 0:
        raise (ValueError)
    else:
        return density_fluid * 9.81 * V
def will_it_float(V, mass):
    # let's you know in Boolean terms if something will float, returns none if equal
    Water_weight = V * 1000
    if Water_weight > mass:
        return True
    elif Water_weight < mass:
        return False
    elif Water_weight == mass:
        return None
    elif (V or mass) <= 0:
        raise (ValueError)
def calculate_pressure(depth):
    # tells you the pressure in pascals at any depth, assuming depth is considered positive
    if depth < 0:
        raise (ValueError)
    elif depth == 0:
        return 101325
    else:
        return depth * 9.81 * 1000 + 101325
def calculate_acceleration(F, m):
    # Finds acceleration in m/s^2 given Force in Newtons and Mass in kilograms
    if m > 0:
        return F / m
    else:
        raise (ValueError)
def calculate_angular_acceleration(tau, I):
    # Finds Angular acceleration given tau in Newtons-meters and moment of inertia in Kg-m^2
    if I > 0:
        return tau / I
    else:
        raise (ValueError)
def calculate_torque(F_direction, F_magnitude, r):
    # Finds torque given Force in Newtons and radius in Meters
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
def calculate_auv_acceleration(
    F_magnitude, F_angle, mass=100, volume=0.1, thruster_distance=0.5, theta=0
):
    
#Takes magnitude in Newtons and Angle in radians, mass, volume, thruster


    Force_matrix=np.array([np.cos(F_angle),np.sin(F_angle)])*F_magnitude

    Acceleration_matrix=(Force_matrix)/mass

    return (Acceleration_matrix)
def calculate_auv_angular_acceleration(
    F_magnitude, F_angle, inertia=1, thruster_distance=0.5
):
    
# takes Magnitude in Newtons and angle in radians
# returns angular acceleration by finding torque and dividing by 
    if inertia > 0:
        return F_magnitude * np.sin(F_angle) * thruster_distance/inertia
    else:
        raise ValueError
def calculate_auv2_acceleration(T, alpha, theta, mass=100):
    # Calculates acceleration in m/s^2 taking a (1,4) shape Array, T
    # and alpha and theta in radians.
    # Mass has a default value of 100 kg, but other inputs can be used in kilograms also

    # if type(T) != np.ndarray:
    #     raise TypeError("T is not an np array")
    # if np.shape(T) != (4,):
    #     raise ValueError("Shape of T is not (1,4)")
    # if mass < 0:
    #     raise ValueError("mass is less than 0")

    # For future integration techniques, an initalization

    F_x = 0
    F_y = 0

    Force = np.array([[F_x, F_y]])

    R = rotation_matrix(theta)

    Force = (((R @np.array([[np.cos(alpha), np.cos(alpha), -np.cos(alpha), -np.cos(alpha)],[np.sin(alpha), -np.sin(alpha), -np.sin(alpha), np.sin(alpha)],]
        ))@ T))
    return (Force / mass)
def calculate_auv2_angular_acceleration(T, alpha, l, L, inertia):
# T is an np.ndarray, alpha is defined in radians with
# T_0 being the bottom right thruster, T_1 being top right, T_2 being top left, T_3 bottom left
# little l is horizontal, big L is vertical, inertia is defined in kg*m^2
    if type(T) != np.ndarray:
        raise TypeError("T is not an np array")
    if np.shape(T) != (4,):
        raise ValueError("Shape of T is not (1,4)")
    if inertia <= 0:
        raise ValueError("inertia is less than 0")

    r = np.sqrt(np.power(l,2) +np.power(L,2))

    beta = np.arctan(L / l)
    translation_array=np.array([1,-1,1,-1]).T
    new_force = np.dot(translation_array,T)


    return np.sin(alpha + beta) * r * new_force / inertia
def simulate_auv2_motion(T,alpha,L,l,inertia,dt,t_final,x0,y0,theta0,mass=100):
    angular_acceleration=calculate_auv2_angular_acceleration(T,alpha,l,L,inertia)
    theta_i=theta0
    axial_acceleration=calculate_auv2_acceleration(T,alpha,theta_i, mass)
    ## Now we have the accelerations for those two degrees of freedom, so we need to integrate to get velocity,
    ## and then at that point we can find total shift for those degrees.

    ## These variables are arrays in the same shape as the number of time steps between t_0 and t_final.
    ## For each time_step(dt) we will have a value for each of these variables that reflects the 
    ## position, acceleration,omega,velocity, etc. at that point.


    ##THINGS TO ADD LATER:
    # DT CANNOT BE 0, MAKE SURE EVERYTHING IS INITIALIZED

    t=np.arange(0,t_final,dt)
    x = np.zeros_like(t)
    y=np.zeros_like(t)
    theta=np.zeros_like(t)
    omega=np.zeros_like(t)
    v_x = np.zeros_like(t)
    v_y = np.zeros_like(t)
    a = np.zeros_like(t)
    omega[0]=0
    a_x=np.zeros_like(t)
    a_y=np.zeros_like(t)
    a_angular=np.zeros_like(t)

    theta[0]=theta0

    for i in range (1,len(t)):
        a_x[i]=calculate_auv2_acceleration(T,alpha,theta[i-1])[0]
        a_y[i]=calculate_auv2_acceleration(T,alpha,theta[i-1])[1]
        a_angular[i]=calculate_auv2_angular_acceleration(T,alpha,l,L,inertia)
        v_x[i]=v_x[i-1]+a_x[i-1]
        v_y[i]=v_y[i-1]+a_y[i-1]
        omega[i]=omega[i-1]+a_angular[i-1]*dt
        theta[i]=theta[i-1]+omega[i-1]*dt
        x[i]=x[i-1]+v_x[i]*dt
        y[i]=y[i-1]+v_y[i]*dt
        
    a=np.array(zip(a_x,a_y,a_angular))
    v=np.array(zip(v_x,v_y))
    return([t,x,y,theta,v,omega,a])
def plot_auv2_motion(t,x,y,theta,v,omega,a):
    plt.plot(t,x, label="X position")
    plt.plot(t,y, label="Y posiiton")
    plt.plot(t,theta,label="Theta value")
    plt.plot(t,omega,label="Angular Velocity")
    ##Can I just make the "i" indicator empty and then it runs through everything??

    for i in range(1,len(v)):
        plt.plot(t,v[i][0], label="X velocity")
        plt.plot(t,v[i][1], label="Y velocity")
    
    for i in range(1,len(a)):
        plt.plot(t,a[i][0], label="X acceleration")
        plt.plot(t,a[i][1], label="Y acceleration")
        plt.plot(t,a[i][2], label="angular acceleration")
def plot_auv2_motion(t,x,y,theta,v,omega,a)
    plt.plot(t,x, label="X position")
    plt.plot(t,y, label="Y posiiton")
    plt.plot(t,theta,label="Theta value")
    plt.plot(t,omega,label="Angular Velocity")
    ##Can I just make the "i" indicator empty and then it runs through everything??

    for i in range(1,len(v)):
        plt.plot(t,v[i][0], label="X velocity")
        plt.plot(t,v[i][1], label="Y velocity")
    
    for i in range(1,len(a)):
        plt.plot(t,a[i][0], label="X acceleration")
        plt.plot(t,a[i][1], label="Y acceleration")
        plt.plot(t,a[i][2], label="angular acceleration")

