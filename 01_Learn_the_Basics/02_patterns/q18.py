class Solution:
    def pattern18(self, n):
        for i in range(1, n + 1):
            for j in range(n - i + 1, n + 1):
                print(chr(64 + j), end=" ")
            print()