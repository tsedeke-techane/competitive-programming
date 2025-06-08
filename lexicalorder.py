class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        current_value = 1
        lex_order_list = []

        for _ in range(n):
            lex_order_list.append(current_value)

            if current_value * 10 <= n:
                current_value *= 10
            else:
                while current_value % 10 == 9 or current_value + 1 > n:
                    current_value //= 10  
                current_value += 1  
        return lex_order_list
