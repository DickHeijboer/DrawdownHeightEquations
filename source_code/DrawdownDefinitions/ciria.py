def CIRIA(W_b,h,B_s,D_s,V_s,C_m,g,L_s,alpha):
    '''
    INPUTS
    -W_b        [m]         Undisturbed channel width at the bottom
    -h          [m]         Cross-sectional averaged water depth
    -B_s        [m]         Ship's width 
    -D_s        [m]         Ship's draught
    -V_s        [m/s]       Ship's speed through water
    -C_m        [-]         Midship coefficient
    -g          [m/s^2]     Gravitational acceleration
    -L_s        [m]         Ship's length
    -alpha      [rad]       slope of the channel bank 

    OUTPUTS
    -dh         [m]         Water level depression 
    '''

    import DrawdownDefinitions as ddd
    import numpy as np

    def cot(alpha): return 1/np.tan(alpha)

    W_s = W_b + 2*h*cot(alpha)           #[m]        Bottom width of the undisturbed channel
    A_c = W_b*h + h**2*cot(alpha)        #[m^2]      Wet cross-sectional trapezaidal area of the undisturbed channel
    A_s = B_s*D_s*C_m                    #[m^2]      Ship's underwater cross-section amidships
    
    ## LIMIT SPEED   
    def LimitFactor(A_s,A_c,F_l):   return (2/3*(1-A_s/A_c + 0.5*F_l**2))**(3/2)
    def F(x):   return LimitFactor(A_s,A_c,x)
    F_l       = ddd.EquationSolver(F,0,2,1000)
    V_lim_1   = F_l *np.sqrt(g*A_c/W_s)
    V_lim_2   = np.sqrt(g*L_s/(2*np.pi))
    V_lim_3   = np.sqrt(g*h)
    V_lim     = min(V_lim_1,V_lim_2,V_lim_3)

    ## CORRECTION FACTOR
    alpha_S = 1.4 - 0.4 * V_s/V_lim

    ## WATER LEVEL DEPRESSION
    def WaterLevelDepression(V_s,g,A_c,A_s,W_s,alpha_S,dh):
            #Water Level drepression based on Continuity and Bernoulli (correction factor) Eq. 4.13 and 4.2 Van Koningsveld et al. (2023)
            A_cs = W_b * (h - dh) + cot(alpha) *(h - dh)**2  - A_s 
            dh = V_s**2/(2*g) * (alpha_S*(A_c/A_cs)**2 - 1)
            return dh
        
    def F(x): return WaterLevelDepression(V_s,g,A_c,A_s,W_s,alpha_S,x)
    dh = ddd.EquationSolver(F,0,2,1000)
    

    return dh