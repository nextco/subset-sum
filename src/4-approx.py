# -*- coding: utf-8 -*-
# Algoritmo de aproximación para SUBSET-SUM.

import itertools
import operator

from timeit import default_timer as timer

def trim(data, delta):
   # Recorta elementos dentro de `delta`
   # de otros elementos en la lista

    output = []
    last = 0

    for element in data:
        if element['value'] > last * (1 + delta):
            output.append(element)
            last = element['value']

    return output


def merge_lists(m, n):
    """
    Mezcla dos listas y devuelva la lista ordenada
    
    No eliminamos los elementos duplicados, 
    We do *not* remove duplicates, ya que queremos ver todas las
    posibles combinaciones para un subconjunto aproximado en vez de
    simplemente confirmar si existe dicho subconjunto

    """
    merged = itertools.chain(m, n)
    return sorted(merged, key=operator.itemgetter('value'))


def approximate_subset_sum(data, target, epsilon):
    """
    Calcula la suma total del conjunto aproximado de  además de los elementos
    que se utilizaron para construir la suma del subconjunto.

    Modificado para rastrear los elementos que componen las sumas parciales
    e identificar qué elementos del subconjunto se eligieron para la solución.
    """

    acc = [{'value': 0, 'partials': [0]}]
    count = len(data)

    # Prepatar datos convirtiendolos en una lista de Hashes
    data = [{'value': d, 'partials': [d]} for d in data]

    for key, element in enumerate(data, start=1):
        augmented_list = [{
            'value': element['value'] + a['value'],
            'partials': a['partials'] + [element['value']]
        } for a in acc]
        acc = merge_lists(acc, augmented_list)
        acc = trim(acc, delta=float(epsilon) / (2 * count))
        acc = [val for val in acc if val['value'] <= target]

    return acc[-1]


if __name__ == "__main__":
    
    start = timer()

    print "=> Algoritmo aproximacion para S"
    
    data = []
    with open("data/numbers/numbers-28.txt") as file:
        for line in file:
            line = line.strip()
            data.append(int(line))

    target = 100000000 # Un valor muy alto
    epsilon = 0.2

    print "numero de elementos = |S| = ", len(data)
    print "target = ", target
    print "epsilon = ", epsilon

    # print "input: {data}; target: {target}; epsilon: {epsilon}".format(data=data, target=target, epsilon=epsilon)

    # print "Encontrado Aproximacion = ", approximate_subset_sum(data, target, epsilon=epsilon)
    print "Encontrado Aproximacion = ", approximate_subset_sum(data, target, epsilon=epsilon)['value']
  
    end = timer()
    print "Tiempo de Ejecucion: ", (end - start)
