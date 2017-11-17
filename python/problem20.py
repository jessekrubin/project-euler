def solution():
    def factorial(n):
        return 1 if n == 1 else n * factorial(n - 1)

    return sum(int(c) for c in str(factorial(100)))
