def Hochstein(W_s,h,B_s,D_s,V_s,C_m,g):
    '''
    Hochstein 1967 method for water level depression
    INPUTS
    -W_s        [m]         Undisturbed channel width at the water surface
    -h          [m]         Cross-sectional averaged water depth
    -B_s        [m]         Ship's width 
    -D_s        [m]         Ship's draught
    -V_s        [m/s]       Ship's speed through water
    -C_m        [-]         Midship coefficient
    -g          [m/s^2]     Gravitational acceleration

    OUTPUTS
    -dh         [m]         Water level depression 

    COMMENTS
    - Not completely sure if the units are indeed metric
    - Not completely sure if the assumption of K=0.7 is necessary
    '''

    import DrawdownDefinitions as ddd
    import numpy as np


    A_c     = W_s*h             #[m^2]      Wet cross-sectional area of the undisturbed channel
    A_s     = B_s*D_s*C_m       #[m^2]      Ship's underwater cross-section amidships
    D       = h                 #[m]        Hydraulic mean depth
    K       = 0.7               #[-]        Constrainment factor than is a function of the blockage ratio and the length to beam ratio

    # Water level depression calculation Eq. A2 Almström, B. and Larson, M. (2020)
    C1       = (A_c/(A_c-A_s))**(2.5)

    if V_s/(K*np.sqrt(g*D)) <=0.65: 
        C2 = 0.3*np.exp(1.8*V_s/(K*np.sqrt(g*D)))
    else: 
        C2 = 1

    dh      = V_s**2*(C1-1)*  C2/(2*g)


    
    return dh

