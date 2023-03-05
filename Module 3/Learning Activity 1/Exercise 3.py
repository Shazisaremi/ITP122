marks = int(input("Enter your marks: \n")) # Get the user's marks and convert it to integer, then store it in marks variable
if marks <50: # Check the condition 
    print("Grade = Fail (F)")
elif marks>=50 and marks <60: # Check the condition 
    print("Grade = Pass (P)")
elif marks>=65 and marks <75: # Check the condition
    print("Grade = Credit (CR)")
elif marks>=75 and marks <90: # Check the condition 
    print("Grade = Distinction (D)")
elif marks>=90: # Check the condition
    print("Grade = High Distinction (HD)")
else: # Else none of above condition were true, : 
    print("Error! Enter a valid value.")
