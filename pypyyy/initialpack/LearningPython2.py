'''
Created on Aug 15, 2016

@author: sidmishraw
'''
def monkCandy():
    T   = input()
    for x in range(T) :
        N,K         = map( int, raw_input().split(" "))
        C           = map( int, raw_input().split(" "))
        C           = [-1] + C
        maxCandy    = 0
        for i in range(N/2,0,-1):
            maxheapify(C,i)
        for p in range(K) :
            print(C)
            maxCandy += C[1]
            C[1] = C[1]/2
            if C[1] <= C[2] or C[1] <= C[3] :
                maxheapify(C,1)

        print(maxCandy)    

def maxheapify(A,i):
    l = i*2 if i*2 <= len(A) - 1 else 0
    r = i*2 + 1 if i*2 + 1 <= len(A) - 1 else 0
    if l != 0 and A[l] > A[i] :
        largest = l
    else:
        largest = i
    if r != 0 and A[r] > A[largest]:
        largest = r  
    if largest != i :
        A[i],A[largest] = A[largest],A[i]
        maxheapify(A,largest)
    
monkCandy()