def My_max(mylist):
    
    User_Input=int(input('How many numbers are you going to enter'))
    print('ok, sounds good')
    mylist=[]


    for i in range(User_Input):
        User_Input2=int(input('what is the number'))
        mylist.append(User_Input2)
    y=len(mylist)
    max=mylist[0]

    for y in mylist:
        if y > max:
            max=y
        
    return max


print('The largest element is', My_max('mylist'))


    