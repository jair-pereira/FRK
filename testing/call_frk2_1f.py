import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from frk2_1f import *

suite = cocoex.Suite("bbob", "", "function_indices:01,06,15,21 dimensions:10 instance_indices:1-15")
observer = cocoex.Observer("bbob", "result_folder: " + "FRK21f_all")

nfe = 1e+6
repetitions = 10

# p01 = {"n": 400, "w": 0.52, "c1": 0.01, "c2": 0.69}
# p06 = {"n":  50, "w": 0.02, "c1": 0.05, "c2": 1.88}
# p15 = {"n": 800, "w": 0.19, "c1": 0.00, "c2": 1.51}
# p21 = {"n": 800, "w": 0.50, "c1": 0.54, "c2": 1.53}
# params = iter([p01, p06, p15, p21])

solver_list = iter([frk2_1f01]*15 + [frk2_1f06]*15 + [frk2_1f15]*15 + [frk2_1f21]*15)
# solver_list = iter([frk2_1f01]*1 + [frk2_1f06]*1 + [frk2_1f15]*1 + [frk2_1f21]*1)


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
