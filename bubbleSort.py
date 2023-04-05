# write your bubble sort algorithm below
def bubble_sort (list):
    for i in range (len(list) - 1):
        swapped = False
        print(f"iteration {i+1}")
        for j in range (len(list) - 1):
            print(f"comparing {list[j], list[j+1]}")
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
        
        if not swapped:
            return
        
    return list

sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")
