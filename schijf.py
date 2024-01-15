def Schijf(W_s,h,B_s,D_s,V_s,C_m,g):
    '''
    Schijf 1949 method for water level depression
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
    import numpy as np

    A_c     = W_s*h             #[m^2]      Wet cross-sectional area of the undisturbed channel
    A_s     = B_s*D_s*C_m       #[m^2]      Ship's underwater cross-section amidships
    alpha_S = 1

    def WaterLevelDepression(V_s,g,A_c,A_s,W_s,dh):
        #Water Level drepression based on Continuity and Bernoulli Eq. 4.1 and 4.2 Van Koningsveld et al. (2023)
        dh = V_s**2/(2*g) * (alpha_S * (A_c/(A_c-A_s-W_s*dh))**2      - 1)
        return dh
    
    dh_guess = 0.01
    while True:
        dh_new = WaterLevelDepression(V_s,g,A_c,A_s,W_s,dh_guess)
        if abs(dh_new-dh_guess) < 0.0001:
            dh = dh_new
            break
        if np.isnan(dh_new):
            dh = np.nan
            break

        dh_guess = dh_new

    #def F(x):
    #    return WaterLevelDepression(V_s,g,A_c,A_s,W_s,x)
    #xp = ddd.EquationSolver(F,0,5,100)
    #dh = np.min(xp) 

    return dh

