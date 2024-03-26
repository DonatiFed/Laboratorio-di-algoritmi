import matplotlib as plt
import numpy as np
import random
import string
import time




'''def Lcs_bruteforce(X,Y):
    if len(X)==0:
        return 0
    maxi=0
    for i in range(0,len(X)):
        s=X[0:i]+X[i+1:len(X)]
        maxi=max(maxi,Lcs_bruteforce(s,Y))
    if X in Y:
            maxi=len(X)
    return maxi        
    
'''    


X = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
Y=''.join(random.choices(string.ascii_letters + string.digits, k=10))
print(X)
print(Y)


def Lcs_recursive(X,Y):
    m=len(X)
    n=len(Y)
    if m==0 or n==0:
        return 0
    if X[m-1]==Y[n-1]:
        return 1 + Lcs_recursive(X[:-1],Y[:-1])
    else: 
        return max(Lcs_recursive(X,Y[:-1]),Lcs_recursive(X[:-1],Y))
    
  
def Lcs_recursive_memoization(X,Y):
    m=len(X)
    n=len(Y)
    lengths = [[-1000] * (n+1 ) for _ in range(m+1)]
    return Lcs_rec_mem_aux(X,Y,m,n,lengths)

def Lcs_rec_mem_aux(X,Y,x,y,lens):
    if x==0 or y==0:
        return 0
    if lens[x][y] >= 0 :
        return lens[x][y] 
    q=-1000
    if X[x-1]==Y[y-1]:
        q= 1 + Lcs_rec_mem_aux(X,Y,x-1,y-1,lens)
    else: 
        q= max(q,Lcs_rec_mem_aux(X,Y,x-1,y,lens),Lcs_rec_mem_aux(X,Y,x,y-1,lens))
    lens[x][y]=q
    return q

 



'''def LCS_Length(X, Y):
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


'''

start_time = time.time()
A= 'Cm4b'
B='Pb4i'
c = Lcs_recursive_memoization(X, Y)
d=Lcs_recursive(X,Y)
'''print("Matrice c:")
for row in c:
    print(row)
print("\nMatrice b:")
for row in b:
    print(row)
'''
#print(Lcs_bruteforce(X,Y))
end_time = time.time() 
elapsed_time = end_time - start_time
print(elapsed_time,c)
print(elapsed_time,d)
