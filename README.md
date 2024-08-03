# Sorting Algorithms Comparison

This project compares the execution time of three sorting algorithms:
- **Merge Sort**
- **Insertion Sort**
- **Timsort** 

## Testing Procedure

I measured the execution time of each algorithm on different dataset sizes:

- 100 items
- 1000 items
- 5000 items
- 10000 items

## Results

### Merge Sort

- **Size 100**: 0.00008 seconds
- **Size 1000**: 0.00095 seconds
- **Size 5000**: 0.00562 seconds
- **Size 10000**: 0.01102 seconds

### Insertion Sort

- **Size 100**: 0.00008 seconds
- **Size 1000**: 0.00914 seconds
- **Size 5000**: 0.20350 seconds
- **Size 10000**: 0.82791 seconds

### Timsort

- **Size 100**: 0.00001 seconds
- **Size 1000**: 0.00005 seconds
- **Size 5000**: 0.00034 seconds
- **Size 10000**: 0.00072 seconds


## Conclusion

Based on the results, Timsort is much faster than both Merge Sort and Insertion Sort for all tested sizes. Timsort combines the best features of both Merge Sort and Insertion Sort, making it very efficient. While Insertion Sort works well for small lists, it slows down significantly with larger lists. Merge Sort is faster than Insertion Sort but still not as quick as Timsort, especially for bigger lists.

