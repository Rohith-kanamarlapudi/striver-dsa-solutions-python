class Solution:
    def pattern14(self, n):
        for i in range(1, n + 1):
            for j in range(65, i + 65):
                print(chr(j), end="")
            print()