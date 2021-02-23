card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []
hand2 = card_deck.pop();
print(hand2)

while sum(hand) <= 17:
    hand.append(card_deck.pop());
print(hand)

print(card_deck);