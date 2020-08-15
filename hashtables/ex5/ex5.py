# Your code here


def finder(files, queries):
    # Your code here
    sep_dict = {}
    for path in files:
        separated = path.split("/")
        if separated[-1] not in queries:
            continue
        else:
            if separated[-1] not in sep_dict:
                else:
                sep_dict[separated[-1]] = [path]
            else:
                sep_dict[separated[-1]].append(path)

    result = []
    for v in sep_dict.values():
        result.append(v)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
