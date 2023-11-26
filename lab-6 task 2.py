def count_frequency(numbers):
    frequency_dict = {}

    for number in numbers:
        frequency_dict[number] = frequency_dict.get(number, 0) + 1

    return frequency_dict

numbers_list = [1, 2, 3, 1, 2, 4, 5, 1, 3, 6, 7, 7, 8]
result_dict = count_frequency(numbers_list)

print("Input List:", numbers_list)
print("Frequency Dictionary:", result_dict)
