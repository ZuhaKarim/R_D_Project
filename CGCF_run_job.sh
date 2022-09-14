#!/bin/bash
#SBATCH --partition=gpu          # partition (queue)
#SBATCH --ntasks-per-node=32     # number of cores per node
#SBATCH --mem=32G                 # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time=0-10:00:00              # total runtime of job allocation (format D-HH:MM:SS; first parts optional)
#SBATCH --output=cluster_op/CGCF_Output.%j.out    # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error=cluster_op/CGCF_Error.%j.err     # filename for STDERR hm  

# here comes the part with the description of the computational work, for example:

source ~/.bashrc

conda activate CGCF

# module load cuda/10.2

python generate.py --ckpt ./pretrained/ckpt_qm9.pt --dataset ./data/qm9/data_15.pkl --num_samples 1 --out ./OP/dataset_15_OP_trial.pkl




