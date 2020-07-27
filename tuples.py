def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums += (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    print(nums[1])
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)

c  = [(1, 2, 3), "Week 3", 6.453, [[1, 2, 3, 4], 5], 678, [True, False]]
print(c[3][0][2])