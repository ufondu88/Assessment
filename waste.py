import sys
import os


def waste(input_file):
    # open the file and read it's contents and store into the 'batch' variable
    with open(os.path.join(sys.path[0], input_file), "r") as f:
        batch = f.read()    

    # replace extraenous characters in the string with null space
    batch = batch.replace('\n', '').replace(' ', '').replace('[', '').replace(']', '').replace('"', '')
    
    # convert the string to a list
    batch = batch.split(',')

    # raise error if the batch length is not exactly 52
    if len(batch) != 52:
        print("Invalid batch. Batch does not contain exactly 52 entries.")
        raise SystemExit
    # raise error if every item in the batch is not unique
    for item in batch:
        if batch.count(item) > 1:
            print(f"This is an invalid batch. {item} appears more than once.")
            raise SystemExit
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
    smallest_waste = waste_list[0]
    smallest_waste_index = 0

    # find the smallest waste and it's index
    for i in range(len(waste_list)):
        if waste_list[i] < smallest_waste:
            smallest_waste = waste_list[i]
            smallest_waste_index = i

    if initial_total <= smallest_waste:
        print (f"The total waste is {initial_total}. Waste is already minimized")
    else:
        print(f"By swapping {batch[smallest_waste_index]} and {batch[smallest_waste_index + 1]}, you could reduce waste metric from {initial_total} to {smallest_waste}")


def calculate_waste(calculate_batch):
    # initialize total waste to 0
    total_waste = 0

    # get the ranks and suits
    for i in range(len(calculate_batch) - 1):
        current_card = calculate_batch[i]
        next_card = calculate_batch[i + 1]
        # if the first character of the current item is A, set rank to 1...
        if current_card[0].upper() == 'A':
            current_rank = 1

        # ...or else if the first character is either K, Q or J, set the rank to 10...
        elif current_card[0].upper() in ['K', 'Q', 'J']:
            current_rank = 10

        else:
            # ...or else, if there are 2 characters in the card (e.g QC or 4H), then rank is neccessarily one digit long.
            # The following two lines set the rank to that digit
            if len(current_card) == 2:
                current_rank = int(current_card[0])
            # ...or else, there have to 3 characters in the card (e.g 10H or 10C) and the rank will be the first 2 characters.
            # The following two lines will set the rank to the first two characters
            else:
                current_rank = int(current_card[:2])

        # we do the same thing for the card below the current card as we did for the current card
        if next_card[0] == 'A':
            next_rank = 1
        elif next_card[0] in ['K', 'Q', 'J']:
            next_rank = 10
        else:
            if len(next_card) == 2:
                next_rank = int(next_card[0])
            else:
                next_rank = int(next_card[:2])

        # the suits are the last characters in the string
        current_suit = current_card[-1]
        next_suit = next_card[-1]

        # if the suit is C or S, the color is red, otherwise the color is black
        if current_suit in ['C', 'S']:
            current_color = 'black'
        else:
            current_color = 'red'

        if next_suit in ['C', 'S']:
            next_color = 'black'
        else:
            next_color = 'red'

        """ check the suits of the current entry and the entry below. 
            The difference is the absolute value of the difference between their ranks"""
        # if the suits are the same, calculate the difference in rank...
        if current_suit == next_suit:
            waste = abs(current_rank - next_rank)
            total_waste += waste

        # ...otherwise, if the colors are the same, multiply the difference in rank by 2...
        elif current_color == next_color:
            waste = 2 * abs(current_rank - next_rank)
            total_waste += waste

        # ...otherwise, multiply the difference in rank by 3
        elif current_color != next_color:
            waste = 3 * abs(current_rank - next_rank)
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