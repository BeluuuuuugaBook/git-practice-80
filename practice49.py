def swap_arry(arr):
    length = len(arr)
     
    temp_arr = arr[0]
    arr[0] = arr[length - 1]
    arr[size - 1] = temp_arr
     
    return newList
     
input_arr = [12, 35, 9, 56, 24]
ans = swap_arry(input_arr)
print(f"交換した配列は{ans}")
