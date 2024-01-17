def Schijf_corrected(W_s,h,B_s,D_s,V_s,C_m,g):
    '''
    Schijf 1949 method for water level depression including a correction factor developed by Delft Hydraulics (1953)
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
    - This method generates way higher values than Schijf original method
    - Iterative method to solve for return current is used instead of iteratively solving for dh
    - Slight deviation in both methods, even though it should be the same
    - Could be caused by the iteration
    '''

    import DrawdownDefinitions as ddd
    import numpy as np

    A_c     = W_s*h             #[m^2]      Wet cross-sectional area of the undisturbed channel
    A_s     = B_s*D_s*C_m       #[m^2]      Ship's underwater cross-section amidships

    ## LIMIT SPEED   
    def LimitSpeed(g,h,A_s,A_c,V_lim):
        #Limit speed calculation Eq. 4.10 Van Koningsveld et al (2023)
        if 3* (V_lim/np.sqrt(g*h))**(2/3) - 2*(1-A_s/A_c) < 0: V_lim = np.nan
        else: V_lim = np.sqrt(g*h) * np.sqrt( 3* (V_lim/np.sqrt(g*h))**(2/3) - 2*(1-A_s/A_c) )  
        return V_lim
    
    
    def F(x):  return LimitSpeed(g,h,A_s,A_c,x)
    V_lim = ddd.EquationSolver(F,0,20,1000)     #Issue: There can be multiple values of V_lim the equation satisfies for, for now the lowest value between the given range [0,20] is taken as the solution
    
    ## RETURN CURRENT
    def ReturnCurrent(A_s,A_c,V_s,g,h,U_r):
        #Return current calculation Eq. 4.11 Van Koningsveld et al (2023)
        U_r = (V_s+U_r) * ( ( (V_s+U_r)**2 - V_s**2 ) / (2*g*h) + A_s/A_c)
        return U_r
    def F(x): return ReturnCurrent(A_s,A_c,V_s,g,h,x)
    U_r = ddd.EquationSolver(F,0,5,100)

    ## CORRECTION FACTOR
    alpha_S = 1.4 - 0.4 * V_s/V_lim #Correction factor calculation (Delft Hydraulics, 1953) Eq. 4.14 Van Koningsveld et al (2023)

    ## WATER LEVEL DEPRESSION
    def WaterLevelDepression(V_s,g,A_c,A_s,W_s,alpha_S,dh):
            #Water Level drepression based on Continuity and Bernoulli (correction factor) Eq. 4.13 and 4.2 Van Koningsveld et al. (2023)
            A_cs = A_c - A_s - W_s*dh
            dh = V_s**2/(2*g) * (alpha_S * (A_c/A_cs)**2   - 1)
            return dh
        
    def F(x): return WaterLevelDepression(V_s,g,A_c,A_s,W_s,alpha_S,x)
    dh = ddd.EquationSolver(F,0,5,100)

    return dh