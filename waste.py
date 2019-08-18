import sys
import os


def waste(input_file):
    # insert input file into variable
    filename = input_file

    # open the file and read it's contents and store into the 'batch' variable
    with open(os.path.join(sys.path[0], filename), "r") as f:
        batch = f.read()

    # check if the length of the batch doesn't equal 52
    if len(batch) != 52:
        return "Invalid batch. Batch does not contain exactly 52 entries."

    # check if every item in the batch is unique
    for item in batch:
        if batch.count(item) > 1:
            return "This is an invalid batch. " + item + " appears more than once."

    # list to hold all the waste calculations
    waste_list = []

    # initial calculation of the batch waste
    initial_total = calculate_waste(batch)

    """ iterate through the original batch and swap out successive entries, 
    then calculate the waste. Append the calculated waste into 'waste_list' """
    for i in range(51):
        """ for some reason, after making the swap in the 'swap' function below, 
    the original batch list was swapped as well. 
    The following two lines are to revert the batch list to it's original form"""
        if i > 0:
            batch = original_batch(batch, i)
        next_waste = swap(batch, i)
        waste_list.append(next_waste)

    # initialize the smallest waste and it's index in 'waste_list'
    least_waste = waste_list[0]
    least_waste_index = 0

    # find the smallest waste and it's index
    for i in range(len(waste_list)):
        if waste_list[i] < least_waste:
            least_waste = waste_list[i]
            least_waste_index = i

    if initial_total <= least_waste:
        return "The total waste is " + str(initial_total) + ". Waste is already minimized"
    else:
        return "By swapping " + batch[least_waste_index] + " and " + batch[least_waste_index + 1] + ", you could reduce waste metric from " + str(initial_total) + " to " + str(least_waste)


def calculate_waste(calculate_batch):
    card = calculate_batch[i]
    card2 = calculate_batch[i + 1]
    # initialize total waste to 0
    total_waste = 0

    # get the ranks and suits
    for i in range(len(calculate_batch) - 1):
        # if the first character of the current item is A, set rank to 1...
        if card[0] == 'A':
            rank_1 = 1

        # ...or else if the first character is either K, Q or J, set the rank to 10...
        elif card[0] in ['K', 'Q', 'J']:
            rank_1 = 10

        else:
            # ...or else, if the rank is one digit long, set the rank to that digit
            if len(card) == 2:
                rank_1 = int(card[0])
            # ...or else, set the rank to the first two characters
            else:
                rank_1 = card[:2]

        # we do the same thing for the card below the current card as we did for the current card
        if card2[0] == 'A':
            rank_2 = 1
        elif card2[0] in ['K', 'Q', 'J']:
            rank_2 = 10
        else:
            if len(card) == 2:
                rank_2 = int(card2[0])
            else:
                rank_2 = card2[:2]

        # the suits are the last characters in the string
        suit_1 = card[-1]
        suit_2 = card2[-1]

        # if the suit is C or S, the color is red, otherwise the color is black
        if suit_1 in ['C', 'S']:
            color_1 = 'red'
        else:
            color_1 = 'black'

        if suit_2 in ['C', 'S']:
            color_2 = 'red'
        else:
            color_2 = 'black'

        """ check the suits of the current entry and the entry below. 
            The difference is the absolute value of the difference between their ranks"""
        # if the suits are the same, calculate the difference in rank...
        if suit_1 == suit_2:
            waste = abs(rank_1 - rank_2)
            total_waste += waste

        # ...otherwise, if the colors are the same, multiply the difference in rank by 2...
        elif color_1 == color_2:
            waste = 2 * abs(rank_1 - rank_2)
            total_waste += waste

        # ...otherwise, multiply the difference in rank by 3
        elif color_1 != color_2:
            waste = 3 * abs(rank_1 - rank_2)
            total_waste += waste

    return total_waste

# function to swap successive entries in the batch list


def swap(swap_batch, j):
    dummy_variable = swap_batch[j]
    swap_batch[j] = swap_batch[j + 1]
    swap_batch[j + 1] = dummy_variable

    return calculate_waste(swap_batch)

# return the swapped batch to it's original form


def original_batch(swap_batch, j):
    dummy_variable = swap_batch[j]
    swap_batch[j] = swap_batch[j - 1]
    swap_batch[j - 1] = dummy_variable

    return swap_batch


if __name__ == '__main__':
    waste(*sys.argv[1:])
