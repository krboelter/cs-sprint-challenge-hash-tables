def get_indices_of_item_weights(weights, length, limit):
    w_1 = {}

    for weight in weights:
        sums = []
        for j in weights:
            if weight == j:
                continue
            else:
                print(sums)
                print(weight, j)
                w_1[weight] = sums.append(weight + j)

    return None

get_indices_of_item_weights([1, 2, 5, 6, 7], 5, 3)
