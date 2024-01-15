def Kriebel(W_s,h,B_s,D_s,V_s,C_m,g,L_s,C_B):
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
    -C_B        [-]         Block coefficient

    OUTPUTS
    -dh         [m]         Water level depression 
    '''

    import numpy as np

    exp2 = np.exp(2.35*(1-C_B)*D_s/h)
    exp1 = np.exp( (-215.8*D_s/L_s + 26.4) * V_s/(np.sqrt(g*L_s)) * exp2 )

    dh   = D_s*(0.0026*C_B - 0.001)*exp1

    return dh

