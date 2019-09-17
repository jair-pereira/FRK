import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solvers import pso

nfe = 1e+6
suite = cocoex.Suite("bbob", "", "function_indices:15 dimensions:5 instance_indices:2")
n, w, c1, c2 = 800, 0.37, 0.03, 1.12

# print(suite)
# print(nfe, n, w, c1, c2)

for reps in range(10):
    for problem in suite:
        sol = pso(n, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, w, c1, c2)
        print(sol.best.getFitness())
