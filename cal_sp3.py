def cal_sp3(t, sp3):
    """
    Computes the satellite position (in meters) at epoch `t` using SP3 ephemeris data.
    
    Args:
        t (float): Epoch value in seconds of day.
        sp3 (ndarray): Matrix of SP3 data. The first three columns contain the X, Y, and Z coordinates
            of the satellite, in kilometers, and the fourth column contains the time of the SP3 data point,
            in seconds of GPS week.
            
    Returns:
        ndarray: A 3-element array containing the X, Y, and Z coordinates of the satellite, in meters.
    """
    x = np.vstack((sp3[:, 0], sp3[:, 1]))
    y = np.vstack((sp3[:, 0], sp3[:, 2]))
    z = np.vstack((sp3[:, 0], sp3[:, 3]))
    
    # Get the times of the SP3 data points, in seconds of GPS week
    #T = sp3[:,0]
    
    # Interpolate the X, Y, and Z coordinates at epoch `T`
    X = lagrange(t, x)
    Y = lagrange(t, y)
    Z = lagrange(t, z)
    
    # Return the satellite position as a 3-element array
    spos = [X, Y ,Z]
    
    return spos
