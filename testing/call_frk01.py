import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solvers import f0105

nfe = 1e+6
suite = cocoex.Suite("bbob", "", "function_indices:1 dimensions:5 instance_indices:2")

for reps in range(10):
    for problem in suite:
        sol = f0105(0, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe)
        print(sol.best.getFitness())
