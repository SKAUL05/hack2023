import time
from codecarbon import track_emissions


# Given a collection of intervals, merge all overlapping intervals.
@track_emissions(project_name="green")
def merge(intervals):
    time.sleep(30)
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


# main function to test the code
if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))
