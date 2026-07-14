n = 6

# Upper part
for i in range(n // 2, n, 2):
    for j in range(1, n - i, 2):
        print(" ", end="")

    for j in range(1, i + 1):
        print("*", end=" ")

    for j in range(1, n - i + 1):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print("*", end=" ")

    print()

# Lower part
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()