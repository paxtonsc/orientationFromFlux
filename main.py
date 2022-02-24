
try:
    from ulab import numpy as np
except ImportError:
    import numpy as np



def ZXZ_rotation_matrix(phi, theta, psi):
    rotation_matrix = np.array([
        [np.cos(phi)*np.cos(psi) - np.cos(theta)*np.sin(phi)* np.sin(psi),
        -np.cos(phi)*np.sin(psi) - np.cos(theta)*np.cos(psi)*np.sin(phi),
        np.sin(phi)*np.sin(theta)],
        [np.cos(psi)*np.sin(phi) + np.cos(phi)*np.cos(theta)*np.sin(psi),
        np.cos(phi)*np.cos(theta)*np.cos(psi) - np.sin(phi)*np.sin(psi),
        -np.cos(phi)*np.sin(theta)],
        [np.sin(theta)*np.sin(psi),
        np.cos(psi)*np.sin(theta),
        np.cos(theta)]
    ])
    return rotation_matrix

def convert_euler_to_flux_percent(phi, theta, psi):
    R = ZXZ_rotation_matrix(phi, theta, psi)
    dot_with_sun_vec = R[:,2]

    normalized_flux = np.zeros(3)
    normalized_flux[0:3] = dot_with_sun_vec

    normalized_flux[normalized_flux<=0] = 0

    # returns percent flux of +X, +Y, +Z, -X, -Y, -Z
    return normalized_flux

# assumes flux input vector was normalized
def convert_flux_to_euler(X_flux, Y_flux, Z_flux):
    theta = np.arccos(Z_flux)
    phi = np.sin(-Y_flux/np.cos(theta))

    #assert(X_flux == np.sin(theta)*np.sin(phi))

    return 0, theta, phi


def convert_flux_percent_to_euler():
    pass

if __name__=="__main__":
    print("starting")

    # third angle applied first
    # R = Z1 * X2 * Z3 ---> theta, phi, psi
    # so first rotate by psi, then phi, then theta
    euler_angles = np.deg2rad(np.array([10, 10, 0]))
    flux = convert_euler_to_flux_percent(*euler_angles)
    print("Flux : ", flux)

    angles = convert_flux_to_euler(*flux)
    print(np.rad2deg(angles))
    print(angles)

    