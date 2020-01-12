import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solvers import cs

suite = cocoex.Suite("bbob", "", "function_indices:01,06,15,21 dimensions:10 instance_indices:2")
observer = cocoex.Observer("bbob", "result_folder: " + "CS_ts")

nfe = 1e+6
repetitions = 10

p01 = {"n": 50, "pr": 0.57, "k": 25}
p06 = {"n": 50, "pr": 0.97, "k": 25}
p15 = {"n": 50, "pr": 0.89, "k": 25}
p21 = {"n": 50, "pr": 0.78, "k": 25}
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
            S = cs(p["n"], problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, pr=p["pr"], k=p["k"])

### post-process data
cocopp.main(observer.result_folder)  # re-run folders look like "...-001" etc
