from metaheuristic import *

def pso(n, my_func, bounds, dimension, max_nfe, w, c1, c2):
    Solution.setProblem(my_func, bounds, dimension, maximize=False)
    Solution.repair = op.repair_random
    X = Solution.initialize(n)
    [Xi.setX(op.init_random(*Solution.bounds, Solution.dimension)) for Xi in X]
    [Xi.getFitness() for Xi in X]

    while Solution.nfe < max_nfe and not my_func.final_target_hit:
        #Round 1
        S  = op.select_current(X)
        U  = op.w_pso(S, w, c1, c2)
        X  = U

        [Xi.getFitness() for Xi in X]
    return Solution

def de(n, my_func, bounds, dimension, max_nfe, beta, pr):
    Solution.setProblem(my_func, bounds, dimension, maximize=False)
    Solution.repair = op.repair_random
    X = Solution.initialize(n)
    [Xi.setX(op.init_random(*Solution.bounds, Solution.dimension)) for Xi in X]
    [Xi.getFitness() for Xi in X]

    while Solution.nfe < max_nfe and not my_func.final_target_hit:
        #Round 1
        S1 = op.select_random(X, 1)
        S2 = op.select_random(X, 1)
        S3 = op.select_random(X, 1)
        U  = op.w_mut_de(S1, S2, S3, beta)
        #Round 2
        S1 = op.select_current(X)
        S2 = op.select_current(U)
        U  = op.w_crx_exp2(S1, S2, pr)
        X  = op.replace_if_best(X, U)

        [Xi.getFitness() for Xi in X]
    return Solution

def ga(n, my_func, bounds, dimension, max_nfe, k, alpha, pr):
    Solution.setProblem(my_func, bounds, dimension, maximize=False)
    Solution.repair = op.repair_random
    X = Solution.initialize(n)
    [Xi.setX(op.init_random(*Solution.bounds, Solution.dimension)) for Xi in X]
    [Xi.getFitness() for Xi in X]

    while Solution.nfe < max_nfe and not my_func.final_target_hit:
        #Round 1
        S1 = op.select_tournament(X, n=1, k=int(k))
        S2 = op.select_tournament(X, n=1, k=int(k))
        U  = op.w_crx_blend2(S1, S2, alpha)
        X  = op.replace_if_best(X, U)
        #Round 2
        S  = op.select_current(X)
        U  = op.w_mut_uni(S, pr)
        X  = U

        [Xi.getFitness() for Xi in X]
    return Solution

def cs(n, my_func, bounds, dimension, max_nfe, pr, k):
    Solution.setProblem(my_func, bounds, dimension, maximize=False)
    Solution.repair = op.repair_random
    X = Solution.initialize(n)
    [Xi.setX(op.init_random(*Solution.bounds, Solution.dimension)) for Xi in X]
    [Xi.getFitness() for Xi in X]

    while Solution.nfe < max_nfe and not my_func.final_target_hit:
        #Round 1
        S  = op.select_current(X)
        U  = op.w_levy_flight(S)
        X  = op.replace_if_random(X, U)

        X = op.drop_worst(X, pr, int(k))

        [Xi.getFitness() for Xi in X]
    return Solution

def cs2(n, problem, bounds, dimension, max_nfe, alpha, beta, pr, kperc):
    Solution.setProblem(problem, bounds, dimension, maximize=False)
    Solution.repair = op.repair_random
    op.levyflight_step = op.levyflight_step_mantegnas
    X = Solution.initialize(n)
    [Xi.setX(op.init_random(*Solution.bounds, Solution.dimension)) for Xi in X]
    [Xi.getFitness() for Xi in X]

    while Solution.nfe < max_nfe and not problem.final_target_hit:
        #Round 1
        S1 = op.select_random(X)
        S2 = op.select_random(X)
        for Xa, Xb in zip(S1[:,0], S2[:,0]):
            ## levy flyght
            U = Solution.initialize(1)[0]
            u = Xa.x + alpha * op.levyflight_step(Xa.x.shape, beta)
            U.setX(u)

            ## replace
            if U.getFitness() < Xb.getFitness():
                Xb.setX(U.x)
                Xb.fitness = U.getFitness()
                Xb.updatePBest()
                Solution.updateBest(Xb)

        ## drop
        X = op.drop_worst( S2[:,0], pr, int(n*kperc))
        [Xi.getFitness() for Xi in X]
    return Solution
