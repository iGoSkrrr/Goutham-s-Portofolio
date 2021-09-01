inpt=input('hello, what number to what number. press enter and write below')

pu1=int(input("starting number"))
pu2=int(input("2nd number"))
x=[pu1, pu2]
for i in range(pu1, pu2+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
               break
               
        else:
                print( i )
        
        
        


         
         
