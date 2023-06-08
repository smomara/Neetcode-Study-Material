# Arrays & Hashing

## Arrays
Arrays hold values of the same type at contiguous memory locations. They are the most common data structure encountered during interviews, so mastery over the topic is absolutely essential.

### Advantages of Arrays
- Accessing elements is O(1)

### Disadvantages of Arrays
- Addition and removal of elements into and from the middle of an array is slow because the remaining elements need to be shifted
- Some languages have fixed array sizes and adding an element when it is at its size limit takes O(n) time

### Common Terms
- Subarray: a range of contiguous values within an array
- Subsequence: a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements.

### Time Complexity
| Operation | Big-O |
| --------- | ----- |
| Access    | O(1)  |
| Search (unsorted array) | O(n)  |
| Search (sorted array) | O(log n) |
| Insert (front or middle) | O(n) |
| Insert (end) | O(1) |
| Remove (front or middle) | O(n) |
| Remove (at the end) | O(1) |

## Hash Tables
A hash table (also known as a hash map or dictionary) is a data structure that implements an associative array abstract data type by mapping key to values using a hash function and an array.

### Advantages of Hash Tables
- Searching, insertion, and removal is O(1)

### Disadvantes of Arrays
- Performance decreases with collisions

### Time Complexity
| Operation | Big-O |
| -- | -- |
| Search | O(1) |
| Insert | O(1) |
| Remove | O(1) |
