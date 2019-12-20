from algorithm.parameters import params
from fitness.base_ff_classes.base_ff import base_ff
import metaheuristic
import cocoex
import numpy as np
from stats.stats import stats, get_stats # for our convenience

class noparam(base_ff):
    maximise = False

    def __init__(self):
        # Initialise base fitness function class.
        super().__init__()

        ### log ###
        self._ind = -1
        self._gen = 0

        self._repetitions = params['REPETITIONS']
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

    def evaluate(self, ind, **kwargs):
        # ind.phenotype will be a string, including function definitions etc.
        # When we exec it, it will create a value XXX_output_XXX, but we exec
        # inside an empty dict for safety.
        p, d = ind.phenotype, {}

        # todo: all of these non default ponyge dict params
        # should be init together
        d['output_fitness'] = None
        d['output_nfe']     = None

        problemid = ""
        code    =  p
        fitness = [np.inf for _ in range(self._repetitions)]
        nfe     = [np.inf for _ in range(self._repetitions)]
        errors  = ["" for _ in range(self._repetitions)]

        for problem in self.suite:
            #inputs for the generated algorithm
            problemid = problem.id
            d = {
                "max_nfe"  : self.max_nfe,
                "dimension": problem.dimension,
                "my_func"  : problem,
                "bounds"   : (problem.lower_bounds[0], problem.upper_bounds[0])
                }

            # Exec the phenotype.
            try:
                for r in range(self._repetitions):
                    exec(p, d)
                    nfe[r]     = d['output_nfe']
                    fitness[r] = d['output_fitness']
            except Exception as err:
                errors[r]  = err
                print("==========================")
                print("A FRK couldnt be executed:")
                print(p)
                print(err)
                print("==========================")
                raise err

        # Log
        self._ind += 1
        if stats['gen'] > self._gen:
          self._gen = stats['gen']
          self._ind = 0

        #write problem id, fitness and nfe spent then the FRK code
        logc = open(params['FILE_PATH']+"/"+str(self._gen)+"_"+str(self._ind)+".txt", 'w')
        logc.write(problemid+"\n")
        logc.write(",".join(map(str,fitness))+"\n")
        logc.write(",".join(map(str,nfe))+"\n")
        logc.write(code)
        logc.flush()
        logc.close()

        return min(fitness)
