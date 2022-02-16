#!/bin/bash
# http://www.cril.univ-artois.fr/~roussel/runsolver/

CAT="../../../../../../../../../programs/gcat.sh"

cd "$(dirname $0)"

#top -n 1 -b > top.txt

[[ -e .finished ]] || $CAT "../../../../../../../../../../MAPF-Project/benchmarks/Preset/small-rooms-16-16.lp" | "../../../../../../../../../programs/runsolver" \
	-M 20000 \
	-w runsolver.watcher \
	-o runsolver.solver \
	-W 1200 \
	"../../../../../../../../../programs/empty-1" python /home/salewsky/MAPF-Project/preset_benchmark_solver.py /home/salewsky/MAPF-Project/encoding/complete-node-combining/encoding.lp ../../../../../../../../../../MAPF-Project/benchmarks/Preset/small-rooms-16-16.lp

touch .finished
