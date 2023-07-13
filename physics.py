# calculates buoyancy in Newtons given Volume in cubic meters and density in kilograms per meters cubed
def calculate_buoyancy(V, density_fluid):
    if V or density_fluid <=0:
        raise(ValueError)
    else:
        return density_fluid * 9.81 * V


# let's you know in simple terms if something will float, returns none if equal
def will_it_float(V, mass):
    if 1000 * V > mass:
        return True
    elif 1000 * V < mass:
        return False
    elif 1000 * V == mass:
        return None
    elif V or mass <= 0:
        raise(ValueError)

# tells you the pressure in pascals at any depth
def calculate_pressure(depth):
    if depth<0:
        raise(ValueError)
    elif depth=0:
        return(101325)
    else:
        return depth * 9.81 * 1000
