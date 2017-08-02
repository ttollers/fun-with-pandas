from functools import reduce


def cumProd(array):
    def reduceFn(acc, item):
        l = len(acc)
        if (l == 0):
            return [item]
        else:
            acc.append(item * acc[-1])
            return acc
    return reduce(reduceFn, array, [])


def cumMax(array):

    def reduceFn(acc, item):

    return reduce()



