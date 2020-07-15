

CONFIG = {
    'ginger': {
        'django': 2,
        'flask': 3,
    },
    'cucumber': {
        'flask': 1,
    },
}


def preprocess_input_config(config):
    lst = []
    for key, value in config.items():
        lst.append([key, sum(value.values())])
    lst.sort(key=lambda x: x[1])
    return lst


def distribute_uniformly(lst, k):
    min = lst[0][1]
    i = 0
    remainder = 0
    while i < len(lst) - 1:
        diff = lst[i + 1][1] - lst[i][1]
        sum_first_i = diff * (i+1)
        if k > sum_first_i:
            min += diff
            k -= sum_first_i
            i += 1
        else:
            div = k // (i+1)  # if this value is less than 1, just add 1 to k first elements
            if div >= 1:
                min += div
                remainder = k % (i+1)
            else:
                remainder = div
            break
    if i == len(lst)-1:
        div = k // (len(lst))
        if div >= 1:
            remainder = k % len(lst)
            for j in range(len(lst)):
                lst[j][1] = min - lst[j][1] + div
            for j in range(remainder):
                lst[j][1] += 1
        else:
            for j in range(k):
                lst[j][1] += 1
    if i != len(lst)-1:
        for j in range(remainder):
            lst[j][1] = min - lst[j][1] + 1
        for j in range(remainder, (i+1)):
            lst[j][1] = min - lst[j][1]
        for j in range((i+1), len(lst)):
            lst[j][1] = 0
    return lst


def update(data, service, count):
    lst = distribute_uniformly(preprocess_input_config(data), count)
    for i, item in enumerate(lst):
        if item[1] >= 1:
            data[item[0]].update({service: item[1]})


update(CONFIG, 'pylons', 7)
print(CONFIG)
