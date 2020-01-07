import numpy as np
import cocoex, cocopp
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solvers import de

suite = cocoex.Suite("bbob", "", "function_indices:01,06,15,21 dimensions:10 instance_indices:2")
observer = cocoex.Observer("bbob", "result_folder: " + "DE_ts")

nfe = 1e+6

p01 = {"n":  50, "beta": 0.14, "pr": 0.16}
p06 = {"n":  50, "beta": 0.63, "pr": 0.97}
p15 = {"n": 100, "beta": 0.11, "pr": 0.91}
p21 = {"n":  50, "beta": 1.38, "pr": 0.06}
params = iter([p01, p06, p15, p21])

for problem in suite:
    problem.observe_with(observer)
    p = next(params)
    S = de(p["n"], problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, beta=p["beta"], pr=p["pr"])

### post-process data
cocopp.main(observer.result_folder)  # re-run folders look like "...-001" etc
webbrowser.open("file://" + os.getcwd() + "/ppdata/index.html")
