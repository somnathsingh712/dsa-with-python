class CardHand:
    def __init__(self):
        self.cards = []
    def add_card(self, rank, suit):
        self.cards.append((rank, suit))
    def play(self, suit):
        for i, card in enumerate(self.cards):
            if card[1] == suit:
                return self.cards.pop(i)
        if self.cards:
            return self.cards.pop(0)
        return None
    def __iter__(self):
        return iter(self.cards)
    def all_of_suit(self, suit):
        for card in self.cards:
            if card[1] == suit:
                yield card
hand = CardHand()
hand.add_card("A", "Heart")
hand.add_card("10", "Spade")
hand.add_card("K", "Heart")
hand.add_card("5", "Club")
print("Cards:")
for card in hand:
    print(card)
print()
print(hand.play("Heart"))
print()
for card in hand.all_of_suit("Club"):
    print(card)