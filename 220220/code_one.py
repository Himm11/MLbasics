p=[True,True,False,False]
q=[True, False,True, False]

#Negation
def negation(p):
    l=[]
    for i in range(0,4):
        l.append(not p[i])
    return l

#Conjunction
def conjunction(p,q):
    l=[]
    for i in range(0,4):
        l.append(p[i] and q[i])
    return l

#Disjunction
def disjunction(p,q):
    l = []
    for i in range(0, 4):
        l.append(p[i] or q[i])
    return l

#Implication
def implication(p,q):
    l=[]
    for i in range(0,4):
        l.append (not p[i] or q[i])
    return l

#Biconditional
def bicondition(p,q):
    l=[]
    for i in range(0,4):
        l.append((not p[i] or q[i]) and (not q[i] or p[i]))
    return l

print("p:", p)
print("q:", q)
print("Negation of p:", negation(p))
print("Negation of q:", negation(q))
print("Conjunction of p and q:", conjunction(p,q))
print("Disjunction of p and q:", disjunction(p,q))
print("Implication p->q :", implication(p,q))
print("Biconditional p<->q :", bicondition(p,q))