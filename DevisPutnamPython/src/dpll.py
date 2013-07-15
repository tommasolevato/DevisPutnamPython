from utils import copyAndAppend, removeAll
import randomGen

def getLiterals(clauses):
    # Restituisce l'insieme dei letterali presenti nelle
    # clausole.
    
    l = []
    for c in clauses:
        for i in range(0, len(c)):
            if (c[i] not in l):
                l.append(c[i])
    return l

def checkClauseTruth(model, c):
    # Controlla la verita' della clausola secondo il modello.
    # Essendo le clausole in forma CNF, appena si trova un
    # letterale vero nel modello si restituisce True.
    # Se tutti i letterali sono falsi nel modello si restituisce
    # False. Nel caso in cui nessuna delle due condizione sia
    # verificata, si restituisce il valore nullo.
    
    unknown = False
    for i in range(0, len(c)):
        val = checkLitTruth(model, c[i])
        if (val == True):
            return True
        if (val == None):
            unknown = True
    if (unknown == True):
        return None
    return False
            
def checkLitTruth(model, lit):
    # Dato il modello, controlla la verita' del letterale secondo
    # il modello. Se il modello non ha fissato il letterale,
    # si restituisce il valore nullo.
    
    s = litToSymbol(lit)
    val = searchModel(model, s)
    if (lit[0] == '~'):
        if (val == None):
            return None
        return not val
    return val

def searchModel(model, symbol):
    # Restituisce la verita' del simbolo secondo il modello.
    # Se il modello non ha ancora fissato il simbolo, si
    # restituisce il valore nullo.
    
    if (model == None):
        return None
    for i in range(0, len(model)):
        if (model[i][0] == symbol):
            return model[i][1]
    return None

def findPureSymbol(symbols, clauses):
    # Date le clausole, restituisce il primo simbolo puro trovato,
    # insieme al valore dei letterali con cui si presenta
    # nelle clausole. Se non si trova niente si restituisce
    # il valore nullo per entrambi.
    
    lit = getLiterals(clauses)
    for s in symbols:
        foundPos, foundNeg = False, False
        if (('~' + s) in lit):
            foundNeg = True
        if (s in lit):
            foundPos = True
        if (foundPos != foundNeg):
            return s, foundPos
    return None, None
            
def findUnitClause(clauses, model):
    # Dato il modello, restituisce la prima Unit Clause trovata
    # e il simbolo associato, con il valore da attribuirgli per
    # renderla vera. Se non si trova nulla, si restituisce il
    # valore nullo per entrambi.
    
    for c in clauses:
        P, val = isUnitClause(model, c)
        if(P and val):
            return P, val
    return None, None

def isUnitClause(model, c):
    # Dato il modello, controlla se la clausola e' una Unit
    # Clause. In caso affermativo, restituisce il simbolo
    # e il valore da attribuirgli per redere la clausola vera,
    # altrimenti restituisce il valore nullo per entrambi.
    
    unknown = 0
    lit = None
    for i in range(0, len(c)):
        if (checkLitTruth(model, c[i])) == None:
            unknown += 1
            lit = c[i]
    if unknown == 1:
        return litToSymbol(lit), litTruth(lit)
    return None, None

def litTruth(lit):
    # Restituisce la "verita'" di un letterale, ad esempio:
    # litTruth('P') restituisce True
    # litTruth('~P') restituisce False
    
    if (lit[0] == '~'):
        return False
    return True

def litToSymbol(lit):
    # Restituisce il simbolo associato al letterale.
    
    if (lit[0] == '~'):
        l = lit.replace("~",'')
        return l
    return lit


def dpll(clauses, symbols, model):
    # Implementa l'algoritmo di Davis-Putnam.
    
    randomGen.count += 1
    unknownClauses = []
    for c in clauses:
        val = checkClauseTruth(model, c)
        if (val == False):
            return False
        if (val == None):
            unknownClauses.append(c)
    if (not unknownClauses):
        return True
    P, value = findPureSymbol(symbols, unknownClauses)
    if (P):
        return dpll(clauses, removeAll(symbols,P), copyAndAppend(model,[P,value]))
    P, value = findUnitClause(unknownClauses, model)
    if (P):
        return dpll(clauses, removeAll(symbols,P), copyAndAppend(model,[P,value]))
    P = symbols[0]
    symbols = removeAll(symbols, P)
    return (dpll(clauses, symbols, copyAndAppend(model, [P,True])) or 
            dpll(clauses, symbols, copyAndAppend(model, [P,False])))
