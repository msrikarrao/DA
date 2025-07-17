def isPrimeNumber(n, i = 2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return isPrimeNumber(n, i + 1)
def main(n):
    if isPrimeNumber(n):
        print(F"{n} is a prime number.")
    else:
        print(F"{n} is not a prime number.")
if __name__ == "__main__":
    n = int(input("Enter a number : "))
    main(n)