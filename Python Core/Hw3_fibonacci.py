def fibonacci(n):

    if n == 1:
        return 0
    elif 1 < n <= 3:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():

    n = int(input('Введіть значення n '))
    print(fibonacci(n))


if __name__ == "__main__":
    main()
