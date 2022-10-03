# Learning Activity 1: Type, Run and Comment Code

## Exercise 1: Lists and Tuples

Write a Python program that takes comma-separated values as an input from the user and converts them into a list and a tuple.

An example of comma separated values are shown below:

user_input = 9, 10, 11, 5, 6

A list contains comma-separated values within square brackets, where the elements do not
belong to the same data type. Lists are mutable, i.e., the content of a list can be changed
during the execution of a program.
A tuple is similar to a list except that it is immutable, i.e., its content cannot be changed during the execution of a program. A tuple contains comma separated values within round brackets.


## Exercise 2: Dictionaries

Consider the following dictionary:

```python
party = {

'money': 1000,

'cake': ['cheesecake', 'sponge cake', 'flourless cake', 'biscuit cake'],

'guests': ['Bob', 'Alicia', 'Eve', 'Tom', 'Harry'],

'venue': ['outdoor', 'indoor']

}
```


Perform the following operations on the above dictionary:

You have to add another key called 'gifts' and set 'gifts' as a list with string values ['phone', 'laptop', 'camera', 'DIY card', 'chocolates']
You have to add 500 to the number that is stored under the 'money' key.
Remove 'Bob' from the list under the 'guests' key.
Write a Python program that performs the above on the dictionary.