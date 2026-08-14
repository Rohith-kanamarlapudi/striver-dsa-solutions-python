class Solution:
    def pattern17(self, n):

        for i in range(1, n + 1):

            # spaces
            for j in range(n - i):
                print(" ", end="")

            # increasing characters
            for j in range(1, i + 1):
                print(chr(64 + j), end="")

            # decreasing characters
            for j in range(i - 1, 0, -1):
                print(chr(64 + j), end="")

            print()