#- run an app several times sequentially
#- output results into separate files in a directory.
mkdir CounterOutputs CmdOutputs

events="instructions:u,LLC-loads,LLC-load-misses,LLC-stores,LLC-store-misses,LLC-prefetches,LLC-prefetch-misses,cpu-cycles,page-faults,cpu-migrations,cs,power/energy-cores/,power/energy-gpu/,power/energy-pkg/,power/energy-ram/"

for ((i = 0; i < 100; i++))
do

appName=$(echo ${app}| cut -d'/' -f 8)
parameters=$(echo ${app}| cut -d'/' -f 10)
paramA=$(echo $parameters| cut -d'_' -f 2)
paramB=$(echo $parameters| cut -d'_' -f 3)
fileName=$appName\_$paramA\_$paramB\_run$i.txt

sudo perf stat -C 3 -e ${events} bash executor.sh > CmdOutputs/$fileName 2> CounterOutputs/$fileName

done

#python parser.py

#mkdir pplots
#Rscript analyzer.r
