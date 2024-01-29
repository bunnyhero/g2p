def chain_with_separator(iterables, sep):
    if len(iterables) == 0:
        return
    iterables = iter(iterables)
    yield from next(iterables)
    for x in iterables:
        yield sep
        yield from x
