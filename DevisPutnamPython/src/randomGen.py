import random
import dpll
import time
from utils import binomialCoefficient

count = 0

def satProbabilityRate(n, m, k, num):
    # Uguale a SatProbability, solo che invece che rendere
    # il numero di esempi positivi e negativi, restituisce
    # la probabilita' di successo.
    results, recCalls, ratio = satProbability(n, m, k, num)
    rate = float(results[0] / float(num))
    return rate, recCalls, ratio

def satProbability(n, m, k, num):
    # Genera la lista dei simboli e successivamente esegue
    # num volte l'implementazione dell'algoritmo di
    # Davis-Putnam, la funzione dpll. La lista results tiene
    # traccia degli esempi positivi e negativi.
    # La funzione restituisce i risultati sotto forma di lista
    # e il numero medio di chiamate ricorsive alla funzione
    # "dpll". Viene inoltre stampato a video il tempo
    # impiegato.
    
    global count
    count = 0
    start = time.time()
    symbols = generateSymbols(n)
    results = [0,0]
    for _ in range(0,num):
        clauses = randomSentence(symbols, m, k)
        if (clauses == None):
            return
        val = dpll.dpll(clauses, symbols, [])
        if (val == True):
            results[0] += 1
        if (val == False):
            results[1] += 1
    end = time.time()
    print end - start
    return results, count / num, float(m / float(n))

def randomSentence(symbols, m, k):
    # Genera una proposizione CNF formata da m clausole con
    # k letterali per clausola. I letterali vengono estratti
    # con probabilita' uniforme dai 2n letterali disponibili,
    # essendo n il numero dei simboli. La proposizione
    # generata e' composta da clausole distinte non banali 
    # costituite da esattamente k letterali (non si accettano
    # clausole con letterali duplicati).
    
    
    if (k > len(symbols)):
        print 'Errore: k > n!'
        return None
    if (m > ((2 ** k) * binomialCoefficient(len(symbols), k))):
        print 'Errore: troppe clausole!'
    clauses = []
    while (len(clauses)):
        clause = generateClause(symbols,k)
        clause.sort()
        if (clause not in clauses):
            clauses.append(clause)
    return clauses

def generateSymbols(n):
    # Genera e restituisce una lista di n simboli 
    # proposizionali in ordine alfabetico.
    
    a = []
    if (n <= 0):
        return
    if (n <= 26):
        for i in range(0,n):
            a.append(chr(i+65))
    else:
        j = n/26
        for i in range(0,26):
            a.append(chr(i+65))
        for i in range(0,j-1):
            for k in range(0,26):
                a.append(a[i]+chr(k+65))
        for i in range(0,n%26):
            a.append(a[j-1]+chr(i+65))
    return a

def generateClause(symbols,k):
    # Genera e restituisce una clausola non banale composta 
    # da k letterali distinti. Si sceglie con probabilita'
    # uniforme un simbolo dalla lista dei simboli, e poi
    # si applica la funzione generateLiteral, che con probabilita'
    # uniforme se creare un letterale positivo o negativo.
    
    clause = []
    choices = []
    while len(choices) < k:
        symbol = random.choice(symbols)
        if (symbol not in choices):
            choices.append(symbol)
            lit = generateLiteral(symbol)
            clause.append(lit)
    return clause


def generateLiteral(symbol):
    # Dato un simbolo, con probabilita' uniforme restituisce
    # il letterale associato positivo o negativo.
    
    values = [True, False]
    truth = random.choice(values)
    if (truth == False):
        symbol = '~' + symbol
    return symbol
