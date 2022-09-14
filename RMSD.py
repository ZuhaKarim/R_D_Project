import pandas as pd
import rdkit
import numpy as np
import matplotlib.pyplot as plt


original_obj = pd.read_pickle(r'CGCF-2/CGCF-ConfGen/data/qm9/data_15.pkl')

generated_CGCF_trails = [pd.read_pickle(r'CGCF-2/CGCF-ConfGen/OP/dataset_15_OP_trial1.pkl'),
                         pd.read_pickle(r'CGCF-2/CGCF-ConfGen/OP/dataset_15_OP_trial2.pkl'),
                         pd.read_pickle(r'CGCF-2/CGCF-ConfGen/OP/dataset_15_OP_trial3.pkl'),
                         pd.read_pickle(r'CGCF-2/CGCF-ConfGen/OP/dataset_15_OP_trial4.pkl'),
                         pd.read_pickle(r'CGCF-2/CGCF-ConfGen/OP/dataset_15_OP_trial5.pkl')]

generated_CGCF_trails = []
generated_CVAE_trails = []
for i in range(1, 6):
    # Reading CGCF output files
    generated_CGCF_trails.append(pd.read_pickle(r'output/CGCF/model_op/dataset_15_OP_trial'+ str(i) +'.pkl'))
    # Reading ConfVAE output files
    generated_CVAE_trails.append(pd.read_pickle(r'output/ConfVAE/model_op/trail_'+ str(i) + 'mols.pkl'))

# Generate covariance matrix for RMSD values for CGCF vs ConfVAE
RMSD_table = []
for idx in range(len(original_obj)):
    CGCF_table = []
    for CGCF_trial in generated_CGCF_trails:
        CVAE_table = []
        for CVAE_trial in generated_CVAE_trails:
            CVAE_table.append(rdkit.Chem.rdMolAlign.AlignMol(CGCF_trial[idx], CVAE_trial[idx]))
        CGCF_table.append(CVAE_table)    
    RMSD_table.append(CGCF_table)


# Generating Gaussian distribution for RMSD value for each molecule

mean_tab = []
st_tab = []

fig_1, axs_1 = plt.subplots(1,3, figsize=(20,10))
# ax is an object so we convert it to numpy s we can loop over it.
axs_1 = np.array(axs_1)
#Index for molecules in RMSD
id_x = 0

for ax in axs_1:
    mol = np.array(RMSD_table)[id_x]
    mol = np.concatenate(mol)

    # cal mean,std for gaussian
    
    mean = np.mean(mol)
    mean_tab.append(mean)
    std = np.std(mol)
    st_tab.append(std)
    print(std)
    var = np.var(mol)
    curr_sample = np.linspace(mean-(3*std),mean+(3*std), 100)
    prob = 1/(np.sqrt(2*np.pi*var))*np.exp( -( ((curr_sample - mean)**2)/(2*var) ) ) * (curr_sample[1]-curr_sample[0])
    prob_y = np.max(prob)
    
    ax.plot(curr_sample, prob, c='r', label='Normal Distribution')
    ax.scatter(mean,prob_y)
    ax.scatter(mol, np.zeros(len(mol)), c='b', label='Original Data')
    ax.text(mean,prob_y, str(np.round([mean] ,3)))
    ax.grid()
    ax.set(xlabel='RMSD Values', ylabel='Probability Density')
    ax.legend(loc='upper left')
    id_x += 1


plt.show()
fig_1.savefig('RMSD_mol1_2_3.png')

# Second graph

fig_2, axs_2 = plt.subplots(1, 2, figsize=(20,10))
axs_2 = np.array(axs_2)

for ax in axs_2:
    
    mol = np.array(RMSD_table)[id_x]
    mol = np.concatenate(mol)

    mean = np.mean(mol)
    mean_tab.append(mean)

    std = np.std(mol)
    st_tab.append(std)

    print(std)
    var = np.var(mol)                           
    curr_sample = np.linspace(mean-(3*std),mean+(3*std), 100)
    prob = 1/(np.sqrt(2*np.pi*var))*np.exp( -( ((curr_sample - mean)**2)/(2*var) ) ) * (curr_sample[1]-curr_sample[0])
    prob_y = np.max(prob)
    
    ax.plot(curr_sample, prob, c='r', label='Normal Distribution')
    ax.scatter(mean,prob_y)
    ax.text(mean,prob_y, str(np.round([mean] ,3)))
    ax.scatter(mol, np.zeros(len(mol)), c='b', label='Original Data') 
    ax.grid()
    ax.set(xlabel='RMSD Values', ylabel='Probability Density')
    ax.legend(loc='upper left')
    id_x += 1

plt.show()
fig_2.savefig('RMSD_mol4_5.png')
