import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solvers import cs

suite = cocoex.Suite("bbob", "", "function_indices:01,06,15,21 dimensions:10 instance_indices:2")
observer = cocoex.Observer("bbob", "result_folder: " + "CS_ts")

nfe = 1e+6

p01 = {"n": 100, "pr": 0.88, "k": 25}
p06 = {"n":  50, "pr": 0.79, "k": 25}
p15 = {"n":  50, "pr": 0.50, "k": 25}
p21 = {"n":  50, "pr": 0.66, "k": 25}
params = iter([p01, p06, p15, p21])

for problem in suite:
    problem.observe_with(observer)
    p = next(params)
    S = cs(p["n"], problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, pr=p["pr"], k=p["k"])

### post-process data
cocopp.main(observer.result_folder)  # re-run folders look like "...-001" etc
webbrowser.open("file://" + os.getcwd() + "/ppdata/index.html")
