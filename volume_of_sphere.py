def compute_volume_of_sphere(radius):
    """
    Computes the volume of a sphere given its radius.

    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    float: The volume of the sphere.
    """
    import math
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    volume = (4/3) * math.pi * (radius ** 3)
    return volume
radius1 = 30 
radius2 = 40

volume1 = compute_volume_of_sphere(radius1)
print(f"The volume of sphere with radius {radius1} is: {volume1}") 

volume2 = compute_volume_of_sphere(radius2)
print(f"The volume of sphere with radius {radius2} is: {volume2}")
