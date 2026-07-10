print("give 2 num to divide")
print("type q to quit")

while True:
    first=input("\n First: ")
    if first=='q':
        break
    second=input("\n Second: ")
    if second=='q':
        break

    try:
        answer=int(first)/int(second)
    except ZeroDivisionError:
        print("you cant divide by 0")

    else:
        print(int(answer))

