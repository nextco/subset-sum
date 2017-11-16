# -*- coding: utf-8 -*-
# Algoritmo de aproximación para SUBSET-SUM.

import itertools
import operator


def trim(data, delta):
   # Recorta elementos dentro de `delta`
   # de otros elementos en la lista
    output = []
    last = 0

    for element in data:
        if element['approx'] > last * (1 + delta):
            output.append(element)
            last = element['approx']
    print "L'", output
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
    return sorted(merged, key=operator.itemgetter('approx'))


def approximate_subset_sum(data, target, epsilon):
    """
    Calcula la suma total del conjunto aproximado de  además de los elementos
    que se utilizaron para construir la suma del subconjunto.

    Modificado para rastrear los elementos que componen las sumas parciales
    e identificar qué elementos del subconjunto se eligieron para la solución.
    """

    acc = [{'approx': 0, 'l_prima': [0]}]
    count = len(data)

    # Prepatar datos convirtiendolos en una lista de hashes
    data = [{'approx': d, 'l_prima': [d]} for d in data]

    for key, element in enumerate(data, start=1):
        augmented_list = [{
            'approx': element['approx'] + a['approx'],
            'l_prima': a['l_prima'] + [element['approx']]
        } for a in acc]
        acc = merge_lists(acc, augmented_list)
        acc = trim(acc, delta=float(epsilon) / (2 * count))
        acc = [val for val in acc if val['approx'] <= target]

    return acc[-1]


if __name__ == "__main__":

    data = [104, 102, 201, 101]
    target = 308

    epsilon = 0.4

    print "S: {data}; target: {target}; epsilon: {epsilon}".format(
        data=data, target=target, epsilon=epsilon)

    print approximate_subset_sum(data, target, epsilon=epsilon)
