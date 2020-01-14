import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solvers import de

suite = cocoex.Suite("bbob", "", "function_indices:01,06,15,21 dimensions:10 instance_indices:2")
observer = cocoex.Observer("bbob", "result_folder: " + "DE_ts")

nfe = 1e+6
repetitions = 10

p01 = {"n": 50, "beta": 0.08, "pr": 0.18}
p06 = {"n": 50, "beta": 0.47, "pr": 0.92}
p15 = {"n": 50, "beta": 0.17, "pr": 0.85}
p21 = {"n": 50, "beta": 0.50, "pr": 0.93}
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
            S = de(p["n"], problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, beta=p["beta"], pr=p["pr"])

### post-process data
cocopp.main(observer.result_folder)  # re-run folders look like "...-001" etc
webbrowser.open("file://" + os.getcwd() + "/ppdata/index.html")
