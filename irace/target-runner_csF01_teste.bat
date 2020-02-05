@echo off
python .\call_cs.py --nfe 1e+4 --n %5 --alpha %6 --beta %7 --kperc %8 --pr %9 --bbob "function_indices:1 dimensions:10 instance_indices:1"

exit 0
