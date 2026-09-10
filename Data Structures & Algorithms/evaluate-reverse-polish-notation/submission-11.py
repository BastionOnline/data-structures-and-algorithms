class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create stack
        integers = []

        # loop through each expression
        for token in tokens:

        # evaluate each operator
            if token == "+":
                a, b = integers.pop(), integers.pop()
                integers.append(b + a)
                
            elif token == "-":
                a, b = integers.pop(), integers.pop()
                integers.append(b - a)

            elif token == "*":
                a, b = integers.pop(), integers.pop()
                integers.append(b*a)


            elif token == "/":
                a, b = integers.pop(), integers.pop()
                integers.append(int(b/a))

            else:
                integers.append(int(token))
                # print(integers)
        
        return integers[-1]

        # store ints in a stack
        # if an operation is found pop 2, a and b, and operate as b and a