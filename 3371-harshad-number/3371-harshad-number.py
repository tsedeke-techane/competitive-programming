class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        str_x = str(x)
        summ = 0
        for i in range(len(str_x)):
            summ += int(str_x[i])

        if x % summ == 0:
            return summ

        else:
            return -1
