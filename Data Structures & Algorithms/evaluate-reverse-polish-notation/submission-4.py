class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create stack
        integers = []
        evaluation = 0

        # loop through each expression
        for token in tokens:

        # evaluate each operator
            if token == "+":
                a, b = integers.pop(), integers.pop()
                evaluation = evaluation + b + a
            elif token == "-":
                a, b = integers.pop(), integers.pop()
                evaluation += b - a
            elif token == "*":
                a, b = integers.pop(), integers.pop()
                evaluation += b*a
            elif token == "/":
                a, b = integers.pop(), integers.pop()
                evaluation += b//a
            else:
                integers.append(int(token))
        
        return evaluation

        # store ints in a stack
        # if an operation is found pop 2, a and b, and operate as b and a