def running_sum(nums) -> [int]:
    finalist = []   # Man, I love puns.
    temp = 0
    for i in range(0, len(nums)):
        temp += nums[i]
        finalist.append(temp)

    return finalist

