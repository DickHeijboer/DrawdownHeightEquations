def Bhowmik(W_s,h,B_s,D_s,V_s,C_m,g,L_s,d_s):
    '''
    INPUTS
    -W_s        [m]         Undisturbed channel width at the water surface
    -h          [m]         Cross-sectional averaged water depth
    -B_s        [m]         Ship's width 
    -D_s        [m]         Ship's draught
    -V_s        [m/s]       Ship's speed through water
    -C_m        [-]         Midship coefficient
    -g          [m/s^2]     Gravitational acceleration
    -L_s        [m]         Ship's length
    -d_s        [m]         Distance between the ship's bow and the water level depression

    OUTPUTS
    -dh         [m]         Water level depression 
    '''

    # Convert to Empirical units
    W_s     = W_s/0.3048        #[ft]       Undisturbed channel width at the water surface
    h       = h/0.3048          #[ft]       Cross-sectional averaged water depth
    B_s     = B_s/0.3048        #[ft]       Ship's width
    D_s     = D_s/0.3048        #[ft]       Ship's draught
    V_s     = V_s/0.3048        #[ft/s]     Ship's speed through water
    g       = g/0.3048          #[ft/s^2]   Gravitational acceleration
    L_s     = L_s/0.3048        #[ft]       Ship's length
    d_s     = d_s/0.3048        #[ft]       Distance between the ship's bow and the water level depression


    A_c     = W_s*h             #[ft^2]     Wet cross-sectional area of the undisturbed channel
    A_s     = B_s*D_s*C_m       #[ft^2]     Ship's underwater cross-section amidships

    # Water level depression calculation Eq. 9 Bhowmik et al. (1981) blz 87
    dh = 1.03 * V_s**2 /(2*g) * (A_s/A_c)**(0.81) * (L_s/d_s)**(0.31)   #[ft] 

    dh = dh * 0.3048            #[m]          Water level depression
    return dh