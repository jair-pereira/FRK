import cocoex
import os, webbrowser
from solvers import pso, cs, de
import datetime

## bbob validation suite ##
suite = cocoex.Suite("bbob", "", "function_indices:1-24 dimensions:2,3,5,10,20,40 instance_indices:1-15")
observer = cocoex.Observer("bbob", "result_folder: " + "DE")

## nfe ##
nfe = 1e+6

## loop over problems ##
solver = "de_1200_0.43_0.32"
print(solver, suite, datetime.datetime.now())
print("solver, problem_id, start_time, spent_time, spent_nfe, max_nfe")
for problem in suite:
    problem.observe_with(observer)
    time_i = datetime.datetime.now()
    print(solver, problem.id, time_i, sep=", ", end=", ")
    S = de(1600, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, beta=0.43, pr=0.32)
    print(datetime.datetime.now() - time_i, S.nfe, nfe, sep=", ")
print(solver, suite, datetime.datetime.now())
