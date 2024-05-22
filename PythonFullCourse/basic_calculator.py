num1 = input("Enter a number: ") 
num2 = input("Enter another number: ")
operation = input("What do you want to do?\n 1. add \n 2. multiply \n 3. divide\n : ").strip(" ")

if operation == "1":
  # float allows using decimal numbers
  print(float(num1) + float(num2))
elif operation == "2": 
  print(float(num1) * float(num2))
elif operation == "3": 
  print(float(num1) / float(num2))
