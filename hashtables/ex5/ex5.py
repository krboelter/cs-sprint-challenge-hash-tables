
def finder(files, queries):
    sep_dict = {}
    for path in files:
        separated = path.split("/")

        if separated[-1] not in path:
            continue
        elif separated[-1] not in sep_dict:
            sep_dict[separated[-1]] = [path]
        else:
            sep_dict[separated[-1]].append(path)


    result = []
    for query in queries:
        if query in sep_dict:
            if len(sep_dict[query]) > 1:
                result += sep_dict[query]
            elif len(sep_dict[query]) < 1:
                continue
            else:
                result += sep_dict[query]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin',
        '/bin/bar',
        '/usr/bin/baz',
        '/usr/bin/local/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz",
        "nosuchfile.txt",
        "hello_world"
    ]
    print(finder(files, queries))
