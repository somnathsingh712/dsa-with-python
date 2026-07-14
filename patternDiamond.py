n = 5

# Upper half
for i in range(1, n + 1):
    # Print leading spaces
    print("  " * (n - i), end="")

    # Print stars with a space after each star
    for j in range(2 * i - 1):
        print("* ", end="")
    print()

# Lower half
for i in range(n - 1, 0, -1):
    # Print leading spaces
    print("  " * (n - i), end="")

    # Print stars with a space after each star
    for j in range(2 * i - 1):
        print("* ", end="")
    print()