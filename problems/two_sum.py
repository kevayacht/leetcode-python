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
def two_sum(supply, target):    # Brute Force, optimized.
    for i in range(0, len(supply)):
        for j in range(i + 1, len(supply)):
            if supply[i] > target or supply[j] > target:
                pass
            elif supply[i] + supply[j] == target:
                return [i, j]

# this problem could be further optimized by using a hash map.


def main():
    print("Hello World")


if __name__ == "__main__":
    main()
