User=int(input(" how many numbers , for the largest element of an array:  "))

what_count=[]

for i in range(User):
    what=int(input("Enter the number here:  "))
    what_count.append(what)
    
y=len(what_count)
max=what_count[0]

for y in what_count:
    if y > max:
        max=y
        

print( max )
