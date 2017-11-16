# -*- coding: utf-8 -*-

# Limites computables
from itertools import chain, combinations
import sys
from timeit import default_timer as timer

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(
        combinations(s, r) for r in range(len(s)+1))

start = timer()

data = []
with open("data/numbers/numbers-5.txt") as file:
	for line in file:
		line = line.strip()
		data.append(int(line))

# print data

target = 1000000 # Algún valor muy alto que no este en el subset

print "=> Busqueda de limite de computacion para S"
print "numero de elementos = |S| = ", len(data)

number_elements = 2 ** len(data) # 2**n
print "number_elements = 2**n = ", number_elements

power_set = powerset(data)
# print "P(S) = ", list(powerset(data))

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

