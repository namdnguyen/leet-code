# Problem 412 - Fizz Buzz

https://leetcode.com/problems/fizz-buzz/description/

## Instructions

Write a program that outputs the string representation of numbers from 1 to *n*.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

### Example

```
n = 15

Return:

[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

:type n: int
:rtype: List[str]
```


## Solution

```python
class Solution:
    def fizzBuzz(self, n):
        fizzbuzz = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                fizzbuzz.append("FizzBuzz")
            elif i % 3 == 0:
                fizzbuzz.append("Fizz")
            elif i % 5 == 0:
                fizzbuzz.append("Buzz")
            else:
                fizzbuzz.append(str(i))

        return fizzbuzz
```
