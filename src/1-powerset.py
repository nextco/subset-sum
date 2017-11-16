# -*- coding: utf-8 -*-

# Enfoque simple propio, el más sencillo de entender
from itertools import chain, combinations
import sys
from timeit import default_timer as timer

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(
        combinations(s, r) for r in range(len(s)+1))

start = timer()

data = [5,8,3]
# data ="ab"
# data = "xyz"
# data = [5, 8, 15, 22, 34, 65, 1, 5]
target = 11 # 22 + 34 + 5
# target = 200

print "S = ", data

number_elements = 2 ** len(data) # 2**n
print "number_elements = 2**n = ", number_elements

power_set = powerset(data)
print "P(S) = ", list(powerset(data))

print "target = ", target

for sub_set in power_set:
	# print sub_set
	suma = 0
	for element in sub_set:
		# print element
		suma = suma + element
		if( suma == target ):
			print "Encontrado = ", sub_set
			end = timer()
			print "Tiempo de Ejecucion: ", (end - start)
			sys.exit()


print "Ninguna combinacion es posible para P(s)"
end = timer()
print "Tiempo de Ejecucion: ", (end - start)

