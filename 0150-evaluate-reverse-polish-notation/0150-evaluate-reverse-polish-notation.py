class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                summ = int(stack.pop())  + int(stack.pop()) 
                stack.append(summ)

            elif token == "-":
                num1 = int(stack.pop()) 
                num2 = int(stack.pop()) 
                diff = num2 - num1
                stack.append(diff) 
            
            elif token == "*":
                mul = int(stack.pop())  * int(stack.pop()) 
                stack.append(mul)

            elif token == "/":
                num1 = int(stack.pop()) 
                num2 = int(stack.pop()) 
                dev = int(num2 / num1)
                stack.append(dev)   

            else:
                stack.append(int(token))             

        return stack[0]