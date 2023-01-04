
print("what is your name human?")
name = input()
print("how old are you?")
age = int(input())
print("what is your weight?")
weight = float(input())
print("how tall are you?")
height = float(input())

bmi = weight / (height ** 2)

print(f"{name} your bmi is {bmi}")
