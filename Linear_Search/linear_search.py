def linear_search(list_or_array,number_to_find):
    n = len(list_or_array)

    for i in range(n):
        if list_or_array[i] == number_to_find:
            return i
    return -1

if __name__ == "__main__":
    l=[23,3,5,7,11,4,55,9]
    print(linear_search(l,1))

# Time Complexity: O(n)
# Space Complexity: O(1)
