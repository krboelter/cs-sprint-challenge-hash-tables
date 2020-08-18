def inverse(x):
    # if negative number, return positive
    if x < 0:
        return abs(x)
    # if positive number, return negative
    else:
        return 0 - x


def has_negatives(a):
    hash = {}
    result = []

    for x in a:
        # if x is positive, make it a key with False as value
        if inverse(x) not in hash:
            hash[x] = False
        else:
            hash[inverse(x)] = True

    for k, v in hash.items():
        if v is True:
            result.append(abs(k))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
