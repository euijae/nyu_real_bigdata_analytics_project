#!/bin/bash
#SBATCH --nodes=1                        # requests 1 compute servers
#SBATCH --ntasks-per-node=1              # runs 1 tasks on each server
#SBATCH --cpus-per-task=2                # uses 1 compute core per task
#SBATCH --time=1:00:00                   # Computation time 1hr
#SBATCH --mem=10GB                       # Memory requested 10GB
#SBATCH --job-name=sbatch-nba-dl
#SBATCH --output=/scratch/dnp9357/rbda/nba_downloader/logs/demo_%j.out
#SBATCH --error=/scratch/dnp9357/rbda/nba_downloader/logs/demo_%j.err
#SBATCH --exclusive
#SBATCH --requeue

module purge
module load python/intel/3.8.6

singularity exec --overlay /scratch/dnp9357/rbda/overlay-15GB-500K.ext3:rw /scratch/work/public/singularity/cuda11.6.124-cudnn8.4.0.27-devel-ubuntu20.04.4.sif /bin/bash -c "
source /ext3/env.sh
python3 download_script.py
"