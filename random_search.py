import hyperopt
from hyperopt import hp, STATUS_OK
import runpy
import matplotlib.pyplot as plt

y=[]
def objective(args):
    print(args)
    doc = open('NOG.txt', 'w')
    # If you want a different number of generations change it here default:25 
    print(25, file=doc)
    doc.close()
    doc = open('para.txt', 'w')
    print(args[0], file=doc)
    doc.close()
    doc = open('cxbp.txt', 'w')
    print(args[1], file=doc)
    doc.close()
    doc = open('mutpb.txt', 'w')
    print(args[2], file=doc)
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
    y.append(float(fit))
    return {'loss': fit, 'status': STATUS_OK }
#This changes the interval for the different Hyperparameters
space=[hp.uniform("coeff", 0, 0.1), hp.uniform("cxpb",0.5,1),hp.uniform("mutpb",0.001,0.2)]

# minimize the objective over the space
from hyperopt import fmin,tpe
#If you change max_evals you also need to change line 54 to the same value
best = fmin(objective, space, algo=tpe.rand.suggest, max_evals=27)
print (best)
x=range(27)
plt.plot(x, y)
plt.xlabel('evaluations')
plt.ylabel('fitness')
plt.show()
