import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from frk3_bf import *

suite = cocoex.Suite("bbob", "", "function_indices:01,06,15,21 dimensions:10 instance_indices:1-15")
observer = cocoex.Observer("bbob", "result_folder: " + "FRK3bf_all")

nfe = 1e+6
repetitions = 10

solver_list = iter([frk3_bf01]*15 + [frk3_bf06]*15 + [frk3_bf15]*15 + [frk3_bf21]*15)
# solver_list = iter([frk3_bf01]*1 + [frk3_bf06]*1 + [frk3_bf15]*1 + [frk3_bf21]*1)


for problem in suite:
    problem.observe_with(observer)
    solver = next(solver_list)

    print(problem)
    print(solver)
    for i in range(repetitions):
        if not problem.final_target_hit:
            print(i, end=" ")
            S = solver(problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe)

    print()

### post-process data
cocopp.main(observer.result_folder)  # re-run folders look like "...-001" etc
#webbrowser.open("file://" + os.getcwd() + "/ppdata/index.html")
