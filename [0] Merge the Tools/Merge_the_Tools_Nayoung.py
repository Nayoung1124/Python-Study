def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def remove_duplicates(list_):
    my_set = set()
    res = []
    for e in list_:
        if e not in my_set:
            res.append(e)
            my_set.add(e)
    return res


def merge_the_tools(string, k):
    string = list(string)
    n = len(string)
    # m = int(n/k)
    a = []

    for i in chunker(string, k):
        a.append(remove_duplicates(i))

    for i in a:
        print(''.join(map(str, i)))


if __name__ == '__main__':