from metaheuristic import *

#20,9
def frkb_1f01(my_func, bounds, dimension, max_nfe):
  n = op.generate_int(min=20, max=1200)
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_truncate
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  Solution.updateHistory(X)
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    U = X
    #Round 1
    S1 = op.select_tournament(U, n=1, k=int(n*op.generate_float(min=0.05, max=1, step=0.05)))
    S2 = op.select_current(X)
    U  = op.w_crx_blend2(S1, S2, alpha=op.generate_float(min=0, max=2, step=0.01))
    X  = U
    #Round 2
    S1 = op.select_random(X, 1)
    S2 = op.select_current(U)
    U  = op.w_crx_exp2(S1, S2, pr=op.generate_float(min=0.05, max=1, step=0.05))
    X  = U
    [Xi.getFitness() for Xi in X]
  return Solution

#23,16
def frkb_1f15(my_func, bounds, dimension, max_nfe):
  n = op.generate_int(min=20, max=1200)
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_random
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  Solution.updateHistory(X)
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    U = X
    #Round 1
    S1 = op.select_tournament(X, n=1, k=int(n*op.generate_float(min=0.05, max=1, step=0.05)))
    S2 = op.select_current(X)
    U  = op.w_crx_exp2(S1, S2, pr=op.generate_float(min=0.05, max=1, step=0.05))
    X  = X
    #Round 2
    S1 = op.select_random(U, 1)
    S2 = op.select_current(X)
    U  = op.w_crx_blend2(S1, S2, alpha=op.generate_float(min=0, max=2, step=0.01))
    X  = op.replace_if_random(X, U)
    [Xi.getFitness() for Xi in X]
  return Solution

#28,11
def frkb_1f06(my_func, bounds, dimension, max_nfe):
  n = op.generate_int(min=20, max=1200)
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
    U  = op.w_crx_uni2(S1, S2, pr=op.generate_float(min=0.05, max=1, step=0.05))
    X  = X
    #Round 2
    S1 = op.select_tournament(X, n=1, k=int(n*op.generate_float(min=0.05, max=1, step=0.05)))
    S2 = op.select_current(U)
    S3 = op.select_random(X, 1)
    U  = op.w_mut_de(S1, S2, S3, beta=op.generate_float(min=0, max=2, step=0.01))
    X  = op.replace_if_best(X, U)
    [Xi.getFitness() for Xi in X]
  return Solution

#12,16
def frkb_1f21(my_func, bounds, dimension, max_nfe):
  n = op.generate_int(min=20, max=1200)
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_truncate
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  Solution.updateHistory(X)
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    U = X
    #Round 1
    S1 = op.select_random(X, 1)
    S2 = op.select_tournament(U, n=1, k=int(n*op.generate_float(min=0.05, max=1, step=0.05)))
    U  = op.w_crx_blend2(S1, S2, alpha=op.generate_float(min=0, max=2, step=0.01))
    X  = op.replace_if_random(X, U)
    #Round 2
    S1 = op.select_tournament(X, n=1, k=int(n*op.generate_float(min=0.05, max=1, step=0.05)))
    S2 = op.select_current(U)
    U  = op.w_crx_exp2(S1, S2, pr=op.generate_float(min=0.05, max=1, step=0.05))
    X  = op.replace_if_random(X, U)
    [Xi.getFitness() for Xi in X]
  return Solution
