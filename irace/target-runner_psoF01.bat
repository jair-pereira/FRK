@echo off

python .\call_pso.py --nfe 1e+4 --n %5 --w %6 --c1 %7 --c2 %8 --bbob "function_indices:1 dimensions:10 instance_indices:1"

exit 0
