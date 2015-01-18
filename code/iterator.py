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
