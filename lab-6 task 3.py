def longest_subarray_with_sum(nums, k):
    cumulative_sum = 0
    max_length = 0
    sum_positions = {0: -1}  

    for i, num in enumerate(nums):
        cumulative_sum += num


        if cumulative_sum - k in sum_positions:
            max_length = max(max_length, i - sum_positions[cumulative_sum - k])


        if cumulative_sum not in sum_positions:
            sum_positions[cumulative_sum] = i

    return max_length


nums_array = [10, 5, 2, 7, 1, 9]
target_sum = 15
result_length = longest_subarray_with_sum(nums_array, target_sum)

print(f"The length of the longest subarray with sum {target_sum} is: {result_length}")
