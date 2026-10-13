print("Numbers from 1 to 20:")
for number in range(1, 21):
    print(number, end=" ")
print()

n = int(input("Enter a number for its multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

print("Even numbers from 1 to 50:")
number = 2
while number <= 50:
    print(number, end=" ")
    number += 2
print()
