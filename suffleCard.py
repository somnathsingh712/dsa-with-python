def shuffle(deck):
    n = len(deck) // 2
    first_half = deck[:n]
    second_half = deck[n:]
    shuffled = []
    for i in range(n):
        shuffled.append(first_half[i])
        shuffled.append(second_half[i])
    return shuffled
deck = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

print("Original List :", deck)
print("Shuffled List :", shuffle(deck))



