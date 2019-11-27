from algorithm.parameters import params
from fitness.base_ff_classes.base_ff import base_ff
import metaheuristic
import cocoex
from stats.stats import stats, get_stats # for our convenience

class landscape(base_ff):
    maximise = False

    def __init__(self):
        # Initialise base fitness function class.
        super().__init__()

        ### log ###
        self._ind = -1
        self._gen = 0

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

        d['output_fitness'] = 0
        d['output_nfe']     = self.max_nfe+1

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
                print("A FRK couldnt be executed")

        # Get the output
        fitness = d['output_fitness']  # this is the program's output: a number.
        nfe = d['output_nfe']

        # Log
        self._ind += 1
        if stats['gen'] > self._gen:
          self._gen = stats['gen']
          self._ind = 0

        #write problem id, fitness and nfe spent then the FRK code
        logc = open(params['FILE_PATH']+"/"+str(self._gen)+"_"+str(self._ind)+".txt", 'w')
        logc.write(problem.id+","+str(fitness)+","+str(nfe)+"\n")
        logc.write(p)
        logc.flush()
        logc.close()

        return fitness
