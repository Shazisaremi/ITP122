# Fundamentals of Decision Logic

## Data Types

The first step to using data in any programming language is to identify its type, which is called data type. You need to
know the type of data required for the need that you are trying to address. In some programming languages, it should be
explicitly mentioned in the code. For example, int a in C++ is used to declare integer data (gladly not in Python). Data
types are the types into which data can be classified. It represents the categories of data.

There are various built-in data types in Python. Some of them are listed below:

1. Integers
2. Float
3. Boolean
4. Strings

One of the basic things that a program works with is, for example, numbers such as 1,2, or letters such as “My First
Program!”. These values can be of different types. For example, 2 is an integer, and “My First Program!” is a string (
i.e., a string of letters). You can also check the type of data, as shown in the following Python code:

```python
>> > print(2)
2
>> > print('My First Program!')
My
First
Program!
>> > type('My First Program!')
<

class 'str'>

>> > type(2)
<

class 'int'>

>> > type(1.2)
<

class 'float'>

>> > type('2')
<

class 'str'>

>> > type('1.2')
<

class 'str'>
```

> **Note** : The values like ‘1.2’ or ‘2’ look like numbers, but as they are in quotation marks, they are dealt with as strings.

## Variables

The examples you have dealt with above are the values. However, the values are represented using variables in a
programming language. Following is an assignment statement — you can find out more in the essential resources — used to
declare a variable and assign a value to it. The type of variable is the type of the value it refers to.

Variable names can not be the same as reserved words or keywords in Python. You will learn more about reserved words in
one of the essential resources.

```python
>> > 76
messages = 'Hello World!'
SyntaxError: invalid
syntax
>> > bigvalue @ = 1000000
SyntaxError: invalid
syntax
>> >

class = 'My First Program!'


SyntaxError: invalid
syntax
```

To perform arithmetic and computation operations, Python uses special symbols called operators. The operators +, -, *,
/, and ** perform addition, subtraction, multiplication, division and exponentiation, as in the following examples:

A combination of values, variables, and operators is called an expression. If you type an expression in interactive
mode, the interpreter evaluates it and displays the result:

```python
>> > 1 + 1
2
```

But in a script, an expression all by itself doesn’t do anything! This is a common source of confusion for beginners.

The %operator works on integers and yields the remainder when the first operand is divided by the second. In Python,
this is called modulus operator. See the following example:

```python
>> > quotient = 7 // 3
>> > print(quotient)
2
>> > remainder = 7 % 3
>> > print(remainder)
1
```

The **+ operator** performs addition, but it also works with strings and performs concatenation, which means joining the
strings by linking them end-to-end. For example:

```python
>> > number1 = 20
>> > number2 = 30
>> > print(number1 + number2)
50
>> > number1 = '100'
>> > number2 = '200'
>> > print(number1 + number2)
100200
```

The * *operator*  also works with strings by multiplying the content of a string by an integer. For example:

```python
>> > message = ' Hello World! '
>> > times = 3
>> > print(message * times)
Hello
World! Hello
World! Hello
World!
```

## Basics of Decision/Conditional Logic

You may rarely come across a programming language that does not feature the conditional logic constructs. The if
statement is one of the popular instructions that can be used as a decision-making statement. It gives the required
intelligence to a program so that the program implements decisions based on the criteria set by the user.

A special kind of expression is a Boolean expression, which can possibly have two results either true or false. True and
False are special values that belong to the class bool; they are not strings:

```python
>> > 7 == 5
False
>> > 6 == 6
True
>> > type(True)
<

class 'bool'>
```

The `==` operator is one of the comparison operators; the others are:

```python
x != y  # x is not equal to y
x > y  # x is greater than y
x < y  # x is less than y
x >= y  # x is greater than or equal to y
x <= y  # x is less than or equal to y
x is y  # x is the same as y
x is not y  # x is not the same as y
```

## Conditional Execution

In programming, the use of condition(s) to check the status of a value and change the behaviour of the program
accordingly is common practice. Conditional statements (the if statement in Python) can be used to achieve it. The
simplest form is:

```python
if x > 0:
    print('x is positive')
```

Notice that the if statement ends with a colon character (:) and the line(s) after the if statement are indented. The
indented statement will be executed if the logical condition evaluates to true. Statements like this are called compound
statements because they consist of more than one line. There is no limit on the number of statements that can appear in
the body, but there must be at least one. Occasionally, it is useful to have a body with no statements (usually as a
placeholder for code you haven’t written yet). In that case, you can use the pass statement, which does nothing.

```python
if x < 0:
    pass  # need to handle negative values!
```

## Algorithms

The task of a programmer is to write code to solve different business problems or to implement business applications.
However, a programmer may find several ways to code the same business problem. In other words, the same business problem
can be solved by different algorithms. Therefore an algorithm may be differentiated from the other based on the
Algorithm complexity.

### What are Algorithms?

Algorithms are rules or instructions that are formulated in a finite, sequential order to solve problems and get the
required results. They give the pseudocode for problems and can be implemented in several languages as they are not
language-specific.

### How do you Write Algorithms?

Algorithms are generally written as a combination of user-understandable language and some common programming languages.
They are commonly written down in steps however, it is not always necessary to do so. There are no distinct rules to
formulate algorithms but you will need to keep the following points in mind:

1. Figure out what is the exact problem
2. Determine where you need to start
3. Determine where you need to stop
4. Formulate the intermediate steps
5. Review your steps

**For example**, if you have to formulate an algorithm to check if a student has passed in an exam or not, you can
follow the given steps:

> **Step 1**: START
>
> **Step 2**: Declare two variables x, y
>
> **Step 3**: Store the marks obtained by the student in x
>
> **Step 4**: Store the minimum passing score in y
>
> **Step 5**: Check if x is greater than or equal to y. If yes, then return “Pass” else return “Fail”
>
> **Step 6**: STOP

However, you can manipulate the steps according to your preference. For instance, you can assign the values to the
variables in step 2 itself rather than taking steps 3 and 4. This way, a single problem can have multiple solutions and
it depends on the problem and the programmer to choose the most feasible and reliable solution.

### Elements of a Good Algorithm:

- The steps need to be finite, clear and understandable
- There should be a clear and precise description of inputs and outputs
- Each step need to have a defined output that depends only on inputs in that step or the preceding steps
- The algorithm should be flexible enough to mold it in order to allow a number of solutions
- The steps should make use of general programming fundamentals and should not be language-specific

# Activities

## **Learning Activity 1**
## Exercise 1:

Flight Deals Alice is planning a vacation to Melbourne soon and wants to book flight tickets from Sydney to Melbourne
one month in advance to get the best deal. She has come across a lucrative deal where the cost of a two-way ticket from
Sydney to Melbourne and back from Melbourne to Sydney is $400. Considering the price that she is paying is less than
what she would have normally paid, she decides to upgrade to first class. This incurs a 15% extra charge on the price
she was initially going to pay. Alice is also getting a flat discount of 20% for booking her flights one month in
advance.

Write a Python program to calculate the total amount Alice will pay for her two-way ticket including the upgrade to
first class and the discount she has received for booking in advance. Round off your final answer to two decimal points.
You may use built-in Python functions or import a math module to help you with the rounding-off of your final answer.

> **Tip**: Python consists of a number of program modules that consist of a number of methods/functions to solve programming tasks.

## **Exercise 2**:

Geometry In this exercise, you will be writing a Python program for simple geometrical calculations.

Consider a rectangle with a length of 15 metres and a breadth of 5 metres. Consider a circle with a radius of 10 metres.
For the rectangle, calculate the following:

1. the perimeter
2. the area, and
3. the diagonal.

For the circle, calculate:

1. the area, and
2. the circumference.

Write a Python program to calculate the above. Convert your answers to float and round them off to 4 decimal points.

> Note:
>
>**Perimeter of a rectangle** = 2 (length + breadth)
>
>**Area of a rectangle** = length * breadth
>
>**Diagonal of a rectangle** = sqrt(breadth2+length2)
>
>**Area of a circle** = 2 * pi * radius
>
>**Circumference of a circle** = pi * radius2

## **Learning Activity 2**

- Convert this float into an integer:
    - variable4 = 23.0
- Convert this integer into a string:
    - variable4 = 23
- Convert this float into a string:
    - variable4 = 23.0
- Convert this string into an integer:
    - variable4 = “123”

## **Learning Activity 3**

Use the operators to solve for the following equation and print the outputs

> 3 > 4
>
> 3 == 4
>
> 15 != 3
>
> 6 + 4
>
> ((27 * 2) + 46) ** 0.5
>
> Find the modulus of 35 / 6
>
> x = 200
>
> print(x > 4 or x < 300)
>
> 3 != 4 and 3 < 4
>
> x = 200
>
> print(not(x > 4 or x < 300))
>
> Assign 10 to x. If x is bigger than 0, print "x is a positive number".

## **Learning Activity 4**

Use the operators to solve for the following equation and print the outputs

1. Assign 10 to x. If x is bigger than 0, print "x is a positive number".
2. Ask a user how many family members they have. Based on the input, print the message ‘large family’ if there are more
   than 5 members.
3. Ask a user for input of two numbers and store them in the variables ‘first_number’ and ‘second_number’. Perform the
   following operations.
    - Subtract the numbers as first_number - second_number, and print the message if the difference is positive or
      negative.
    - Check if the numbers are even or odd, and print the message as ‘first_number is even/odd’ and ‘second number is
      even/odd’.
    - Add 5 to first_number and -2 to second_number, and perform tasks a and b again.
    
## **Learning Activity 5**
An algorithm to check if a student has passed in an exam or not, you can follow the given steps:

>Step 1: START
>
>Step 2: Declare two variables x, y
>
>Step 3: Store the marks obtained by the student in x
>
>Step 4: Store the minimum passing score in y
>
>Step 5: Check if x is greater than or equal to y. If yes, then return “Pass” else return “Fail”
>
>Step 6: STOP
>
Write an algorithm for the following tasks.

**Check whether a given numbe r is even or odd**

>Step 1: START
>
>Step 2: Declare a variable
>
>Step 3: Store the number in a
>
>Step 5: Check if the residual of a divide in 2 is zero. If yes, then return “even” else return “odd”
>
>Step 6: STOP
>

**Check whether a given number is a prime number.**

>STEP 1: Take num as input.
>
>STEP 2: Initialize a variable temp to 0.
>
>STEP 3: Iterate a “for” loop from 2 to num/2.
>
>STEP 4: If num is divisible by loop iterator, then increment temp.
>
>STEP 5: If the temp is equal to 0,
>
>    Return “Num IS PRIME”.
>
>Else,
>
>    Return “Num IS NOT PRIME”.
