def twoNumberSum(array, targetSum):
    hash = {}
    result = []

    for i in array:
        target = targetSum - i

        if target in hash:
            result.append(target)
            result.append(i)
            return result
        else:
            hash[i] = True
    return result

# 