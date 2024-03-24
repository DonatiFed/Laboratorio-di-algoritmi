import matplotlib as plt
import numpy as np
import random
import string
import time




def Lcs_bruteforce(X,Y):
    if len(X)==0:
        return 0
    maxi=0
    for i in range(0,len(X)):
        s=X[0:i]+X[i+1:len(X)]
        maxi=max(maxi,Lcs_bruteforce(s,Y))
    if X in Y:
            maxi=len(X)
    return maxi        
    
    


X = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
Y=''.join(random.choices(string.ascii_letters + string.digits, k=10))
print(X)
print(Y)








def LCS_Length(X, Y):
    m = len(X)
    n = len(Y)
    b = [["" for _ in range(n)] for _ in range(m)]
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1, m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = "↖"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = "↑"
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = "←"
                
    return c, b




start_time = time.time()
c, b = LCS_Length(X, Y)
print("Matrice c:")
for row in c:
    print(row)
print("\nMatrice b:")
for row in b:
    print(row)
#print(Lcs_bruteforce(X,Y))
end_time = time.time() 
elapsed_time = end_time - start_time
print(elapsed_time)
