def Gelencser(W_s,h,B_s,D_s,V_s,C_m,g,L_s,d_s):
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
    import numpy as np

    A_c     = W_s*h             #[m^2]      Wet cross-sectional area of the undisturbed channel
    A_s     = B_s*D_s*C_m       #[m^2]      Ship's underwater cross-section amidships
    
    # Water level depression calculation Eq. 6 Bhowmik et. al. (1981)
    dh = 2*10**(-4) * ( (  V_s *A_s * L_s**2  / (d_s*np.sqrt(A_c))   )**(1/3) )**(2.8)

    ## NOTE: papers often give the factor to be -6, but this does not give results that make sense. Power of -4 gives appropiate results.

    return dh
