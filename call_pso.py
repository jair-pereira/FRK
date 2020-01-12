import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solvers import pso

suite = cocoex.Suite("bbob", "", "function_indices:01,06,15,21 dimensions:10 instance_indices:2")
observer = cocoex.Observer("bbob", "result_folder: " + "PSO_ts")

nfe = 1e+6
repetitions = 10

p01 = {"n": 100, "w": 0.39, "c1": 0.00, "c2": 1.84}
p06 = {"n": 200, "w": 0.56, "c1": 0.00, "c2": 1.67}
p15 = {"n": 800, "w": 0.12, "c1": 0.01, "c2": 1.82}
p21 = {"n": 400, "w": 0.49, "c1": 0.12, "c2": 1.79}
# params = iter([p01]*15 + [p06]*15 + [p15]*15 + [p21]*15)
params = iter([p01]*1 + [p06]*1 + [p15]*1 + [p21]*1)

for problem in suite:
    problem.observe_with(observer)
    p = next(params)
    
    print(problem)
    print(p)
    for i in range(repetitions):
        if not problem.final_target_hit:
            print(i, end=", ")
            S = pso(p["n"], problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, w=p["w"], c1=p["c1"], c2=p["c2"])

    print()
### post-process data
cocopp.main(observer.result_folder)  # re-run folders look like "...-001" etc
