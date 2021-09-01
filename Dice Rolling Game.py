yy=input("Enter the operation:   ")

enter1=int(input("Enter the first number:  "))
enter2=int(input("Enter the second number:  "))


if yy==("division"):
    divi=(enter1)/(enter2)
if yy==("multiplication"):
    divi=(enter1)*(enter2)
if yy==("addition"):
    divi=(enter1)+(enter2)
if yy==("subtraction"):
    divi=(enter1)-(enter2)
    
divi=str(divi)
print ("The Answer Is", divi) 