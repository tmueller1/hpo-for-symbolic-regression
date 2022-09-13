import runpy
from skopt import gp_minimize
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
    print(fit)
    y.append(float(fit))
    return float(fit)


res = gp_minimize(objective,                  # the function to minimize 
                  [(0.001, 0.1),(0.5,1),(0.001,0.2)],      # the bounds on each dimension of x
                  acq_func="EI",      # the acquisition function
                  n_calls=27,         # the number of evaluations of f, if changed please change line 54 to the same value
                  n_random_starts=5,  # the number of random initialization points
                  random_state=1234)    #seed
print(res)
x=range(27)
plt.plot(x, y)
plt.xlabel('evaluations')
plt.ylabel('fitness')
plt.show()
