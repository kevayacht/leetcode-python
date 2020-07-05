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


# so initially I completely misunderstood this problem... I should be using
# TWO numbers to find the solution, that makes it a hell of a lot easier!!!
def two_sum(supply, target):
    index_list = []    # add tuples in here of (index, value)
    value_list = []

    for index, value in enumerate(supply):

        if sum(value_list) < target:
            # print(f"SUM: {sum(value_list)}")
            index_list.append(index)
            value_list.append(value)
        elif sum(value_list) > target:
            # print(f"SUM: {sum(value_list)}")
            difference = sum(value_list) - target
            # print(f"Difference: {difference}")

            if difference in value_list:
                removed_index = value_list.index(difference)
                # print(f"removed_index: {removed_index}")
                value_list.remove(difference)
                index_list.remove(removed_index)
        else:
            break

    # this particular problem will persist till infinity, maybe look at a
    # while loop, or recursion

    return index_list
