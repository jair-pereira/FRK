import numpy as np
from metaheuristic import *

def frk1_1f21(n, my_func, bounds, dimension, max_nfe):
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_truncate
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    U = X
    #Round 1
    S1 = op.select_tournament(X, n=1, k=int(n*0.50))
    U = op.w_mut_uni(S1, pr=0.10)
    X  = op.replace_if_random(X, U)
    #Round 2
    S1 = op.select_tournament(X, n=1, k=int(n*0.25))
    U  = op.w_levy_flight(S1)
    X  = op.replace_if_best(X, U)
    [Xi.getFitness() for Xi in X]
  return Solution

def frk1_1f15(n, my_func, bounds, dimension, max_nfe):
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_random
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    U = X
    #Round 1
    S1 = op.select_tournament(U, n=1, k=int(n*0.75))
    U = op.w_mut_uni(S1, pr=0.25)
    X  = op.replace_if_best(X, U)
    #Round 2
    S1 = op.select_random(X, 1)
    S2 = op.select_tournament(X, n=1, k=int(n*0.10))
    U  = op.w_crx_blend2(S1, S2, alpha=0.00)
    X  = op.replace_if_random(X, U)
    #Round Drop
    X = op.drop_probability(X, pr=0.10)
    [Xi.getFitness() for Xi in X]
  return Solution

def frk1_1f01(n, my_func, bounds, dimension, max_nfe):
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_truncate
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    U = X
    #Round 1
    S1 = op.select_tournament(U, n=1, k=int(n*0.10))
    S2 = op.select_random(U, 1)
    U  = op.w_crx_uni2(S1, S2, pr=0.50)
    X  = op.replace_if_random(X, U)
    #Round 2
    S1 = op.select_random(X, 1)
    S2 = op.select_tournament(U, n=1, k=int(n*0.25))
    S3 = op.select_tournament(X, n=1, k=int(n*0.10))
    U  = op.w_mut_de(S1, S2, S3, beta=0.75)
    X  = op.replace_if_best(X, U)
    [Xi.getFitness() for Xi in X]
  return Solution

def frk1_1f06(n, my_func, bounds, dimension, max_nfe):
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_truncate
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    U = X
    #Round 1
    S1 = op.select_current(X)
    U = op.w_levy_flight(S1)
    X  = X
    #Round 2
    S1 = op.select_current(U)
    S2 = op.select_tournament(X, n=1, k=int(n*0.50))
    U  = op.w_crx_blend2(S1, S2, alpha=0.20)
    X  = U
    [Xi.getFitness() for Xi in X]
  return Solution
