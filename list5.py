def maxList(list_item):
    max_num = 0;
    
    for m in range(len(list_item)):
        if(max_num < list_item[m]):
            max_num = list_item[m];
    return max_num


mList = [2, 4, 77, 89, 3, 5];
print(max(mList));
print(maxList(mList));