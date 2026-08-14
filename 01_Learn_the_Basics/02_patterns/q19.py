class Solution:
    def pattern19(self, n):

        # Upper half
        for i in range(n, 0, -1):
            print("*" * i, end="")
            print(" " * (2 * (n - i)), end="")
            print("*" * i)

        # Lower half
        for i in range(1, n + 1):
            print("*" * i, end="")
            print(" " * (2 * (n - i)), end="")
            print("*" * i)