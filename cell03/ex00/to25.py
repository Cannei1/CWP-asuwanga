Number = int(input("Enter a number less than 25 : "))
if Number > 25:
    print("Error")
else:
    looping = 25-Number
    for i in range(looping+1):
        print (f"inside the loop, my varible is {Number}")
        Number += 1
