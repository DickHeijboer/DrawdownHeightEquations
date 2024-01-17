import DrawdownDefinitions as ddd   
import numpy as np


## Parameters
g       = 9.81              #[m/s^2]    Gravitational acceleration
W_s     = 100               #[m]        Undisturbed channel surface width 
h       = 5                 #[m]        Cross-sectional averaged water depth in the channel (A_c/W_c)
alpha   = np.deg2rad(30)    #[rad]      Slope of the bank (required for CIRIA)
W_b     = 80                #[m]        Channel bottom width (required for CIRIA)
B_s     = 22.8              #[m]        Ships beam
D_s     = 3.3               #[m]        Ships draught
V_s     = 3.5               #[m/s]      Ships speed
L_s     = B_s*6             #[m]        Ships length
C_m     = 0.9               #[-]        Midship coefficient
C_B     = 0.8               #[-]        Block coefficient
d_s     = W_s/2             #[m]        Distance of the ship from the sailing line

## Calculations
dh_Schijf               = ddd.Schijf            (W_s,h,B_s,D_s,V_s,C_m,g)               #1949
dh_Schijf_corrected     = ddd.Schijf_corrected  (W_s,h,B_s,D_s,V_s,C_m,g)               #1953
dh_Hochstein            = ddd.Hochstein         (W_s,h,B_s,D_s,V_s,C_m,g)               #1967
dh_Dand_and_White       = ddd.Dand_and_White    (W_s,h,B_s,D_s,V_s,C_m,g)               #1978
dh_Kriebel              = ddd.Kriebel           (W_s,h,B_s,D_s,V_s,C_m,g,L_s,C_B)       #2003
dh_Gelencser            = ddd.Gelencser         (W_s,h,B_s,D_s,V_s,C_m,g,L_s,d_s)       #1977
dh_Bhowmik              = ddd.Bhowmik           (W_s,h,B_s,D_s,V_s,C_m,g,L_s,d_s)       #1981
dh_Maynord              = ddd.Maynord           (W_s,h,B_s,D_s,V_s,C_m,g,L_s,d_s)       #1996
dh_CIRIA                = ddd.CIRIA             (W_b,h,B_s,D_s,V_s,C_m,g,L_s,alpha)     #2007

## Print results
print('Schijf: ',round(dh_Schijf,2),'[m]')
print('Schijf_corrected: ',round(dh_Schijf_corrected,2),'[m]')
print('Hochstein: ',round(dh_Hochstein,2),'[m]')
print('Dand_and_White: ',round(dh_Dand_and_White,2),'[m]')
print('Kriebel: ',round(dh_Kriebel,2),'[m]')
print('Gelencser: ',round(dh_Gelencser,2),'[m]')
print('Bhowmik: ',round(dh_Bhowmik,2),'[m]')
print('Maynord: ',round(dh_Maynord,2),'[m]')
print('CIRIA: ',round(dh_CIRIA,2),'[m]')
