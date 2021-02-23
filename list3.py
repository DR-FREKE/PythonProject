def top_three(input_list):
    sorted_list = sorted(input_list, reverse=True);
    return sorted_list[:3];

print(top_three([2,3,5,6,8,4,2,1,10]));
