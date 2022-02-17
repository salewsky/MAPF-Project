#!/bin/bash
# http://www.cril.univ-artois.fr/~roussel/runsolver/

CAT="../../../../../../../../../programs/gcat.sh"

cd "$(dirname $0)"

#top -n 1 -b > top.txt

[[ -e .finished ]] || $CAT "../../../../../../../../../../MAPF-Project/benchmarks/Random/medium-open-64-64.lp" | "../../../../../../../../../programs/runsolver" \
	-M 20000 \
	-w runsolver.watcher \
	-o runsolver.solver \
	-W 1200 \
	"../../../../../../../../../programs/empty-1" python /home/salewsky/MAPF-Project/random_benchmark_solver.py /home/salewsky/MAPF-Project/encoding/reachable-nodes/encoding.lp ../../../../../../../../../../MAPF-Project/benchmarks/Random/medium-open-64-64.lp

touch .finished
