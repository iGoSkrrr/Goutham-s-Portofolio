def bubble(arr): #Bubble Sort
    n=len(arr)
    
    
    for i in range(n-1):
        
        
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
            
arr=[3,4,2,5,7]
bubble(arr)
print("sorted array is,")
for i in range(len(arr)):
    print(" %d" % arr[i])


            
            