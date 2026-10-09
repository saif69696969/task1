# ==========================================
# TASK 1: Basic Python Concepts
# ==========================================

# Question 1: Name Greeting
print("--- Question 1 ---")
name = input("Enter your name: ")
print(f"Hello, {name}")

# Question 2: Gross Pay Calculator
print("\n--- Question 2 ---")
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
gross_pay = hours * rate
print("Gross Pay:", gross_pay)

# Question 3: Celsius to Fahrenheit
print("\n--- Question 3 ---")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Question 4: Exponentiation
print("\n--- Question 4 ---")
base = float(input("Enter base number: "))
exponent = float(input("Enter exponent: "))
print(f"{base} raised to the power of {exponent} is {base ** exponent}")

# Question 5: Type Conversion Explanation
print("\n--- Question 5 ---")
age = 20
item = 5
print("age : ", age)
print("items : ", item)

age = float(age)
item = float(item)
print("age : ", age)
print("items: ", item)
print("Explanation: The float() function explicitly converts integer values into floating-point numbers.")