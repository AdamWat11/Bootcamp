print("week01: loops")

# Exercise 1: print 1..10
for i in range(0, 10):
    print(i)

    # Exercise 2: sum 1..100
total = 0
for i in range(1, 101):
    total = total + i
    print("sum 1..100 =", total)

# Exercise 3: count evens between 1 and 50
count = 0
for i in range(____, ____):
    if i % 2 == ____:
        count = count + 1
print("evens 1..50 =", count)

# Exercise 4: multiplication table for one number
n = 7
for i in range(____, ____):
    print(n, "*", i, "=", ____)

# Exercise 5: fizzbuzz 1..30
for i in range(____, ____):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(____)

# Exercise 6: while loop countdown from 10
x = ____
while x > ____:
    print(x)
    x = x - ____
print("GO")

# Exercise 7: list loop + compute average
nums = [4, 8, 15, 16, 23, 42]
total = 0
for v in ____:
    total += v
avg = total / ____
print("avg =", avg)

# Exercise 8: nested loops draw a rectangle of stars (5 rows, 10 cols)
rows = 5
cols = 10
for r in range(rows):
    line = ""
    for c in range(____):
        line += "*"
    print(line)