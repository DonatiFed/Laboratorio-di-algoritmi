##Insertion sort
def insertion_sort(A):
    for j in range(1,len(A)):
     key = A[j]
     i = j-1
     while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i-1
     A[i+1] = key


##Bubble sort
def bubble_sort(A):
    for i in range(len(A)):
     swapped=False
     for j in range(0, len(A)-i-1):
        if A[j]>A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]
            swapped=True
     if not swapped:
        break