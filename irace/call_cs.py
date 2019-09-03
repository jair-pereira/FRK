import numpy as np
import cocoex, cocopp
import sys, argparse, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solvers import cs

### interface between the target-runner and the solvers for irace ###

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--nfe'  , dest='nfe'  , type=float, help="Integer   : Number of Function Evaluations")
    parser.add_argument('--n'    , dest='n'    , type=float, help="Integer   : Population size")
    parser.add_argument('--pr'   , dest='pr'   , type=float, help="Real value: CS.dropworst probability")
    parser.add_argument('--k'    , dest='k'    , type=float, help="Interger  : CS.dropworst size")
    parser.add_argument('--bbob' , dest='bbob' , type=str  , help="String    : BBOB suite e.g.:function_indices:1 dimensions:2 instance_indices:1")
    args = parser.parse_args()

    suite = cocoex.Suite("bbob", "", args.bbob)
    fitness = 0
    for problem in suite:
        sol = cs(args.n, problem, (problem.lower_bounds[0], problem.upper_bounds[0]), problem.dimension, args.nfe, args.pr, args.k)
        fitness = sol.best.getFitness()
    print(fitness)
    return

if __name__ == "__main__":
   np.warnings.filterwarnings('ignore')
   main(sys.argv[1:])
