class Solution:
    def whileLoop(self, d: int) -> int:
        total = 0
        count = 0
        num = d

        # For d = 0, start from 10 because 0 is not positive
        if d == 0:
            num = 10

        while count < 50:
            total += num
            count += 1
            num += 10

        return total