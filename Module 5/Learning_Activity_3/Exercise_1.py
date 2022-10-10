id = input("Enter your student id:\t")

sum = 0
for letter in id:
    try:
        sum += int(letter)
    except ValueError:
        pass

output = 'Prime'
for i in range(2, int(sum/2)):
    if sum % i == 0:
        output = "Not Prime"
        break
print(output)
