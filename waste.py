def waste(batch):
    if len(batch) != 52:
        return "Invalid batch. Batch does not contain exactly 52 entries."
    for card in range(len(batch)):
        if batch.count(card) > 1:
            return "This is an invalid batch. " + card + " appears more than once."
    
    total_waste = 0

    for i in range(len(batch) - 1):
        if batch[i][0] == 'A':
            rank_1 = 1
        elif batch[i][0] in ['K', 'Q', 'J']:
            rank_1 = 10
        else:
            rank_1 = int(batch[i][0])

        if batch[i + 1][0] == 'A':
            rank_2 = 1
        elif batch[i + 1][0] in ['K', 'Q', 'J']:
            rank_2 = 10
        else:
            rank_2 = int(batch[i + 1][0])

        suit_1 = batch[i][1]
        suit_2 = batch[i + 1][1]

        if suit_1 in ['C', 'S']:
            color_1 = 'red'
        else:
            color_1 = 'black'

        if suit_2 in ['C', 'S']:
            color_2 = 'red'
        else:
            color_2 = 'black'

        if suit_1 == suit_2:
            waste = abs(rank_1 - rank_2)
            total_waste += waste
        elif color_1 == color_2:
            waste = 2 * abs(rank_1 - rank_2)
            total_waste += waste
        elif color_1 != color_2:
            waste = 3 * abs(rank_1 - rank_2)
            total_waste += waste
    
    return "The total waste is " + str(total_waste)

batch = [
    "AH",
    "KH",
    "10D",
    "5H",
    "AC",
    "10S",
    "AS",
    "8H",
    "9D",
    "5S",
    "3D",
    "7S",
    "2D",
    "JH",
    "QS",
    "2H",
    "QD",
    "6S",
    "5D",
    "8D",
    "2C",
    "JC",
    "KS",
    "KD",
    "4H",
    "3H",
    "3C",
    "6D",
    "QH",
    "9H",
    "JD",
    "7D",
    "AD",
    "2S",
    "3S",
    "4S",
    "9S",
    "9C",
    "5C",
    "7C",
    "QC",
    "10H",
    "10C",
    "8S",
    "JS",
    "4D",
    "6H",
    "4C",
    "8C",
    "7H",
    "6C",
    "KC"
]

print(waste(batch))