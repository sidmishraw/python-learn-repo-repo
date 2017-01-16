'''
# Read input from stdin and provide input before running code
name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
import math

def monkmultiplication():
    N = input()
    A = map(int, raw_input().split(" "))
    print(A)
    q= [0,0,0]
    
    for i in A :
        if i >= q[2] :
            q[0]             = q[1]
            q[1]             = q[2]
            q[2]             = i
        elif i < q[2] and i >= q[1] : 
            q[0]             = q[1]
            q[1]             = i
        elif i < q[1] and i > q[0] :
            q[0] = i
        
        product = q[0] * q[1] * q[2]
        
        if product <= 0 :
            print(-1)
        else :
            print(product)

def monkCandy():
    T   = input()
    for x in range(T) :
        N,K         = map( int, raw_input().split(" "))
        C           = map( int, raw_input().split(" "))
        C           = [-1] + C
        maxCandy    = 0
        #heapsort(C)
        for p in range(K%N,0,-1) :
            print(C)
            if len(C) > 2 : 
                maxheapify(C, p)
                if p+1 < N and C[p] < C[p+1] :
                    maxCandy += C[p+1]
                    C[p+1] /= 2
                else :
                    maxCandy += C[p]
                    C[p] /= 2
            else:
                maxCandy += C[1]
                C[1] /= 2
            
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
        
    
def heapsort(A):
    for i in range(len(A)/2 if (len(A)/2) % 2 == 0 else len(A)/2 + 1, 0, -1):
        maxheapify(A,i)
    
    
monkCandy()