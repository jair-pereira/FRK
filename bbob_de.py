import cocoex
import os, webbrowser
from solvers import pso, cs, de
import datetime

## bbob validation suite ##
suite = cocoex.Suite("bbob", "", "function_indices:1-24 dimensions:2,3,5,10,20,40 instance_indices:1-15")
observer = cocoex.Observer("bbob", "result_folder: " + "DE")

## nfe ##
nfe = 1e+6

file = open("results_de.txt", 'w')

## loop over problems ##
solver = "de_1200_0.43_0.32"
file.write(solver+","+suite.info+","+str(datetime.datetime.now())+"\n")
file.write("solver, problem_id, start_time, spent_time, spent_nfe, max_nfe"+"\n")
for problem in suite:
    problem.observe_with(observer)
    time_i = datetime.datetime.now()
    file.write(solver+","+problem.id+","+str(time_i)+",")
    S = de(1600, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, beta=0.43, pr=0.32)
    file.write(str(datetime.datetime.now() - time_i)+","+str(S.nfe)+","+str(nfe)+"\n")
    file.flush()

file.write(solver+","+suite.info+","+str(datetime.datetime.now())+"\n")
file.close()
