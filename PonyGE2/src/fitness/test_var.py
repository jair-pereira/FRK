from algorithm.parameters import params
from fitness.base_ff_classes.base_ff import base_ff
import numpy as np
from math import *
import metaheuristic
import cocoex, cocopp  # bbob experimentation and post-processing modules
import pickle
from stats.stats import stats, get_stats # for our convenience


class test_var(base_ff):

    maximise = False

    def __init__(self):
        # Initialise base fitness function class.
        super().__init__()

        ### log ###
        self._ind = -1
        self._gen = 0

    def evaluate(self, ind, **kwargs):
        # ind.phenotype will be a string, including function definitions etc.
        # When we exec it, it will create a value XXX_output_XXX, but we exec
        # inside an empty dict for safety.
        p, d = ind.phenotype, {}

        #inputs for the generated algorithm
        d = {}

        d['XXX_output_XXX'] = 0
        self._ind += 1
        if stats['gen'] > self._gen:
          self._gen = stats['gen']
          self._ind = 0
        logc = open(params['FILE_PATH']+"/"+str(self._gen)+"_"+str(self._ind)+".txt", 'w')
        logc.write(p)
        logc.flush()
        logc.close()

        # Get the output
        result = d['XXX_output_XXX']  # this is the program's output: a number.
        ###

        return result
