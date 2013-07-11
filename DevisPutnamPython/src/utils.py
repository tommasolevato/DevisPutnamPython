
def removeAll(seq, item):
    # Copia la lista "seq" e rimuove da essa tutte le
    # occorrenze dell'elemento "item". Viene restituita la
    # copia.
    
    return [x for x in seq if x != item]

def copyAndAppend(l, item):
    # Copia la lista "l" e appende l'elemento "item" alla copia.
    # Viene restituita la copia.
    
    l = list(l)
    l.append(item)
    return l

def factorial(n):
    # Restituisce il fattoriale di n.
    
    if (n < 0):
        return None
    if (n == 0 or n == 1):
        return 1
    return n * factorial(n - 1)

def binomialCoefficient(n, k):
    #Restituisce il coefficiente binomiale n su k.
    
    return factorial(n) / (factorial(k) * factorial(n - k))