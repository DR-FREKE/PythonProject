def list_sum(input_list):
    sum = 0
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable
    for list in range(len(input_list)):
        sum = sum + input_list[list];
    return sum

print(list_sum([2, 4, 5]));