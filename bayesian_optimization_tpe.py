import hyperopt
from hyperopt import hp, STATUS_OK
import runpy
import matplotlib.pyplot as plt

y=[]
def objective(args):
    print(args)
    doc = open('num_in_gen.txt', 'w')
    print(100, file=doc)
    doc.close()
    doc = open('NOG.txt', 'w')
    # If you want a different number of generations change it here default:25 
    print(50, file=doc)
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

space=[hp.uniform("coeff", 0.00000001, 0.000005), hp.uniform("cxpb",0.5,1),hp.uniform("mutpb",0.2,0.5)]

# minimize the objective over the space
from hyperopt import fmin,tpe
#If you change max_evals you also need to change line 54 to the same value
best = fmin(objective, space, algo=tpe.suggest, max_evals=54)
print (best)
x=range(54)
plt.plot(x, y)
plt.xlabel('evaluations')
plt.ylabel('fitness')
plt.show()
