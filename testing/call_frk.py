import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solvers import f1702

nfe = 1e+6
suite = cocoex.Suite("bbob", "", "function_indices:17 dimensions:2 instance_indices:2")

for reps in range(10):
    for problem in suite:
        sol = f1702(0, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe)
        print(sol.best.getFitness())
