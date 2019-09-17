import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solvers import de

nfe = 1e+6
suite = cocoex.Suite("bbob", "", "function_indices:1 dimensions:5 instance_indices:2")
n, beta, pr = 1600, 1.52, 0.89

# print(suite)
# print(nfe, n, w, c1, c2)

for reps in range(10):
    for problem in suite:
        sol = de(n, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, beta, pr)
        print(sol.best.getFitness())
