def get_pivot(a, l, u):
    m = l + (u-l) / 2
    if a[l] >= a[m] and a[l] >= a[u]:
        if [m] >= a[u]:
            a[m], a[l] = a[l], a[m]
        else:
            a[u], a[l] = a[l], a[u]
    elif a[m] >= a[l] and a[m] >= a[u]:
        if a[u] >= a[l]:
            a[u], a[l] = a[l], a[u]
    elif a[m] >= a[l]:
        a[m], a[l] = a[l], a[m]


def partition_arr(a, l, u):
    i = l+1
    p = a[l]
    for j in range(l+1, u+1):  # (j=l+1; j<=u; j++):
        if a[j] < p:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[i-1], a[l] = a[l], a[i-1]
    return i-1


def quick_sort(a, l, u):
    """
    non-random quicksort algorithm
    """
    if u <= l:
        return 0
    comp = u-l
    # a[l], a[u] = a[u], a[l]
    # get_pivot(a, l, u)
    j = partition_arr(a, l, u)
    comp += quick_sort(a, l, j-1)
    comp += quick_sort(a, j+1, u)
    return comp


if __name__ == "__main__":
    user_input = []
    for line in open('QuickSort.txt', 'r'):
        user_input.append(int(line))
    print(quick_sort(user_input, 0, len(user_input)-1))
