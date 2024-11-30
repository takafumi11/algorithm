from typing import List

def linear_search(arr: List[int], target: int) -> int:
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

# binary search is a search algorithm that finds the position of a target value within a sorted array.
# It compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target is found or the entire array is searched.
def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    print(linear_search(numbers, target))
    print(binary_search(numbers, target))