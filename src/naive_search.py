def naive_search(T, P):
    occurrences = []
    n = len(T)
    m = len(P)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if T[i + j] != P[j]:
                match = False
                break
        if match:
            occurrences.append(i)

    return occurrences
    

def naive_search_shifts(T, P):
    n = len(T)
    m = len(P)
    num_shifts = 0

    for i in range(n - m + 1):
        match = True
        num_shifts += 1
        for j in range(m):
            if T[i + j] != P[j]:
                match = False
                break
        if match:
            pass

    return num_shifts