def binary_search(sorted_list, number_to_find):

    first_index = 0
    last_index = len(sorted_list)-1

    while first_index <= last_index:
        mid = (first_index + last_index)//2

        if sorted_list[mid] == number_to_find:
            return mid
        elif sorted_list[mid] < number_to_find:
            first_index = mid+1
        else:
            last_index = mid-1

    return -1

if __name__ == "__main__":
    l=[2,7,11,19,22,35,48,111]
    print(binary_search(l, 22))


"""
Time Complexity: O(logn)
Space Complexity: O(1)

"""