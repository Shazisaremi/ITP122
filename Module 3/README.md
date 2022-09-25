# ITP122 : Module 2

## Python If ... Else

### Python Conditions and If statements

Python supports the usual logical conditions from mathematics:

- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the `if` keyword.

```python
a = 33
b = 200
if b > a:
    print("b is greater than a")
```

### Indentation

Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming
languages often use curly-brackets for this purpose.

```python
a = 33
b = 200
if b > a:
    print("b is greater than a")  # you will get an error
```

### Elif

The `elif` keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

```python
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
```

### Else

The `else` keyword catches anything which isn't caught by the preceding conditions.

```python
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
```

You can also have an `else` without the `elif`:

```python
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
```

## Python Strings

### Strings

Strings in python are surrounded by either single quotation marks, or double quotation marks.

`'hello'` is the same as `"hello"`.

You can display a string literal with the `print()` function:

```python
print("Hello")
print('Hello')
```

### Multiline Strings

You can assign a multiline string to a variable by using three quotes:

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

### Strings are Arrays

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

```python
a = "Hello, World!"
print(a[1])  # Print the second character in the string a
print(a[0:4])  # Print from first character to fifth character
print(a[6:])  # Print from Sixth character to the end character
print(a[-1])  # Print the last character
```

## Python RegEx

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

### RegEx Module

Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module:

```python
import re
```

### RegEx Functions

The re module offers a set of functions that allows us to search a string for a match:

| Function | Description                                                       |
|----------|-------------------------------------------------------------------|
| findall  | Returns a list containing all matches                             |
| search   | Returns a Match object if there is a match anywhere in the string |
| split    | Returns a list where the string has been split at each match      |
| sub      | Replaces one or many matches with a string                        |

### The search() Function

The `search()` function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:

```python
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
```

### Sets

A set is a set of characters inside a pair of square brackets `[]` with a special meaning:

| Set        | Description                                                                                                           |
|------------|-----------------------------------------------------------------------------------------------------------------------|
| [arn]      | Returns a match where one of the specified characters (a, r, or n) is present                                         |
| [a-n]      | Returns a match for any lower case character, alphabetically between a and n                                          |
| [^arn]     | Returns a match for any character EXCEPT a, r, and n                                                                  |
| [0123]     | Returns a match where any of the specified digits (0, 1, 2, or 3) are present                                         |
| [0-9]      | Returns a match for any digit between 0 and 9                                                                         |
| [0-5][0-9] | Returns a match for any two-digit numbers from 00 and 59                                                              |
| [a-zA-Z]   | Returns a match for any character alphabetically between a and z, lower case OR upper case                            |
| [+]        | In sets, +, *, ., \|, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string |

### Example :

```python
import re

user_input = input("Enter your password: \n")
temp = True
while temp:
    if (len(user_input) < 5 or len(user_input) > 20):
        break
    elif not re.search("[A-Z]", user_input):
        break
    elif not re.search("[a-z]", user_input):
        break
    elif not re.search("[0-9]", user_input):
        break
    elif not re.search("[$#@]", user_input):
        break
    elif re.search("\s", user_input):
        break
    else:
        print("\nValid Password")
        temp = False
        break
if temp:
    print("\nNot a Valid Password")
```

## Exercise 1: Temperature Conversion

You’re in charge of noting down the temperature in a laboratory experiment. You took down values in Celsius and later
found out that you had to note them down in Fahrenheit. Write a Python program to convert your temperature values from
Celsius to Fahrenheit. Similarly, write a Python program that will convert temperature values recorded in Fahrenheit to
Celsius. Round off your answers to 4 decimal points.

Note:

Tf = Tc * (9/5 +32)

Tc = (Tf - 32) * 5/9

Where,

Tf = Temperature in Fahrenheit

Tc = Temperature in Celsius

## Exercise 2: Financial Help Scheme

To be eligible for a financial help scheme that has been implemented to help students with their education costs,
students must be over 18 years of age and have a total annual income of less than $20,000. If students are over 18 years
of age but have an income of more than $20,000, they are not eligible for the scheme and will not receive any financial
help. Also, if students have an income of less than $20,000 but are under 18 years of age, they will still not be
eligible for the scheme. Both requirements should be met in order to receive financial help. Write a Python program that
will take the age and income as input from the user and determine if they are eligible for the financial help scheme or
not.

Hint: Use logical operators

## Exercise 3: Grade Predictor

You have to build a grade predictor algorithm based on the grading system provided by your university. You have to take
the scores/marks of the user as an input and then determine which grading category it belongs to. Once that is
determined, you have to return the user’s scores corresponding grade as the output.

Assume the grading system at your university is as follows:

| <50                | &Fail (F)             |
|--------------------|-----------------------|
| 50 <= (Marks) < 65 | Pass (P)              |
| 65 <= (Marks) < 75 | Credit (CR)           |
| 75 <= (Marks) < 90 | Distinction (D)       |
| > = 90              | High Distinction (HD) |

If the user gives a number that is beyond the range 0-100, you should return, ‘Error! Enter a valid value.’

## Exercise 4: Password Validation

As a web designer, you have designed a brand new website, and additionally, you have created a login page that requires
the user to input a username and password. You have to validate the password the user chooses. The minimum requirements
for a strong password are the following:

- The number of characters in the password should be between 5 to 20.
- The password must contain at least one capital letter
- The password must contain at least one small letter.
- The password must contain at least one number.
- The password must contain at least one special character.

Write a Python program to validate the password by keeping in mind the above requirements. If the password meets all the
requirements listed above, return a statement saying, ‘Password is valid!’. If the password does not meet all the
requirements listed above, return an error saying ‘Error!
The password does not meet all requirements. Please try again.’