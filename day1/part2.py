TARGET = 2020

# After looking at the dataset, most of these combos of entires add up to way more than the goal
# So I decided to sort the data to put all of the candidates at the front, and then iterate through those
# Then, I effectively performed the same operation as part 1, with an additional iteration to select the first number which creates a combined target for the operation

with open("input.dat", "r") as file:
    nums = [ int(item) for item in file.readlines()]
    nums.sort()
    for i, num in enumerate(nums):
        for candidate in nums[i:]:
            diff = TARGET - num - candidate
            if diff in nums:
                print(diff * num * candidate)
                exit(0)