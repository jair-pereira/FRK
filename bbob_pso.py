import cocoex
import os, webbrowser
from solvers import pso, cs
import datetime

## bbob validation suite ##
suite = cocoex.Suite("bbob", "", "function_indices:1-24 dimensions:2,3,5,10,20,40 instance_indices:1-15")
observer = cocoex.Observer("bbob", "result_folder: " + "PSO")

## nfe ##
nfe = 1e+6

## loop over problems ##
print(solver, suite, datetime.datetime.now())
print("solver, problem_id, start_time, spent_time, spent_nfe, max_nfe")
solver = "pso_400_0.50_0.50_1.50"
for problem in suite:
    problem.observe_with(observer)
    print(solver, problem.id, time_i, sep=", ", end=", ")
    time_i = datetime.datetime.now()
    S = pso(400, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension,
            nfe, w=0.50, c1=0.50, c2=1.50)
    print(datetime.datetime.now() - time_i, S.nfe, nfe, sep=", ")
    #S = cs(50, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, pr=25, k=0.45)
    #S = de(1600, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, beta=0.43, pr=0.32)
print(solver, suite, datetime.datetime.now())
