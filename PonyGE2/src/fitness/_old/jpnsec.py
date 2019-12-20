from algorithm.parameters import params
from fitness.base_ff_classes.base_ff import base_ff
import numpy as np
from math import *
import metaheuristic
import cocoex, cocopp  # bbob experimentation and post-processing modules
import pickle
from stats.stats import stats, get_stats # for our convenience


class jpnsec(base_ff):

    maximise = False

    def __init__(self):
        # Initialise base fitness function class.
        super().__init__()

        #parameters for bbbob
        self.max_nfe = params['MAX_NFE']
        self.runs    = params['RUNS']
        self.suite   = cocoex.Suite(
                            "bbob", "",
                            "function_indices:"  +str(params['FUNCTION'])+
                            " dimensions:"       +str(params['DIMENSIONS'])+
                            " instance_indices:" +str(params['INSTANCE_INDICES'])
                            )

        #
        print("Using BBOB suite: ",self.suite)


        ### log ###
        self._ind = -1
        self._gen = 0
        self.logh = open(params['FILE_PATH']+"/history.csv", 'w')
        output_list = []
        output_list.append("gen")
        output_list.append("indv")
        output_list.append("hh_fit")
        for p in self.suite:
            output_list.append(p.id)
        self.logh.write(",".join(map(str,output_list))+"\n")
        ###

    def evaluate(self, ind, **kwargs):
        # ind.phenotype will be a string, including function definitions etc.
        # When we exec it, it will create a value XXX_output_XXX, but we exec
        # inside an empty dict for safety.
        p, d = ind.phenotype, {}

        # for jpnsec, we are training only on one instance, thus this script handle only one instance
        for problem in self.suite:
            #inputs for the generated algorithm
            d = {
                "max_nfe"  : self.max_nfe,
                "dimension": problem.dimension,
                "my_func"  : problem,
                "bounds"   : (problem.lower_bounds[0], problem.upper_bounds[0])
                }

            # Exec the phenotype.
            try:
                exec(p, d)
            except Exception as err:
                print(p)
                print(err)
                raise err

            # Get the output
            result = d['XXX_output_XXX']  # this is the program's output: a number.

            ### log ###
            self._ind += 1
            if stats['gen'] > self._gen:
                self._gen = stats['gen']
                self._ind = 0
            output_list = []
            output_list.append(stats['gen'])
            output_list.append(self._ind)
            output_list.append(result)
            self.logh.write(",".join(map(str,output_list))+"\n")
            self.logh.flush()
            ###

        return result
