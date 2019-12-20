import cocoex
import os, webbrowser
from solvers import pso, cs
from metaheuristic import *
import datetime
import numpy as np

## bbob validation suite ##
suite = cocoex.Suite("bbob", "", "function_indices:1 dimensions:10 instance_indices:1")
#observer = cocoex.Observer("bbob", "result_folder: " + "PSO")

## nfe ##
nfe  = 1e+5
nrep = range(275)
minf  = np.inf
file = open("results_pso.txt", 'w')

## loop over problems ##
solver = "pso_rnd"
file.write(solver+","+suite.info+","+str(datetime.datetime.now())+"\n")
file.write("solver, problem_id, start_time, spent_time, spent_nfe, max_nfe, fitness"+"\n")
for problem in suite:
    #problem.observe_with(observer)
    for r in nrep:
        time_i = datetime.datetime.now()
        file.write(solver+","+problem.id+","+str(time_i)+",")
        S = pso(op.generate_int(min=20, max=2000),
                problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension,
                nfe,
                w=op.generate_float(min=0, max=3, step=0.01),
                c1=op.generate_float(min=0, max=3, step=0.01),
                c2=op.generate_float(min=0, max=3, step=0.01))
        file.write(str(datetime.datetime.now() - time_i)+","+str(S.nfe)+","+str(nfe)+","+str(S.best.getFitness())+"\n")
        #S = cs(50, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, pr=25, k=0.45)
        #S = de(1600, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, beta=0.43, pr=0.32)
        file.flush()

        if minf > S.best.getFitness():
            minf = S.best.getFitness()
file.write(solver+","+str(minf)+","+suite.info+","+str(datetime.datetime.now())+"\n")
file.close()
