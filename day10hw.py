def recursive_range(start, end, gap=1):
   
    if (gap > 0 and start >= end) or (gap < 0 and start <= end):
        return []
    return [start] + recursive_range(start + gap, end, gap)
start = 2
end = 20
gap = 4

result = recursive_range(start, end, gap)
print(result)
