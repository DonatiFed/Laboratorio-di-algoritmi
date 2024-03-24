import matplotlib as plt
import numpy as np


X="XCGABBAYTU"
Y="ABBABBABBAYU"

def Lcs_bruteforce(X,Y):
    if len(X)==0:
        return 0
    maxi=0
    for i in range(0,len(X)):
        s=X[0:i]+X[i+1:len(X)]
        maxi=max(maxi,Lcs_bruteforce(s,Y))
    for j in range(0,len(Y)):
        if X in Y:
            maxi=len(X)
    return maxi        
    
    
print(Lcs_bruteforce(X,Y))
