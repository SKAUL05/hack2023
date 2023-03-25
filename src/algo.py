from codecarbon import track_emissions
import time

# Merge Sort Algorithm
@track_emissions(project_name="green")
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge_list(left, right)

@track_emissions(project_name="green")
def merge_list(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# Merge Intervals Algorithm
@track_emissions(project_name="green")
def merge_intervals(intervals):
    print("Merging intervals...")
    time.sleep(30)
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


# Driver code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print(arr)
    arr = merge_sort(arr)
    print("Sorted array is: ", end="\n")
    print(arr)
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print("Given intervals are", end="\n")
    print(intervals)
    intervals = merge_intervals(intervals)
    print("Merged intervals are", end="\n")
    print(intervals)