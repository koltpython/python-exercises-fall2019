def iterative_factorial(n):
  # implement iterative version of the factorial function here
    result = 1
    for number in range(1, n + 1):
        result *= number
    return result


def recursive_factorial(n):
  # implement recursive version of the factorial function here
    if n == 0:
        return 1
    return n * recursive_factorial(n-1)


# Let's play
print(f'Gimme a number so that I can calculate its factorial with the two cool methods I just learned')
while True:
    x = int(input('Enter negative number to exit: '))
    if x < 0:
        break
    print(
        f'Recursive call produced {recursive_factorial(x)} and the iterative call produced {iterative_factorial(x)} ')
