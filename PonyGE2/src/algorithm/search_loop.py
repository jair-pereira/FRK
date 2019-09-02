from multiprocessing import Pool
from algorithm.parameters import params
from fitness.evaluation import evaluate_fitness
from stats.stats import stats, get_stats
from utilities.stats import trackers
from operators.initialisation import initialisation
from utilities.algorithm.initialise_run import pool_init

import psutil
import gc

### log ###
def write_log(file, generation, m, individuals):
    output_list = []
    output_list.append(generation)
    output_list.append(m)
    output_list.append(np.nanmedian([indv.fitness for indv in individuals]))
    for indv in individuals:
        output_list.append(indv.fitness)
    file.write(",".join(map(str,output_list))+"\n")
    file.flush()
    
    return
    
def write_best(generation, m, individuals):
    file = open(params['FILE_PATH']+"/"+str(generation)+".txt", 'w')
    output_list = []
    output_list.append(generation)
    output_list.append(m)
    
    best = max(individuals[1:])
    output_list.append(best.fitness)
    output_list.append(best.phenotype)    
    
    file.write(",".join(map(str,output_list))+"\n")
    file.flush()
    file.close()

###    

def search_loop():
    """
    This is a standard search process for an evolutionary algorithm. Loop over
    a given number of generations.
    
    :return: The final population after the evolutionary process has run for
    the specified number of generations.
    """
    ### log
    logf = open(params['FILE_PATH']+"/log.csv", 'w') 


    if params['MULTICORE']:
        # initialize pool once, if mutlicore is enabled
        params['POOL'] = Pool(processes=params['CORES'], initializer=pool_init,
                              initargs=(params,))  # , maxtasksperchild=1)

    # Initialise population
    individuals = initialisation(params['POPULATION_SIZE'])

    # Evaluate initial population
    individuals = evaluate_fitness(individuals)

    # Generate statistics for run so far
    get_stats(individuals)

    # Set the max size of the cache
    set_max_cache_size(individuals)

    # Traditional GE
    for generation in range(1, (params['GENERATIONS']+1)):
        # print("Generation is: " + str(generation))
        # print("Available memory is: " + str(psutil.virtual_memory().available))

        stats['gen'] = generation

        # New generation
        individuals = params['STEP'](individuals)
        
        ### log
        write_log(logf, generation, params['M'], individuals)
        print("generation ", generation, "/",params['GENERATIONS'], " finished at ",datetime.datetime.now()) #timestamp

    if params['MULTICORE']:
        # Close the workers pool (otherwise they'll live on forever).
        params['POOL'].close()

    logf.close() ### log
    return individuals


def set_max_cache_size(individuals):
    mem_per_cpu = psutil.virtual_memory().available / psutil.cpu_count()
    size_of_all_ind = 0
    for ind in individuals:
        size_of_all_ind += ind.get_mem_size() * 2
    avg_ind_size = size_of_all_ind / len(individuals)
    max_inds_fit_mem = mem_per_cpu / avg_ind_size
    cache_size = round(max_inds_fit_mem / 3)
    trackers.max_cache_size = cache_size
    # print("Max cache size is: " + str(cache_size))


def search_loop_from_state():
    """
    Run the evolutionary search process from a loaded state. Pick up where
    it left off previously.

    :return: The final population after the evolutionary process has run for
    the specified number of generations.
    """
    
    individuals = trackers.state_individuals
    
    if params['MULTICORE']:
        # initialize pool once, if mutlicore is enabled
        params['POOL'] = Pool(processes=params['CORES'], initializer=pool_init,
                              initargs=(params,))  # , maxtasksperchild=1)
    
    # Traditional GE
    for generation in range(stats['gen'] + 1, (params['GENERATIONS'] + 1)):
        stats['gen'] = generation
        
        # New generation
        individuals = params['STEP'](individuals)
    
    if params['MULTICORE']:
        # Close the workers pool (otherwise they'll live on forever).
        params['POOL'].close()
    
    return individuals