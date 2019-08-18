def waste(batch):
    waste_batch = batch
    if len(batch) != 52:
        return "Invalid batch. Batch does not contain exactly 52 entries."
    for item in batch:
        if batch.count(item) > 1:
            return "This is an invalid batch. " + item + " appears more than once."    

    waste_list = []
    initial_total = calculate_waste(batch)

    for i in range(51):
        if i > 0:
            batch = original_batch(batch, i)
        next_waste = swap(batch, i)
        waste_list.append(next_waste)
    
    least_waste = waste_list[0]
    least_waste_index = 0

    for i in range(len(waste_list)):
        if waste_list[i] < least_waste:
            least_waste = waste_list[i]
            least_waste_index = i

    if initial_total <= least_waste:
        return "The total waste is " + str(initial_total) + ". Waste is already minimized"
    else:
        return "By swapping " + batch[least_waste_index] + " and " + batch[least_waste_index + 1] + ", you could reduce waste metric from " + str(initial_total) + " to " + str(least_waste)

def calculate_waste(calculate_batch):
    total_waste = 0
    for i in range(len(calculate_batch) - 1):
        if calculate_batch[i][0] == 'A':
            rank_1 = 1
        elif calculate_batch[i][0] in ['K', 'Q', 'J']:
            rank_1 = 10
        else:
            rank_1 = int(calculate_batch[i][0])

        if calculate_batch[i + 1][0] == 'A':
            rank_2 = 1
        elif calculate_batch[i + 1][0] in ['K', 'Q', 'J']:
            rank_2 = 10
        else:
            rank_2 = int(calculate_batch[i + 1][0])

        suit_1 = calculate_batch[i][1]
        suit_2 = calculate_batch[i + 1][1]

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

    return total_waste

def swap(swap_batch, j):
    dummy_variable = swap_batch[j]
    swap_batch[j] = swap_batch[j + 1]
    swap_batch[j + 1] = dummy_variable

    return calculate_waste(swap_batch)

def original_batch(swap_batch, j):
    dummy_variable = swap_batch[j]
    swap_batch[j] = swap_batch[j - 1]
    swap_batch[j - 1] = dummy_variable

    return swap_batch
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