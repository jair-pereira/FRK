from metaheuristic import *

#16,17
def frk2_4f01(my_func, bounds, dimension, max_nfe):
  n = op.generate_int(min=20, max=1200)
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_truncate
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  Solution.updateHistory(X)
  psetA = op.gen_var_param()
  psetB = op.gen_var_param()
  psetC = op.gen_var_param()
  seltourn_pk = op.gen_tourn_param()
  pDrop = op.gen_drop_param()
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    pTourn = iter(seltourn_pk)
    U = X
    #Round 1
    pset = psetA
    S1 = op.select_tournament(U, n=1, k=int(n*next(pTourn)))
    S2 = op.select_random(U, 1)
    U  = op.w_crx_uni2(S1, S2, pr=pset['crxuni_pr'])
    X  = X
    #Round 2
    pset = psetB
    S1 = op.select_random(U, 1)
    S2 = op.select_current(U)
    U  = op.w_crx_blend2(S1, S2, alpha=pset['crxbld_alpha'])
    X  = op.replace_if_random(X, U)
    [Xi.getFitness() for Xi in X]
  return Solution

#16,3
def frk2_4f06(my_func, bounds, dimension, max_nfe):
  n = op.generate_int(min=20, max=1200)
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_random
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  Solution.updateHistory(X)
  psetA = op.gen_var_param()
  psetB = op.gen_var_param()
  psetC = op.gen_var_param()
  seltourn_pk = op.gen_tourn_param()
  pDrop = op.gen_drop_param()
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    pTourn = iter(seltourn_pk)
    U = X
    #Round 1
    pset = psetA
    S1 = op.select_tournament(X, n=1, k=int(n*next(pTourn)))
    S2 = op.select_tournament(U, n=1, k=int(n*next(pTourn)))
    S3 = op.select_current(X)
    U  = op.w_mut_de(S1, S2, S3, beta=pset['mutde_beta'])
    X  = op.replace_if_best(X, U)
    #Round 2
    pset = psetB
    S1 = op.select_tournament(X, n=1, k=int(n*next(pTourn)))
    S2 = op.select_random(U, 1)
    U  = op.w_crx_blend2(S1, S2, alpha=pset['crxbld_alpha'])
    X  = op.replace_if_random(X, U)
    [Xi.getFitness() for Xi in X]
  return Solution

#19,4
def frk2_4f15(my_func, bounds, dimension, max_nfe):
  n = op.generate_int(min=20, max=1200)
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_random
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  Solution.updateHistory(X)
  psetA = op.gen_var_param()
  psetB = op.gen_var_param()
  psetC = op.gen_var_param()
  seltourn_pk = op.gen_tourn_param()
  pDrop = op.gen_drop_param()
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    pTourn = iter(seltourn_pk)
    U = X
    #Round 1
    pset = psetA
    S1 = op.select_tournament(X, n=1, k=int(n*next(pTourn)))
    S2 = op.select_current(X)
    S3 = op.select_tournament(U, n=1, k=int(n*next(pTourn)))
    U  = op.w_mut_de(S1, S2, S3, beta=pset['mutde_beta'])
    X  = X
    #Round 2
    pset = psetB
    S1 = op.select_tournament(U, n=1, k=int(n*next(pTourn)))
    S2 = op.select_current(X)
    U  = op.w_crx_blend2(S1, S2, alpha=pset['crxbld_alpha'])
    X  = op.replace_if_best(X, U)
    [Xi.getFitness() for Xi in X]
  return Solution

#20,7
def frk2_4f21(my_func, bounds, dimension, max_nfe):
  n = op.generate_int(min=20, max=1200)
  Solution.setProblem(my_func, bounds, dimension, maximize=False)
  Solution.repair = op.repair_truncate
  X = Solution.initialize(n)
  for Xi in X:    Xi.setX(op.init_random(*Solution.bounds, Solution.dimension))
  [Xi.getFitness() for Xi in X]
  Solution.updateHistory(X)
  psetA = op.gen_var_param()
  psetB = op.gen_var_param()
  psetC = op.gen_var_param()
  seltourn_pk = op.gen_tourn_param()
  pDrop = op.gen_drop_param()
  while Solution.nfe < max_nfe and not my_func.final_target_hit:
    pTourn = iter(seltourn_pk)
    U = X
    #Round 1
    pset = psetA
    S1 = op.select_tournament(U, n=1, k=int(n*next(pTourn)))
    S2 = op.select_random(U, 1)
    U  = op.w_crx_exp2(S1, S2, pr=pset['crxexp_pr'])
    X  = op.replace_if_best(X, U)
    #Round 2
    pset = psetB
    S1 = op.select_random(X, 1)
    S2 = op.select_tournament(U, n=1, k=int(n*next(pTourn)))
    U  = op.w_crx_blend2(S1, S2, alpha=pset['crxbld_alpha'])
    X  = U
    #Round Drop
    X = op.drop_worst(X, pr=pDrop['drpwrst_pr'], k=int(n*pDrop['drpwrst_pk']))
    [Xi.getFitness() for Xi in X]
  return Solution
