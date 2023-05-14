i = int(input("Want print the table -- Enter the no between 1 to 5 :"))
if i == 1 :
    n = 10
elif i == 2 :
    n = 20
elif i == 3 :
    n = 30
elif i == 4 :
    n = 40 
elif i == 5 :
    n = 50
else : 
    print("Please entere the no between 1 to 5")
    
while i <= n :
    if n == 10 :
        print(i)
        i = i + 1
    elif n == 20 :
        print(i)
        i = i+2
    elif n == 30 :
        print(i)
        i = i+3
    elif n == 40 :
        print(i)
        i = i+4 
    elif n == 50 :
        print(i)
        i = i+5
    elif i > 5 :
        break
    else :
        print("Your reslut is printed sucessfully")