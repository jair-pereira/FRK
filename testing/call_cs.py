import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solvers import cs

nfe = 1e+6
suite = cocoex.Suite("bbob", "", "function_indices:1 dimensions:5 instance_indices:2")
n, k, pr = 50, 25, 0.91

# print(suite)
# print(nfe, n, w, c1, c2)

for reps in range(10):
    for problem in suite:
        sol = cs(n, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, pr, k)
        print(sol.best.getFitness())
