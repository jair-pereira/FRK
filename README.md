#### Note: This repository contains the experiment setup for the paper submitted to the CEC 2020.

# Introduction
--------------
This is a framework based on grammatical evolution (GE) to automatically generate swarm intelligence (SI) algorithms given a training instance.

Such framework is necessary because the performance of an algorithm depends on the target problem, and it is difficult to know a priori what algorithm and what parameters will perform best on a new problem.


# Requirements
--------------
The component library (meta-heuristic operators) are in-house implementation, while the recombination framework (GE) uses PonyGE2.

Python 3.6 or higher, matplotlib, numpy, pandas, and [PonyGE2](https://github.com/PonyGE/PonyGE2).

# Running
---------------
To perform the training you need to to run [PonyGE2](https://github.com/PonyGE/PonyGE2) (check for details in the link). It is necessary to create a parameter and fitness files. Refer to the sample files in PonyGE2/parameters and PonyGE2/src/fitness. The sample experiments use the [COCO benchmark](https://github.com/numbbo/coco). 

After the training, you need to run the processing.py script to gather the best code. Some other processing tools are available.
