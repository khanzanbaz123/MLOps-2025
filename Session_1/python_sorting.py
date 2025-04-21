# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
if __name__ == "__main__":
    data1 = [64, 34, 25, 12, 22, 11, 90]
    data2 = data1.copy()

    print("Original array:", data1)

    selection_sort(data1)
    print("Sorted array using Selection Sort:", data1)

    bubble_sort(data2)
    print("Sorted array using Bubble Sort:", data2)