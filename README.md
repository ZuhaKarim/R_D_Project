# HBRS R&D Project
### 3D Molecular Representation Using Machine Learning Models
Supervisors: Dr. Karl N. Kirschner, Dr. Sebastian Houben

### Setup
According to the evaluation performed in report, two machine elarning models (CGCF, ConfVAE) were used for generating 3D multiple conformations using dataset QM9. Fifteen random molecules were selected for the evaluation based on RMSD and dihedral angles.

Follow the instructions provided in the repositories below to setup the environment and run the respective models.
1. [CGCF](https://github.com/MinkaiXu/CGCF-ConfGen)
2. [ConfVAE](https://github.com/MinkaiXu/ConfVAE-ICML21)

Run the following command to create input pickle file.
~~~
python gen_input_pkl.py
~~~

Run the following command to generate XYZ files for dihedral angles.
~~~
python gen_XYZ.py
~~~

Run the following command to generate RMSD values and export Gaussian distribution for CGCF vs ConfVAE.
~~~
python RMSD.py
~~~

Run the following command to generates dihedral angles in .csv format <sup>1</sup>.
~~~
python pymol_dihedral.py
~~~
```
1. Kirschner,K.N., PyMol Dihedral Script, personal communication on August, 8th, 2022.
```


## Contact

If you have any question, please contact me at <zuha.karim@smail.inf.h-brs.de>.




