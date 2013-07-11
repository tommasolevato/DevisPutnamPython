import randomGen
import dpll

#TODO: test

def satProbability(n,m,k,num):
    return randomGen.satProbability(n, m, k, num)

def randomSentenceNum(n,m,k):
    symbols = randomGen.generateSymbols(n)
    return randomGen.randomSentence(symbols, m, k)

def randomSentenceSym(symbols,m,k):
    return randomGen.randomSentence(symbols, m, k)

def generateSymbols(n):
    return randomGen.generateSymbols(n)

def dpllSat(clauses, symbols):
    return dpll.dpll(clauses, symbols, [])
