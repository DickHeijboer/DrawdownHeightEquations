def Dand_and_White(W_s,h,B_s,D_s,V_s,C_m,g):
    '''
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
    '''

    # Convert to Empirical units
    W_s     = W_s/0.3048        #[ft]       Undisturbed channel width at the water surface
    h       = h/0.3048          #[ft]       Cross-sectional averaged water depth
    B_s     = B_s/0.3048        #[ft]       Ship's width
    D_s     = D_s/0.3048        #[ft]       Ship's draught
    V_s     = V_s/0.3048        #[ft/s]     Ship's speed through water
    g       = g/0.3048          #[ft/s^2]   Gravitational acceleration

    A_c     = W_s*h             #[m^2]      Wet cross-sectional area of the undisturbed channel
    A_s     = B_s*D_s*C_m       #[m^2]      Ship's underwater cross-section amidships
                   
    dh = 8.8*(A_c/A_s)**(-1.4) *(V_s**2/(2*g)) # [ft] Eq. A4 Almström, B. and Larson, M. (2020)

    dh = dh * 0.3048            #[m]          Water level depression

    return dh