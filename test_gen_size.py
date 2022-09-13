import runpy
from pprint import pprint
 
import matplotlib.pyplot as plt

fitnesses=[]
def objective(gen):
    doc = open('NOG.txt', 'w')
    print(gen, file=doc)
    doc.close()
    doc = open('para.txt', 'w')
    print(0.0005, file=doc)
    doc.close()
    doc = open('cxbp.txt', 'w')
    print(0.2, file=doc)
    doc.close()
    doc = open('mutpb.txt', 'w')
    print(0.5, file=doc)
    doc.close()
    runpy.run_path(path_name='hh.py')
    doc = open('tmp.txt', 'r')
    ss = doc.read()
    doc.close()
    lenss = len(ss)
    step = 0
    formu = ""
    fit = ""
    fit2 = ""
    while (ss[step] != '\n'):
        formu = formu + ss[step]
        step = step + 1
    while (step <= lenss - 1 and (ss[step] > '9' or ss[step] < '0')):
        step = step + 1
    while (step <= lenss - 1 and (ss[step] != '\n')):
        fit = fit + ss[step]
        step = step + 1
    while (step <= len(ss) - 1 and (ss[step] > '9' or ss[step] < '0')):
        step = step + 1
    while (step <= len(ss) - 1 and (ss[step] != '\n')):
        fit2 = fit2 + ss[step]
        step = step + 1
    fitnesses.append(float(fit))
    return float(fit)

gens=[25,50,75,100,150]
for x in range(len(gens)):
    objective(gens[x])
print("********************************************************************")
plt.plot(gens,fitnesses)
plt.xlabel('SIze of Population')
plt.ylabel('fitness')
plt.show()
