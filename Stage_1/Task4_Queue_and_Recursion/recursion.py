"""
Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller
subproblems until you get to a small enough problem that it can be solved trivially.

Usually recursion involves a function calling itself.


Example: Sum of a List of Numbers
    def listsum(numList):
        if len(numList) == 1:
            return numList[0]
        else:
            return numList[0] + listsum(numList[1:])

    print listsum([5,7,9,11,13])


Three Laws of Recursion
    1. A recursive algorithm must have a base case;
    2. A recursive algorithm must change its state and move toward the base case;
    3. A recursive algorithm must call itself, recursively.
"""


# Calculate n factorial: n!
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# Converting an Integer to a String in Any Base
# 10 -> "10" (base 10)
# 10 -> "1010" (base 2)

def toStr(n: int, base: int) -> str:
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]


if __name__ == '__main__':
    print(factorial(4))
    print(toStr(10, 2))
