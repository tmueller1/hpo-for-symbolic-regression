import runpy
from pprint import pprint

import matplotlib.pyplot as plt

fitnesses=[]
def objective(coe,mut,cx):
    doc = open('NOG.txt', 'w')
    #If you want a different number of generations change it here default:25
    print(25, file=doc)
    doc.close()
    doc = open('para.txt', 'w')
    print(coe, file=doc)
    doc.close()
    doc = open('cxbp.txt', 'w')
    print(mut, file=doc)
    doc.close()
    doc = open('mutpb.txt', 'w')
    print(cx, file=doc)
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
#The different Values for the Hyperparameter are defined here 
#If you change the Number of Values please also change the range of the array in the next line
#Important: If you change the number of Values you will also have to change line 66 to the total number of values you evaluate
erg = [[[0 for k in range(3)] for j in range(3)] for i in range(3)]
coeff=[0.001,0.05,0.1]
mutpb=[0.5,0.75,1]
cxpb=[0.001,0.1,0.2]
for x in range(len(coeff)):
    for y in range(len(mutpb)):
        for z in range(len(cxpb)):
            print(x,y,z)
            print(coeff[x],mutpb[y],cxpb[z])
            erg[x][y][z]=objective(coeff[x],mutpb[y],cxpb[z])
            print("STEP---------------------------------------------------------------------")
print("********************************************************************")
pprint(erg)
min=float("inf")
vec=[]
vec.append(0)
vec.append(0)
vec.append(0)
evals=range(27)
for a in range(len(coeff)):
    for b in range(len(mutpb)):
        for c in range(len(cxpb)):
            if(erg[a][b][x]<min):
                min=erg[a][b][x]
                vec[0]=coeff[a]
                vec[1]=mutpb[b]
                vec[2]=cxpb[c]
print (min)
print(vec)
plt.plot(evals, fitnesses)
plt.xlabel('evaluations')
plt.ylabel('fitness')
plt.show()
