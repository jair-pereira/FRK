import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from frk2_1f import *

suite = cocoex.Suite("bbob", "", "function_indices:21 dimensions:10 instance_indices:1-15")
observer = cocoex.Observer("bbob", "result_folder: " + "frk21f_01")

nfe = 1e+6
repetitions = 10

# solver_list = iter([frk2_1f01]*15 + [frk2_1f06]*15 + [frk2_1f15]*15 + [frk2_1f21]*15)
# solver_list = iter([frk2_1f01]*1 + [frk2_1f06]*1 + [frk2_1f15]*1 + [frk2_1f21]*1)
solver_list = iter([frk2_1f21]*15)


for problem in suite:
    problem.observe_with(observer)
    solver = next(solver_list)

    print(problem)
    print(solver)
    for i in range(repetitions):
        if not problem.final_target_hit:
            print(i, end=" ")
            S = solver(problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe)

            fw = open("frk2_1f21_"+str(problem.id)+"_r"+str(i)+".pkl", "wb")
            pickle.dump(S, fw)
            fw.close()

    print()

### post-process data
cocopp.main(observer.result_folder)  # re-run folders look like "...-001" etc
#webbrowser.open("file://" + os.getcwd() + "/ppdata/index.html")
