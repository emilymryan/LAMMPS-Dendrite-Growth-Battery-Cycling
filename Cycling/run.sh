 #! /bin/bash
module load openmpi/3.1.1
module load python3/3.6.5

# lmp=/projectnb/ryanlab/andrewca/mylammps/src/lmp_mpi
# dname1=test01
# mkdir -p ${dname1}
# mpirun -np $NSLOTS ${lmp} -in input_bvtest1.lmp -var dname ${dname1}

lmp=/projectnb/ryanlab/mmorey/mylammps/src/lmp_mpi

dname=cycle_test_04Nov
output=/projectnb/ryanlab/mmorey/ButlerVolmer/cycling/${dname}
dname1=${output}
mkdir -p ${dname1}

${lmp} -in input_bv_cycle.lmp -var dname ${dname1}

exit
