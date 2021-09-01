def t(arr, low, high, x):
    
    if high>=low:
        
        
        mid=(high+low)//2
        
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return t(arr,low,mid-1, x)
        else:
            return t(arr,mid+1,high, x)
    else:
        return -1
x=8
array=[6,2,2,3,4,5,6,7,8]
result = t(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")