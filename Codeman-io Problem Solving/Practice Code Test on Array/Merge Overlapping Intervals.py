def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
    merged = [intervals[0]]

    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:  # Check for overlap
            merged[-1][1] = max(merged[-1][1], interval[1])  # Merge overlapping intervals
        else:
            merged.append(interval)

    return merged

# Read input
N = int(input())
intervals = []
for _ in range(N):
    l, r = map(int, input().split())
    intervals.append([l, r])

# Merge overlapping intervals and print the result
merged_intervals = merge_intervals(intervals)
for interval in merged_intervals:
    print(interval[0], interval[1])
