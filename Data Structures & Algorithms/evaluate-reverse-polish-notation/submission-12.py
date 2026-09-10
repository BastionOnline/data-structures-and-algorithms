class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create stack
        integers = []

        # loop through each expression
        for token in tokens:

        # evaluate each operator
            if token == "+":
                # need to assign each one uniquely
                a, b = integers.pop(), integers.pop()
                # APPEND eval to stack
                integers.append(b + a)
                
            elif token == "-":
                a, b = integers.pop(), integers.pop()
                integers.append(b - a)

            elif token == "*":
                a, b = integers.pop(), integers.pop()
                integers.append(b*a)


            elif token == "/":
                a, b = integers.pop(), integers.pop()
                # use INT on division for rounding towards 0
                # and convert to int
                integers.append(int(b/a))

            else:
                integers.append(int(token))
        # should ONLY be one value in stack, so 0 is fine to return, -1 implies there may be more
        return integers[0]

        # store ints in a stack
        # if an operation is found pop 2, a and b, and operate as b and a