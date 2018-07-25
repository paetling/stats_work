suits = ['*', '+', '&', '$']
numbers = [1, 2, 3, 4, 5]


cards = []
for suit in suits:
    for number in numbers:
        cards.append((number, suit))

print cards, len(cards)

hands = []
i = 0
j = 1
k = 2
l = 3
m = 4

while i < len(cards):
    j = i + 1
    while j < len(cards):
        k = j + 1
        while k < len(cards):
            l = k + 1
            while l < len(cards):
                m = l + 1
                while m < len(cards):
                    hands.append((cards[i], cards[j], cards[k], cards[l], cards[m]))
                    m += 1
                l +=1
            k += 1
        j += 1
    i += 1

def hand_has_2_pair(hand):
    numbers = {}
    for card in hand:
        if not (numbers.get(card[0])):
            numbers[card[0]] = {}
        if not (numbers[card[0]].get(card[1])):
            numbers[card[0]][card[1]] = 0
        numbers[card[0]][card[1]] += 1
    if (len(numbers.keys()) != 3):
        return False

    for key in numbers:
        number_of_suits = len(numbers[key])
        if (number_of_suits != 1 and number_of_suits != 2):
            return False
    return True

print "SHOULD BE FALSE"
print hand_has_2_pair([(1, '*'), (2, '*'), (3, '*'), (4, '*'), (5, '*')])
print hand_has_2_pair([(1, '*'), (2, '*'), (4, '+'), (4, '*'), (4, '$')])
print hand_has_2_pair([(1, '*'), (2, '*'), (2, '$'), (4, '*'), (5, '$')])
print "SHOULD BE TRUE"
print hand_has_2_pair([(1, '*'), (2, '*'), (2, '$'), (4, '*'), (4, '$')])
print hand_has_2_pair([(2, '*'), (1, '*'), (2, '$'), (4, '*'), (4, '$')])
print hand_has_2_pair([(2, '*'), (2, '$'), (1, '*'), (4, '*'), (4, '$')])
print hand_has_2_pair([(2, '*'), (2, '$'), (4, '*'), (1, '*'), (4, '$')])
print hand_has_2_pair([(2, '*'), (2, '$'), (4, '*'), (4, '$'), (1, '*')])

hands_with_2_pairs = []

for hand in hands:
    if hand_has_2_pair(hand):
        hands_with_2_pairs.append(hand)

print len(hands_with_2_pairs)
for hand in hands_with_2_pairs:
    print hand

