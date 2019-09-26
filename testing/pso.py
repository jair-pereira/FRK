from __future__ import division, print_function
import numpy as np
import cocoex, cocopp
import os, webbrowser, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solvers import pso

nfe = 1e+6
n, w, c1, c2 = 50, 0.51, 0, 1.42

output_folder = "pso1702"
suite = cocoex.Suite("bbob", "", "function_indices:17 dimensions:2 instance_indices:2")
observer = cocoex.Observer("bbob", "result_folder: " + output_folder)

for problem in suite:
    problem.observe_with(observer)
    restarts = 0
    while (restarts < 10 and not problem.final_target_hit):
        sol = pso(n, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, nfe, w, c1, c2)
        restarts += 1
        print(sol.best.getFitness())


cocopp.main(observer.result_folder)
webbrowser.open("file://" + os.getcwd() + "/ppdata/index.html")
