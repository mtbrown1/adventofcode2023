(five,four,fullh,three,tpair,pair,high) = (
    "five_of_a_kind",
    "four_of_a_kind",
    "full_house",
    "three_of_a_kind",
    "two_pair",
    "one_pair",
    "high_card"
)
card_values = {
    "A": 0xD,
    "K": 0xC,
    "Q": 0xB,
    "J": 0xA,
    "T": 0x9,
    "9": 0x8,
    "8": 0x7,
    "7": 0x6,
    "6": 0x5,
    "5": 0x4,
    "4": 0x3,
    "3": 0x2,
    "2": 0x1,
    "-": 0x0
}

hand_values = {
    five: 0x6,
    four: 0x5,
    fullh: 0x4,
    three: 0x3,
    tpair: 0x2,
    pair: 0x1,
    high: 0x0
}

def get_hand_cards_value(hand):
    val = 0
    for i in range(len(hand)):
        val += card_values[hand[(len(hand)-i-1)]]*(16**i)
    return val

def get_hand_type_value(hand):
    cards = {}
    for card in hand:
        cards[card] = cards[card] + 1 if card in cards else 1
    ccounts = cards.values()
    if 5 in ccounts:
        return hand_values[five]
    elif 4 in ccounts:
        return hand_values[four]
    elif 3 in ccounts and 2 in ccounts:
        return hand_values[fullh]
    elif 3 in ccounts:
        return hand_values[three]
    elif sum(value==2 for value in ccounts) == 2:
        return hand_values[tpair]
    elif 2 in ccounts:
        return hand_values[pair]
    else:
        return hand_values[high]


def get_hand_value(hand):
    type_value = get_hand_type_value(hand)
    cards_value = get_hand_cards_value(hand)
    # print(type_value, cards_value)
    # print(hex(type_value), hex(cards_value))
    return (type_value*(16**5)) + cards_value

hands = []
with open("day07.input") as input:
    for line in input:
        splitline = line.split()
        hands.append((get_hand_value(splitline[0]), int(splitline[1])))

hands.sort()
points = 0
for i in range(len(hands)):
    # print(hands[i][1], "*", i+1, "=", (i+1)*hands[i][1])
    points += ((i+1)*hands[i][1])

print(points)