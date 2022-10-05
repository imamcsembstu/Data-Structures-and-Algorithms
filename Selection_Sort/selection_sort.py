def selection_sort(L):
    n = len(L)

    for i in range(0, n-1):
        index_min = i

        for j in range(i+1, n):
            if L[j] < L[index_min]:
                index_min = j
        if index_min != i:
            L[i], L[index_min] = L[index_min], L[i]

if __name__ == "__main__":
    L_i_s_t = [11, 2, 3, 54, 32, 12, 2]
    print("\nBefore_Sort: ", L_i_s_t ) 
    selection_sort(L_i_s_t )
    print("\nAfter_selection: ", L_i_s_t )

# Time Complexity: O(n^2)
# Space Complexity: O(1)
