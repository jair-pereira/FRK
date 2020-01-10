import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from frk1_1f import *

suite = cocoex.Suite("bbob", "", "function_indices:01,06,15,21 dimensions:10 instance_indices:1-15")
observer = cocoex.Observer("bbob", "result_folder: " + "FRK11f_all")

nfe = 1e+6

# p01 = {"n": 400, "w": 0.52, "c1": 0.01, "c2": 0.69}
# p06 = {"n":  50, "w": 0.02, "c1": 0.05, "c2": 1.88}
# p15 = {"n": 800, "w": 0.19, "c1": 0.00, "c2": 1.51}
# p21 = {"n": 800, "w": 0.50, "c1": 0.54, "c2": 1.53}
# params = iter([p01, p06, p15, p21])

solvers = iter([frk1_1f01, frk1_1f06, frk1_1f15, frk1_1f21])


for problem in suite:
    problem.observe_with(observer)
    p = next(params)
    S = pso(p["n"], problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension,
            nfe, w=p["w"], c1=p["c1"], c2=p["c2"])

### post-process data
cocopp.main(observer.result_folder)  # re-run folders look like "...-001" etc
webbrowser.open("file://" + os.getcwd() + "/ppdata/index.html")
