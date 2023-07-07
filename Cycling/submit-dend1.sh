#! /bin/bash -l
#$ -l h_rt=120:00:00
#$ -P ryanlab
#$ -m bea
#$ -j y
#$ -N bvCycle1
#$ -o /projectnb/ryanlab/tmelsh/chargingProfiles/final/results/BVcycling/$JOB_NAME.o$JOB_ID 
#$ -e /projectnb/ryanlab/tmelsh/chargingProfiles/final/results/BVcycling/$JOB_NAME.e$JOB_ID 
#$ -pe mpi_16_tasks_per_node 128
module load openmpi/3.1.1
module load python3/3.6.5

lmp=/projectnb/ryanlab/mmorey/mylammps/src/lmp_mpi

output=/projectnb/ryanlab/tmelsh/chargingProfiles/final/results/BVcycling/${JOB_NAME}_${JOB_ID}
mkdir -p ${output}
dname=${output}

mpirun -np $NSLOTS ${lmp} -in ${JOB_NAME}_input.lmp -var dname ${dname}

exit
