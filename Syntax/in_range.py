def in_range(nums, lowest, highest):
    """Print numbers inside range."""
    for num in nums:
        if lowest <= num <= highest:
            print(num, "fits")

in_range([10, 20, 30, 40, 50], 15, 30)
