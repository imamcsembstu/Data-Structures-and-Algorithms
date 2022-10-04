def babble_sort(L):
    n = len(L)

    for i in range(n):
        for j in range (0, n-1-i):
            if L[j]>L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

if __name__ == "__main__":
    l = [11, 2, 3, 54, 32, 12, 2]
    print("\nBefore_Sort: ", l)
    babble_sort(l)
    print("\nAfter_Babble_Sort: ", l)

# Time Complexity: O(n^2)
# Space Complexity: O(1)