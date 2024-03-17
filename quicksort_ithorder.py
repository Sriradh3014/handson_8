def partition(array):
    pivot = array[len(array) // 2]
    less = [x for x in array if x < pivot]
    greater = [x for x in array if x > pivot]
    return less,pivot, greater

def ith_order_statistic(array, i):
    less,pivot, greater = partition(array)
    if i < len(less):
        return ith_order_statistic(less, i)
    elif i >= len(array) - len(greater):
        return ith_order_statistic(greater, i - (len(array) - len(greater)))
    else:
        return pivot

array = [12, 45, 72, 3, 93, 20, 51]
i = 5
result = ith_order_statistic(array, i-1)
print(f"The {i}th order statistic is: {result}")
