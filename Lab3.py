print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1

def bubble_sort(arr, sorting_order):
    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)
    if n == 0:
        return 0
    else:
        if n < 10:
            # Traverse through all array elements
            for i in range(n - 1):
                # Last i elements are already in place
                for j in range(0, n - i - 1):
                    # Handle non-integer elements
                    if not isinstance(arr_result[j], int) or not isinstance(arr_result[j + 1], int):
                        return 2

                    if sorting_order == SORT_ASCENDING:
                        if arr_result[j] > arr_result[j + 1]:
                            arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
                    elif sorting_order == SORT_DESCENDING:
                        if arr_result[j] < arr_result[j + 1]:
                            arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
                    else:
                        # Return an empty array
                        return []

        else:
            return 1

    return arr_result

def main():
    # Driver code to test above
    arr = [64, 34, 25, 20, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

if __name__ == "__main__":
    main()
