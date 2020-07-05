# Okay, we have an input list and a target sum, we need to achieve the
# target sum through the use of integers in the input list/array.
# 1. take the target and subtract until we reach zero, allow a backtrack option
# 2. add to a variable and compare, until we get what we need.
# 3. find the closest highest possible int, then fill up until reached.
# build a list as we progress, and make that track the total sum, then if we
# need to remove something, we can

# input, target and list of supply.
# output is the index of all the required elements.
# question: is the supplied list/array already sorted?


def two_sum(supply, target):
    supply_list = []    # add tuples in here of (index, value)
    count_sum = 0

    for index, value in enumerate(supply):
        # add
        # if

        if count_sum == target:
            break

    return supply_list


if __name__ == "__main__":
    two_sum()


