def EquationSolver(F,xmin,xmax,res):
    # x = EquationSolver(F,xmin,xmax,res)
    # Finds x such that F(x)==x in range [xmin,xmax] with resolution res
    
    ## UPDATE COMMENTS
    # 2023-10-12: Returns the first value of x where F(x)==x, instead of all values of x where F(x)==x in the range [xmin,xmax]
    #             Added a break point after the value is found to improve speed


    import numpy as np
    xp=np.nan
    X = np.linspace(xmin,xmax,res);  Y = [];        #xp = [] (see update comments)
    for i,x in enumerate(X):
        if F(x) is None:
            raise ValueError("The function F(x) does not generate output. Check the input function.") 
        Y.append(F(x) - x)                  
        if Y[i-1] is not None and (Y[i-1]<0 and Y[i]>0 or Y[i-1]>0 and Y[i]<0):
            x_point = X[i-1] - (Y[i-1] * (X[i] - X[i-1])/ (Y[i] - Y[i-1]))
            xp = x_point                            #.append(x_point) (see update comments)
            break       
    if np.isnan(xp):
        print('WARNING: No solution found in the range [' + str(xmin) + ',' + str(xmax) + '] try to extend the range')
    return xp