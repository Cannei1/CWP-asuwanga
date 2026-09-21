first_number = int(input("Enter first number: "))
second_number = int(input("Enter first number: "))
result = first_number*second_number
print(f"{first_number} x {second_number} = {result}")

if result > 0:
    print("This number is positive.")
elif result < 0:
    print("This number is negative.")
else:
    print("This number is both positive and negative.")


