fruits = ["apple", "cherry", "grape", "melon"]

for i in fruits:
    print(i)

i = 0
while True:
    try:
        print(fruits[i])
        i += 1
    except IndexError:
        break