# Assignment - 2

# 1. Write a Python program to get a list, sorted in increasing order by the last element in
# each tuple from a given list of non-empty tuples

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print("List of tuple before sorting :", sample_list)

length = len(sample_list)
for i in range(length):
    for j in range(length - i - 1):
        if sample_list[j][-1] > sample_list[j + 1][-1]:
            swap = sample_list[j]
            sample_list[j] = sample_list[j+1]
            sample_list[j+1] = swap


print("List of tuple after sorting :", sample_list)
