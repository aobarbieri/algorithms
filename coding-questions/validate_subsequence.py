def isValidSubsequence(array, sequence):
    seqIdx = 0

    for i in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == i:
            # if num in sequence is equal num in array -> we found the first match index, we need to look for the next index in sequence
            # increase position of the sequence so we can verify that index now
            seqIdx += 1

    return (seqIdx == len(sequence))


print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))

# subsequence -> is a set of numbers that aren't necessarily
# adjacent in the array but that are in the same order as they appear
# in the array.

# Time = O(n) - where N is the length of the main array. We will have to go through the entire array in the worst case.
# Space = 0(1) - constant, we are not storying anything extra.
