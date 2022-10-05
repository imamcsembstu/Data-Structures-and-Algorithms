def insertion_sort(L):
    n = len(L)

    for i in range(1, n):
        item = L[i]

        j = i-1

        while j>= 0 and L[j] > item:
            L[j+1] = L[j]
            j = j-1
            L[j+1] = item 

if __name__ == "__main__":
    L_i_s_t = [11, 2, 3, 54, 32, 12, 2]
    print("\nInsertion_Sort: ", L_i_s_t ) 
    insertion_sort(L_i_s_t )
    print("\nAfter_Insertion_Sort: ", L_i_s_t )

# Time Complexity: O(n^2)
# Space Complexity: O(1)