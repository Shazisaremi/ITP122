marks = int(input("Enter your marks: \n"))
if marks <50:
    print("Grade = Fail (F)")
elif marks>=50 and marks <60:
    print("Grade = Pass (P)")
elif marks>=65 and marks <75:
    print("Grade = Credit (CR)")
elif marks>=75 and marks <90:
    print("Grade = Distinction (D)")
elif marks>=90:
    print("Grade = High Distinction (HD)")
else:
    print("Error! Enter a valid value.")