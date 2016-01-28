#!/bin/bash

mkdir CounterOutputs CmdOutputs

#declare -a app=('ls' 'pwd' 'cat shnote.sh')

path='/home/xiaosha/start/cpu2006-1.1/benchspec/CPU2006/'
#401.bzip2
app[0]=$path'401.bzip2/run/run_base_test_amd64-m64-gcc43-nn.0000/bzip2_base.amd64-m64-gcc43-nn '$path'401.bzip2/run/run_base_test_amd64-m64-gcc43-nn.0000/dryer.jpg'

app[1]=$path'401.bzip2/run/run_peak_test_amd64-m64-gcc43-nn.0000/bzip2_peak.amd64-m64-gcc43-nn '$path'401.bzip2/run/run_peak_test_amd64-m64-gcc43-nn.0000/dryer.jpg'

app[2]=$path'401.bzip2/run/run_base_ref_amd64-m64-gcc43-nn.0000/bzip2_base.amd64-m64-gcc43-nn '$path'401.bzip2/run/run_base_ref_amd64-m64-gcc43-nn.0000/liberty.jpg'
#403.gcc
app[3]=$path'403.gcc/run/run_base_test_amd64-m64-gcc43-nn.0000/gcc_base.amd64-m64-gcc43-nn '$path'403.gcc/run/run_base_test_amd64-m64-gcc43-nn.0000/cccp.i -o cccp.s'

app[4]=$path'403.gcc/run/run_peak_test_amd64-m64-gcc43-nn.0000/gcc_peak.amd64-m64-gcc43-nn '$path'403.gcc/run/run_peak_test_amd64-m64-gcc43-nn.0000/cccp.i -o cccp.s'
#458.sjeng
app[5]=$path'458.sjeng/run/run_base_test_amd64-m64-gcc43-nn.0001/sjeng_base.amd64-m64-gcc43-nn '$path'458.sjeng/run/run_base_test_amd64-m64-gcc43-nn.0001/test.txt'

app[6]=$path'458.sjeng/run/run_peak_test_amd64-m64-gcc43-nn.0000/sjeng_peak.amd64-m64-gcc43-nn '$path'458.sjeng/run/run_peak_test_amd64-m64-gcc43-nn.0000/test.txt'


#app[??]='/home/xiaosha/start/cpu2006-1.1/benchspec/CPU2006/473.astar/exe/astar_base.amd64-m64-gcc43-nn' '/home/xiaosha/start/cpu2006-1.1/benchspec/CPU2006/473.astar/data/test/input/lake.cfg'

events="instructions,LLC-loads,LLC-load-misses,LLC-stores,LLC-store-misses,LLC-prefetches,LLC-prefetch-misses,cpu-cycles,page-faults"

for ((i = 0; i < ${#app[@]}; i++))
do

appName=$(echo ${app[$i]}| cut -d'/' -f 8)
parameters=$(echo ${app[$i]}| cut -d'/' -f 10)
paramA=$(echo $parameters| cut -d'_' -f 2)
paramB=$(echo $parameters| cut -d'_' -f 3)
fileName=$appName\_$paramA\_$paramB\_run$i.txt

sudo perf stat -e $events ${app[$i]} > CmdOutputs/$fileName 2> CounterOutputs/$fileName

done


