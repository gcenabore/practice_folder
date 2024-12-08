sample_list = [8,2,7,3,1,2]

def if_ordered(lst):
    for i in range(1, len(lst)):
        if not lst[i] >= lst[i-1]:
            return False
    return True

def bubble_sort(lst):
    while not if_ordered(lst):
        for i in range(0,len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    
    return lst

print(bubble_sort(sample_list))