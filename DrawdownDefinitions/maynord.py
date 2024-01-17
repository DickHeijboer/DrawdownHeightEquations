def Maynord(W_s,h,B_s,D_s,V_s,C_m,g,L_s,d_s):
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
    import DrawdownDefinitions as ddd

    A_c     = W_s*h             #[m^2]      Wet cross-sectional area of the undisturbed channel
    A_s     = B_s*D_s*C_m       #[m^2]      Ship's underwater cross-section amidships
    D       = h                 #[m]        Hydraulic mean depth
    
    def LimitCurrent(g,A_s,A_c,D,U_lim):
        # Limit current velocity calculation Eq. A7 Almström, B. and Larson, M. (2020)
        if 2*g*D*(A_s/A_c+1.5*(U_lim**2/(g*D))**(1/3) -1 ) > 0: 
            U_lim = np.sqrt(2*g*D*(A_s/A_c+1.5*(U_lim**2/(g*D))**(1/3) -1 ))
        else:
            U_lim = np.nan
        return U_lim
    
    def F(x):
        return LimitCurrent(g,A_s,A_c,D,x)
    U_lim = ddd.EquationSolver(F,0,20,100)
    

    factor1 = ((V_s*((V_s*A_c/(A_c-A_s)-V_s)*(1.9-1.29*V_s/U_lim)))**2/(2*g)- V_s**2/(2*g))
    factor2 = np.sqrt(0.75*(A_c/A_s)**(0.18))
    factor3 = np.exp(3*np.log(1/(0.75*(A_c/A_s)**(0.18))))
    if d_s/W_s<0.5:
        dh = factor1*(1.65-1.3*d_s/W_s)*factor2*factor3
    else:
        dh = factor2*(1.35-0.7*d_s/W_s)*factor2*factor3
    return dh