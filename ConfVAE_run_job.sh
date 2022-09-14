#!/bin/bash
#SBATCH --partition=gpu          # partition (queue)
#SBATCH --ntasks-per-node=64     # number of cores per node
#SBATCH --mem=180G                 # memory per node in MB (different units with suffix K|M|G|T)
#SBATCH --time=2-16:00:00              # total runtime of job allocation (format D-HH:MM:SS; first parts optional)
#SBATCH --output=ConfVAE.%j.out    # filename for STDOUT (%N: nodename, %j: job-ID)
#SBATCH --error=Error.%j.err     # filename for STDERR hm  

# here comes the part with the description of the computational work, for example:

source ~/.bashrc

conda activate ConfVAE

module load cuda/10.2

python eval_vae.py \
    --ckpt ./logs/VAE_2022_08_03__16_10_51 \
    --dataset ./data/qm9/data_15.pkl \
    --num_samples 1

