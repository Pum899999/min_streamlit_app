

print("Hello, welcome to the basic Python script!")


name = input("Please enter your name: ")


print(f"Nice to meet you, {name}!")


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "undefined"


print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The difference between {num1} and {num2} is: {difference}")
print(f"The product of {num1} and {num2} is: {product}")
print(f"The quotient of {num1} divided by {num2} is: {quotient}")


print("Thanks for using the basic Python script!")

