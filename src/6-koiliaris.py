# https://arxiv.org/pdf/1507.02318.pdf

import operator
import itertools

from itertools import chain, combinations
import sys
from timeit import default_timer as timer


def approx_with_accounting_and_duplicates(x_list,
                                s,      # target value
                                ):    
    c = .01              # fraction error (constant)
    N = len(x_list)      # number of values

    S = [(0, [])]
    for x in sorted(x_list):
        T = []
        for y, y_list in S:
            T.append((x + y, y_list + [x]))
        U = T + S
        U = sort_by_col(U, 0)
        y, y_list = U[0]
        S = [(y, y_list)]

        for z, z_list in U:
            lower_bound = (float(y) + c * float(s) / float(N))
            if lower_bound < z <= s:
                y = z
                S.append((z, z_list))

    return sort_by_col(S, 0)[-1]


def sort_by_col(table, col=0):
    '''
    http://www.saltycrane.com/blog/2007/12/how-to-sort-table-by-columns-in-python/
    '''
    return sorted(table, key=operator.itemgetter(col))

data = []
with open("data/numbers/numbers-100.txt") as file:
    for line in file:
        line = line.strip()
        data.append(int(line))

target = 10000000

print "numero de elementos = |S| = ", len(data)
print "target = ", target

start = timer()
bf = approx_with_accounting_and_duplicates(data, target)
end = timer()


print "Tiempo de Ejecucion: ", (end - start)