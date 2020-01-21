"""
Balanced parentheses means each opening symbol has a corresponding closing symbol and the pairs of parentheses
are properly nested.

Example:
    Balanced        (()()()())      (()((())()))
    Not balanced    ((((((())       (()()(()


The general case of balanced parentheses is that each different opening symbol `(, [ or {` matches
the corresponding closing symbol `), ] or }`.
    Balanced        { { ( [ ] [ ] ) } ( ) }
    Not balanced    ( ( ( ) ] ) )
"""
from Stage_1.Task3_Stack.stack import Stack


def simple_parChecker(symbolStr: str) -> bool:
    s = Stack()
    for symbol in symbolStr:
        if symbol == '(':
            s.push(symbol)
        elif symbol == ')':
            if not s.pop():
                return False

    if not s.isEmpty():
        return False
    else:
        return True


def parChecker(symbolStr: str) -> bool:
    match = {'(': ')', '[': ']', '{': '}'}
    s = Stack()
    for symbol in symbolStr:
        if symbol in "([{":
            s.push(symbol)
        elif symbol in ")]}":
            # Check whether the symbol is matched
            top = s.pop()
            if not top or match[top] != symbol:
                return False

    if not s.isEmpty():
        return False
    else:
        return True


if __name__ == '__main__':
    print(simple_parChecker('((()))'))
    print(parChecker('([[]])[{)]()'))
