number=int(input("enter the number "))
if number < 1:
    print("not prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print("not prime")
            break
    else:
        print("prime")