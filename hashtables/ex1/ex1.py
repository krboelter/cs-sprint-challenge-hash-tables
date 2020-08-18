def get_indices_of_item_weights(weights, length, limit):
    wait = {}
    indecies = []

    for index in range(len(weights)):
        if weights[index] not in wait:
            wait[weights[index]] = index
        else:
            wait[weights[index] + .1] = index

    print(4.1 % 4.1)
    answers = []
    for k, v in wait.items():
        key = round(k, 0)
        if (limit - key) in wait:
            indecies.insert(0, v)

    if len(indecies) < 1:
        return None
    else:
        return indecies
