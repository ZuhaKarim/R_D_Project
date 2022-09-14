import rdkit
import pandas as pd

for i in range(1, 6):
    # Reading CGCF output files
    generated_CGCF_trail = pd.read_pickle(r'output/CGCF/model_op/dataset_15_OP_trial'+ str(i) +'.pkl')
    # Reading ConfVAE output files
    generated_CVAE_trail = pd.read_pickle(r'output/ConfVAE/model_op/trail_'+ str(i) + 'mols.pkl')
    
    for j in range(len(generated_CGCF_trail)):
        # Generating XYZ molecules for CGCF files
        rdkit.Chem.rdmolfiles.MolToXYZFile(generated_CGCF_trail[i],"output/CGCF/XYZ/XYZ_Trial" + str(i)+ "/trial" + str(i) + "_mol_" + str(j) + '.xyz')
        # Generating XYZ molecules for ConfVAE files
        rdkit.Chem.rdmolfiles.MolToXYZFile(generated_CVAE_trail[i],"output/ConfVAE/XYZ/XYZ_Trial" + str(i)+ "/trial" + str(i) + "_mol_" + str(j) + '.xyz')
