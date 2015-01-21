def chain(*args):
    for it in args:
        for e in it:
            yield e


def izip(*args):
    iterators = map(iter, args)
    while iterators:
        yield tuple(map(next, iterators))


def izip_longest(*args, **kwargs):
    fill=kwargs["fill"]
    counter = [len(args)-1]

    def filler():
        if not counter[0]:
            raise StopIteration
        counter[0] -= 1
        while True:
            yield fill

    iterators = [chain(it, filler()) for it in args]

    while True:
        yield tuple([next(it) for it in iterators])


def foldr(f, acc, it):
    try:
        v = next(it)
    except StopIteration:
        return acc

    acc = foldr(f, acc, it)
    return f(acc, v)


def merge(f, *iters):
    empty = []
    values = []

    for i, it in enumerate(iters):
        try:
            values.append(next(it))
        except StopIteration:
            empty.append(i)

    iters = [it for i, it in enumerate(iters) if i not in empty]

    while iters:
        m = f(values)
        i = values.index(m)
        yield m

        try:
            values[i] = next(iters[i])
        except StopIteration:
            values.pop(i)
            iters.pop(i)
