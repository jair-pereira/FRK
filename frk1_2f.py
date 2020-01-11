from metaheuristic import *

#27,19
def frk1_2f06(my_func, bounds, dimension, max_nfe):
  n = 50
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_random
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  Solution.updateHistory(X)
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    U = X
    #Round 1
    S1 = op.select_tournament(U, n=1, k=n)
    S2 = op.select_current(U)
    U  = op.w_crx_blend2(S1, S2, alpha=0.50)
    X  = op.replace_if_random(X, U)
    #Round 2
    S1 = op.select_current(X)
    S2 = op.select_tournament(U, n=1, k=int(n*0.75))
    U  = op.w_crx_blend2(S1, S2, alpha=0.50)
    X  = op.replace_if_random(X, U)
    #Round Drop
    X = op.drop_worst(X, pr=0.50, k=int(n*0.25))
    [Xi.getFitness() for Xi in X]
  return Solution

#22,6
def frk1_2f01(my_func, bounds, dimension, max_nfe):
  n = 200
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_random
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  Solution.updateHistory(X)
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    U = X
    #Round 1
    S1 = op.select_random(X, 1)
    S2 = op.select_current(X)
    U  = op.w_crx_uni2(S1, S2, pr=0.50)
    X  = U
    #Round 2
    S1 = op.select_current(X)
    U  = op.w_pso(S1, w=0.50, c1=0.00, c2=0.75)
    X  = U
    [Xi.getFitness() for Xi in X]
  return Solution

#21,14
def frk1_2f15(my_func, bounds, dimension, max_nfe):
  n = 400
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_random
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  Solution.updateHistory(X)
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    U = X
    #Round 1
    S1 = op.select_tournament(U, n=1, k=int(n*0.25))
    S2 = op.select_random(U, 1)
    S3 = op.select_random(U, 1)
    U  = op.w_mut_de(S1, S2, S3, beta=0.50)
    X  = op.replace_if_best(X, U)
    #Round 2
    S1 = op.select_current(X)
    U  = op.w_pso(S1, w=0.25, c1=0.00, c2=0.75)
    X  = U
    [Xi.getFitness() for Xi in X]
  return Solution

#10,2
def frk1_2f21(my_func, bounds, dimension, max_nfe):
  n = 100
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_truncate
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  Solution.updateHistory(X)
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    U = X
    #Round 1
    S1 = op.select_random(U, 1)
    S2 = op.select_tournament(X, n=1, k=n)
    S3 = op.select_current(X)
    U  = op.w_mut_de(S1, S2, S3, beta=0.50)
    X  = X
    #Round 2
    S1 = op.select_tournament(X, n=1, k=1)
    S2 = op.select_tournament(U, n=1, k=int(n*0.25))
    U  = op.w_crx_exp2(S1, S2, pr=0.75)
    X  = op.replace_if_random(X, U)
    [Xi.getFitness() for Xi in X]
  return Solution
