from _collections_abc import Iterable


def flattenlist(items, ignore_types=(str, bytes)):
    # check if the item is an iterable and also check if its not in the types to ignore
    for v in items:
        if isinstance(v, Iterable) and not isinstance(v, ignore_types):
            yield from flattenlist(v)
        else:
            yield v

# driver function


lst = ['A', 'B', ['C', 'D', ['E', 'F']],
        'G', 'H', ['I', ['J', ['K', 'L', 'M']]]]
print(list(flattenlist(lst)))
