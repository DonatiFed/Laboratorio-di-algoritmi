import matplotlib.pyplot as plt 
import numpy as np
import random
import string
import time
import sys
sys.setrecursionlimit(50000)

##test algoritmo brute-force
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




##Test algoritmo ricorsivo
def Lcs_recursive(X,Y):
    m=len(X)
    n=len(Y)
    if m==0 or n==0:
        return 0
    if X[m-1]==Y[n-1]:
        return 1 + Lcs_recursive(X[:-1],Y[:-1])
    else: 
        return max(Lcs_recursive(X,Y[:-1]),Lcs_recursive(X[:-1],Y))
    



#test algoritmo ricorsivo con memoization
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



##test Algoritmo iterativo
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




def eseguiTest(a):
    if a==1:
        n_values = list(range(1,13))
        time_values = []
        for i in n_values:
            X= ''.join(random.choices(string.ascii_letters + string.digits, k=i))
            Y=''.join(random.choices(string.ascii_letters + string.digits, k=i))
            start_time = time.time()
            c = Lcs_bruteforce(X, Y)
            end_time = time.time() 
            elapsed_time = end_time - start_time
            print(i,c,elapsed_time)
            time_values.append(elapsed_time)
        plt.subplot(2,1,1)
        plt.plot(n_values, time_values, linestyle='-',color='red')
        plt.title('Tempo impiegato da LCS_brute_force')
        plt.xlabel('Dimensione delle due stringhe (m=n)')
        plt.ylabel('Tempo impiegato (secondi)')
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.plot(n_values,n_values * np.power(2, n_values),linestyle='-')
        plt.title('$f(x) = x*2^x$')
        plt.grid(True)
        plt.subplots_adjust(hspace=0.8) 
        plt.show()
    elif a==2:
        n_values = list(range(1, 16))
        time_values = []
        for i in n_values:
            X= ''.join(random.choices(string.ascii_letters + string.digits, k=i))
            Y=''.join(random.choices(string.ascii_letters + string.digits, k=i))
            start_time = time.time()
            c = Lcs_recursive(X, Y)
            end_time = time.time() 
            elapsed_time = end_time - start_time
            print(i,c,elapsed_time)
            time_values.append(elapsed_time)
        plt.subplot(2,1,1)
        plt.plot(n_values, time_values, linestyle='-',color='red')
        plt.title('Tempo impiegato da LCS_recursive')
        plt.xlabel('Dimensione delle due stringhe (m=n)')
        plt.ylabel('Tempo impiegato (secondi)')
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.plot(n_values,np.exp(n_values),linestyle='-')
        plt.title('$f(x) = 2^x$')
        plt.grid(True)
        plt.subplots_adjust(hspace=0.8) 
        plt.show()
    elif a==3:
        n_values = list(range(1, 5010,200))
        time_values = []
        for i in n_values:
            X = ''.join(random.choices(string.ascii_letters + string.digits, k=i))
            Y=''.join(random.choices(string.ascii_letters + string.digits, k=i))
            start_time = time.time()
            c = Lcs_recursive_memoization(X, Y)
            end_time = time.time() 
            elapsed_time = end_time - start_time
            print(i,c,elapsed_time)
            time_values.append(elapsed_time)
        plt.subplot(2,1,1)
        plt.plot(n_values, time_values, linestyle='-',color='red')
        plt.title('Tempo impiegato da LCS_recursive_memoization')
        plt.xlabel('Dimensione delle due stringhe (m=n)')
        plt.ylabel('Tempo impiegato (secondi)')
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.plot(n_values, np.array(n_values) ** 2, linestyle='-')
        plt.title('$f(x) = x^2$')
        plt.grid(True)
        plt.subplots_adjust(hspace=0.8) 
        plt.show()

    elif a==4:
        n_values = list(range(1, 5010,100))
        time_values = []
        for i in n_values:
            X = ''.join(random.choices(string.ascii_letters + string.digits, k=i))
            Y=''.join(random.choices(string.ascii_letters + string.digits, k=i))
            start_time = time.time()
            c, b = LCS_Length(X, Y)
            end_time = time.time() 
            elapsed_time = end_time - start_time
            print(i,c[-1][-1],elapsed_time)
            time_values.append(elapsed_time)
        plt.subplot(2,1,1)
        plt.plot(n_values, time_values, linestyle='-',color='red')
        plt.title('Tempo impiegato da Lcs_recursive_table')
        plt.xlabel('Dimensione delle stringhe (m=n)')
        plt.ylabel('Tempo impiegato (secondi)')
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.plot(n_values,np.array(n_values) ** 2,linestyle='-')
        plt.title('$f(x) = x^2$')
        plt.grid(True)
        plt.subplots_adjust(hspace=0.8) 
        plt.show()

    else:
        print("Inserire un valore compreso tra 1 e 4")

